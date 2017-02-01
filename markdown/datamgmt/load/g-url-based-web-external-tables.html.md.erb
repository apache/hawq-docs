---
title: URL-based Web External Tables
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

A URL-based web table accesses data from a web server using the HTTP protocol. Web table data is dynamic; the data is not rescannable.

Specify the `LOCATION` of files on a web server using `http://`. The web data file(s) must reside on a web server that HAWQ segment hosts can access. The number of URLs specified corresponds to the minimum number of virtual segments that work in parallel to access the web table.

The following sample command defines a web table that gets data from several URLs.

``` sql
=# CREATE EXTERNAL WEB TABLE ext_expenses (
    name text, date date, amount float4, category text, description text) 
LOCATION ('http://intranet.company.com/expenses/sales/file.csv',
          'http://intranet.company.com/expenses/exec/file.csv',
          'http://intranet.company.com/expenses/finance/file.csv',
          'http://intranet.company.com/expenses/ops/file.csv',
          'http://intranet.company.com/expenses/marketing/file.csv',
          'http://intranet.company.com/expenses/eng/file.csv' 
      )
FORMAT 'CSV' ( HEADER );
```


