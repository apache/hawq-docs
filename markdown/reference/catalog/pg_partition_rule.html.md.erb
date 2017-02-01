---
title: pg_partition_rule
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

The `pg_partition_rule` system catalog table is used to track partitioned tables, their check constraints, and data containment rules. Each row of `pg_partition_rule` represents either a leaf partition (the bottom level partitions that contain data), or a branch partition (a top or mid-level partition that is used to define the partition hierarchy, but does not contain any data).

<a id="topic1__hc179425"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_partition\_rule</span>


| column              | type     | references                 | description                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------|----------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `paroid`            | oid      | pg\_partition.oid          | Row identifier of the partitioning level (from [pg\_partition](pg_partition.html#topic1)) to which this partition belongs. In the case of a branch partition, the corresponding table (identified by `pg_partition_rule`) is an empty container table. In case of a leaf partition, the table contains the rows for that partition containment rule. |
| `parchildrelid`     | oid      | pg\_class.oid              | The table identifier of the partition (child table).                                                                                                                                                                                                                                                                                                                         |
| `parparentrule`     | oid      | pg\_partition\_rule.paroid | The row identifier of the rule associated with the parent table of this partition.                                                                                                                                                                                                                                                                                           |
| `parname`           | name     |                            | The given name of this partition.                                                                                                                                                                                                                                                                                                                                            |
| `parisdefault`      | boolean  |                            | Whether or not this partition is a default partition.                                                                                                                                                                                                                                                                                                                        |
| `parruleord`        | smallint |                            | For range partitioned tables, the rank of this partition on this level of the partition hierarchy.                                                                                                                                                                                                                                                                           |
| `parrangestartincl` | boolean  |                            | For range partitioned tables, whether or not the starting value is inclusive.                                                                                                                                                                                                                                                                                                |
| `parrangeendincl`   | boolean  |                            | For range partitioned tables, whether or not the ending value is inclusive.                                                                                                                                                                                                                                                                                                  |
| `parrangestart`     | text     |                            | For range partitioned tables, the starting value of the range.                                                                                                                                                                                                                                                                                                               |
| `parrangeend`       | text     |                            | For range partitioned tables, the ending value of the range.                                                                                                                                                                                                                                                                                                                 |
| `parrangeevery`     | text     |                            | For range partitioned tables, the interval value of the `EVERY` clause.                                                                                                                                                                                                                                                                                                      |
| `parlistvalues`     | text     |                            | For list partitioned tables, the list of values assigned to this partition.                                                                                                                                                                                                                                                                                                  |
| `parreloptions`     | text     |                            | An array describing the storage characteristics of the particular partition.                                                                                                                                                                                                                                                                                                 |



