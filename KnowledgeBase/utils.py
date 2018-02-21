from Classes import *


def retrieve_object_by_identifier(name):
    '''

    :param name:
    :return:
    '''
    all_entrys = Person.objects(name=name) + \
                 Location.object(name=name) + \
                 Room.objects(name=name) + \
                 RCObject.objects(name=name)
    if len(all_entrys) < 1:
        print('Failed! Found no person, location, room or RCObject with name ' + name)
        return None
    if len(all_entrys) > 1:
        print('Found more than one person, location, room or RCObject with name ' +
              name + ' using Person > Location > Room > RCObject')
    return all_entrys[0]


def deserialize_point2d(point):
    return 'not implemented yet'