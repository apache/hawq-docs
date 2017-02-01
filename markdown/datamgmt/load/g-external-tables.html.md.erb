---
title: Accessing File-Based External Tables
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

External tables enable accessing external files as if they are regular database tables. They are often used to move data into and out of a HAWQ database.

To create an external table definition, you specify the format of your input files and the location of your external data sources. For information input file formats, see [Formatting Data Files](g-formatting-data-files.html#topic95).

Use one of the following protocols to access external table data sources. You cannot mix protocols in `CREATE EXTERNAL TABLE` statements:

-   `gpfdist://` points to a directory on the file host and serves external data files to all HAWQ segments in parallel. See [gpfdist Protocol](g-gpfdist-protocol.html#topic_sny_yph_kr).
-   `gpfdists://` is the secure version of `gpfdist`. See [gpfdists Protocol](g-gpfdists-protocol.html#topic_sny_yph_kr).
-   `pxf://` specifies data accessed through the HAWQ Extensions Framework (PXF). PXF is a service that uses plug-in Java classes to read and write data in external data sources. PXF includes plug-ins to access data in HDFS, HBase, and Hive. Custom plug-ins can be written to access other external data sources.

External tables allow you to access external files from within the database as if they are regular database tables. Used with `gpfdist`, the HAWQ parallel file distribution program, or HAWQ Extensions Framework (PXF), external tables provide full parallelism by using the resources of all HAWQ segments to load or unload data.

You can query external table data directly and in parallel using SQL commands such as `SELECT`, `JOIN`, or `SORT EXTERNAL TABLE             DATA`, and you can create views for external tables.

The steps for using external tables are:

1.  Define the external table.
2.  Start the gpfdist file server(s) if you plan to use the `gpfdist` or `gpdists` protocols.
3.  Place the data files in the correct locations.
4.  Query the external table with SQL commands.

HAWQ provides readable and writable external tables:

-   Readable external tables for data loading. Readable external tables support basic extraction, transformation, and loading (ETL) tasks common in data warehousing. HAWQ segment instances read external table data in parallel to optimize large load operations. You cannot modify readable external tables.
-   Writable external tables for data unloading. Writable external tables support:

    -   Selecting data from database tables to insert into the writable external table.
    -   Sending data to an application as a stream of data. For example, unload data from HAWQ and send it to an application that connects to another database or ETL tool to load the data elsewhere.
    -   Receiving output from HAWQ parallel MapReduce calculations.

    Writable external tables allow only `INSERT` operations.

External tables can be file-based or web-based.

-   Regular (file-based) external tables access static flat files. Regular external tables are rescannable: the data is static while the query runs.
-   Web (web-based) external tables access dynamic data sources, either on a web server with the `http://` protocol or by executing OS commands or scripts. Web external tables are not rescannable: the data can change while the query runs.

Dump and restore operate only on external and web external table *definitions*, not on the data sources.


