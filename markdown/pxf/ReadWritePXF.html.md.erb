---
title: Using Profiles to Read and Write Data
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

PXF profiles are collections of common metadata attributes that can be used to simplify the reading and writing of data. You can use any of the built-in profiles that come with PXF or you can create your own.

For example, if you are writing single line records to text files on HDFS, you could use the built-in HdfsTextSimple profile. You specify this profile when you create the PXF external table used to write the data to HDFS.

## <a id="built-inprofiles"></a>Built-In Profiles

PXF comes with a number of built-in profiles that group together a collection of metadata attributes. PXF built-in profiles simplify access to the following types of data storage systems:

-   HDFS File Data (Read + Write)
-   Hive (Read only)
-   HBase (Read only)
-   JSON (Read only)

You can specify a built-in profile when you want to read data that exists inside HDFS files, Hive tables, HBase tables, or JSON files, and when you want to write data into HDFS files.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Profile</th>
<th>Description</th>
<th>Fragmenter/Accessor/Resolver/Metadata/OutputFormat</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HdfsTextSimple</td>
<td>Read or write delimited single line records from or to plain text files on HDFS.</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hdfs.LineBreakAccessor</li>
<li>org.apache.hawq.pxf.plugins.hdfs.StringPassResolver</li>
</ul></td>
</tr>
<tr class="even">
<td>HdfsTextMulti</td>
<td>Read delimited single or multi-line records (with quoted linefeeds) from plain text files on HDFS. This profile is not splittable (non parallel); reading is slower than reading with HdfsTextSimple.</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hdfs.QuotedLineBreakAccessor</li>
<li>org.apache.hawq.pxf.plugins.hdfs.StringPassResolver</li>
</ul></td>
</tr>
<tr class="odd">
<td>Hive</td>
<td>Read a Hive table with any of the available storage formats: text, RC, ORC, Sequence, or Parquet.</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hive.HiveDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveAccessor</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveResolver</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveMetadataFetcher</li>
<li>org.apache.hawq.pxf.service.io.GPDBWritable</li>
</ul></td>
</tr>
<tr class="even">
<td>HiveRC</td>
<td>Optimized read of a Hive table where each partition is stored as an RCFile. 
<div class="note note">
Note: The <code class="ph codeph">DELIMITER</code> parameter is mandatory.
</div></td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hive.HiveInputFormatFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveRCFileAccessor</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveColumnarSerdeResolver</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveMetadataFetcher</li>
<li>org.apache.hawq.pxf.service.io.Text</li>
</ul></td>
</tr>
<tr class="odd">
<td>HiveORC</td>
<td>Optimized read of a Hive table where each partition is stored as an ORC file.
</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hive.HiveInputFormatFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveORCAccessor</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveORCSerdeResolver</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveMetadataFetcher</li>
<li>org.apache.hawq.pxf.service.io.GPDBWritable</li>
</ul></td>
</tr>
<tr class="even">
<td>HiveVectorizedORC</td>
<td>Optimized bulk/batch read of a Hive table where each partition is stored as an ORC file.
</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hive.HiveInputFormatFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveORCVectorizedAccessor</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveORCVectorizedResolver</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveMetadataFetcher</li>
<li>org.apache.hawq.pxf.service.io.GPDBWritable</li>
</ul></td>
</tr>
<tr class="odd">
<td>HiveText</td>
<td>Optimized read of a Hive table where each partition is stored as a text file.
<div class="note note">
Note: The <code class="ph codeph">DELIMITER</code> parameter is mandatory.
</div></td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hive.HiveInputFormatFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveLineBreakAccessor</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveStringPassResolver</li>
<li>org.apache.hawq.pxf.plugins.hive.HiveMetadataFetcher</li>
<li>org.apache.hawq.pxf.service.io.Text</li>
</ul></td>
</tr>
<tr class="even">
<td>HBase</td>
<td>Read an HBase data store engine.</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hbase.HBaseDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hbase.HBaseAccessor</li>
<li>org.apache.hawq.pxf.plugins.hbase.HBaseResolver</li>
</ul></td>
</tr>
<tr class="odd">
<td>Avro</td>
<td>Read Avro files (fileName.avro).</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.hdfs.AvroFileAccessor</li>
<li>org.apache.hawq.pxf.plugins.hdfs.AvroResolver</li>
</ul></td>
</tr>
<tr class="odd">
<td>JSON</td>
<td>Read JSON files (fileName.json) from HDFS.</td>
<td><ul>
<li>org.apache.hawq.pxf.plugins.hdfs.HdfsDataFragmenter</li>
<li>org.apache.hawq.pxf.plugins.json.JsonAccessor</li>
<li>org.apache.hawq.pxf.plugins.json.JsonResolver</li>
</ul></td>
</tr>
</tbody>
</table>

**Notes**: Metadata identifies the Java class that provides field definitions in the relation. OutputFormat identifies the output serialization format (text or binary) for which a specific profile is optimized. While the built-in `Hive*` profiles provide Metadata and OutputFormat classes, other profiles may have no need to implement or specify these classes.

## <a id="addingandupdatingprofiles"></a>Adding and Updating Profiles

Each profile has a mandatory unique name and an optional description. In addition, each profile contains a set of plug-ins that are an extensible set of metadata attributes.  Administrators can add new profiles or edit the built-in profiles defined in `/etc/pxf/conf/pxf-profiles.xml`. 

**Note:** Add the JAR files associated with custom PXF plug-ins to the `/etc/pxf/conf/pxf-public.classpath` configuration file.

After you make changes in `pxf-profiles.xml` (or any other PXF configuration file), propagate the changes to all nodes with PXF installed, and then restart the PXF service on all nodes.


