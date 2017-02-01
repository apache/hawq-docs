---
title: hawq extract
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

Extracts the metadata of a specified table into a YAML file.

## Synopsis

``` pre
hawq extract [<connection_options>] [-o <output_file>] <tablename>

hawq extract -?

hawq extract --version
```
where:

``` pre
<connection_options> =
  [-h <host>] 
  [-p <port>] 
  [-U <username>] 
  [-d <database>]
  [-W]
```

## Description

`hawq extract` is a utility that extracts a table's metadata into a YAML formatted file. HAWQ's InputFormat uses this YAML-formatted file to read a HAWQ file stored on HDFS directly into the MapReduce program. The YAML configuration file can also be used provide the metadata for registering files into HAWQ with the `hawq register` command.

**Note:**
`hawq extract` is bound by the following rules:

-   You must start up HAWQ to use `hawq extract`.
-   `hawq extract` only supports AO and Parquet tables.
-   `hawq extract` supports partitioned tables, but does not support sub-partitions.

## Arguments

<dt>&lt;tablename&gt;  </dt>
<dd>Name of the table that you need to extract metadata. You can use the format *namespace\_name.table\_name*.</dd>

## Options

<dt>-o &lt;output\_file&gt;  </dt>
<dd>Is the name of a file that `hawq extract` uses to write the metadata. If you do not specify a name, `hawq extract` writes to `stdout`.</dd>

<dt>-v (verbose mode)  </dt>
<dd>Displays the verbose output of the extraction process.</dd>

<dt>-? (help)  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

**&lt;connection_options&gt;**

<dt>-h &lt;host&gt;  </dt>
<dd>Specifies the host name of the machine on which the HAWQ master database server is running. If not specified, it reads from the environment variable `$PGHOST` or defaults to `localhost`.</dd>

<dt>-p &lt;port&gt;  </dt>
<dd>Specifies the TCP port on which the HAWQ master database server is listening for connections. If not specified, reads from the environment variable `$PGPORT` or defaults to 5432.</dd>

<dt>-U &lt;username&gt;  </dt>
<dd>The database role name to connect as. If not specified, reads from the environment variable `$PGUSER` or defaults to the current system user name.</dd>

<dt>-d &lt;database&gt;  </dt>
<dd>The database to connect to. If not specified, it reads from the environment variable `$PGDATABASE` or defaults to `template1`.</dd>

<dt>-W (force password prompt)  </dt>
<dd>Force a password prompt. If not specified, reads the password from the environment variable `$PGPASSWORD` or from a password file specified by `$PGPASSFILE` or in `~/.pgpass`.</dd>

## Metadata File Format

`hawq extract` exports the table metadata into a file using YAML 1.1 document format. The file contains various key information about the table, such as table schema, data file locations and sizes, partition constraints and so on.

The basic structure of the metadata file is as follows:

``` pre
Version: string (1.0.0)
DBVersion: string 
FileFormat: string (AO/Parquet) 
TableName: string (schemaname.tablename)
DFS_URL: string (hdfs://127.0.0.1:9000)
Encoding: UTF8
AO_Schema: 
    - name: string
      type: string
      Bucketnum: 6
      Distribution_policy: DISTRIBUTED RANDOMLY 
 
AO_FileLocations:
      Blocksize: int
      Checksum: boolean
      CompressionType: string
      CompressionLevel: int
      PartitionBy: string ('PARTITION BY ...')
      Files:
      - path: string (/gpseg0/16385/35469/35470.1)
        size: long
 
      Partitions:
      - Blocksize: int
        Checksum: Boolean
        CompressionType: string
        CompressionLevel: int
        Name: string
        Constraint: string (PARTITION Jan08 START (date '2008-01-01') INCLUSIVE)
        Files:
        - path: string
          size: long

Parquet_Schema: 
    - name: string
      type: string
       
Parquet_FileLocations:
  RowGroupSize: long
  PageSize: long
  CompressionType: string
  CompressionLevel: int
  Checksum: boolean
  EnableDictionary: boolean
  PartitionBy: string
  Files:
  - path: string
    size: long
  Partitions:
  - Name: string
    RowGroupSize: long
    PageSize: long
    CompressionType: string
    CompressionLevel: int
    Checksum: boolean
    EnableDictionary: boolean
    Constraint: string
    Files:
    - path: string
      size: long
```

## Example - Extracting an AO table

Extract the `rank` table's metadata into a file named `rank_table.yaml`:

``` shell
$ hawq extract -o rank_table.yaml -d postgres rank
```

**Output content in rank\_table.yaml**

