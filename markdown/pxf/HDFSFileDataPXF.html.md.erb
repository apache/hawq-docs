---
title: Accessing HDFS File Data
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

HDFS is the primary distributed storage mechanism used by Apache Hadoop applications. The PXF HDFS plug-in reads file data stored in HDFS.  The plug-in supports plain delimited and comma-separated-value format text files.  The HDFS plug-in also supports the Avro binary format.

This section describes how to use PXF to access HDFS data, including how to create and query an external table from files in the HDFS data store.

## <a id="hdfsplugin_prereq"></a>Prerequisites

Before working with HDFS file data using HAWQ and PXF, ensure that:

-   The HDFS plug-in is installed on all cluster nodes. See [Installing PXF Plug-ins](InstallPXFPlugins.html) for PXF plug-in installation information.
-   All HDFS users have read permissions to HDFS services and that write permissions have been restricted to specific users.

## <a id="hdfsplugin_fileformats"></a>HDFS File Formats

The PXF HDFS plug-in supports reading the following file formats:

- Text File - comma-separated value (.csv) or delimited format plain text file
- Avro - JSON-defined, schema-based data serialization format

The PXF HDFS plug-in includes the following profiles to support the file formats listed above:

- `HdfsTextSimple` - text files
- `HdfsTextMulti` - text files with embedded line feeds
- `Avro` - Avro files

