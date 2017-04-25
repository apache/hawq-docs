---
title: Loading and Unloading Data
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

The topics in this section describe methods for loading and writing data into and out of HAWQ, and how to format data files. It also covers registering HDFS files and folders directly into HAWQ internal tables.

HAWQ supports high-performance parallel data loading and unloading, and for smaller amounts of data, single file, non-parallel data import and export.

HAWQ can read from and write to several types of external data sources, including text files, Hadoop file systems, and web servers.

-   The `COPY` SQL command transfers data between an external text file on the master host and a HAWQ database table.
-   External tables allow you to query data outside of the database directly and in parallel using SQL commands such as `SELECT`, `JOIN`, or `SORT           EXTERNAL TABLE DATA`, and you can create views for external tables. External tables are often used to load external data into a regular database table using a command such as `CREATE TABLE table AS SELECT * FROM ext_table`.
-   External web tables provide access to dynamic data. They can be backed with data from URLs accessed using the HTTP protocol or by the output of an OS script running on one or more segments.
-   The `gpfdist` utility is the HAWQ parallel file distribution program. It is an HTTP server that is used with external tables to allow HAWQ segments to load external data in parallel, from multiple file systems. You can run multiple instances of `gpfdist` on different hosts and network interfaces and access them in parallel.
-   The `hawq load` utility automates the steps of a load task using a YAML-formatted control file.

The method you choose to load data depends on the characteristics of the source data—its location, size, format, and any transformations required.

In the simplest case, the `COPY` SQL command loads data into a table from a text file that is accessible to the HAWQ master instance. This requires no setup and provides good performance for smaller amounts of data. With the `COPY` command, the data copied into or out of the database passes between a single file on the master host and the database. This limits the total size of the dataset to the capacity of the file system where the external file resides and limits the data transfer to a single file write stream.

More efficient data loading options for large datasets take advantage of the HAWQ MPP architecture, using the HAWQ segments to load data in parallel. These methods allow data to load simultaneously from multiple file systems, through multiple NICs, on multiple hosts, achieving very high data transfer rates. External tables allow you to access external files from within the database as if they are regular database tables. When used with `gpfdist`, the HAWQ parallel file distribution program, external tables provide full parallelism by using the resources of all HAWQ segments to load or unload data.

HAWQ leverages the parallel architecture of the Hadoop Distributed File System to access files on that system.

-   **[Working with File-Based External Tables](../../datamgmt/load/g-working-with-file-based-ext-tables.html)**

-   **[Using the HAWQ File Server (gpfdist)](../../datamgmt/load/g-using-the-hawq-file-server--gpfdist-.html)**

-   **[Creating and Using Web External Tables](../../datamgmt/load/g-creating-and-using-web-external-tables.html)**

-   **[Loading Data Using an External Table](../../datamgmt/load/g-loading-data-using-an-external-table.html)**

-   **[Registering Files into HAWQ Internal Tables](../../datamgmt/load/g-register_files.html)**

-   **[Loading and Writing Non-HDFS Custom Data](../../datamgmt/load/g-loading-and-writing-non-hdfs-custom-data.html)**

-   **[Creating External Tables - Examples](../../datamgmt/load/creating-external-tables-examples.html#topic44)**

-   **[Handling Load Errors](../../datamgmt/load/g-handling-load-errors.html)**

-   **[Loading Data with hawq load](../../datamgmt/load/g-loading-data-with-hawqload.html)**

-   **[Loading Data with COPY](../../datamgmt/load/g-loading-data-with-copy.html)**

-   **[Running COPY in Single Row Error Isolation Mode](../../datamgmt/load/g-running-copy-in-single-row-error-isolation-mode.html)**

-   **[Optimizing Data Load and Query Performance](../../datamgmt/load/g-optimizing-data-load-and-query-performance.html)**

-   **[Unloading Data from HAWQ](../../datamgmt/load/g-unloading-data-from-hawq-database.html)**

-   **[Transforming XML Data](../../datamgmt/load/g-transforming-xml-data.html)**

-   **[Formatting Data Files](../../datamgmt/load/g-formatting-data-files.html)**


