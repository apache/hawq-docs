---
title: pg_index
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

The `pg_index` system catalog table contains part of the information about indexes. The rest is mostly in [pg\_class](pg_class.html#topic1).

<a id="topic1__gq143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_index</span>

| column           | type       | references           | description                                                                                                                                                                                                                                                                                                                                             |
|------------------|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `indexrelid`     | oid        | pg\_class.oid        | The OID of the `pg_class` entry for this index.                                                                                                                                                                                                                                                                                                          |
| `indrelid`       | oid        | pg\_class.oid        | The OID of the `pg_class` entry for the table this index is for.                                                                                                                                                                                                                                                                                         |
| `indnatts`       | smallint   |                      | The number of columns in the index (duplicates `pg_class.relnatts`).                                                                                                                                                                                                                                                                                     |
| `indisunique`    | boolean    |                      | If true, this is a unique index.                                                                                                                                                                                                                                                                                                                        |
| `indisclustered` | boolean    |                      | If true, the table was last clustered on this index via the `CLUSTER` command.                                                                                                                                                                                                                                                                          |
| `indisvalid`     | boolean    |                      | If true, the index is currently valid for queries. False means the index is possibly incomplete: it must still be modified by `INSERT` operations, but it cannot safely be used for queries.                                                                                                                                                   |
| `indkey`         | int2vector | pg\_attribute.attnum | This is an array of indnatts values that indicate which table columns this index indexes. For example a value of 1 3 would mean that the first and the third table columns make up the index key. A zero in this array indicates that the corresponding index attribute is an expression over the table columns, rather than a simple column reference. |
| `indclass`       | oidvector  | pg\_opclass.oid      | For each column in the index key, this contains the OID of the operator class to use.                                                                                                                                                                                                                                                                    |
| `indexprs`       | text       |                      | Expression trees (in `nodeToString()` representation) for index attributes that are not simple column references. This is a list with one element for each zero entry in indkey. NULL if all index attributes are simple references.                                                                                                                    |
| `indpred`        | text       |                      | Expression tree (in `nodeToString()` representation) for partial index predicate. NULL if not a partial index.                                                                                                                                                                                                                                          |