If you find that the pre-defined PXF HDFS profiles do not meet your needs, you may choose to create a custom HDFS profile from the existing HDFS serialization and deserialization classes. Refer to [Adding and Updating Profiles](ReadWritePXF.html#addingandupdatingprofiles) for information on creating a custom profile.

## <a id="hdfsplugin_cmdline"></a>HDFS Shell Commands
Hadoop includes command-line tools that interact directly with HDFS.  These tools support typical file system operations including copying and listing files, changing file permissions, and so forth.

The HDFS file system command syntax is `hdfs dfs <options> [<file>]`. Invoked with no options, `hdfs dfs` lists the file system options supported by the tool.

The user invoking the `hdfs dfs` command must have sufficient privileges to the HDFS data store to perform HDFS file system operations. Specifically, the user must have write permission to HDFS to create directories and files.

`hdfs dfs` options used in this topic are:

| Option  | Description |
|-------|-------------------------------------|
| `-cat`    | Display file contents. |
| `-mkdir`    | Create directory in HDFS. |
| `-put`    | Copy file from local file system to HDFS. |

Examples:

Create a directory in HDFS:

``` shell
$ hdfs dfs -mkdir -p /data/exampledir
```

Copy a text file to HDFS:

``` shell
$ hdfs dfs -put /tmp/example.txt /data/exampledir/
```

Display the contents of a text file in HDFS:

``` shell
$ hdfs dfs -cat /data/exampledir/example.txt
```


## <a id="hdfsplugin_queryextdata"></a>Querying External HDFS Data
The PXF HDFS plug-in supports the `HdfsTextSimple`, `HdfsTextMulti`, and `Avro` profiles.

Use the following syntax to create a HAWQ external table representing HDFS data: 

``` sql
CREATE EXTERNAL TABLE <table_name> 
    ( <column_name> <data_type> [, ...] | LIKE <other_table> )
LOCATION ('pxf://<host>[:<port>]/<path-to-hdfs-file>
    ?PROFILE=HdfsTextSimple|HdfsTextMulti|Avro[&<custom-option>=<value>[...]]')
FORMAT '[TEXT|CSV|CUSTOM]' (<formatting-properties>);
```

HDFS-plug-in-specific keywords and values used in the [CREATE EXTERNAL TABLE](../reference/sql/CREATE-EXTERNAL-TABLE.html) call are described in the table below.

| Keyword  | Value |
|-------|-------------------------------------|
| \<host\>    | The PXF host. While \<host\> may identify any PXF agent node, use the HDFS NameNode as it is guaranteed to be available in a running HDFS cluster. If HDFS High Availability is enabled, \<host\> must identify the HDFS NameService. |
| \<port\>    | The PXF port. If \<port\> is omitted, PXF assumes \<host\> identifies a High Availability HDFS Nameservice and connects to the port number designated by the `pxf_service_port` server configuration parameter value. Default is 51200. |
| \<path-to-hdfs-file\>    | The path to the file in the HDFS data store. |
| PROFILE    | The `PROFILE` keyword must specify one of the values `HdfsTextSimple`, `HdfsTextMulti`, or `Avro`. |
| \<custom-option\>  | \<custom-option\> is profile-specific. Profile-specific options are discussed in the relevant profile topic later in this section.|
| FORMAT 'TEXT' | Use '`TEXT`' `FORMAT` with the `HdfsTextSimple` profile when \<path-to-hdfs-file\> references a plain text delimited file.  |
| FORMAT 'CSV' | Use '`CSV`' `FORMAT` with `HdfsTextSimple` and `HdfsTextMulti` profiles when \<path-to-hdfs-file\> references a comma-separated value file.  |
| FORMAT 'CUSTOM' | Use the`CUSTOM` `FORMAT` with  the `Avro` profile. The `Avro` '`CUSTOM`' `FORMAT` supports only the built-in `(formatter='pxfwritable_import')` \<formatting-property\> |
 \<formatting-properties\>    | \<formatting-properties\> are profile-specific. Profile-specific formatting options are discussed in the relevant profile topic later in this section. |

*Note*: When creating PXF external tables, you cannot use the `HEADER` option in your `FORMAT` specification.

## <a id="profile_hdfstextsimple"></a>HdfsTextSimple Profile

Use the `HdfsTextSimple` profile when reading plain text delimited or .csv files where each row is a single record.

\<formatting-properties\> supported by the `HdfsTextSimple` profile include:

| Keyword  | Value |
|-------|-------------------------------------|
| delimiter    | The delimiter character in the file. Default value is a comma `,`.|

### <a id="profile_hdfstextsimple_query"></a>Example: Using the HdfsTextSimple Profile

Perform the following steps to create a sample data file, copy the file to HDFS, and use the `HdfsTextSimple` profile to create PXF external tables to query the data:

1. Create an HDFS directory for PXF example data files:

    ``` shell
    $ hdfs dfs -mkdir -p /data/pxf_examples
    ```

2. Create a delimited plain text data file named `pxf_hdfs_simple.txt`:

    ``` shell
    $ echo 'Prague,Jan,101,4875.33
Rome,Mar,87,1557.39
Bangalore,May,317,8936.99
Beijing,Jul,411,11600.67' > /tmp/pxf_hdfs_simple.txt
    ```

    Note the use of the comma `,` to separate the four data fields.

4. Add the data file to HDFS:

    ``` shell
    $ hdfs dfs -put /tmp/pxf_hdfs_simple.txt /data/pxf_examples/
    ```

5. Display the contents of the `pxf_hdfs_simple.txt` file stored in HDFS:

    ``` shell
    $ hdfs dfs -cat /data/pxf_examples/pxf_hdfs_simple.txt
    ```

1. Use the `HdfsTextSimple` profile to create a queryable HAWQ external table from the `pxf_hdfs_simple.txt` file you previously created and added to HDFS:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_hdfs_textsimple(location text, month text, num_orders int, total_sales float8)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_hdfs_simple.txt?PROFILE=HdfsTextSimple')
              FORMAT 'TEXT' (delimiter=E',');
    gpadmin=# SELECT * FROM pxf_hdfs_textsimple;          
    ```

    ``` pre
       location    | month | num_orders | total_sales 
    ---------------+-------+------------+-------------
     Prague        | Jan   |        101 |     4875.33
     Rome          | Mar   |         87 |     1557.39
     Bangalore     | May   |        317 |     8936.99
     Beijing       | Jul   |        411 |    11600.67
    (4 rows)
    ```

2. Create a second external table from `pxf_hdfs_simple.txt`, this time using the `CSV` `FORMAT`:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_hdfs_textsimple_csv(location text, month text, num_orders int, total_sales float8)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_hdfs_simple.txt?PROFILE=HdfsTextSimple')
              FORMAT 'CSV';
    gpadmin=# SELECT * FROM pxf_hdfs_textsimple_csv;          
    ```

    When specifying `FORMAT 'CSV'` for a comma-separated value file, no `delimiter` formatter option is required, as comma is the default.

## <a id="profile_hdfstextmulti"></a>HdfsTextMulti Profile

Use the `HdfsTextMulti` profile when reading plain text files with delimited single- or multi- line records that include embedded (quoted) linefeed characters.

\<formatting-properties\> supported by the `HdfsTextMulti` profile include:

| Keyword  | Value |
|-------|-------------------------------------|
| delimiter    | The delimiter character in the file. |

### <a id="profile_hdfstextmulti_query"></a>Example: Using the HdfsTextMulti Profile

Perform the following steps to create a sample data file, copy the file to HDFS, and use the `HdfsTextMulti` profile to create a PXF external table to query the data:

1. Create a second delimited plain text file:

    ``` shell
    $ vi /tmp/pxf_hdfs_multi.txt
    ```

2. Copy/paste the following data into `pxf_hdfs_multi.txt`:

    ``` pre
    "4627 Star Rd.
    San Francisco, CA  94107":Sept:2017
    "113 Moon St.
    San Diego, CA  92093":Jan:2018
    "51 Belt Ct.
    Denver, CO  90123":Dec:2016
    "93114 Radial Rd.
    Chicago, IL  60605":Jul:2017
    "7301 Brookview Ave.
    Columbus, OH  43213":Dec:2018
    ```

    Notice the use of the colon `:` to separate the three fields. Also notice the quotes around the first (address) field. This field includes an embedded line feed separating the street address from the city and state.

3. Add the data file to HDFS:

    ``` shell
    $ hdfs dfs -put /tmp/pxf_hdfs_multi.txt /data/pxf_examples/
    ```

4. Use the `HdfsTextMulti` profile to create a queryable external table from the `pxf_hdfs_multi.txt` HDFS file, making sure to identify the `:` as the field separator:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_hdfs_textmulti(address text, month text, year int)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_hdfs_multi.txt?PROFILE=HdfsTextMulti')
              FORMAT 'CSV' (delimiter=E':');
    ```
    
2. Query the `pxf_hdfs_textmulti` table:

    ``` sql
    gpadmin=# SELECT * FROM pxf_hdfs_textmulti;
    ```

    ``` pre
             address          | month | year 
    --------------------------+-------+------
     4627 Star Rd.            | Sept  | 2017
     San Francisco, CA  94107           
     113 Moon St.             | Jan   | 2018
     San Diego, CA  92093               
     51 Belt Ct.              | Dec   | 2016
     Denver, CO  90123                  
     93114 Radial Rd.         | Jul   | 2017
     Chicago, IL  60605                 
     7301 Brookview Ave.      | Dec   | 2018
     Columbus, OH  43213                
    (5 rows)
    ```

## <a id="profile_hdfsavro"></a>Avro Profile

Apache Avro is a data serialization framework where the data is serialized in a compact binary format. 

Avro specifies that data types be defined in JSON. Avro format files have an independent schema, also defined in JSON. An Avro schema, together with its data, is fully self-describing.

### <a id="profile_hdfsavrodatamap"></a>Data Type Mapping

Avro supports both primitive and complex data types. 

To represent Avro primitive data types in HAWQ, map data values to HAWQ columns of the same type. 

Avro supports complex data types including arrays, maps, records, enumerations, and fixed types. Map top-level fields of these complex data types to the HAWQ `TEXT` type. While HAWQ does not natively support these types, you can create HAWQ functions or application code to extract or further process subcomponents of these complex data types.

The following table summarizes external mapping rules for Avro data.

<a id="topic_oy3_qwm_ss__table_j4s_h1n_ss"></a>

| Avro Data Type                                                    | PXF/HAWQ Data Type                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primitive type (int, double, float, long, string, bytes, boolean) | Use the corresponding HAWQ built-in data type; see [Data Types](../reference/HAWQDataTypes.html). |
| Complex type: Array, Map, Record, or Enum                         | TEXT, with delimiters inserted between collection items, mapped key-value pairs, and record data.                                                                                           |
| Complex type: Fixed                                               | BYTEA                                                                                                                                                                                               |
| Union                                                             | Follows the above conventions for primitive or complex data types, depending on the union; supports Null values.                                                                     |

### <a id="profile_hdfsavroptipns"></a>Avro-Specific Custom Options

For complex types, the PXF `Avro` profile inserts default delimiters between collection items and values. You can use non-default delimiter characters by identifying values for specific `Avro` custom options in the `CREATE EXTERNAL TABLE` call. 

The `Avro` profile supports the following \<custom-options\>:

| Option Name   | Description       
|---------------|--------------------|                                                                                        
| COLLECTION_DELIM | The delimiter character(s) to place between entries in a top-level array, map, or record field when PXF maps an Avro complex data type to a text column. The default is the comma `,` character. |
| MAPKEY_DELIM | The delimiter character(s) to place between the key and value of a map entry when PXF maps an Avro complex data type to a text column. The default is the colon `:` character. |
| RECORDKEY_DELIM | The delimiter character(s) to place between the field name and value of a record entry when PXF maps an Avro complex data type to a text column. The default is the colon `:` character. |


### <a id="topic_tr3_dpg_ts__section_m2p_ztg_ts"></a>Avro Schemas and Data

Avro schemas are defined using JSON, and composed of the same primitive and complex types identified in the data mapping section above. Avro schema files typically have a `.avsc` suffix.

Fields in an Avro schema file are defined via an array of objects, each of which is specified by a name and a type.


### <a id="topic_tr3_dpg_ts_example"></a>Example: Using the Avro Profile

The examples in this section will operate on Avro data with the following record schema:

- id - long
- username - string
- followers - array of string
- fmap - map of long
- address - record comprised of street number (int), street name (string), and city (string)
- relationship - enumerated type


#### <a id="topic_tr3_dpg_ts__section_m2p_ztg_ts_99"></a>Create Schema

Perform the following operations to create an Avro schema to represent the example schema described above.

1. Create a file named `avro_schema.avsc`:

    ``` shell
    $ vi /tmp/avro_schema.avsc
    ```

2. Copy and paste the following text into `avro_schema.avsc`:

    ``` json
    {
    "type" : "record",
      "name" : "example_schema",
      "namespace" : "com.example",
      "fields" : [ {
        "name" : "id",
        "type" : "long",
        "doc" : "Id of the user account"
      }, {
        "name" : "username",
        "type" : "string",
        "doc" : "Name of the user account"
      }, {
        "name" : "followers",
        "type" : {"type": "array", "items": "string"},
        "doc" : "Users followers"
      }, {
        "name": "fmap",
        "type": {"type": "map", "values": "long"}
      }, {
        "name": "relationship",
        "type": {
            "type": "enum",
            "name": "relationshipEnum",
            "symbols": ["MARRIED","LOVE","FRIEND","COLLEAGUE","STRANGER","ENEMY"]
        }
      }, {
        "name": "address",
        "type": {
            "type": "record",
            "name": "addressRecord",
            "fields": [
                {"name":"number", "type":"int"},
                {"name":"street", "type":"string"},
                {"name":"city", "type":"string"}]
        }
      } ],
      "doc:" : "A basic schema for storing messages"
    }
    ```

#### <a id="topic_tr3_dpgspk_15g_tsdata"></a>Create Avro Data File (JSON)

Perform the following steps to create a sample Avro data file conforming to the above schema.

1.  Create a text file named `pxf_hdfs_avro.txt`:

    ``` shell
    $ vi /tmp/pxf_hdfs_avro.txt
    ```

2. Enter the following data into `pxf_hdfs_avro.txt`:

    ``` pre
    {"id":1, "username":"john","followers":["kate", "santosh"], "relationship": "FRIEND", "fmap": {"kate":10,"santosh":4}, "address":{"number":1, "street":"renaissance drive", "city":"san jose"}}
    
    {"id":2, "username":"jim","followers":["john", "pam"], "relationship": "COLLEAGUE", "fmap": {"john":3,"pam":3}, "address":{"number":9, "street":"deer creek", "city":"palo alto"}}
    ```

    The sample data uses a comma `,` to separate top level records and a colon `:` to separate map/key values and record field name/values.

3. Convert the text file to Avro format. There are various ways to perform the conversion, both programmatically and via the command line. In this example, we use the [Java Avro tools](http://avro.apache.org/releases.html); the jar file resides in the current directory:

    ``` shell
    $ java -jar ./avro-tools-1.8.1.jar fromjson --schema-file /tmp/avro_schema.avsc /tmp/pxf_hdfs_avro.txt > /tmp/pxf_hdfs_avro.avro
    ```

    The generated Avro binary data file is written to `/tmp/pxf_hdfs_avro.avro`. 
    
4. Copy the generated Avro file to HDFS:

    ``` shell
    $ hdfs dfs -put /tmp/pxf_hdfs_avro.avro /data/pxf_examples/
    ```
    
#### <a id="topic_avro_querydata"></a>Query With Avro Profile

Perform the following steps to create and query an external table accessing the `pxf_hdfs_avro.avro` file you added to HDFS in the previous section. When creating the table:

-  Map the top-level primitive fields, `id` (type long) and `username` (type string), to their equivalent HAWQ types (bigint and text). 
-  Map the remaining complex fields to type text.
-  Explicitly set the record, map, and collection delimiters using the Avro profile custom options.


1. Use the `Avro` profile to create a queryable external table from the `pxf_hdfs_avro.avro` file:

    ``` sql
    gpadmin=# CREATE EXTERNAL TABLE pxf_hdfs_avro(id bigint, username text, followers text, fmap text, relationship text, address text)
                LOCATION ('pxf://namenode:51200/data/pxf_examples/pxf_hdfs_avro.avro?PROFILE=Avro&COLLECTION_DELIM=,&MAPKEY_DELIM=:&RECORDKEY_DELIM=:')
              FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
    ```

2. Perform a simple query of the `pxf_hdfs_avro` table:

    ``` sql
    gpadmin=# SELECT * FROM pxf_hdfs_avro;
    ```

    ``` pre
     id | username |   followers    |        fmap         | relationship |                      address                      
    ----+----------+----------------+--------------------+--------------+---------------------------------------------------
      1 | john     | [kate,santosh] | {kate:10,santosh:4} | FRIEND       | {number:1,street:renaissance drive,city:san jose}
      2 | jim      | [john,pam]     | {pam:3,john:3}      | COLLEAGUE    | {number:9,street:deer creek,city:palo alto}
    (2 rows)
    ```

    The simple query of the external table shows the components of the complex type data separated with the delimiters identified in the `CREATE EXTERNAL TABLE` call.


3. Process the delimited components in the text columns as necessary for your application. For example, the following command uses the HAWQ internal `string_to_array` function to convert entries in the `followers` field to a text array column in a new view.

    ``` sql
    gpadmin=# CREATE VIEW followers_view AS 
  SELECT username, address, string_to_array(substring(followers FROM 2 FOR (char_length(followers) - 2)), ',')::text[] 
        AS followers 
      FROM pxf_hdfs_avro;
    ```

4. Query the view to filter rows based on whether a particular follower appears in the array:

    ``` sql
    gpadmin=# SELECT username, address FROM followers_view WHERE followers @> '{john}';
    ```

    ``` pre
     username |                   address                   
    ----------+---------------------------------------------
     jim      | {number:9,street:deer creek,city:palo alto}
    ```

## <a id="accessdataonahavhdfscluster"></a>Accessing HDFS Data in a High Availability HDFS Cluster

To access external HDFS data in a High Availability HDFS cluster, change the `CREATE EXTERNAL TABLE` `LOCATION` clause to use \<HA-nameservice\> rather than  \<host\>[:\<port\>].

``` sql
gpadmin=# CREATE EXTERNAL TABLE <table_name> ( <column_name> <data_type> [, ...] | LIKE <other_table> )
            LOCATION ('pxf://<HA-nameservice>/<path-to-hdfs-file>?PROFILE=HdfsTextSimple|HdfsTextMulti|Avro[&<custom-option>=<value>[...]]')
         FORMAT '[TEXT|CSV|CUSTOM]' (<formatting-properties>);
```

The opposite is true when a highly available HDFS cluster is reverted to a single NameNode configuration. In that case, any table definition that has specified \<HA-nameservice\> should use the \<host\>[:\<port\>] syntax. 

