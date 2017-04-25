---
title: SQL Command Permissions Summary
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

The following table identifies the permissions required for common SQL commands.

**Notes**: 

- A \<db-name\>/\*/* policy with `connect` permission is assumed for all SQL operations in the table.
- A `&&` in the **SQL Command** column identifies a super-user operation.
- A `##` in the **Resource** column signifies that additional policies may be required to provide access to resources used within the operation(s).

<table>
<colgroup>
<col width="30%" />
<col width="20%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>SQL Command</th>
<th>Permission</th>
<th>Resource</th>
</tr>
</thead>
<tbody>

<tr class="odd">
<td>\d</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/public/*</td>
</tr>

<tr class="even">
<td rowspan="2">ANALYZE &lt;table-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="even">
<td>ALTER AGGREGATE ... RENAME TO</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="odd">
<td>ALTER SEQUENCE</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="even">
<td>ALTER TABLE ... RENAME</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="odd">
<td rowspan="2">ALTER TABLE<p>&lt;table-name&gt;<p>SET DISTRIBUTED BY</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="odd">
<td rowspan="2">BEGIN ... COMMIT</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td></td>
<td>##</td>
</tr>

<tr class="odd">
<td> \c, CONNECT &lt;db-name&gt;</td>
<td> connect </td>
<td>&lt;db-name&gt;/*/*</td>
</tr>

<tr class="even">
<td rowspan="2">COPY &lt;table-name&gt; FROM &&</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>insert, select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="even">
<td rowspan="2">COPY &lt;table-name&gt; TO &&</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="even">
<td rowspan="2">CREATE AGGREGATE</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;sfunc-name&gt;</td>
</tr>

<tr class="even">
<td rowspan="2">CREATE EXTERNAL TABLE</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>select</td>
<td>&lt;protocol-name&gt;</td>
</tr>

<tr class="even">
<td rowspan="4">CREATE FUNCTION<p>&lt;func-name&gt;<p>(trusted &lt;language-name&gt;)</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>usage</td>
<td>&lt;db-name&gt;/&lt;language-name&gt;</td>
</tr>
<tr class="even">
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;func-name&gt;</td>
</tr>
<tr class="odd">
<td></td>
<td>##</td>
</tr>


<tr class="even">
<td rowspan="2">CREATE FUNCTION<p>&lt;func-name&gt;<p>(untrusted &lt;language-name&gt;) &&</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td></td>
<td>##</td>
</tr>


<tr class="even">
<td>CREATE LANGUAGE &&</td>
<td>usage</td>
<td>&lt;db-name&gt;/c</td>
</tr>

<tr class="odd">
<td>CREATE OPERATOR<p>CREATE OPERATOR CLASS && <p>CREATE SEQUENCE<p>CREATE TABLE<p>CREATE TYPE<p>CREATE VIEW</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="even">
<td>CREATE SCHEMA</td>
<td>create-schema</td>
<td>&lt;db-name&gt;/*/*</td>
</tr>

<tr class="odd">
<td>CREATE TABLE<p>(&lt;private-schema&gt;) </td>
<td>create</td>
<td>&lt;db-name&gt;/&lt;private-schema&gt;/*</td>
</tr>

<tr class="even">
<td rowspan="2">CREATE TABLE ... AS</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="even">
<td rowspan="2">CREATE TABLE ...<p>TABLESPACE<p>&lt;tablespace-name&gt;</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>create</td>
<td>&lt;tablespace-name&gt;</td>
</tr>

<tr class="even">
<td>CREATE TEMP SEQUENCE<p>CREATE TEMP TABLE</td>
<td>temp</td>
<td>&lt;db-name&gt;/*/*</td>
</tr>

<tr class="odd">
<td rowspan="2">CREATE WRITABLE EXTERNAL TABLE</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>insert</td>
<td>&lt;protocol-name&gt;</td>
</tr>

<tr class="odd">
<td>DROP AGGREGATE<p>DROP FUNCTION<p>DROP OPERATOR<p>DROP OPERATOR CLASS &&<p>DROP SCHEMA<p>DROP TABLE<p>DROP VIEW</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="even">
<td rowspan="2">EXECUTE</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td></td>
<td>##</td>
</tr>


<tr class="even">
<td rowspan="2">EXPLAIN</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td></td>
<td>##</td>
</tr>

<tr class="even">
<td rowspan="2">INSERT INTO<p>&lt;table-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="odd">
<td>insert</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="even">
<td>PREPARE</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="odd">
<td rowspan="4">SELECT &lt;agg-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;agg-name&gt;</td>
</tr>
<tr class="odd">
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;sfunc-name&gt;</td>
</tr>
<tr class="even">
<td></td>
<td>##</td>
</tr>


<tr class="odd">
<td rowspan="2">SELECT &lt;func-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;func-name&gt;</td>
</tr>

<tr class="odd">
<td rowspan="2">SELECT (using operator)</td>
<td>execute</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;op-func&gt;</td>
</tr>
<tr class="even">
<td></td>
<td>##</td>
</tr>

<tr class="odd">
<td rowspan="2">SELECT...FROM<p>&lt;table-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="odd">
<td rowspan="2">SELECT...INTO...FROM &lt;table-name&gt;</td>
<td>usage-schema, create</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

<tr class="odd">
<td rowspan="2">SELECT...FROM<p>&lt;view-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;view-name&gt;</td>
</tr>

<tr class="odd">
<td>TRUNCATE</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="even">
<td>VACUUM</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>

<tr class="odd">
<td rowspan="2">VACUUM ANALYZE<p>&lt;table-name&gt;</td>
<td>usage-schema</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/*</td>
</tr>
<tr class="even">
<td>select</td>
<td>&lt;db-name&gt;/&lt;schema-name&gt;/&lt;table-name&gt;</td>
</tr>

</tbody>
</table>



