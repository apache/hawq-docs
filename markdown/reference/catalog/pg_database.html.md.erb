---
title: pg_database
---

<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

The `pg_database` system catalog table stores information about the available databases. Databases are created with the `CREATE DATABASE` SQL command. Unlike most system catalogs, `pg_database` is shared across all databases in the system. There is only one copy of `pg_database` per system, not one per database.

<a id="topic1__gj143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_database</span>

| column          | type        | references         | description                                                                                                                                                                                                                                                                                                                            |
|-----------------|-------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `datname`       | name        |                    | Database name.                                                                                                                                                                                                                                                                                                                         |
| `datdba`        | oid         | pg\_authid.oid     | Owner of the database, usually the user who created it.                                                                                                                                                                                                                                                                                |
| `encoding`      | integer     |                    | Character encoding for this database. `pg_encoding_to_char()` can translate this number to the encoding name.                                                                                                                                                                                                                          |
| `datistemplate` | boolean     |                    | If true then this database can be used in the `TEMPLATE` clause of `CREATE DATABASE` to create a new database as a clone of this one.                                                                                                                                                                                                  |
| `datallowconn`  | boolean     |                    | If false then no one can connect to this database. This is used to protect the `template0` database from being altered.                                                                                                                                                                                                                |
| `datconnlimit`  | integer     |                    | Sets the maximum number of concurrent connections that can be made to this database. `-1` means no limit.                                                                                                                                                                                                                              |
| `datlastsysoid` | oid         |                    | Last system OID in the database.                                                                                                                                                                                                                                                                                                       |
| `datfrozenxid ` | xid         |                    | All transaction IDs before this one have been replaced with a permanent (frozen) transaction ID in this database. This is used to track whether the database needs to be vacuumed in order to prevent transaction ID wraparound or to allow pg\_clog to be shrunk. It is the minimum of the per-table *pg\_class.relfrozenxid* values. |
| `dattablespace` | oid         | pg\_tablespace.oid | The default tablespace for the database. Within this database, all tables for which *pg\_class.reltablespace* is zero will be stored in this tablespace. All non-shared system catalogs will also be there.                                                                                                                            |
| `datconfig`     | text\[\]    |                    | Session defaults for user-settable server configuration parameters.                                                                                                                                                                                                                                                                    |
| `datacl`        | aclitem\[\] |                    | Database access privileges as given by `GRANT` and `REVOKE`.                                                                                                                                                                                                                                                                           |




