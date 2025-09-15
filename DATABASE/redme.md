<-----------------Python with database----------------->
CSV-> comma seperated value.
JSON--> json return value in string format. that change according to language. its use in all programing language.
{ "key" : "value"}

DB--> DBMS, RDBMS, OORDBMS

SQL--> DDL, DML, DML, TCL, DQL

DDL-> create, alter, truncate, drop
DML-> insert, delete, update
DCL-> grant, revoke
DQL-> select
TCL-> commit, rollback, savepoint

types of communication
-> hw to hw
-> hw to sw
-> sw to hw
-> sw to sw

mysql.connector moodule -> external module not avilable in python

mysql.connector provide translator's

import mysql.connector as ms
con = ms.connect("path","username", "password")
cr = con.cursor()
cr.execute("query")
con.commite()
