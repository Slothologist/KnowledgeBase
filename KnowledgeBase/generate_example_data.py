from Classes.Classes import RCObjects, Crowd,Context,Arena,ObjectEncoder,KBase,Room,Person,Location,Door,RCObject,ObjectDecoder
import json

#Lists to add your entries to
arena_r = []
arena_l = []
arena_d = []
objs = []
crowd = []
#pers = [] #no person list as those will be hardcoded and properly generated during runtime

##################################################################################################################################################################

##Data which shall be put into the database
## Modifiy at will

#Arena-entries (locations, rooms etc)
#<N_placementTwo> = (dinner table) | cabinet | bookshelf | (kitchen counter) | sofa | (couch table) | (side table) | (stove) | bed | closet | desk | bar;
arena_r.append(Room(name='diningroom', numberOfDoors='2'))
arena_l.append(Location(name='dinnertable', room='diningroom', isBeacon='True'))
arena_l.append(Location(name='closet', room='diningroom', isBeacon='True'))
arena_l.append(Location(name='desk', room='diningroom', isPlacement='True'))

arena_r.append(Room(name='livingroom', numberOfDoors='0'))
arena_l.append(Location(name='couchtable', room='livingroom'))
arena_l.append(Location(name='sofa', room='livingroom'))
arena_l.append(Location(name='bar', room='livingroom'))
arena_l.append(Location(name='cabinet', room='livingroom'))

arena_r.append(Room(name='kitchen', numberOfDoors='0'))
arena_l.append(Location(name='bookshelf', room='kitchen'))
arena_l.append(Location(name='kitchencounter', room='kitchen'))
arena_l.append(Location(name='stove', room='kitchen'))

arena_r.append(Room(name='bedroom', numberOfDoors='1'))
arena_l.append(Location(name='bed', room='bedroom'))
arena_l.append(Location(name='sidetable', room='bedroom'))

arena_r.append(Room(name='outside', numberOfDoors='0'))#if you have doors to the outside it would make sense to also annotate an extra room for the outside

arena_d.append(Door(roomOne='outside', roomTwo='bedroom'))
arena_d.append(Door(roomOne='diningroom', roomTwo='outside'))

