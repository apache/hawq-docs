---
title: Basic Data Operations
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

This topic describes basic data operations that you perform in HAWQ.

## <a id="topic3"></a>Inserting Rows

Use the `INSERT` command to create rows in a table. This command requires the table name and a value for each column in the table; you may optionally specify the column names in any order. If you do not specify column names, list the data values in the order of the columns in the table, separated by commas.

For example, to specify the column names and the values to insert:

``` sql
INSERT INTO products (name, price, product_no) VALUES ('Cheese', 9.99, 1);
```

To specify only the values to insert:

``` sql
INSERT INTO products VALUES (1, 'Cheese', 9.99);
```

Usually, the data values are literals (constants), but you can also use scalar expressions. For example:

``` sql
INSERT INTO films SELECT * FROM tmp_films WHERE date_prod <
'2004-05-07';
```

You can insert multiple rows in a single command. For example:

``` sql
INSERT INTO products (product_no, name, price) VALUES
    (1, 'Cheese', 9.99),
    (2, 'Bread', 1.99),
    (3, 'Milk', 2.99);
```

To insert data into a partitioned table, you specify the root partitioned table, the table created with the `CREATE TABLE` command. You also can specify a leaf child table of the partitioned table in an `INSERT` command. An error is returned if the data is not valid for the specified leaf child table. Specifying a child table that is not a leaf child table in the `INSERT` command is not supported.

To insert large amounts of data, use external tables or the `COPY` command. These load mechanisms are more efficient than `INSERT` for inserting large quantities of rows. See [Loading and Unloading Data](load/g-loading-and-unloading-data.html#topic1) for more information about bulk data loading.

## <a id="topic9"></a>Vacuuming the System Catalog Tables

Only HAWQ system catalog tables use multiple version concurrency control. Deleted or updated data rows in the catalog tables occupy physical space on disk even though new transactions cannot see them. Periodically running the `VACUUM` command removes these expired rows. 

The `VACUUM` command also collects table-level statistics such as the number of rows and pages.

For example:

``` sql
VACUUM pg_class;
```

### <a id="topic10"></a>Configuring the Free Space Map

Expired rows are held in the *free space map*. The free space map must be sized large enough to hold all expired rows in your database. If not, a regular `VACUUM` command cannot reclaim space occupied by expired rows that overflow the free space map.

**Note:** `VACUUM FULL` is not recommended with HAWQ because it is not safe for large tables and may take an unacceptably long time to complete. See [VACUUM](../reference/sql/VACUUM.html#topic1).

Size the free space map with the following server configuration parameters:

-   `max_fsm_pages`
-   `max_fsm_relations`
