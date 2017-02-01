---
title: Table Storage Model and Distribution Policy
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

HAWQ supports several storage models and a mix of storage models. When you create a table, you choose how to store its data. This topic explains the options for table storage and how to choose the best storage model for your workload.

**Note:** To simplify the creation of database tables, you can specify the default values for some table storage options with the HAWQ server configuration parameter `gp_default_storage_options`.

## <a id="topic39"></a>Row-Oriented Storage 

HAWQ provides storage orientation models of either row-oriented or Parquet tables. Evaluate performance using your own data and query workloads to determine the best alternatives.

-   Row-oriented storage: good for OLTP types of workloads with many iterative transactions and many columns of a single row needed all at once, so retrieving is efficient.

    **Note:** Column-oriented storage is no longer available. Parquet storage should be used, instead.

Row-oriented storage provides the best options for the following situations:

-   **Frequent INSERTs.** Where rows are frequently inserted into the table
-   **Number of columns requested in queries.** Where you typically request all or the majority of columns in the `SELECT` list or `WHERE` clause of your queries, choose a row-oriented model. 
-   **Number of columns in the table.** Row-oriented storage is most efficient when many columns are required at the same time, or when the row-size of a table is relatively small. 

## <a id="topic55"></a>Altering a Table 

The `ALTER TABLE`command changes the definition of a table. Use `ALTER TABLE` to change table attributes such as column definitions, distribution policy, storage model, and partition structure \(see also [Maintaining Partitioned Tables](ddl-partition.html)\). For example, to add a not-null constraint to a table column:

``` sql
=> ALTER TABLE address ALTER COLUMN street SET NOT NULL;
```

### <a id="topic56"></a>Altering Table Distribution 

`ALTER TABLE` provides options to change a table's distribution policy . When the table distribution options change, the table data is redistributed on disk, which can be resource intensive. You can also redistribute table data using the existing distribution policy.

### <a id="topic57"></a>Changing the Distribution Policy 

For partitioned tables, changes to the distribution policy apply recursively to the child partitions. This operation preserves the ownership and all other attributes of the table. For example, the following command redistributes the table sales across all segments using the customer\_id column as the distribution key:

``` sql
ALTER TABLE sales SET DISTRIBUTED BY (customer_id);
```

When you change the hash distribution of a table, table data is automatically redistributed. Changing the distribution policy to a random distribution does not cause the data to be redistributed. For example:

``` sql
ALTER TABLE sales SET DISTRIBUTED RANDOMLY;
```

### <a id="topic58"></a>Redistributing Table Data 

To redistribute table data for tables with a random distribution policy \(or when the hash distribution policy has not changed\) use `REORGANIZE=TRUE`. Reorganizing data may be necessary to correct a data skew problem, or when segment resources are added to the system. For example, the following command redistributes table data across all segments using the current distribution policy, including random distribution.

``` sql
ALTER TABLE sales SET WITH (REORGANIZE=TRUE);
```

## <a id="topic62"></a>Dropping a Table 

The`DROP TABLE`command removes tables from the database. For example:

``` sql
DROP TABLE mytable;
```

`DROP TABLE` always removes any indexes, rules, triggers, and constraints that exist for the target table. Specify `CASCADE`to drop a table that is referenced by a view. `CASCADE` removes dependent views.

To empty a table of rows without removing the table definition, use `TRUNCATE`. For example:

``` sql
TRUNCATE mytable;
```
