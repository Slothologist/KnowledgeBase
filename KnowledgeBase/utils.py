from Classes import *
import xml.etree.ElementTree as ET

point_shrinking_factor = 1000

def retrieve_object_by_identifier(name):
    '''

    :param name:
    :return:
    '''
    all_entrys = list(Person.objects(name=name)) + \
                 list(Location.objects(name=name)) + \
                 list(Room.objects(name=name)) + \
                 list(Rcobject.objects(name=name))
    if len(all_entrys) < 1:
        print('Failed! Found no person, location, room or RCObject with name ' + name)
        return None
    if len(all_entrys) > 1:
        print('Found more than one person, location, room or RCObject with name ' +
              name + ' using Person > Location > Room > RCObject')
    return all_entrys[0]


def deserialize_point2d(point):
    if type(point) == str:
        point = ET.fromstring(point)
    print('DEBUG: deserialize Point2D: ' + ET.tostring(point, encoding='utf-8'))
    return float(point.get('x'))/point_shrinking_factor, float(point.get('y'))/point_shrinking_factor


def filter_fillwords(query):
    '''
    Filters some fillerwords out of a query.
    :param query: the unfiltered query as a list, split by space
    :return: the filtered query as a list, split by space
    '''
    fillwords = ['are', 'is', 'was', 'the', 'of', 'that', 'were', 'have', 'has', 'a', 'an']
    ret_query = [x for x in query if x not in fillwords]
    return ret_query

def save_complete_db(kbase):
    for room in kbase.arena.rooms:
        room.save()
    for location in kbase.arena.locations:
        location.save()
    for door in kbase.arena.doors:
        door.save()
    for obj in kbase.rcobjects.rcobjects:
        obj.save()
    for per in kbase.crowd.persons:
        per.save()

    kbase.arena.save()
    kbase.crowd.save()
    kbase.rcobjects.save()
    kbase.save()

def add_annotation(arenaobj, annotations_xml):
    loc_type = ''
    xml_identifier = ''
    if type(arenaobj) is Room:
        loc_type = 'room'
        xml_identifier = arenaobj.name
    elif type(arenaobj) is Location:
        loc_type = 'location'
        xml_identifier = arenaobj.name
    elif type(arenaobj) is Door:
        loc_type = 'door'
        xml_identifier = arenaobj.roomOne.name + '_' + arenaobj.roomTwo.name

    annot = Annotation()
    annot.label = xml_identifier
    vps = []
    for annot_xml in annotations_xml:
        if annot_xml.get('label') == loc_type + ':' + xml_identifier:
            poly = False
            vp_main = False
            for annotChild in annot_xml.getchildren():
                if annotChild.tag == 'VIEWPOINT':
                    if annotChild.get('label') == 'main':
                        vp_main = True
                    vp = Robotposition.from_xml(annotChild)
                    vps.append(vp)
                elif annotChild.tag == 'PRECISEPOLYGON':
                    poly = True
                    points = []
                    for point2d in annotChild.getchildren():
                        if point2d.tag == 'POINT2D':
                            points.append(list(deserialize_point2d(point2d)))
                    points.append(points[0]) #polygon needs to begin and end at same location
                    annot.polygon = [points]
            if not poly:
                print('Polygon from ' + xml_identifier + ' is missing.')
            if not vp_main:
                print('ViewPoint \'main\' from ' + xml_identifier + ' is missing.')
    annot.viewpoints = vps
    arenaobj.annotation = annot
    return arenaobj
