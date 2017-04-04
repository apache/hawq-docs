---
title: HAWQ Resources and Permissions
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

The HAWQ Ranger policy editor always displays the complete list of HAWQ permissions. This list is not filtered by the operations that are actually supported by the resource(s) you have selected.

The following table identifies the specific permissions supported by each HAWQ resource.

![Permissions Supported by each HAWQ Resource](../images/resource-perms.png)


## <a id="dbops"></a> Policies for Database Operations

The database operations governed by HAWQ-Ranger authorization are those that you perform at the purely database-level. These operations include connecting to the database, creating schemas, and creating temporary tables and sequences. Use the following HAWQ Ranger Policy Details to assign permissions for these operations:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| database | \<db-name\> | The database to which you want to provide access |
| schema | `*` | Must specify `*` |
| table | `*` | Must specify `*` |

specifying the permissions you wish to assign:

| Permission    | Allows SQL Commands     |  Equivalent GRANT Command |
|-------------|----------------------|------------------------|
| connect | CONNECT | GRANT CONNECT ON DATABASE \<db-name\> TO \<user-name\> |
| create-schema | CREATE SCHEMA | GRANT CREATE ON DATABASE \<db-name\> TO \<user-name\> |
| temp| CREATE TEMP TABLE<p>CREATE TEMP SEQUENCE | GRANT TEMP ON DATABASE \<db-name\> TO \<user-name\> |


## <a id="dbschemaops"></a> Policies for Schema Operations

You perform many HAWQ operations within the scope of a specific database and schema, including creating/dropping/altering database objects. These operations will require permission to use the specified schema. 

The HAWQ schema named `public` is the default schema. When HAWQ-Native authorization is in effect, users are automatically granted access to this schema. When Ranger is enabled, users must be explicitly assigned the `usage-schema` permission to the `public` schema.

Use these HAWQ Ranger Policy Details to assign permission for schema-related operations:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| database | \<db-name\> | The database to which you want to provide access |
| schema | \<schema-name\> | The schema in which you want to provide access |
| table &#124; sequence &#124; function | `* `| No table/sequence/function |

specifying these permissions:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|------------------------------|----------------------|
| usage-schema | MANY |  GRANT USAGE ON SCHEMA \<schema-name\> TO \<user-name\> |
| create | ALTER/CREATE AGGREGATE, ALTER TABLE, CREATE [EXTERNAL] TABLE, CREATE FUNCTION, CREATE OPERATOR, CREATE OPERATOR CLASS (superuser only), CREATE SEQUENCE, CREATE VIEW, CREATE TYPE, SELECT INTO  |    GRANT CREATE ON SCHEMA \<schema-name\> TO \<user-name\> |


## <a id="tblops"></a> Policies for Table Operations

You can insert data into and select a table within schemas in which you have `usage-schema` permissions. Use the following HAWQ Ranger Policy Details to assign permission for these operations:

| Resource    | Value   |  Description     |
|-------------|---------------|-------------------|
| database | \<db-name\> | The database to which you want to provide access |
| schema | \<schema-name\> | The schema in which you want to provide access |
| table | \<table-name\> | The table to which you want to provide access |

specifying the permissions you wish to assign:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|---------------------------|-----------------|
| select  | ANALYZE, COPY INTO, SELECT, VACUUM ANALYZE | GRANT SELECT ON TABLE \<table-name\> TO \<user-name\> |
| insert  | COPY FROM, INSERT | GRANT INSERT ON TABLE \<table-name\> TO \<user-name\> |


## <a id="sequenceops"></a> Policies for Sequence Operations

You can use and select sequences and update sequence values in schemas in which you have `usage-schema` permissions. You can also use the `nextval()` and `setval()` HAWQ built-in functions to return and set sequence values. Use the following HAWQ Ranger Policy Details to assign permission for these operations:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| database | \<db-name\> | The database to which you want to provide access |
| schema | \<schema-name\> | The schema in which you want to provide access |
| sequence | \<sequence-name\> | The sequence to which you want to provide access |

specifying the permissions you wish to assign:

| Permission    | Allows SQL Commands, built-in functions   | Equivalent GRANT Command |
|-------------|---------------------------|------|
| select | SELECT \<sequence-name\> | GRANT SELECT ON SEQUENCE \<sequence-name\> TO \<user-name\> |
| usage, update | nextval() | GRANT USAGE, UPDATE ON SEQUENCE \<sequence-name\> TO \<user-name\> |
| update | setval() | GRANT UPDATE ON SEQUENCE \<sequence-name\> TO \<user-name\> |


## <a id="functionops"></a> Policies for Function Operations

You can execute user-defined functions in schemas in which you have `usage-schema` permissions. Use the following HAWQ Ranger Policy Details to assign permission for this operation:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| database | \<db-name\> | The database to which you want to provide access |
| schema | \<schema-name\> | The schema in which you want to provide access |
| function | \<function-name\> | The user-defined function to which you want to provide access |

specifying the permissions you wish to assign:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|---------------------------|-------|
| execute | SELECT \<function-name\>() | GRANT EXECUTE ON FUNCTION \<function-name\> TO \<user-name\>  |

**Note**: Functions typically access database objects such as tables, views, sequences, etc and other functions. When setting up your HAWQ policies, ensure you have also provided access to all database resources referenced within the function (recursively).


## <a id="dblangops"></a> Policies for Language Operations

Only super-users may register and drop languages for a specific database. These operations are governed by HAWQ-Native authorization. 

You may choose to permit users to use a specific language to create user-defined functions. Use these HAWQ Ranger Policy Details to assign such permission:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| database | \<db-name\> | The database to which you want to provide access |
| language | \<language-name\> | The language to which you want to provide access (plpgsql, sql, other languages explicitly registered in the database) |

specifying these permissions:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|------------------------------|----------------------|
| usage | CREATE FUNCTION ... LANGUAGE \<language-name\> |    GRANT USAGE ON LANGUAGE\<language-name\> TO \<user-name\> |


## <a id="dbtblspaceops"></a> Policies for Tablespace Operations

Only super-users may create and drop tablespaces. These operations are governed by HAWQ-Native authorization. 

You may choose to allow specific users to create tables within an existing tablespace. Use these HAWQ Ranger Policy Details to assign such permissions:

| Resource    | Value   |  Description     |
|-------------|----------------------|------------------------|
| tablespace | \<tablespace-name\> | The tablespace to which you want to provide access |

specifying these permissions:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|------------------------------|----------------------|
| create | CREATE TABLE ... TABLESPACE |  GRANT CREATE ON \<tablespace-name\> TO \<user-name\> |


## <a id="dbprotocolops"></a> Policies for Protocol Operations

You may choose to permit access to the `pxf`, `gpfdist`, and/or `http`  protocols to create readable and writable external tables. Use the following HAWQ Ranger Policy Details to assign permission for these operations:

| Resource    | Value   |  Description     |
|-------------|---------------|-------------------|
| protocol | \<protocol-name\> | The protocol to which you want to provide access \(pxf, gpfdist, http\) |

specifying the permissions you wish to assign:

| Permission    | Allows SQL Commands     | Equivalent GRANT Command |
|-------------|---------------------------|-----------------|
| select | CREATE READABLE EXTERNAL TABLE | GRANT SELECT ON PROTOCOL \<protocol-name\> TO \<user-name\> |
| insert  | CREATE WRITABLE EXTERNAL TABLE | GRANT INSERT ON PROTOCOL \<protocol-name\> TO \<user-name\> |