``` pre
AO_FileLocations:
    Blocksize: 32768
    Checksum: false
    CompressionLevel: 0
    CompressionType: null
    Files:
    - path: /gpseg0/16385/35469/35692.1
      size: 0
    - path: /gpseg1/16385/35469/35692.1
      size: 0
    PartitionBy: PARTITION BY list (gender)
    Partitions:
    - Blocksize: 32768
      Checksum: false
      CompressionLevel: 0
      CompressionType: null
      Constraint: PARTITION girls VALUES('F') WITH (appendonly=true)
    Files:
    - path: /gpseg0/16385/35469/35697.1
      size: 0
    - path: /gpseg1/16385/35469/35697.1
      size: 0
      Name: girls
    - Blocksize: 32768
      Checksum: false
      CompressionLevel: 0
      CompressionType: null
      Constraint: PARTITION boys VALUES('M') WITH (appendonly=true)
      Files:
      - path: /gpseg0/16385/35469/35703.1
        size: 0
      - path: /gpseg1/16385/35469/35703.1
        size: 0
      Name: boys
    - Blocksize: 32768
      Checksum: false
      CompressionLevel: 0
      CompressionType: null
      Constraint: DEFAULT PARTITION other WITH appendonly=true)
      Files:
      - path: /gpseg0/16385/35469/35709.1
        size: 90071728
      - path: /gpseg1/16385/35469/35709.1
        size: 90071512
      Name: other
    AO_Schema:
    - name: id
      type: int4
    - name: rank
      type: int4
    - name: year
      type: int4
    - name: gender
      type: bpchar
    - name: count
      type: int4
    DFS_URL: hdfs://127.0.0.1:9000
    Distribution_policy: DISTRIBUTED RANDOMLY
    Encoding: UTF8
    FileFormat: AO
    TableName: public.rank
    Version: 1.0.0
```

## Example - Extracting a Parquet table

Extract the `orders` table's metadata into a file named `orders.yaml`:

``` shell
$ hawq extract -o orders.yaml -d postgres orders
```

**Output content in orders.yaml**

``` pre
DFS_URL: hdfs://127.0.0.1:9000
Encoding: UTF8
FileFormat: Parquet
TableName: public.orders
Version: 1.0.0
Parquet_FileLocations:
  Checksum: false
  CompressionLevel: 0
  CompressionType: none
  EnableDictionary: false
  Files:
  - path: /hawq-data/gpseg0/16385/16626/16657.1
    size: 0
  - path: /hawq-data/gpseg1/16385/16626/16657.1
    size: 0
  PageSize: 1048576
  PartitionBy: PARTITION BY range (o_orderdate)
  Partitions:
  - Checksum: false
    CompressionLevel: 0
    CompressionType: none
    Constraint: PARTITION p1_1 START ('1992-01-01'::date) END ('1994-12-31'::date)
      EVERY ('3 years'::interval) WITH (appendonly=true, orientation=parquet, pagesize=1048576,
      rowgroupsize=8388608, compresstype=none, compresslevel=0)
    EnableDictionary: false
    Files:
    - path: /hawq-data/gpseg0/16385/16626/16662.1
      size: 8140599
    - path: /hawq-data/gpseg1/16385/16626/16662.1
      size: 8099760
    Name: orders_1_prt_p1_1
    PageSize: 1048576
    RowGroupSize: 8388608
  - Checksum: false
    CompressionLevel: 0
    CompressionType: none
    Constraint: PARTITION p1_11 START ('1995-01-01'::date) END ('1997-12-31'::date)
      EVERY ('e years'::interval) WITH (appendonly=true, orientation=parquet, pagesize=1048576,
      rowgroupsize=8388608, compresstype=none, compresslevel=0)
    EnableDictionary: false
    Files:
    - path: /hawq-data/gpseg0/16385/16626/16668.1
      size: 8088559
    - path: /hawq-data/gpseg1/16385/16626/16668.1
      size: 8075056
    Name: orders_1_prt_p1_11
    PageSize: 1048576
    RowGroupSize: 8388608
  - Checksum: false
    CompressionLevel: 0
    CompressionType: none
    Constraint: PARTITION p1_21 START ('1998-01-01'::date) END ('2000-12-31'::date)
      EVERY ('3 years'::interval) WITH (appendonly=true, orientation=parquet, pagesize=1048576,
      rowgroupsize=8388608, compresstype=none, compresslevel=0)
    EnableDictionary: false
    Files:
    - path: /hawq-data/gpseg0/16385/16626/16674.1
      size: 8065770
    - path: /hawq-data/gpseg1/16385/16626/16674.1
      size: 8126669
    Name: orders_1_prt_p1_21
    PageSize: 1048576
    RowGroupSize: 8388608
  RowGroupSize: 8388608
  Parquet_Schema:
  - name: o_orderkey
    type: int8
  - name: o_custkey
    type: int4
  - name: o_orderstatus
    type: bpchar
  - name: o_totalprice
    type: numeric
  - name: o_orderdate
    type: date
  - name: o_orderpriority
    type: bpchar
  - name: o_clerk
    type: bpchar
  - name: o_shippriority
    type: int4
  - name: o_comment
    type: varchar
    Distribution_policy: DISTRIBUTED RANDOMLY
```

## See Also

[hawq load](hawqload.html#topic1), [hawq register](hawqregister.html#topic1)


