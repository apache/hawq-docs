---
title: pg_largeobject
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

The `pg_largeobject` system catalog table holds the data making up 'large objects'. A large object is identified by an OID assigned when it is created. Each large object is broken into segments or 'pages' small enough to be conveniently stored as rows in `pg_largeobject`. The amount of data per page is defined to be `LOBLKSIZE` (which is currently `BLCKSZ`/4, or typically 8K).

Each row of `pg_largeobject` holds data for one page of a large object, beginning at byte offset (*pageno*` * LOBLKSIZE`) within the object. The implementation allows sparse storage: pages may be missing, and may be shorter than `LOBLKSIZE` bytes even if they are not the last page of the object. Missing regions within a large object read as zeroes.

<a id="topic1__gt143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_largeobject</span>

| column   | type    | references | description                                                                                             |
|----------|---------|------------|---------------------------------------------------------------------------------------------------------|
| `loid`   | oid     |            | Identifier of the large object that includes this page.                                                 |
| `pageno` | integer |            | Page number of this page within its large object (counting from zero).                                  |
| `data`   | bytea   |            | Actual data stored in the large object. This will never be more than `LOBLKSIZE` bytes and may be less. |



