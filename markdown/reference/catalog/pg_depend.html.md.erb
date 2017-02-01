---
title: pg_depend
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

The `pg_depend` system catalog table records the dependency relationships between database objects. This information allows `DROP` commands to find which other objects must be dropped by `DROP CASCADE` or prevent dropping in the `DROP RESTRICT` case. See also [pg\_shdepend](pg_shdepend.html#topic1), which performs a similar function for dependencies involving objects that are shared across a HAWQ system.

In all cases, a `pg_depend` entry indicates that the referenced object may not be dropped without also dropping the dependent object. However, there are several subflavors identified by `deptype`:

-   **DEPENDENCY\_NORMAL (n)** — A normal relationship between separately-created objects. The dependent object may be dropped without affecting the referenced object. The referenced object may only be dropped by specifying `CASCADE`, in which case the dependent object is dropped, too. Example: a table column has a normal dependency on its data type.
-   **DEPENDENCY\_AUTO (a)** — The dependent object can be dropped separately from the referenced object, and should be automatically dropped (regardless of `RESTRICT` or `CASCADE` mode) if the referenced object is dropped. Example: a named constraint on a table is made autodependent on the table, so that it will go away if the table is dropped.
-   **DEPENDENCY\_INTERNAL (i)** — The dependent object was created as part of creation of the referenced object, and is really just a part of its internal implementation. A `DROP` of the dependent object will be disallowed outright (we'll tell the user to issue a `DROP` against the referenced object, instead). A `DROP` of the referenced object will be propagated through to drop the dependent object whether `CASCADE` is specified or not.
-   **DEPENDENCY\_PIN (p)** — There is no dependent object; this type of entry is a signal that the system itself depends on the referenced object, and so that object must never be deleted. Entries of this type are created only by system initialization. The columns for the dependent object contain zeroes. <a id="topic1__gk143898"></a>

<span class="tablecap">Table 1. pg\_catalog.pg\_depend</span>

    | column         | type    | references     | description                                                                                                |
    |----------------|---------|----------------|------------------------------------------------------------------------------------------------------------|
    | `classid`      | oid     | pg\_class.oid  | The OID of the system catalog the dependent object is in.                                                  |
    | `objid`        | oid     | any OID column | The OID of the specific dependent object.                                                                  |
    | `objsubid `    | integer |                | For a table column, this is the column number. For all other object types, this column is zero.            |
    | `refclassid`   | oid     | pg\_class.oid  | The OID of the system catalog the referenced object is in.                                                 |
    | `refobjid`     | oid     | any OID column | The OID of the specific referenced object.                                                                 |
    | `refobjsubid ` | integer |                | For a table column, this is the referenced column number. For all other object types, this column is zero. |
    | `deptype`      | char    |                | A code defining the specific semantics of this dependency relationship.                                    |


