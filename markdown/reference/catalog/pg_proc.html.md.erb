---
title: pg_proc
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

The `pg_proc` system catalog table stores information about functions (or procedures), both built-in functions and those defined by `CREATE FUNCTION`. The table contains data for aggregate and window functions as well as plain functions. If `proisagg` is true, there should be a matching row in `pg_aggregate`. If `proiswin` is true, there should be a matching row in `pg_window`.

For compiled functions, both built-in and dynamically loaded, `prosrc` contains the function's C-language name (link symbol). For all other currently-known language types, `prosrc` contains the function's source text. `probin` is unused except for dynamically-loaded C functions, for which it gives the name of the shared library file containing the function.

<a id="topic1__hg150092"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_proc</span>

| column           | type        | references        | description                                                                                                                                                                                                                                                                                                                                        |
|------------------|-------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `proname`        | name        |                   | Name of the function.                                                                                                                                                                                                                                                                                                                              |
| `pronamespace`   | oid         | pg\_namespace.oid | The OID of the namespace that contains this function.                                                                                                                                                                                                                                                                                              |
| `proowner`       | oid         | pg\_authid.oid    | Owner of the function.                                                                                                                                                                                                                                                                                                                             |
| `prolang`        | oid         | pg\_language.oid  | Implementation language or call interface of this function.                                                                                                                                                                                                                                                                                        |
| `proisagg`       | boolean     |                   | Function is an aggregate function.                                                                                                                                                                                                                                                                                                                 |
| `prosecdef`      | boolean     |                   | Function is a security definer (for example, a 'setuid' function).                                                                                                                                                                                                                                                                                 |
| `proisstrict`    | boolean     |                   | Function returns NULL if any call argument is NULL. In that case the function will not actually be called at all. Functions that are not strict must be prepared to handle NULL inputs.                                                                                                                                                            |
| `proretset`      | boolean     |                   | Function returns a set (multiple values of the specified data type).                                                                                                                                                                                                                                                                               |
| `provolatile`    | char        |                   | Tells whether the function's result depends only on its input arguments, or is affected by outside factors. `i` = *immutable* (always delivers the same result for the same inputs), `s` = *stable* (results (for fixed inputs) do not change within a scan), or `v` = *volatile* (results may change at any time or functions with side-effects). |
| `pronargs`       | smallint    |                   | Number of arguments.                                                                                                                                                                                                                                                                                                                               |
| `prorettype`     | oid         | pg\_type.oid      | Data type of the return value.                                                                                                                                                                                                                                                                                                                     |
| `proiswin`       | boolean     |                   | Function is neither an aggregate nor a scalar function, but a pure window function.                                                                                                                                                                                                                                                                |
| `proargtypes`    | oidvector   | pg\_type.oid      | An array with the data types of the function arguments. This includes only input arguments (including `INOUT` arguments), and thus represents the call signature of the function.                                                                                                                                                                  |
| `proallargtypes` | oid\[\]     | pg\_type.oid      | An array with the data types of the function arguments. This includes all arguments (including `OUT` and `INOUT` arguments); however, if all the arguments are `IN` arguments, this field will be null. Note that subscripting is 1-based, whereas for historical reasons proargtypes is subscripted from 0.                                       |
| `proargmodes`    | char\[\]    |                   | An array with the modes of the function arguments: `i` = `IN`, `o` = `OUT` , `b` = `INOUT`. If all the arguments are IN arguments, this field will be null. Note that subscripts correspond to positions of proallargtypes not proargtypes.                                                                                                        |
| `proargnames`    | text\[\]    |                   | An array with the names of the function arguments. Arguments without a name are set to empty strings in the array. If none of the arguments have a name, this field will be null. Note that subscripts correspond to positions of proallargtypes not proargtypes.                                                                                  |
| `prosrc `        | text        |                   | This tells the function handler how to invoke the function. It might be the actual source code of the function for interpreted languages, a link symbol, a file name, or just about anything else, depending on the implementation language/call convention.                                                                                       |
| `probin`         | bytea       |                   | Additional information about how to invoke the function. Again, the interpretation is language-specific.                                                                                                                                                                                                                                           |
| `proacl`         | aclitem\[\] |                   | Access privileges for the function as given by `GRANT`/`REVOKE`.                                                                                                                                                                                                                                                                                   |




