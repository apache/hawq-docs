---
title: Creating and Managing Tables
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

HAWQ Tables are similar to tables in any relational database, except that table rows are distributed across the different segments in the system. When you create a table, you specify the table's distribution policy.

## <a id="topic26"></a>Creating a Table 

The `CREATE TABLE` command creates a table and defines its structure. When you create a table, you define:

-   The columns of the table and their associated data types. See [Choosing Column Data Types](#topic27).
-   Any table constraints to limit the data that a column or table can contain. See [Setting Table Constraints](#topic28).
-   The distribution policy of the table, which determines how HAWQ divides data is across the segments. See [Choosing the Table Distribution Policy](#topic34).
-   The way the table is stored on disk.
-   The table partitioning strategy for large tables, which specifies how the data should be divided. See [Creating and Managing Databases](../ddl/ddl-database.html).

### <a id="topic27"></a>Choosing Column Data Types 

The data type of a column determines the types of data values the column can contain. Choose the data type that uses the least possible space but can still accommodate your data and that best constrains the data. For example, use character data types for strings, date or timestamp data types for dates, and numeric data types for numbers.

There are no performance differences among the character data types `CHAR`, `VARCHAR`, and `TEXT` apart from the increased storage size when you use the blank-padded type. In most situations, use `TEXT` or `VARCHAR` rather than `CHAR`.

Use the smallest numeric data type that will accommodate your numeric data and allow for future expansion. For example, using `BIGINT` for data that fits in `INT` or `SMALLINT` wastes storage space. If you expect that your data values will expand over time, consider that changing from a smaller datatype to a larger datatype after loading large amounts of data is costly. For example, if your current data values fit in a `SMALLINT` but it is likely that the values will expand, `INT` is the better long-term choice.

Use the same data types for columns that you plan to use in cross-table joins. When the data types are different, the database must convert one of them so that the data values can be compared correctly, which adds unnecessary overhead.

HAWQ supports the parquet columnar storage format, which can increase performance on large queries. Use parquet tables for HAWQ internal tables.

### <a id="topic28"></a>Setting Table Constraints 

You can define constraints to restrict the data in your tables. HAWQ support for constraints is the same as PostgreSQL with some limitations, including:

-   `CHECK` constraints can refer only to the table on which they are defined.
-   `FOREIGN KEY` constraints are allowed, but not enforced.
-   Constraints that you define on partitioned tables apply to the partitioned table as a whole. You cannot define constraints on the individual parts of the table.

#### <a id="topic29"></a>Check Constraints 

Check constraints allow you to specify that the value in a certain column must satisfy a Boolean \(truth-value\) expression. For example, to require positive product prices:

``` sql
=> CREATE TABLE products
     ( product_no integer,
       name text,
       price numeric CHECK (price > 0) );
```

#### <a id="topic30"></a>Not-Null Constraints 

Not-null constraints specify that a column must not assume the null value. A not-null constraint is always written as a column constraint. For example:

``` sql
=> CREATE TABLE products
     ( product_no integer NOT NULL,
       name text NOT NULL,
       price numeric );
```

#### <a id="topic33"></a>Foreign Keys 

Foreign keys are not supported. You can declare them, but referential integrity is not enforced.

Foreign key constraints specify that the values in a column or a group of columns must match the values appearing in some row of another table to maintain referential integrity between two related tables. Referential integrity checks cannot be enforced between the distributed table segments of a HAWQ database.

### <a id="topic34"></a>Choosing the Table Distribution Policy 

All HAWQ tables are distributed. The default is `DISTRIBUTED RANDOMLY` \(round-robin distribution\) to determine the table row distribution. However, when you create or alter a table, you can optionally specify `DISTRIBUTED BY` to distribute data according to a hash-based policy. In this case, the `bucketnum` attribute sets the number of hash buckets used by a hash-distributed table. Columns of geometric or user-defined data types are not eligible as HAWQ distribution key columns. 

Randomly distributed tables have benefits over hash distributed tables. For example, after expansion, HAWQ's elasticity feature lets it automatically use more resources without needing to redistribute the data. For extremely large tables, redistribution is very expensive. Also, data locality for randomly distributed tables is better, especially after the underlying HDFS redistributes its data during rebalancing or because of DataNode failures. This is quite common when the cluster is large.

However, hash distributed tables can be faster than randomly distributed tables. For example, for TPCH queries, where there are several queries, HASH distributed tables can have performance benefits. Choose a distribution policy that best suits your application scenario. When you `CREATE TABLE`, you can also specify the `bucketnum` option. The `bucketnum` determines the number of hash buckets used in creating a hash-distributed table or for PXF external table intermediate processing. The number of buckets also affects how many virtual segments will be created when processing this data. The bucketnumber of a gpfdist external table is the number of gpfdist location, and the bucketnumber of a command external table is `ON #num`. PXF external tables use the `default_hash_table_bucket_number` parameter to control virtual segments. 

HAWQ's elastic execution runtime is based on virtual segments, which are allocated on demand, based on the cost of the query. Each node uses one physical segment and a number of dynamically allocated virtual segments distributed to different hosts, thus simplifying performance tuning. Large queries use large numbers of virtual segments, while smaller queries use fewer virtual segments. Tables do not need to be redistributed when nodes are added or removed.

In general, the more virtual segments are used, the faster the query will be executed. You can tune the parameters for `default_hash_table_bucket_number` and `hawq_rm_nvseg_perquery_limit` to adjust performance by controlling the number of virtual segments used for a query. However, be aware that if the value of `default_hash_table_bucket_number` is changed, data must be redistributed, which can be costly. Therefore, it is better to set the `default_hash_table_bucket_number` up front, if you expect to need a larger number of virtual segments. However, you might need to adjust the value in `default_hash_table_bucket_number` after cluster expansion, but should take care not to exceed the number of virtual segments per query set in `hawq_rm_nvseg_perquery_limit`. Refer to the recommended guidelines for setting the value of `default_hash_table_bucket_number`, later in this section.

For random or gpfdist external tables, as well as user-defined functions, the value set in the `hawq_rm_nvseg_perquery_perseg_limit` parameter limits the number of virtual segments that are used for one segment for one query, to optimize query resources. Resetting this parameter is not recommended.

Consider the following points when deciding on a table distribution policy.

-   **Even Data Distribution** — For the best possible performance, all segments should contain equal portions of data. If the data is unbalanced or skewed, the segments with more data must work harder to perform their portion of the query processing.
-   **Local and Distributed Operations** — Local operations are faster than distributed operations. Query processing is fastest if the work associated with join, sort, or aggregation operations is done locally, at the segment level. Work done at the system level requires distributing tuples across the segments, which is less efficient. When tables share a common distribution key, the work of joining or sorting on their shared distribution key columns is done locally. With a random distribution policy, local join operations are not an option.
-   **Even Query Processing** — For best performance, all segments should handle an equal share of the query workload. Query workload can be skewed if a table's data distribution policy and the query predicates are not well matched. For example, suppose that a sales transactions table is distributed based on a column that contains corporate names \(the distribution key\), and the hashing algorithm distributes the data based on those values. If a predicate in a query references a single value from the distribution key, query processing runs on only one segment. This works if your query predicates usually select data on a criteria other than corporation name. For queries that use corporation name in their predicates, it's possible that only one segment instance will handle the query workload.

HAWQ utilizes dynamic parallelism, which can affect the performance of a query execution significantly. Performance depends on the following factors:

-   The size of a randomly distributed table.
-   The `bucketnum` of a hash distributed table.
-   Data locality.
-   The values of `default_hash_table_bucket_number`, and `hawq_rm_nvseg_perquery_limit` \(including defaults and user-defined values\).

For any specific query, the first four factors are fixed values, while the configuration parameters in the last item can be used to tune performance of the query execution. In querying a random table, the query resource load is related to the data size of the table, usually one virtual segment for one HDFS block. As a result, querying a large table could use a large number of resources.

The `bucketnum` for a hash table specifies the number of hash buckets to be used in creating virtual segments. A HASH distributed table is created with `default_hash_table_bucket_number` buckets. The default bucket value can be changed in session level or in the `CREATE TABLE` DDL by using the `bucketnum` storage parameter.

In an Ambari-managed HAWQ cluster, the default bucket number \(`default_hash_table_bucket_number`\) is derived from the number of segment nodes. In command-line-managed HAWQ environments, you can use the `--bucket_number` option of `hawq init` to explicitly set `default_hash_table_bucket_number` during cluster initialization.

**Note:** For best performance with large tables, the number of buckets should not exceed the value of the `default_hash_table_bucket_number` parameter. Small tables can use one segment node, `WITH bucketnum=1`. For larger tables, the `bucketnum` is set to a multiple of the number of segment nodes, for the best load balancing on different segment nodes. The elastic runtime will attempt to find the optimal number of buckets for the number of nodes being processed. Larger tables need more virtual segments, and hence use larger numbers of buckets.

The following statement creates a table “sales” with 8 buckets, which would be similar to a hash-distributed table on 8 segments.

``` sql
=> CREATE TABLE sales(id int, profit float)  WITH (bucketnum=8) DISTRIBUTED BY (id);
```

There are four ways of creating a table from an origin table. The ways in which the new table is generated from the original table are listed below.

<table>
  <tr>
    <th></th>
    <th>Syntax</th>
  </tr>
  <tr><td>INHERITS</td><td><pre><code>CREATE TABLE new_table INHERITS (origintable) [WITH(bucketnum=x)] <br/>[DISTRIBUTED BY col]</code></pre></td></tr>
  <tr><td>LIKE</td><td><pre><code>CREATE TABLE new_table (LIKE origintable) [WITH(bucketnum=x)] <br/>[DISTRIBUTED BY col]</code></pre></td></tr>
  <tr><td>AS</td><td><pre><code>CREATE TABLE new_table [WITH(bucketnum=x)] AS SUBQUERY [DISTRIBUTED BY col]</code></pre></td></tr>
  <tr><td>SELECT INTO</td><td><pre><code>CREATE TABLE origintable [WITH(bucketnum=x)] [DISTRIBUTED BY col]; SELECT * <br/>INTO new_table FROM origintable;</code></pre></td></tr>
</table>

The optional `INHERITS` clause specifies a list of tables from which the new table automatically inherits all columns. Hash tables inherit bucketnumbers from their origin table if not otherwise specified. If `WITH` specifies `bucketnum` in creating a hash-distributed table, it will be copied. If distribution is specified by column, the table will inherit it. Otherwise, the table will use default distribution from `default_hash_table_bucket_number`.

The `LIKE` clause specifies a table from which the new table automatically copies all column names, data types, not-null constraints, and distribution policy. If a `bucketnum` is specified, it will be copied. Otherwise, the table will use default distribution.

For hash tables, the `SELECT INTO` function always uses random distribution.

#### <a id="topic_kjg_tqm_gv"></a>Declaring Distribution Keys 

`CREATE TABLE`'s optional clause `DISTRIBUTED BY` specifies the distribution policy for a table. The default is a random distribution policy. You can also choose to distribute data as a hash-based policy, where the `bucketnum` attribute sets the number of hash buckets used by a hash-distributed table. HASH distributed tables are created with the number of hash buckets specified by the `default_hash_table_bucket_number` parameter.

Policies for different application scenarios can be specified to optimize performance. The number of virtual segments used for query execution can now be tuned using the `hawq_rm_nvseg_perquery_limit `and `hawq_rm_nvseg_perquery_perseg_limit` parameters, in connection with the `default_hash_table_bucket_number` parameter, which sets the default `bucketnum`. For more information, see the guidelines for Virtual Segments in the next section and in [Query Performance](../query/query-performance.html#topic38).

#### <a id="topic_wff_mqm_gv"></a>Performance Tuning 

Adjusting the values of the configuration parameters `default_hash_table_bucket_number` and `hawq_rm_nvseg_perquery_limit` can tune performance by controlling the number of virtual segments being used. In most circumstances, HAWQ's elastic runtime will dynamically allocate virtual segments to optimize performance, so further tuning should not be needed..

Hash tables are created using the value specified in `default_hash_table_bucket_number`. Queries for hash tables use a fixed number of buckets, regardless of the amount of data present. Explicitly setting `default_hash_table_bucket_number` can be useful in managing resources. If you desire a larger or smaller number of hash buckets, set this value before you create tables. Resources are dynamically allocated to a multiple of the number of nodes. If you use `hawq init --bucket_number` to set the value of `default_hash_table_bucket_number` during cluster initialization or expansion, the value should not exceed the value of `hawq_rm_nvseg_perquery_limit`. This server parameter defines the maximum number of virtual segments that can be used for a query \(default = 512, with a maximum of 65535\). Modifying the value to greater than 1000 segments is not recommended.

The following per-node guidelines apply to values for `default_hash_table_bucket_number`.

|Number of Nodes|default\_hash\_table\_bucket\_number value|
|---------------|------------------------------------------|
|<= 85|6 \* \#nodes|
|\> 85 and <= 102|5 \* \#nodes|
|\> 102 and <= 128|4 \* \#nodes|
|\> 128 and <= 170|3 \* \#nodes|
|\> 170 and <= 256|2 \* \#nodes|
|\> 256 and <= 512|1 \* \#nodes|
|\> 512|512|

Reducing the value of `hawq_rm_nvseg_perquery_perseg_limit`can improve concurrency and increasing the value of `hawq_rm_nvseg_perquery_perseg_limit`could possibly increase the degree of parallelism. However, for some queries, increasing the degree of parallelism will not improve performance if the query has reached the limits set by the hardware. Therefore, increasing the value of `hawq_rm_nvseg_perquery_perseg_limit` above the default value is not recommended. Also, changing the value of `default_hash_table_bucket_number` after initializing a cluster means the hash table data must be redistributed. If you are expanding a cluster, you might wish to change this value, but be aware that retuning could adversely affect performance.
