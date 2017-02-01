---
title: pg_shdepend
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

The `pg_shdepend` system catalog table records the dependency relationships between database objects and shared objects, such as roles. This information allows HAWQ to ensure that those objects are unreferenced before attempting to delete them. See also [pg\_depend](pg_depend.html#topic1), which performs a similar function for dependencies involving objects within a single database. Unlike most system catalogs, `pg_shdepend` is shared across all databases of HAWQ system: there is only one copy of `pg_shdepend` per system, not one per database.

In all cases, a `pg_shdepend` entry indicates that the referenced object may not be dropped without also dropping the dependent object. However, there are several subflavors identified by `deptype`:

-   **SHARED\_DEPENDENCY\_OWNER (o)** — The referenced object (which must be a role) is the owner of the dependent object.
-   **SHARED\_DEPENDENCY\_ACL (a)** — The referenced object (which must be a role) is mentioned in the ACL (access control list) of the dependent object.
-   **SHARED\_DEPENDENCY\_PIN (p)** — There is no dependent object; this type of entry is a signal that the system itself depends on the referenced object, and so that object must never be deleted. Entries of this type are created only by system initialization. The columns for the dependent object contain zeroes. <a id="topic1__ho143898"></a>

<span class="tablecap">Table 1. pg\_catalog.pg\_shdepend</span>

| column         | type    | references       | description                                                                                                |
|----------------|---------|------------------|------------------------------------------------------------------------------------------------------------|
| `dbid`         | oid     | pg\_database.oid | The OID of the database the dependent object is in, or zero for a shared object.                           |
| `classid`      | oid     | pg\_class.oid    | The OID of the system catalog the dependent object is in.                                                  |
| `objid`        | oid     | any OID column   | The OID of the specific dependent object.                                                                  |
| `objsubid `    | integer |                  | For a table column, this is the column number. For all other object types, this column is zero.            |
| `refclassid`   | oid     | pg\_class.oid    | The OID of the system catalog the referenced object is in (must be a shared catalog).                      |
| `refobjid`     | oid     | any OID column   | The OID of the specific referenced object.                                                                 |
| `refobjsubid ` | integer |                  | For a table column, this is the referenced column number. For all other object types, this column is zero. |
| `deptype`      | char    |                  | A code defining the specific semantics of this dependency relationship.                                    |




