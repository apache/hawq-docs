---
title: pg_class
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

The system catalog table `pg_class` catalogs tables and most everything else that has columns or is otherwise similar to a table (also known as *relations*). This includes indexes (see also [pg\_index](pg_index.html#topic1)), sequences, views, composite types, and TOAST tables. Not all columns are meaningful for all relation types.

<a id="topic1__gf143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_class</span>

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>column</th>
<th>type</th>
<th>references</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">relname</code></td>
<td>name</td>
<td> </td>
<td>Name of the table, index, view, etc.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relnamespace</code></td>
<td>oid</td>
<td>pg_namespace.oid</td>
<td>The OID of the namespace (schema) that contains this relation</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">reltype</code></td>
<td>oid</td>
<td>pg_type.oid</td>
<td>The OID of the data type that corresponds to this table's row type, if any (zero for indexes, which have no <code class="ph codeph">pg_type</code> entry)</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relowner</code></td>
<td>oid</td>
<td>pg_authid.oid</td>
<td>Owner of the relation</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relam</code></td>
<td>oid</td>
<td>pg_am.oid</td>
<td>If this is an index, the access method used (B-tree, Bitmap, hash, etc.)</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relfilenode</code></td>
<td>oid</td>
<td> </td>
<td>Name of the on-disk file of this relation; <code class="ph codeph">0</code> if none.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">reltablespace</code></td>
<td>oid</td>
<td>pg_tablespace.oid</td>
<td>The tablespace in which this relation is stored. If zero, the database's default tablespace is implied. (Not meaningful if the relation has no on-disk file.)</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relpages</code></td>
<td>integer</td>
<td> </td>
<td>Size of the on-disk representation of this table in pages (of 32K each). This is only an estimate used by the planner. It is updated by  <code class="ph codeph">ANALYZE</code>, and a few DDL commands.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">reltuples</code></td>
<td>real</td>
<td> </td>
<td>Number of rows in the table. This is only an estimate used by the planner. It is updated by <code class="ph codeph">VACUUM</code>, <code class="ph codeph">ANALYZE</code>, and a few DDL commands.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">reltoastrelid</code></td>
<td>oid</td>
<td>pg_class.oid</td>
<td>OID of the TOAST table associated with this table, <code class="ph codeph">0</code> if none. The TOAST table stores large attributes &quot;out of line&quot; in a secondary table.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">reltoastidxid</code></td>
<td>oid</td>
<td>pg_class.oid</td>
<td>For a TOAST table, the OID of its index. <code class="ph codeph">0</code> if not a TOAST table.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relaosegidxid</code></td>
<td>oid</td>
<td> </td>
<td>Deprecated.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relaosegrelid</code></td>
<td>oid</td>
<td> </td>
<td>Deprecated.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relhasindex </code></td>
<td>boolean</td>
<td> </td>
<td>True if this is a table and it has (or recently had) any indexes. This is set by <code class="ph codeph">CREATE INDEX</code>, but not cleared immediately by <code class="ph codeph">DROP INDEX</code>. <code class="ph codeph">VACUUM</code> will clear if it finds the table has no indexes.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relisshared</code></td>
<td>boolean</td>
<td> </td>
<td>True if this table is shared across all databases in the system. Only certain system catalog tables are shared.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relkind</code></td>
<td>char</td>
<td> </td>
<td>The type of object
<p><code class="ph codeph">r</code> = heap table, <code class="ph codeph">i</code> = index, <code class="ph codeph">S</code> = sequence, <code class="ph codeph">v</code> = view, <code class="ph codeph">c</code> = composite type, <code class="ph codeph">t</code> = TOAST value, <code class="ph codeph">c</code> = composite type, <code class="ph codeph">u</code> = uncataloged temporary heap table</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relstorage</code></td>
<td>char</td>
<td> </td>
<td>The storage mode of a table
<p><code class="ph codeph">a</code> = append-only, <code class="ph codeph">h</code> = heap, <code class="ph codeph">p</code> = append-only parquet, <code class="ph codeph">v</code> = virtual, <code class="ph codeph">x</code>= external table.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">relnatts</code></td>
<td>smallint</td>
<td> </td>
<td>Number of user columns in the relation (system columns not counted). There must be this many corresponding entries in pg_attribute.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relchecks</code></td>
<td>smallint</td>
<td> </td>
<td>Number of check constraints on the table.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">reltriggers</code></td>
<td>smallint</td>
<td> </td>
<td>Number of triggers on the table.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relukeys</code></td>
<td>smallint</td>
<td> </td>
<td>Unused</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relfkeys</code></td>
<td>smallint</td>
<td> </td>
<td>Unused</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relrefs</code></td>
<td>smallint</td>
<td> </td>
<td>Unused</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relhasoids</code></td>
<td>boolean</td>
<td> </td>
<td>True if an OID is generated for each row of the relation.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relhaspkey</code></td>
<td>boolean</td>
<td> </td>
<td>True if the table once had a primary key.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relhasrules</code></td>
<td>boolean</td>
<td> </td>
<td>True if table has rules.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relhassubclass</code></td>
<td>boolean</td>
<td> </td>
<td>True if table has (or once had) any inheritance children.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">relfrozenxid</code></td>
<td>xid</td>
<td> </td>
<td>All transaction IDs before this one have been replaced with a permanent (frozen) transaction ID in this table. This is used to track whether the table needs to be vacuumed in order to prevent transaction ID wraparound or to allow pg_clog to be shrunk. Zero (<code class="ph codeph">InvalidTransactionId</code>) if the relation is not a table.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">relacl</code></td>
<td>aclitem[]</td>
<td> </td>
<td>Access privileges assigned by <code class="ph codeph">GRANT</code> and <code class="ph codeph">REVOKE</code>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">reloptions</code></td>
<td>text[]</td>
<td> </td>
<td>Access-method-specific options, as &quot;keyword=value&quot; strings.</td>
</tr>
</tbody>
</table>




