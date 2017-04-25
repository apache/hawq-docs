---
title: pg_partition
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

The `pg_partition` system catalog table is used to track partitioned tables and their inheritance level relationships. Each row of `pg_partition` represents either the level of a partitioned table in the partition hierarchy, or a subpartition template description. The value of the attribute `paristemplate` determines what a particular row represents.

<a id="topic1__gz143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_partition</span>

| column          | type       | references      | description                                                                                                                                         |
|-----------------|------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `parrelid`      | oid        | pg\_class.oid   | The object identifier of the table.                                                                                                                 |
| `parkind`       | char       |                 | The partition type - `R` for range or `L` for list.                                                                                                 |
| `parlevel`      | smallint   |                 | The partition level of this row: 0 for the top-level parent table, 1 for the first level under the parent table, 2 for the second level, and so on. |
| `paristemplate` | boolean    |                 | Whether or not this row represents a subpartition template definition (true) or an actual partitioning level (false).                               |
| `parnatts`      | smallint   |                 | The number of attributes that define this level.                                                                                                    |
| `paratts`       | int2vector |                 | An array of the attribute numbers (as in `pg_attribute.attnum`) of the attributes that participate in defining this level.                          |
| `parclass`      | oidvector  | pg\_opclass.oid | The operator class identifier(s) of the partition columns.                                                                                          |


