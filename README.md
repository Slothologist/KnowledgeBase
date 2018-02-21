# KnowledgeBase
A simple Database for Ros

## Dependencies
pip install mongo mongoengine

...or just use pip install

## Overview
coming soon...

## Database Schema
coming soon...

## Services
The Node realises querrys as Ros Servicecalls. The main call for querryies is under the topic 
/KBase/querry, accepts a querry in string form and returns one or more database objects in xml 
form. 

Querries are accepted in a form inspired by native human speech. Each querry starts with a question
word, e.g. where, who, what, which, when. This word defines the type of the return value.


### Querrys


#### Where
Will return a Viewpoint. 

##### Examples
* where kitchen
  * Will return the main viewpoint of the room 'kitchen'
* where fridge grasp_loc_1
  * Will return the viewpoint with label 'grasp_loc_1' of the location 'fridge'
* where michael
  * Will return the 'lastKnownPosition' of the person 'michael'
* where cup
  * Will return the viewpoint with label 'main' of the object 'cup'


#### What
Will return a RCObject (or string).

##### Examples
* what cup
  * Will return the RCObject with name 'cup'
* what shape melon
  * Will return a string which is the 'shape' of the RCObject with name 'melon'
* what color apple
  * Will return a string which is the 'color' of the RCObject with name 'apple'

#### Which
Will return a List of basic database objects (BDO, i.e. Person, Location, Room, Door, RCObject).

##### Examples
* which rcobject color green
  * Will return a List of RCObject. Every 'color' of these RCObject will have the value 'green'
* which room name kitchen
  * Will return a List of Room. Every Room's 'name' attribute will have the value 'kitchen'. Note 
  that this List will probably have length 1.
* which person gender female
  * Will return a List of Person. Every Persons 'gender' attribute will have the value 'female'.

#### Who
will return a Person.

##### Examples
* who peter
  * Will return the Person with the 'name' attributes value being 'peter' 
 
#### In which
Will return either a Location or a Room.

##### Examples
* in which room cup
  * Will return the Room in which the Location lies, in which again the RCObject with the 'name'
   attribute 'cup' is located.  
* in which location alex
  * Will return the Location in which the 'lastKnownPosition' of the Person with the name 'alex' 
  is located. Note that this may return just a String with a error message, if alex is not known 
  to be in any Location.

#### How many
Will return a int.

##### Examples
* how many category rcobject
  * Will return an Int which is equal to the number of distinct attribute 'category' values of all 
  the known RCObject instances have. 
* how many name person
  * Will return an Int which is equal to the number of distinct attribute 'name' values of all the 
  known Person instances have. Because in this case 'name' is the unique identifier, this querry 
  will return the number of distinct Persons.

#### Get
With get you can 

##### Examples
* get kbase
  * Will return the entire Knowledgebase as an KBase object.
* get ARENA
  * Will return the entire Arena, with all Locations, Rooms and Doors as Arena object.

### Saving new Data
coming soon...

