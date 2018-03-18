from Classes import *
import xml.etree.ElementTree as ET
from utils import retrieve_object_by_identifier, get_class_of_bdo


def handle_forget(data):
    '''
    Hander for the data word forget. Will delete a bdo from the knowledge base.
    :param data:
    :return:
    '''
    # data is list with one or two elements. if it is of length one, it will contain the unique identifier of the bdo
    # to delete. otherwise the first element shall be "all" and the second either "person(s)", "object(s)", "door(s)",
    # "location(s)" or "room(s)"
    # TODO: filter wrong querries
    if len(data) > 1:  # "all" path
        types = {'person' : Person,
                 'object' : Rcobject,
                 'rcobject' : Rcobject,
                 'room' : Room,
                 'location' : Location,
                 'door': Door}
        if not data[0] == 'all':
            print('More than one element for forget and first element not \"all\"')
            return False, 11
        if data[1] not in types:
            if data[1].endswith('s') and data[1][:-1] in types:  # got plural of type, e.g. persons
                data[1] = data[1][:-1]
            else:
                print('Identification word not in classes allowed to delete!')
                return False, 12
        types[data[1]].objects().delete()
        return True, 0
    else:
        obj = retrieve_object_by_identifier(data[0])
        if obj is None:
            print('No object with identifier \"' + data[0] + '\" found!')
            return False, 13
        obj.delete()
        return True, 0


def handle_remember(data):
    '''
    Hander for the data word remember. Will save a bdo to the knowledge base.
    :param data:
    :return:
    '''
    # data is list with one element. It is a xml format of a BDO class.
    # TODO: filter wrong querries
    xml_string = data[0]
    try:
        xml_tree = ET.fromstring(xml_string)
    except Exception:
        print('XML parsing not successful.')
        return False, 21
    available_classes = {'persondata' : Person,
               'location' : Location,
               'room' : Room,
               'door' : Door,
               'rcobject' : Rcobject
               }
    if xml_tree.tag not in available_classes:
        print('Class \"' + xml_tree.tag + '\" is not a valid BDO class')
        return False, 22
    try:
        new_obj = available_classes[xml_tree.tag].from_xml(xml_tree)
        new_obj.save()
        return True, 0
    except Exception:
        print('Error in converting the given xml to a BDO')
        return False, 23

