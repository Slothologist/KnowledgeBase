# KnowledgeBase
A simple Database for Ros

# Dependencies
pip install mongo mongoengine

# Overview
coming soon...

# Database Schema
coming soon...

# Services
The Node realises querrys as Ros Servicecalls. The main call for querryies is under the topic 
/KBase/querry, accepts a querry in string form and returns one or more database objects in xml 
form. 

Querries are accepted in a form inspired by native human speech. Each querry starts with a question
word, i.e. where, who, what, which, when. This word defines the type of the return value.


## Querrys


### Where
Will return a room


### What
Will RCObject (or string)


### Which
List(database object)


### Who
Person


### When


### Show

