---
title: pg_constraint
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

The `pg_constraint` system catalog table stores check and foreign key constraints on tables. Column constraints are not treated specially. Every column constraint is equivalent to some table constraint. Not-null constraints are represented in the [pg\_attribute](pg_attribute.html#topic1) catalog table. Check constraints on domains are stored here, too.

<a id="topic1__gh143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_constraint</span>

| column          | type         | references           | description                                                                                                                                                                                                                                                                                                   |
|-----------------|--------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `conname`       | name         |                      | Constraint name                                                                                                                                                                                                                                                                                               |
| `connamespace`  | oid          | pg\_namespace.oid    | The OID of the namespace (schema) that contains this constraint.                                                                                                                                                                                                                                              |
| `contype `      | char         |                      | `c` = check constraint, `f` = foreign key constraint.                                                                                                                                                                                                                                                         |
| `condeferrable` | boolean      |                      | Is the constraint deferrable?                                                                                                                                                                                                                                                                                 |
| `condeferred `  | boolean      |                      | Is the constraint deferred by default?                                                                                                                                                                                                                                                                        |
| `conrelid`      | oid          | pg\_class.oid        | The table this constraint is on; 0 if not a table constraint.                                                                                                                                                                                                                                                 |
| `contypid `     | oid          | pg\_type.oid         | The domain this constraint is on; 0 if not a domain constraint.                                                                                                                                                                                                                                               |
| `confrelid`     | oid          | pg\_class.oid        | If a foreign key, the referenced table; else 0.                                                                                                                                                                                                                                                               |
| `confupdtype`   | char         |                      | Foreign key update action code.                                                                                                                                                                                                                                                                               |
| `confdeltype`   | char         |                      | Foreign key deletion action code.                                                                                                                                                                                                                                                                             |
| `confmatchtype` | char         |                      | Foreign key match type.                                                                                                                                                                                                                                                                                       |
| `conkey`        | smallint\[\] | pg\_attribute.attnum | If a table constraint, list of columns which the constraint constrains.                                                                                                                                                                                                                                       |
| `confkey`       | smallint\[\] | pg\_attribute.attnum | If a foreign key, list of the referenced columns.                                                                                                                                                                                                                                                             |
| `conbin`        | text         |                      | If a check constraint, an internal representation of the expression.                                                                                                                                                                                                                                          |
| `consrc`        | text         |                      | If a check constraint, a human-readable representation of the expression. This is not updated when referenced objects change; for example, it won't track renaming of columns. Rather than relying on this field, it is best to use `pg_get_constraintdef()` to extract the definition of a check constraint. |




