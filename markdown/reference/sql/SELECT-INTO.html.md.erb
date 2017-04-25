---
title: SELECT INTO
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

Defines a new table from the results of a query.

## <a id="topic1__section2"></a>Synopsis

``` pre
SELECT [ALL | DISTINCT [ON ( <expression> [, ...] )]]
    * | <expression> [AS <output_name>] [, ...]
    INTO [TEMPORARY | TEMP] [TABLE] <new_table>
    [FROM <from_item> [, ...]]
    [WHERE <condition>]
    [GROUP BY <expression> [, ...]]
    [HAVING <condition> [, ...]]
    [{UNION | INTERSECT | EXCEPT} [ALL] <select>]
    [ORDER BY <expression> [ASC | DESC | USING <operator>] [, ...]]
    [LIMIT {<count> | ALL}]
    [OFFSET <start>]
    [FOR {UPDATE | SHARE} [OF <table_name> [, ...]] [NOWAIT]
    [...]]
```

## <a id="topic1__section3"></a>Description

`SELECT INTO` creates a new table and fills it with data computed by a query. The data is not returned to the client, as it is with a normal `SELECT`. The new table's columns have the names and data types associated with the output columns of the `SELECT`. Data is always distributed randomly.

## <a id="topic1__section4"></a>Parameters

The majority of parameters for `SELECT INTO` are the same as [SELECT](SELECT.html).

<dt>TEMPORARY,  
TEMP  </dt>
<dd>If specified, the table is created as a temporary table.</dd>

<dt> \<new\_table\>  </dt>
<dd>The name (optionally schema-qualified) of the table to be created.</dd>

## <a id="topic1__section5"></a>Examples

Create a new table `films_recent` consisting of only recent entries from the table `films`:

``` sql
SELECT * INTO films_recent FROM films WHERE date_prod >=
'2006-01-01';
```

## <a id="topic1__section6"></a>Compatibility

The SQL standard uses `SELECT INTO` to represent selecting values into scalar variables of a host program, rather than creating a new table. The HAWQ usage of `SELECT INTO` to represent table creation is historical. It is best to use [CREATE TABLE AS](CREATE-TABLE-AS.html) for this purpose in new applications.

## <a id="topic1__section7"></a>See Also

[SELECT](SELECT.html), [CREATE TABLE AS](CREATE-TABLE-AS.html)
