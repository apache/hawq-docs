---
title: Accessing JSON File Data
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

The PXF JSON plug-in reads native JSON stored in HDFS.  The plug-in supports common data types, as well as basic (N-level) projection and arrays.

To access JSON file data with HAWQ, the data must be stored in HDFS and an external table created from the HDFS data store.

## Prerequisites<a id="jsonplugprereq"></a>

Before working with JSON file data using HAWQ and PXF, ensure that:

-   The PXF HDFS plug-in is installed on all cluster nodes.
-   The PXF JSON plug-in is installed on all cluster nodes.
-   You have tested PXF on HDFS.


## Working with JSON Files<a id="topic_workwjson"></a>

JSON is a text-based data-interchange format.  JSON data is typically stored in a file with a `.json` suffix. A `.json` file will contain a collection of objects.  A JSON object is a collection of unordered name/value pairs.  A value can be a string, a number, true, false, null, or an object or array. Objects and arrays can be nested.

Refer to [Introducing JSON](http://www.json.org/) for specific information on JSON syntax.

Sample JSON data file content:

``` json
  {
    "created_at":"MonSep3004:04:53+00002013",
    "id_str":"384529256681725952",
    "user": {
      "id":31424214,
       "location":"COLUMBUS"
    },
    "coordinates":null
  }
```

### JSON to HAWQ Data Type Mapping<a id="topic_workwjson"></a>

To represent JSON data in HAWQ, map data values that use a primitive data type to HAWQ columns of the same type. JSON supports complex data types including projections and arrays. Use N-level projection to map members of nested objects and arrays to primitive data types.

The following table summarizes external mapping rules for JSON data.

<caption><span class="tablecap">Table 1. JSON Mapping</span></caption>

<a id="topic_table_jsondatamap"></a>

| JSON Data Type                                                    | HAWQ Data Type                                                                                                                                                                                            |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primitive type (integer, float, string, boolean, null) | Use the corresponding HAWQ built-in data type; see [Data Types](../reference/HAWQDataTypes.html). |
| Array                         | Use `[]` brackets to identify a specific array index to a member of primitive type.                                                                                            |
| Object                | Use dot `.` notation to specify each level of projection (nesting) to a member of a primitive type.                                                                                         |


### JSON File Read Modes<a id="topic_jsonreadmodes"></a>


The PXF JSON plug-in reads data in one of two modes. The default mode expects one full JSON record per line.  The JSON plug-in also supports a read mode operating on multi-line JSON records.

In the following discussion, a data set defined by a sample schema will be represented using each read mode of the PXF JSON plug-in.  The sample schema contains data fields with the following names and data types:

   - "created_at" - text
   - "id_str" - text
   - "user" - object
      - "id" - integer
      - "location" - text
   - "coordinates" - object (optional)
      - "type" - text
      - "values" - array
         - [0] - integer
         - [1] - integer


Example 1 - Data Set for Single-JSON-Record-Per-Line Read Mode:

``` pre
{"created_at":"FriJun0722:45:03+00002013","id_str":"343136551322136576","user":{
"id":395504494,"location":"NearCornwall"},"coordinates":{"type":"Point","values"
: [ 6, 50 ]}},
{"created_at":"FriJun0722:45:02+00002013","id_str":"343136547115253761","user":{
"id":26643566,"location":"Austin,Texas"}, "coordinates": null},
{"created_at":"FriJun0722:45:02+00002013","id_str":"343136547136233472","user":{
"id":287819058,"location":""}, "coordinates": null}
```  

Example 2 - Data Set for Multi-Line JSON Record Read Mode:

``` json
{
  "root":[
    {
      "record_obj":{
        "created_at":"MonSep3004:04:53+00002013",
        "id_str":"384529256681725952",
        "user":{
          "id":31424214,
          "location":"COLUMBUS"
        },
        "coordinates":null
      },
      "record_obj":{
        "created_at":"MonSep3004:04:54+00002013",
        "id_str":"384529260872228864",
        "user":{
          "id":67600981,
          "location":"KryberWorld"
        },
        "coordinates":{
          "type":"Point",
          "values":[
             8,
             52
          ]
        }
      }
    }
  ]
}
```

## Loading JSON Data to HDFS<a id="jsontohdfs"></a>

The PXF JSON plug-in reads native JSON stored in HDFS. Before JSON data can be queried via HAWQ, it must first be loaded to an HDFS data store.

Copy and paste the single line JSON record data set to a file named `singleline.json`.  Similarly, copy and paste the multi-line JSON record data set to `multiline.json`.

**Note**:  Ensure there are **no** blank lines in your JSON files.

Add the data set files to the HDFS data store:

``` shell
$ hdfs dfs -mkdir /user/data
$ hdfs dfs -put singleline.json /user/data
$ hdfs dfs -put multiline.json /user/data
```

Once loaded to HDFS, JSON data may be queried and analyzed via HAWQ.

## Querying External JSON Data<a id="jsoncetsyntax1"></a>

Use the following syntax to create an external table representing JSON data: 

``` sql
CREATE EXTERNAL TABLE <table_name> 
    ( <column_name> <data_type> [, ...] | LIKE <other_table> )
LOCATION ( 'pxf://<host>[:<port>]/<path-to-data>?PROFILE=Json[&IDENTIFIER=<value>]' )
      FORMAT 'CUSTOM' ( FORMATTER='pxfwritable_import' );
```
JSON-plug-in-specific keywords and values used in the `CREATE EXTERNAL TABLE` call are described below.

| Keyword  | Value |
|-------|-------------------------------------|
| \<host\>    | The PXF host. While \<host\> may identify any PXF agent node, use the HDFS NameNode as it is guaranteed to be available in a running HDFS cluster. If HDFS High Availability is enabled, \<host\> must identify the HDFS NameService. |
| \<port\>    | The PXF port. If \<port\> is omitted, PXF assumes \<host\> identifies a High Availability HDFS Nameservice and connects to the port number designated by the `pxf_service_port` server configuration parameter value. Default is 51200. |
| PROFILE    | The `PROFILE` keyword must specify the value `Json`. |
| IDENTIFIER  | Include the `IDENTIFIER` keyword and \<value\> in the `LOCATION` string only when accessing a JSON file with multi-line records. \<value\> should identify the member name used to determine the encapsulating JSON object to return.  (If the JSON file is the multi-line record Example 2 above, `&IDENTIFIER=created_at` would be specified.) |  
| FORMAT    | The `FORMAT` clause must specify `CUSTOM`. |
| FORMATTER    | The JSON `CUSTOM` format supports only the built-in `pxfwritable_import` `FORMATTER`. |

**Note**: The `ANALYZE` command is not supported on external tables you create with the `Json` profile.

### Example 1 <a id="jsonexample1"></a>

The following [CREATE EXTERNAL TABLE](../reference/sql/CREATE-EXTERNAL-TABLE.html) SQL call creates a queryable external table based on the data in the single-line-per-record JSON example.

``` sql 
CREATE EXTERNAL TABLE sample_json_singleline_tbl(
  created_at TEXT,
  id_str TEXT,
  text TEXT,
  "user.id" INTEGER,
  "user.location" TEXT,
  "coordinates.values[0]" INTEGER,
  "coordinates.values[1]" INTEGER
)
LOCATION('pxf://namenode:51200/user/data/singleline.json?PROFILE=Json')
FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
SELECT * FROM sample_json_singleline_tbl;
```

Notice the use of `.` projection to access the nested fields in the `user` and `coordinates` objects.  Also notice the use of `[]` to access the specific elements of the `coordinates.values` array.

### Example 2 <a id="jsonexample2"></a>

A `CREATE EXTERNAL TABLE` SQL call to create a queryable external table based on the multi-line-per-record JSON data set would be very similar to that of the single line data set above. You might specify a different database name, `sample_json_multiline_tbl` for example. 

The `LOCATION` clause would differ.  The `IDENTIFIER` keyword and an associated value must be specified when reading from multi-line JSON records:

``` sql
LOCATION('pxf://namenode:51200/user/data/multiline.json?PROFILE=Json&IDENTIFIER=created_at')
```

`created_at` identifies the member name used to determine the encapsulating JSON object, `record_obj` in this case.

To query this external table populated with JSON data:

``` sql
SELECT * FROM sample_json_multiline_tbl;
```