#Objects-Entries
#wie mit fork, spoon and knife umgehen?
#categorys:
#fruit, container, food, drink, snack, cleaning stuff,
#weitere infos folgen vmtl
objs.append(RCObject(name="apple",          category='fruit', color="red and green",         location="desk", room="kitchen", shape="round", size='1'))
objs.append(RCObject(name="bag",            category='container', color="brown",             location="bookshelf", room="living room", shape="quite flat", size='4'))
objs.append(RCObject(name="banana milk",    category='drink', color="blue and white",        location="kitchen counter", room="kitchen", shape="boxy", size='1'))
objs.append(RCObject(name="basket",         category='container', color="green",             location="bookshelf", room="living room", shape="rectangular", size='4'))
objs.append(RCObject(name="bread",          category='food', color="blue and yellow",        location="stove", room="kitchen", shape="bar", size='2'))
objs.append(RCObject(name="cappucino",     category='drink', color="brown",                 location="kitchen counter", room="kitchen", shape="cylindrical", size='2'))
objs.append(RCObject(name="cereals",        category='food', color="green and red",          location="stove", room="kitchen", shape="boxy", size='2'))
objs.append(RCObject(name="chocolate cookies", category='snack', color="brown",              location="couch table", room="living room", shape="boxy", size='2'))
objs.append(RCObject(name="cloth",          category='cleaning stuff', color="yellow green or blue",  location="closet", room="bedroom", shape="quite flat", size='4'))
objs.append(RCObject(name="coffeecup",      category='container', color="white and brown",   location="bookshelf", room="living room", shape="cylindrical", size='2'))
objs.append(RCObject(name="coke",           category='drink', color="red",                   location="kitchen counter", room="kitchen", shape="cylindrical", size='2'))
objs.append(RCObject(name="cornflakes",     category='food', color="green white and red",    location="stove", room="kitchen", shape="boxy", size='2'))
objs.append(RCObject(name="crackers",       category='food', color="yellow and green",       location="stove", room="kitchen", shape="baggy", size='2'))
objs.append(RCObject(name="egg",            category='snack', color="white and red",         location="couch table", room="living room", shape="oval", size='0'))
objs.append(RCObject(name="fork",           category='cutlery', color="red blue or green",   location="cabinet", room="diningroom", shape="pointy", size='2'))
objs.append(RCObject(name="spoon",          category='cutlery', color="red blue or green",   location="cabinet", room="diningroom", shape="elongated", size='2'))
objs.append(RCObject(name="knife",          category='cutlery', color="red blue or green",   location="cabinet", room="diningroom", shape="pointy", size='2'))
objs.append(RCObject(name="lemon",          category='fruit', color="yellow",                location="desk", room="kitchen", shape="round", size='0'))
objs.append(RCObject(name="noodles",        category='food', color="yellow and black",       location="stove", room="kitchen", shape="baggy", size='1'))
objs.append(RCObject(name="orange drink",   category='drink', color="blue and orange",       location="kitchen counter", room="kitchen", shape="boxy", size='1'))
objs.append(RCObject(name="paper",          category='cleaning stuff', color="white",        location="closet", room="bedroom", shape="cylindrical", size='4'))
objs.append(RCObject(name="paprika",        category='food', color="red yellow or green",    location="stove", room="kitchen", shape="round", size='1'))
objs.append(RCObject(name="party cracker",  category='snack', color="red",                   location="couch table", room="living room", shape="baggy", size='2'))
objs.append(RCObject(name="pear",           category='fruit', color="green",                 location="desk", room="kitchen", shape="oval", size='0'))
objs.append(RCObject(name="peas",           category='food', color="green and black",        location="stove", room="kitchen", shape="cylindrical", size='1'))
objs.append(RCObject(name="pepper",         category='food', color="black",                  location="stove", room="kitchen", shape="cylindrical", size='0'))
objs.append(RCObject(name="plate",          category='container', color="white",             location="bookshelf", room="living room", shape="that of a flat bowl", size='4'))
objs.append(RCObject(name="potato",         category='food', color="brown",                  location="stove", room="kitchen", shape="potato e", size='0'))
objs.append(RCObject(name="potato soup",    category='food', color="yellow",                 location="stove", room="kitchen", shape="boxy", size='2'))
objs.append(RCObject(name="pringles",       category='snack', color="yellow",                location="couch table", room="living room", shape="cylindrical", size='4'))
objs.append(RCObject(name="red bowl",       category='container', color="red",               location="bookshelf", room="living room", shape="that of a deep plate", size='2'))
objs.append(RCObject(name="salt",           category='food', color="black and blue",         location="stove", room="kitchen", shape="cylindrical", size='0'))
objs.append(RCObject(name="sponge",         category='cleaning stuff', color="light green",  location="closet", room="bedroom", shape="rather boxy", size='0'))
objs.append(RCObject(name="tomato pasta",   category='food', color="red and green",          location="stove", room="kitchen", shape="that of a toothpaste tube", size='2'))
objs.append(RCObject(name="towel",          category='cleaning stuff', color="purple",       location="closet", room="bedroom", shape="rather flat", size='2'))
objs.append(RCObject(name="water",          category='drink', color="light blue",            location="kitchen counter", room="kitchen", shape="cylindrical", size='2'))
objs.append(RCObject(name="white bowl",     category='container', color="white",             location="bookshelf", room="living room", shape="that af a deep plate", size='2'))

#Crowd-entries
#dummys, overwritten by reportGroup
crowd.append(Person(age='3', gender="male", gesture="pointing", pose="sitting", shirtcolor="blue"))
crowd.append(Person(age='1', gender="female", gesture="waving", pose="standing", shirtcolor="green"))

#
arena = Arena(rooms=arena_r, doors=arena_d, locations=arena_l)
crowd = Crowd(persons=crowd)
rcobjects = RCObjects(objects=objs)
#context, will use default initializer
context = Context()


kbase = KBase(arena=arena, crowd=crowd, context=context, rcobjects=rcobjects, identifier='TestKBase')

#dump = json.dumps(kbase, cls=ObjectEncoder, indent=2, sort_keys=True)
#print(dump)
#print(json.loads(dump, cls=ObjectDecoder).arena.locations)


