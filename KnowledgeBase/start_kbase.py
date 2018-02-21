#!/usr/bin/env python

# ros imports
import rospy
from KnowledgeBase.srv import *

# database imports
from Classes import *
import Classes
import inspect

# config
import yaml
import sys

# handlers
import handling.query_handling as qh

# mongoengine
import mongoengine as me

argv = sys.argv
if len(argv) < 2:
    print('Need path to configfile as first parameter!')
    exit('1')
path_to_config = argv[1]
data = yaml.safe_load(open(path_to_config))

db_to_use_as_blueprint_name = data['db_name']

# create database connections to perm_db and working db
me.connect(db_to_use_as_blueprint_name, alias='perm_db')
db_run = me.connect('temp_db')
# drop the database from the previous run
db_run.drop_database('temp_db')


def switch_db(to):
    '''
    To permanently switch databases, it is necessary to modify the class variables of the used database classes.
    This is a shortcoming of mongoengine. For more information see https://github.com/MongoEngine/mongoengine/issues/607
    :param to: String; Name of the database to switch to
    :return: None
    '''
    for name, obj in inspect.getmembers(Classes):
        if inspect.isclass(obj):
            obj._meta['db_alias'] = to
            obj._collection = None


# copy the knowledge base from permanent to temporary database
switch_db('perm_db')
kbase = KBase.objects(identifier=data['db_identifier'])[0]
switch_db('default')
kbase.save()


def handle_query(req):
    accepted_w_word = {
        'who': qh.handle_who,
        'what': qh.handle_what,
        'where': qh.handle_where,
        'which': qh.handle_which,
        'in which': qh.handle_in_which,
        'how many': qh.handle_how_many,
        'get': qh.handle_get,

        'when': qh.handle_when,
        'show': qh.handle_show
    }
    msg = req.query.lower()
    query = msg.split(' ')
    q_word = query[0]
    if q_word not in accepted_w_word or \
                            q_word + ' ' + query[1] in accepted_w_word:
        return 'Failed, bad question word'
    ans = QuerryResponse()
    ans.answer = accepted_w_word[q_word](query[1:]) or 'Failed'
    return ans



def handle_data(req):
    success = True
    print('command: ' + req.command + '; object: ' + req.object)
    ans = DataResponse()
    ans.success = success
    return ans


# initialize the rosnode and services
rospy.init_node('KnowledgeBase')
query_handler = rospy.Service('KBase/query', Querry, handle_query)
data_handler = rospy.Service('KBase/data', Data, handle_data)

rospy.spin()
