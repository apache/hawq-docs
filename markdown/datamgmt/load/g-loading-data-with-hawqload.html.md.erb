---
title: Loading Data with hawq load
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

The HAWQ `hawq load` utility loads data using readable external tables and the HAWQ parallel file server ( `gpfdist` or `gpfdists`). It handles parallel file-based external table setup and allows users to configure their data format, external table definition, and `gpfdist` or `gpfdists` setup in a single configuration file.

## <a id="topic62__du168147"></a>To use hawq load

1.  Ensure that your environment is set up to run `hawq                         load`. Some dependent files from your HAWQ /&gt; installation are required, such as `gpfdist` and Python, as well as network access to the HAWQ segment hosts.
2.  Create your load control file. This is a YAML-formatted file that specifies the HAWQ connection information, `gpfdist` configuration information, external table options, and data format.

    For example:

    ``` pre
    ---
    VERSION: 1.0.0.1
    DATABASE: ops
    USER: gpadmin
    HOST: mdw-1
    PORT: 5432
    GPLOAD:
       INPUT:
        - SOURCE:
             LOCAL_HOSTNAME:
               - etl1-1
               - etl1-2
               - etl1-3
               - etl1-4
             PORT: 8081
             FILE: 
               - /var/load/data/*
        - COLUMNS:
               - name: text
               - amount: float4
               - category: text
               - description: text
               - date: date
        - FORMAT: text
        - DELIMITER: '|'
        - ERROR_LIMIT: 25
        - ERROR_TABLE: payables.err_expenses
       OUTPUT:
        - TABLE: payables.expenses
        - MODE: INSERT
    SQL:
       - BEFORE: "INSERT INTO audit VALUES('start', current_timestamp)"
       - AFTER: "INSERT INTO audit VALUES('end', current_timestamp)"
    ```

3.  Run `hawq load`, passing in the load control file. For example:

    ``` shell
    $ hawq load -f my_load.yml
    ```


