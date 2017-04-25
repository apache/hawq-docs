---
title: Defining a File-Based Writable External Table
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

Writable external tables that output data to files use the HAWQ parallel file server program, `gpfdist`, or HAWQ Extensions Framework (PXF).

Use the `CREATE WRITABLE EXTERNAL TABLE` command to define the external table and specify the location and format of the output files.

-   With a writable external table using the `gpfdist` protocol, the HAWQ segments send their data to `gpfdist`, which writes the data to the named file. `gpfdist` must run on a host that the HAWQ segments can access over the network. `gpfdist` points to a file location on the output host and writes data received from the HAWQ segments to the file. To divide the output data among multiple files, list multiple `gpfdist` URIs in your writable external table definition.
-   A writable external web table sends data to an application as a stream of data. For example, unload data from HAWQ and send it to an application that connects to another database or ETL tool to load the data elsewhere. Writable external web tables use the `EXECUTE` clause to specify a shell command, script, or application to run on the segment hosts and accept an input stream of data. See [Defining a Command-Based Writable External Web Table](g-defining-a-command-based-writable-external-web-table.html#topic71) for more information about using `EXECUTE` commands in a writable external table definition.

You can optionally declare a distribution policy for your writable external tables. By default, writable external tables use a random distribution policy. If the source table you are exporting data from has a hash distribution policy, defining the same distribution key column(s) for the writable external table improves unload performance by eliminating the requirement to move rows over the interconnect. If you unload data from a particular table, you can use the `LIKE` clause to copy the column definitions and distribution policy from the source table.

-   **[Example - HAWQ file server (gpfdist)](../../datamgmt/load/g-example-hawq-file-server-gpfdist.html)**


