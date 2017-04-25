---
title: Define an External Table with Single Row Error Isolation
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

The following example logs errors internally in HAWQ and sets an error threshold of 10 errors.

``` sql
=# CREATE EXTERNAL TABLE ext_expenses ( name text, date date, amount float4, category text, desc1 text )
   LOCATION ('gpfdist://etlhost-1:8081/*', 'gpfdist://etlhost-2:8082/*')
   FORMAT 'TEXT' (DELIMITER '|')
   LOG ERRORS INTO errortable SEGMENT REJECT LIMIT 10 ROWS;
```

The following example creates an external table, *ext\_expenses*, sets an error threshold of 10 errors, and writes error rows to the table *err\_expenses*.

``` sql
=# CREATE EXTERNAL TABLE ext_expenses
     ( name text, date date, amount float4, category text, desc1 text )
   LOCATION ('gpfdist://etlhost-1:8081/*', 'gpfdist://etlhost-2:8082/*')
   FORMAT 'TEXT' (DELIMITER '|')
   LOG ERRORS INTO err_expenses SEGMENT REJECT LIMIT 10 ROWS;
```


