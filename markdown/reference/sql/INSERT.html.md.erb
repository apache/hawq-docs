---
title: INSERT
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

Creates new rows in a table.

## <a id="topic1__section2"></a>Synopsis

``` pre
INSERT INTO <table> [( <column> [, ...] )]
   {DEFAULT VALUES | VALUES ( {<expression> | DEFAULT} [, ...] ) 
   [, ...] | <query>}
```

## <a id="topic1__section3"></a>Description

`INSERT` inserts new rows into a table. One can insert one or more rows specified by value expressions, or zero or more rows resulting from a query.

The target column names may be listed in any order. If no list of column names is given at all, the default is the columns of the table in their declared order. The values supplied by the `VALUES` clause or query are associated with the explicit or implicit column list left-to-right.

Each column not present in the explicit or implicit column list will be filled with a default value, either its declared default value or null if there is no default.

If the expression for any column is not of the correct data type, automatic type conversion will be attempted.

You must have `INSERT` privilege on a table in order to insert into it.

**Note:** HAWQ supports 127 concurrent inserts currently.

**Outputs**
On successful completion, an `INSERT` command returns a command tag of the form:

``` pre
INSERT oid
               count           
```

The *count* is the number of rows inserted. If count is exactly one, and the target table has OIDs, then *oid* is the OID assigned to the inserted row. Otherwise *oid* is zero.

## <a id="topic1__section5"></a>Parameters

<dt> \<table\>   </dt>
<dd>The name (optionally schema-qualified) of an existing table.</dd>

<dt> \<column\>   </dt>
<dd>The name of a column in table. The column name can be qualified with a subfield name or array subscript, if needed. (Inserting into only some fields of a composite column leaves the other fields null.)</dd>

<dt>DEFAULT VALUES  </dt>
<dd>All columns will be filled with their default values.</dd>

<dt> \<expression\>   </dt>
<dd>An expression or value to assign to the corresponding column.</dd>

<dt>DEFAULT  </dt>
<dd>The corresponding column will be filled with its default value.</dd>

<dt> \<query\>   </dt>
<dd>A query (`SELECT` statement) that supplies the rows to be inserted. Refer to the [SELECT](SELECT.html) statement for a description of the syntax.</dd>

## <a id="topic1__section7"></a>Examples

Insert a single row into table `films`:

``` pre
INSERT INTO films VALUES ('UA502', 'Bananas', 105, 
'1971-07-13', 'Comedy', '82 minutes');
```

In this example, the `length` column is omitted and therefore it will have the default value:

``` pre
INSERT INTO films (code, title, did, date_prod, kind) VALUES 
('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');
```

This example uses the `DEFAULT` clause for the `date_prod` column rather than specifying a value:

``` pre
INSERT INTO films VALUES ('UA502', 'Bananas', 105, DEFAULT, 
'Comedy', '82 minutes');
```

To insert a row consisting entirely of default values:

``` pre
INSERT INTO films DEFAULT VALUES;
```

To insert multiple rows using the multirow `VALUES` syntax:

``` pre
INSERT INTO films (code, title, did, date_prod, kind) VALUES
    ('B6717', 'Tampopo', 110, '1985-02-10', 'Comedy'),
    ('HG120', 'The Dinner Game', 140, DEFAULT, 'Comedy');
```

This example inserts some rows into table `films` from a table `tmp_films` with the same column layout as `films`:

``` pre
INSERT INTO films SELECT * FROM tmp_films WHERE date_prod < 
'2004-05-07';
```

## <a id="topic1__section8"></a>Compatibility

`INSERT` conforms to the SQL standard. The case in which a column name list is omitted, but not all the columns are filled from the `VALUES` clause or query, is disallowed by the standard.

Possible limitations of the *query* clause are documented under `SELECT`.

## <a id="topic1__section9"></a>See Also

[COPY](COPY.html), [SELECT](SELECT.html), [CREATE EXTERNAL TABLE](CREATE-EXTERNAL-TABLE.html)
