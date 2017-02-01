---
title: Creating and Managing Schemas
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

Schemas logically organize objects and data in a database. Schemas allow you to have more than one object \(such as tables\) with the same name in the database without conflict if the objects are in different schemas.

## <a id="topic18"></a>The Default "Public" Schema 

Every database has a default schema named *public*. If you do not create any schemas, objects are created in the *public* schema. All database roles \(users\) have `CREATE` and `USAGE` privileges in the *public* schema. When you create a schema, you grant privileges to your users to allow access to the schema.

## <a id="topic19"></a>Creating a Schema 

Use the `CREATE SCHEMA` command to create a new schema. For example:

``` sql
=> CREATE SCHEMA myschema;
```

To create or access objects in a schema, write a qualified name consisting of the schema name and table name separated by a period. For example:

```
myschema.table
```

See [Schema Search Paths](#topic20) for information about accessing a schema.

You can create a schema owned by someone else, for example, to restrict the activities of your users to well-defined namespaces. The syntax is:

``` sql
=> CREATE SCHEMA schemaname AUTHORIZATION username;
```

## <a id="topic20"></a>Schema Search Paths 

To specify an object's location in a database, use the schema-qualified name. For example:

``` sql
=> SELECT * FROM myschema.mytable;
```

You can set the `search_path` configuration parameter to specify the order in which to search the available schemas for objects. The schema listed first in the search path becomes the *default* schema. If a schema is not specified, objects are created in the default schema.

### <a id="topic21"></a>Setting the Schema Search Path 

The `search_path` configuration parameter sets the schema search order. The `ALTER DATABASE` command sets the search path. For example:

``` sql
=> ALTER DATABASE mydatabase SET search_path TO myschema,
public, pg_catalog;
```

### <a id="topic22"></a>Viewing the Current Schema 

Use the `current_schema()` function to view the current schema. For example:

``` sql
=> SELECT current_schema();
```

Use the `SHOW` command to view the current search path. For example:

``` sql
=> SHOW search_path;
```

## <a id="topic23"></a>Dropping a Schema 

Use the `DROP SCHEMA` command to drop \(delete\) a schema. For example:

``` sql
=> DROP SCHEMA myschema;
```

By default, the schema must be empty before you can drop it. To drop a schema and all of its objects \(tables, data, functions, and so on\) use:

``` sql
=> DROP SCHEMA myschema CASCADE;
```

## <a id="topic24"></a>System Schemas 

The following system-level schemas exist in every database:

-   `pg_catalog` contains the system catalog tables, built-in data types, functions, and operators. It is always part of the schema search path, even if it is not explicitly named in the search path.
-   `information_schema` consists of a standardized set of views that contain information about the objects in the database. These views get system information from the system catalog tables in a standardized way.
-   `pg_toast` stores large objects such as records that exceed the page size. This schema is used internally by the HAWQ system.
-   `pg_bitmapindex` stores bitmap index objects such as lists of values. This schema is used internally by the HAWQ system.
-   `hawq_toolkit` is an administrative schema that contains external tables, views, and functions that you can access with SQL commands. All database users can access `hawq_toolkit` to view and query the system log files and other system metrics.
