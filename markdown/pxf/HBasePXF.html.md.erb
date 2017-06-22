---
title: Accessing HBase Data
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

## <a id="installingthepxfhbaseplugin"></a>Prerequisites

Before trying to access HBase data with PXF, verify the following:

-   The `/etc/hbase/conf/hbase-env.sh` configuration file must reference the `pxf-hbase.jar`. For example, `/etc/hbase/conf/hbase-env.sh` should include the line:

    ``` bash
    export HBASE_CLASSPATH=${HBASE_CLASSPATH}:/usr/lib/pxf/pxf-hbase.jar
    ```

    **Note:** You must restart HBase after making any changes to the HBase configuration.

-   PXF HBase plug-in is installed on all cluster nodes.
-   HBase and ZooKeeper jars are installed on all cluster nodes.

## <a id="syntax3"></a>Syntax

To create an external HBase table, use the following syntax:

``` sql
CREATE READABLE EXTERNAL TABLE table_name 
    ( column_name data_type [, ...] | LIKE other_table )
LOCATION ('pxf://host[:port]/hbase-table-name?Profile=HBase')
FORMAT 'CUSTOM' (Formatter='pxfwritable_import');
```

The HBase profile is equivalent to the following PXF parameters:

-   Fragmenter=org.apache.hawq.pxf.plugins.hbase.HBaseDataFragmenter
-   Accessor=org.apache.hawq.pxf.plugins.hbase.HBaseAccessor
-   Resolver=org.apache.hawq.pxf.plugins.hbase.HBaseResolver

**Note**: The `ANALYZE` command is not supported on external tables you create with the `HBase` profile.

## <a id="columnmapping"></a>Column Mapping

Most HAWQ external tables (PXF or others) require that the HAWQ table attributes match the source data record layout, and include all the available attributes. With HAWQ, however, you use the PXF HBase plug-in to specify the subset of HBase qualifiers that define the HAWQ PXF table. To set up a clear mapping between each attribute in the PXF table and a specific qualifier in the HBase table, you can use either direct mapping or indirect mapping. In addition, the HBase row key is handled in a special way.

### <a id="rowkey"></a>Row Key

You can use the HBase table row key in several ways. For example, you can see them using query results, or you can run a WHERE clause filter on a range of row key values. To use the row key in the HAWQ query, define the HAWQ table with the reserved PXF attribute `recordkey.` This attribute name tells PXF to return the record key in any key-value based system and in HBase.

**Note:** Because HBase is byte and not character-based, you should define the recordkey as type bytea. This may result in better ability to filter data and increase performance.

``` sql
CREATE EXTERNAL TABLE <tname> (recordkey bytea, ... ) LOCATION ('pxf:// ...')
```

### <a id="directmapping"></a>Direct Mapping

Use Direct Mapping to map HAWQ table attributes to HBase qualifiers. You can specify the HBase qualifier names of interest, with column family names included, as quoted values. 

For example, you have defined an HBase table called `hbase_sales` with multiple column families and many qualifiers. To create a HAWQ table with these attributes:

-   `rowkey`
-   qualifier `saleid` in the column family `cf1`
-   qualifier `comments` in the column family `cf8` 

use the following `CREATE EXTERNAL TABLE` syntax:

``` sql
CREATE EXTERNAL TABLE hbase_sales (
  recordkey bytea,
  "cf1:saleid" int,
  "cf8:comments" varchar
) ...
```

The PXF HBase plug-in uses these attribute names as-is and returns the values of these HBase qualifiers.

### <a id="indirectmappingvialookuptable"></a>Indirect Mapping (via Lookup Table)

The direct mapping method is fast and intuitive, but using indirect mapping helps to reconcile HBase qualifier names with HAWQ behavior:

-   HBase qualifier names may be longer than 32 characters. HAWQ has a 32-character limit on attribute name size.
-   HBase qualifier names can be binary or non-printable. HAWQ attribute names are character based.

In either case, Indirect Mapping uses a lookup table on HBase. You can create the lookup table to store all necessary lookup information. This works as a template for any future queries. The name of the lookup table must be `pxflookup` and must include the column family named `mapping`.

Using the sales example in Direct Mapping, if our `rowkey` represents the HBase table name and the `mapping` column family includes the actual attribute mapping in the key value form of`<hawq attr name>=<hbase                             cf:qualifier>`.

#### <a id="example5"></a>Example

This example maps the `saleid` qualifier in the `cf1` column family to the HAWQ `id` column and the `comments` qualifier in the `cf8` family to the HAWQ `cmts` column.

| (row key) | mapping           |
|-----------|-------------------|
| sales     | id=cf1:saleid     |
| sales     | cmts=cf8:comments |

The mapping assigned new names for each qualifier. You can use these names in your HAWQ table definition:

``` sql
CREATE EXTERNAL TABLE hbase_sales (
  recordkey bytea
  id int,
  cmts varchar
) ...
```

PXF automatically matches HAWQ to HBase column names when a `pxflookup` table exists in HBase.


