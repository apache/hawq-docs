---
title: Using MADLib with Ranger Authorization
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


You can use MADlib, an open source library for in-database analytics, with your HAWQ installation. MADlib functions typically operate on source, output, and model tables. When Ranger is enabled for HAWQ authorization, you will need to explicitly provide access to all MADlib-related databases, schemas, tables, and functions to the appropriate users.  

Consider the following when setting up HAWQ Ranger policies for MADlib access:

- Assign `temp` permission to the database(s) on which users will run MADlib functions. This permission is required because MADlib creates temporary tables at runtime.
- MADlib users often share their output tables. If this is the case in your deployment, create a shared schema dedicated to output tables, assigning `usage-schema` and `create` privileges to this shared schema to all MADlib users. 
    - When calling a MADlib function, prepend the output table name with the shared schema name; for example, `shared_schema.output_table1`. This ensures that all tables created by the MADlib function (model summary tables, dictionary tables, etc.) are written to the same, accessible shared schema.
    - MADlib sometimes creates output tables in addition to the one specified by the user. Prepending the shared schema name to the output table name ensures that these MADlib-generated output tables are accessible. 
- Assign the `create-schema` database permission to those MADlib users who choose not to share their output tables. This permits those users to create private schemas for their MADlib output tables, rendering them inaccessible to other users.

- `madlib` Schema-Level Permissions
    - By default, MADlib is installed in a schema named `madlib`. You can choose to install MADlib in a different schema. References to `madlib` in the list below apply to the schema in which you installed MADlib.
    - Assign `usage-schema` and `create` privileges to the `madlib` schema.
    - Assign `execute` permissions on all functions within the `madlib` schema, including any functions called within.
    - Assign `insert` and `select` permissions to all tables within the `madlib` schema.
    - Assign the `usage-schema` and `create` permissions for the current schema, and any schema in which the source, output, and model tables may reside.
