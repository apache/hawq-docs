---
title: Table Distribution and Storage
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

HAWQ stores all table data, except the system table, in HDFS. When a user creates a table, the metadata is stored on the master's local file system and the table content is stored in HDFS.

In order to simplify table data management, all the data of one relation are saved under one HDFS folder.

For all HAWQ table storage formats, AO \(Append-Only\) and Parquet, the data files are splittable, so that HAWQ can assign multiple virtual segments to consume one data file concurrently. This increases the degree of query parallelism.

## Table Distribution Policy

The default table distribution policy in HAWQ is random.

Randomly distributed tables have some benefits over hash distributed tables. For example, after cluster expansion, HAWQ can use more resources automatically without redistributing the data. For huge tables, redistribution is very expensive, and data locality for randomly distributed tables is better after the underlying HDFS redistributes its data during rebalance or DataNode failures. This is quite common when the cluster is large.

On the other hand, for some queries, hash distributed tables are faster than randomly distributed tables. For example, hash distributed tables have some performance benefits for some TPC-H queries. You should choose the distribution policy that is best suited for your application's scenario.

See [Choosing the Table Distribution Policy](../ddl/ddl-table.html) for more details.

## Data Locality

Data is distributed across HDFS DataNodes. Since remote read involves network I/O, a data locality algorithm improves the local read ratio. HAWQ considers three aspects when allocating data blocks to virtual segments:

-   Ratio of local read
-   Continuity of file read
-   Data balance among virtual segments

## External Data Access

HAWQ can access data in external files using the HAWQ Extension Framework (PXF).
PXF is an extensible framework that allows HAWQ to access data in external
sources as readable or writable HAWQ tables. PXF has built-in connectors for
accessing data inside HDFS files, Hive tables, and HBase tables. PXF also
integrates with HCatalog to query Hive tables directly. See [Using PXF
with Unmanaged Data](../pxf/HawqExtensionFrameworkPXF.html) for more
details.

Users can create custom PXF connectors to access other parallel data stores or
processing engines. Connectors are Java plug-ins that use the PXF API. For more
information see [PXF External Tables and API](../pxf/PXFExternalTableandAPIReference.html).
