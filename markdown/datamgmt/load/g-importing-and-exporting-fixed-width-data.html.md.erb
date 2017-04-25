---
title: Importing and Exporting Fixed Width Data
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

Specify custom formats for fixed-width data with the HAWQ functions `fixedwith_in` and `fixedwidth_out`. These functions already exist in the file `$GPHOME/share/postgresql/cdb_external_extensions.sql`. The following example declares a custom format, then calls the `fixedwidth_in` function to format the data.

``` sql
CREATE READABLE EXTERNAL TABLE students (
  name varchar(20), address varchar(30), age int)
LOCATION ('gpfdist://mdw:8081/students.txt')
FORMAT 'CUSTOM' (formatter=fixedwidth_in, name='20', address='30', age='4');
```

The following options specify how to import fixed width data.

-   Read all the data.

    To load all the fields on a line of fixed with data, you must load them in their physical order. You must specify the field length, but cannot specify a starting and ending position. The fields names in the fixed width arguments must match the order in the field list at the beginning of the `CREATE TABLE` command.

-   Set options for blank and null characters.

    Trailing blanks are trimmed by default. To keep trailing blanks, use the `preserve_blanks=on` option.You can reset the trailing blanks option to the default with the `preserve_blanks=off` option.

    Use the null=`'null_string_value'` option to specify a value for null characters.

-   If you specify `preserve_blanks=on`, you must also define a value for null characters.
-   If you specify `preserve_blanks=off`, null is not defined, and the field contains only blanks, HAWQ writes a null to the table. If null is defined, HAWQ writes an empty string to the table.

    Use the `line_delim='line_ending'` parameter to specify the line ending character. The following examples cover most cases. The `E` specifies an escape string constant.

    ``` pre
    line_delim=E'\n'
    line_delim=E'\r'
    line_delim=E'\r\n'
    line_delim='abc'
    ```


