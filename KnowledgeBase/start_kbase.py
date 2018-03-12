#!/usr/bin/env python

# ros imports
import rospy
from knowledge_base_msgs.srv import *

# database imports
from knowledge_base.Classes import *
import knowledge_base.Classes
import inspect

# config
import yaml
import sys

# handlers
import handling.query_handling as qh

# pymongo and mongoengine
import pymongo
import mongoengine as me

#utils
import utils
import xml.etree.ElementTree as ET


# initialize database node by loading config file
argv = sys.argv
if len(argv) < 2:
    print('Need path to configfile as first parameter!')
    exit('1')
path_to_config = argv[1]
data = yaml.safe_load(open(path_to_config))

#initialize config parameters
db_to_use_as_blueprint_name = data['db_name']
copy_on_startup = data['copy_on_startup']
mongodb_port = int(data['mongodb_port'])

if copy_on_startup:
    # drop the database from the previous run
    db_run = me.connect('temp_db', host="127.0.0.1", port=mongodb_port)
    db_run.drop_database('temp_db')
    # copy the blueprint db to the temporary database
    client = pymongo.MongoClient('localhost', mongodb_port)
    client.admin.command('copydb',
                              fromdb=db_to_use_as_blueprint_name,
                              todb='temp_db')

else:
    me.connect(db_to_use_as_blueprint_name)


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
    ans = QueryResponse()
    msg = req.query.lower()
    print('DEBUG: got query ' + str(msg))
    query = utils.reduce_query(msg, accepted_w_word)
    print('DEBUG: reduced query ' + str(query))
    q_word = query[0]
    if q_word not in accepted_w_word:
        ans.answer = 'Failed, bad question word for query: ' + msg
        ans.success = False
    else:
        ans.answer = accepted_w_word[q_word](query[1:]) or 'Failed'
        if ans.answer.startswith('Failed'):
            ans.success = False
        else:
            ans.success = True
    return ans



def handle_data(req):
    success = True
    print('command: ' + req.command + '; object: ' + req.object)
    ans = DataResponse()
    ans.success = success
    return ans


# initialize the rosnode and services
rospy.init_node('knowledge_base')
query_handler = rospy.Service('KBase/query', Query, handle_query)
data_handler = rospy.Service('KBase/data', Data, handle_data)

rospy.spin()
