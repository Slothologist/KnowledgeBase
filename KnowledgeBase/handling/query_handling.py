from Classes import *
import xml.etree.ElementTree as ET
from utils import retrieve_object_by_identifier, deserialize_point2d

def str_to_xml(str):
    # TODO: rewrite proper
    return '<str val= ' + str + '>'


def handle_who(query):
    '''
    Hander for the question word who. Will return a xml-ified Person.
    :param query:
    :return:
    '''
    # query is list with one element, which is a identifier for a person
    # TODO: filter wrong querries
    pers = Person.objects(name=query[0])[0]
    return ET.tostring(pers.to_xml(), encoding='utf-8')


def handle_what(query):
    '''

    :param query:
    :return:
    '''
    # query is either list with one element ('[what] cup'), so we return a object
    # or with two elements ('[what] shape cup'), so we return the attribute of the object as string
    # TODO: filter wrong querries
    obj = RCObject.objects(query[-1])[0]
    if len(query) > 1:
        attr = query[0]
        ans = obj.__dict__[attr]
        return str(ans)

    return ET.tostring(obj.to_xml(), encoding='utf-8')


def handle_where(query):
    '''

    :param query:
    :return:
    '''
    # query is a list with one element, which is the unique identifier of either a location, person, room or
    # object. It may have a second element, which would be a unique identifier for one of many robotposition/
    # viewpoints a location or room may have
    # TODO: filter wrong querries
    name = query[0]
    viewpoint_name = None
    if len(query) > 1:
        viewpoint_name = query[1]
    entry = retrieve_object_by_identifier(name)

    if not entry:
        return 'Failed! Found no person, location, room or RCObject with name ' + name

    # retrieve annotation of the fetched thingy
    annot = None
    if type(entry) == Room or type(entry) == Location:
        annot = entry.annotation
    elif type(entry) == Person:
        return ET.tostring(entry.lastKnownPosition.to_xml(), encoding='utf-8') # persons have a position themselves
        #  so we do not need to go over annot
    elif type(entry) == RCObject:
        annot = entry.location.annotation

    # retrieve viewpoint
    viewpoint = None
    if viewpoint_name:
        viewpoint = [vp for vp in annot.viewpoints if vp.label == viewpoint_name][0]
    else:
        viewpoint = [vp for vp in annot.viewpoints if vp.label == 'main'][0]

    return ET.tostring(viewpoint.to_xml(), encoding='utf-8')


def handle_in_which(query):
    '''
    query is a list with 3-(4+) elements for which the second element is always either 'location' or 'room' and the
    third is either the keyword 'point' or a unique identifier of either a location, person, room or object. In the case
    the third element is 'point', a Point2D in xml format should follow.
    :param query:
    :return:
    '''
    # TODO: filter wrong querries
    query = query[1:] # throw away 'which'

    # due to hacky programming, the elements 4+ should be joined and parsed into point2D
    point = None
    if len(query) > 2 and query[1] is 'point':
        point = ' '.join(query[2:])
        point = deserialize_point2d(point)

    # retrieve thingy by identifier if we dont already have a point
    if not point:
        entry = retrieve_object_by_identifier(query[1])
        if not entry:
            return 'Failed! Found no person, location, room or RCObject with name ' + query[1]

        # now there are 4 possibilities: we have retrieved a person (->point), location, room or object
        if type(entry) == Person:
            point = entry.lastKnownPosition


        elif type(entry) == Location:
            if query[0] is 'room':
                return ET.tostring(entry.room.to_xml(), encoding='utf-8')
            elif query[0] is 'location':
                return ET.tostring(entry.to_xml(), encoding='utf-8')


        elif type(entry) == Room:
            if query[0] is 'room':
                return ET.tostring(entry.to_xml(), encoding='utf-8')
            elif query[0] is 'location':
                print('Failed, query ' + ' '.join(query) + ' makes no sense! A room cannot be in a location.')
                return 'Failed, a room cannot be in a location!'


        elif type(entry) == RCObject:
            if query[0] is 'room':
                return ET.tostring(entry.location.room.to_xml(), encoding='utf-8')
            elif query[0] is 'location':
                return ET.tostring(entry.location.to_xml(), encoding='utf-8')

    # for persons and given points we need to keep going
    ## retrieve room/ location in which this point lies


    if query[0] is 'room':
        for room in Room.objects(annotation__polygon__geo_intersects=[point.x, point.y]):
            return ET.tostring(room.to_xml(), encoding='utf-8')
    elif query[0] is 'location':
        for loc in Location.objects(annotation__polygon__geo_intersects=[point.x, point.y]):
            return ET.tostring(loc.to_xml(), encoding='utf-8')

    print('Failed, query ' + ' '.join(query) + ' could not find a corresponding item!')
    return 'Failed, something unforseen happened, maybe the there is no room/location this point/object/location/room/person lies in'


def handle_which(query):
    '''
    query is a list with length 3. first element is either location, room, rcobject or person, second element is a
    attribute of the class of the first element. the third element is a value that this attribute shall have to be
    retrieved
    :param query:
    :return:
    '''
    # TODO: filter wrong querries
    pass

def handle_how_many(query):
    '''
    query is a list of length 2. the second element is either location, room, rcobject or person. the first element is
    a attribute of the first element. 
    :param query:
    :return:
    '''
    # TODO: filter wrong querries
    pass


def handle_get(query):
    '''
    Method to get a non-basic object. query is always a list of exactly one element, which can be 'kbase', 'rcobjects',
    'crowd', 'arena' or 'context'.
    :param query:
    :return:
    '''
    # TODO: filter wrong querries
    if query[0] is 'kbase':
        return ET.tostring(KBase.objects()[0].to_xml(), encoding='utf-8')
    elif query[0] is 'arena':
        return ET.tostring(KBase.objects()[0].arena.to_xml(), encoding='utf-8')
    elif query[0] is 'rcobjects':
        return ET.tostring(KBase.objects()[0].rcobjects.to_xml(), encoding='utf-8')
    elif query[0] is 'crowd':
        return ET.tostring(KBase.objects()[0].crowd.to_xml(), encoding='utf-8')
    elif query[0] is 'context':
        return ET.tostring(KBase.objects()[0].context.to_xml(), encoding='utf-8')

    print('Failed, query get ' + query[0] + ' could not be answered!')
    return 'Failed, query get ' + query[0] + ' could not be answered!'

#################### low prio:

def handle_when(query):
    # TODO: filter wrong querries
    pass


def handle_show(query):
    # TODO: filter wrong querries
    pass
