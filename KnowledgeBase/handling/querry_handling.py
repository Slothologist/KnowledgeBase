from Classes import *
import xml.etree.ElementTree as ET

def str_to_xml(str):
    # TODO: rewrite proper
    return '<xml str= ' + str + '>'


def handle_who(querry):
    '''
    Hander for the question word who. Will return a xml-ified Person.
    :param querry:
    :return:
    '''
    # querry is list with one element, which is a identifier for a person
    # TODO: filter wrong querries
    pers = Person.objects(name=querry[0])[0]
    return ET.tostring(pers.to_xml(), encoding='utf-8')


def handle_what(querry):
    '''

    :param querry:
    :return:
    '''
    # querry is either list with one element ('[what] cup'), so we return a object
    # or with two elements ('[what] shape cup'), so we return the attribute of the object as string
    # TODO: filter wrong querries
    obj = RCObject.objects(querry[-1])[0]
    if len(querry) > 1:
        attr = querry[0]
        ans = obj.__dict__[attr]
        return ans

    return ET.tostring(obj.to_xml(), encoding='utf-8')


def handle_where(querry):
    '''

    :param querry:
    :return:
    '''
    # querry is a list with one element, which is the unique identifier of either a location, person, room or
    # object. It may have a second element, which would be a unique identifier for one of many robotposition/
    # viewpoints a location or room may have
    # TODO: filter wrong querries
    name = querry[0]
    viewpoint_name = None
    if len(querry) > 1:
        viewpoint_name = querry[1]
    all_entrys = Person.objects(name=name) + Location.object(name=name) + Room.objects(name=name) + RCObject.objects(name=name)
    if len(all_entrys) < 1:
        print('Failed! Found no person, location, room or RCObject with name ' + querry[0])
        return 'Failed! Found no person, location, room or RCObject with name ' + querry[0]
    if len(all_entrys) > 1:
        print('Found more than one person, location, room or RCObject with name ' + querry[0] + ' using a random one.')
    entry = all_entrys[0]

    # retrieve annotation of the fetched thingy
    annot = None
    if type(entry) == Room or type(entry) == Location:
        annot = entry.annotation
    elif type(entry) == Person:
        return ET.tostring(entry.lastKnownPosition.to_xml(), encoding='utf-8') # persons have a position themselves so we do not need to go over annot
    elif type(entry) == RCObject:
        annot = entry.location.annotation

    # retrieve viewpoint
    viewpoint = None
    if viewpoint_name:
        viewpoint = [vp for vp in annot.viewpoints if vp.label == viewpoint_name][0]
    else:
        viewpoint = [vp for vp in annot.viewpoints if vp.label == 'main'][0]

    return ET.tostring(viewpoint.to_xml(), encoding='utf-8')


def handle_in_what(querry):
    '''

    :param querry:
    :return:
    '''
    # TODO: filter wrong querries
    pass


def handle_which(querry):
    '''

    :param querry:
    :return:
    '''
    # querry is always
    # TODO: filter wrong querries
    pass


#################### low prio:

def handle_when(querry):
    # TODO: filter wrong querries
    pass


def handle_show(querry):
    # TODO: filter wrong querries
    pass
