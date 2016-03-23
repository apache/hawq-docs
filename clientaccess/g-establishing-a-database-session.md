---
title: Establishing a Database Session
---

Users can connect to HAWQ using a PostgreSQL-compatible client program, such as `psql`. Users and administrators *always* connect to HAWQ through the *master*; the segments cannot accept client connections.

In order to establish a connection to the HAWQ master, you will need to know the following connection information and configure your client program accordingly.

|Connection Parameter|Description|Environment Variable|
|--------------------|-----------|--------------------|
|Application name|The application name that is connecting to the database. The default value, held in the `application_name` connection parameter is *psql*.|`$PGAPPNAME`|
|Database name|The name of the database to which you want to connect. For a newly initialized system, use the `template1` database to connect for the first time.|`$PGDATABASE`|
|Host name|The host name of the HAWQ master. The default host is the local host.|`$PGHOST`|
|Port|The port number that the HAWQ master instance is running on. The default is 5432.|`$PGPORT`|
|User name|The database user \(role\) name to connect as. This is not necessarily the same as your OS user name. Check with your HAWQ administrator if you are not sure what you database user name is. Note that every HAWQ system has one superuser account that is created automatically at initialization time. This account has the same name as the OS name of the user who initialized the HAWQ system \(typically `gpadmin`\).|`$PGUSER`|

[Connecting with psql](g-connecting-with-psql.html) provides example commands for connecting to HAWQ.
