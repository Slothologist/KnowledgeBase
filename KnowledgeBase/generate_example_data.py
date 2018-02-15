from Classes.Classes import RCObject, Door, Location, Person, Room, KBase, Context


#Lists to add your entries to
arena = []
objs = []
crowd = []
#pers = [] #no person list as those will be hardcoded and properly generated during runtime

##################################################################################################################################################################

##Data which shall be put into the database
## Modifiy at will

#Arena-entries (locations, rooms etc)
#<N_placementTwo> = (dinner table) | cabinet | bookshelf | (kitchen counter) | sofa | (couch table) | (side table) | (stove) | bed | closet | desk | bar;
arena.append(Room(name='diningroom', numberOfDoors='2'))
arena.append(Location(name='dinnertable', room='diningroom', isBeacon='True'))
arena.append(Location(name='closet', room='diningroom', isBeacon='True'))
arena.append(Location(name='desk', room='diningroom', isPlacement='True'))

arena.append(Room(name='livingroom', numberOfDoors='0'))
arena.append(Location(name='couchtable', room='livingroom'))
arena.append(Location(name='sofa', room='livingroom'))
arena.append(Location(name='bar', room='livingroom'))
arena.append(Location(name='cabinet', room='livingroom'))

arena.append(Room(name='kitchen', numberOfDoors='0'))
arena.append(Location(name='bookshelf', room='kitchen'))
arena.append(Location(name='kitchencounter', room='kitchen'))
arena.append(Location(name='stove', room='kitchen'))

arena.append(Room(name='bedroom', numberOfDoors='1'))
arena.append(Location(name='bed', room='bedroom'))
arena.append(Location(name='sidetable', room='bedroom'))

arena.append(Room(name='outside', numberOfDoors='0'))#if you have doors to the outside it would make sense to also annotate an extra room for the outside

arena.append(Door(roomOne='outside', roomTwo='bedroom'))
arena.append(Door(roomOne='diningroom', roomTwo='outside'))

#Objects-Entries
#wie mit fork, spoon and knife umgehen?
#categorys:
#fruit, container, food, drink, snack, cleaning stuff,
#weitere infos folgen vmtl
#gewicht fällt raus
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

#context, will use default initializer
context = Context()

#Crowd-entries
#dummys, overwritten by reportGroup
crowd.append(Person(age='3', gender="male", gesture="pointing", pose="sitting", shirtcolor="blue"))
crowd.append(Person(age='1', gender="female", gesture="waving", pose="standing", shirtcolor="green"))

kbase = KBase(arena=arena, crowd=crowd, context=context, rcobjects=objs)

