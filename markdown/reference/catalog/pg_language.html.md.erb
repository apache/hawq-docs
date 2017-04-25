---
title: pg_language
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

The `pg_language` system catalog table registers languages in which you can write functions or stored procedures. It is populated by `CREATE LANGUAGE`.

<a id="topic1__gs143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_language</span>

| column          | type        | references   | description                                                                                                                                                                                                                                   |
|-----------------|-------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `lanname`       | name        |              | Name of the language.                                                                                                                                                                                                                         |
| `lanispl `      | boolean     |              | This is false for internal languages (such as SQL) and true for user-defined languages. Currently, `pg_dump` still uses this to determine which languages need to be dumped, but this may be replaced by a different mechanism in the future. |
| `lanpltrusted ` | boolean     |              | True if this is a trusted language, which means that it is believed not to grant access to anything outside the normal SQL execution environment. Only superusers may create functions in untrusted languages.                                |
| `lanplcallfoid` | oid         | pg\_proc.oid | For noninternal languages this references the language handler, which is a special function that is responsible for executing all functions that are written in the particular language.                                                      |
| `lanvalidator`  | oid         | pg\_proc.oid | This references a language validator function that is responsible for checking the syntax and validity of new functions when they are created. Zero if no validator is provided.                                                              |
| `lanacl `       | aclitem\[\] |              | Access privileges for the language.                                                                                                                                                                                                           |




