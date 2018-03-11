# KnowledgeBase
A simple Database for Ros

## Dependencies
pip install mongo mongoengine

This repository has a corresponding message file repository: https://github.com/Slothologist/KnowledgeBase_mgs

## Overview
coming soon...

### Starting the rosnode
Use the launchfile contained in the launch folder. A config file for the KBasenode must be
given as additional paramenter. 

### Physical location of the database
MongoDB's default saving location is under /var/lib/mongodb. This can be changed in the
/etc/mongod.conf. 

## Database Schema
coming soon...

## Services
The Node realises queries as Ros Servicecalls. The main call for queries is under the topic 
/KBase/query, accepts a query in string form and returns one or more database objects in xml 
form. 

Queries are accepted in a form inspired by native human speech. Each query starts with a question
word, e.g. where, who, what, which, when. This word defines the type of the return value.

Queries can be enhanced by adding 'filler' words, making the queries more human-like. These 
filler words are (amongst others) 'are', 'is', 'was', 'the', 'of', 'that', 'were', 'have' and 'has'.
This makes theses queries valid:
* where is the kitchen
* what is the size of the milk
* which rcobjects have the shape cylindrical
* in which room is the cup
* how many category have the rcobjects

### Queries


#### Where
Will return a Viewpoint corresponding to a given identifier. 'Where' queries shall be of the form 
'where *unique_identifier* [*viewpoint_label*]'. The *unique identifier* can be of either a 
Location, Person, Room or RCObject. The optional *viewpoint label* can be specified to retrieve a 
specific viewpoint a Room or Location may have by its label. If *viewpoint label* is not specified,
the Viewpoint with label 'main' will be used. 

##### Examples
* where kitchen
  * Will return the main viewpoint of the room 'kitchen'
* where fridge grasp_loc_1
  * Will return the viewpoint with label 'grasp_loc_1' of the location 'fridge'
* where michael
  * Will return the 'position' of the person 'michael'
* where cup
  * Will return the viewpoint with label 'main' of the object 'cup'


#### What
Will return a RCObject (or String). 'What' queries shall be of the form 'what [*attribute_name*]
*unique_identifier*'. The *unique identifier* shall be the 'name' of a RCObject. The optional 
*attribute name* can be specified to retrieve (instead of the complete RCObject) the value of a
specific attribute of the RCObject specified by the *unique identifier* as a String.

##### Examples
* what cup
  * Will return the RCObject with name 'cup'
* what shape melon
  * Will return a string which is the 'shape' of the RCObject with name 'melon'
* what color apple
  * Will return a string which is the 'color' of the RCObject with name 'apple'

#### Which
Will return a List of basic database objects (BDO, i.e. Person, Location, Room, Door, RCObject)
where a given attribute has a given value. 'Which' queries shall be of the form 'which *BDO* 
*attribute* *value*'. The *BDO* must be either 'Location', 'Person', 'Room' or 'RCObject'. The 
*attribute* must be one of the attributes the *BDO* has. The *value* shall be the value of the
given *attribute*.

##### Examples
* which rcobject color green
  * Will return a List of RCObject. Every 'color' of these RCObject will have the value 'green'
* which room name kitchen
  * Will return a List of Room. Every Room's 'name' attribute will have the value 'kitchen'. Note 
  that this List will probably have length 1.
* which person gender female
  * Will return a List of Person. Every Persons 'gender' attribute will have the value 'female'.

#### Who
will return a Person corresponding to a given identifier. 'Who' queries shall be of the form 'who
*unique_identifier*. The *unique identifier* shall be the 'name' of a Person.

##### Examples
* who peter
  * Will return the Person with the 'name' attributes value being 'peter' 
 
#### In which
Will return either a Location or a Room. 'In which' queries shall be of the form 'in which
('Location' | 'Room') *unique_identifier*'. The *unique identifier* can be of either a 
Location, Person, Room or RCObject. The second argument so to say must be either 'Location' or 
'Room' and will determine, if this query returns a Location or Room.

##### Examples
* in which room cup
  * Will return the Room in which the Location lies, in which again the RCObject with the 'name'
   attribute 'cup' is located.  
* in which location alex
  * Will return the Location in which the 'position' of the Person with the name 'alex' 
  is located. Note that this may return just a String with a error message, if alex is not known 
  to be in any Location.
* in which room point *<Point2D_xml>*

#### How many
Will return a int corresponding to the number of distinct occurences a specified attribute has
in a BDO. 'How many' queries shall be of the form 'how many *attribute* *BDO*'. The 
*BDO* must be either 'Location', 'Person', 'Room' or 'RCObject'. The 
*attribute* must be one of the attributes the *BDO* has.

##### Examples
* how many category rcobject
  * Will return an Int which is equal to the number of distinct attribute 'category' values of all 
  the known RCObject instances have. 
* how many name person
  * Will return an Int which is equal to the number of distinct attribute 'name' values of all the 
  known Person instances have. Because in this case 'name' is the unique identifier, this querry 
  will return the number of distinct Persons.

#### Get
With get you can retrieve a non basic data object. 'Get' queries shall be of the form 'get *NBDO*'.
The *NBDO* must be either 'KBase', 'Arena', 'Context', 'RCObjects' or 'Crowd'.

##### Examples
* get kbase
  * Will return the entire Knowledgebase as an KBase object.
* get ARENA
  * Will return the entire Arena, with all Locations, Rooms and Doors as Arena object.

### Saving new Data
coming soon...

