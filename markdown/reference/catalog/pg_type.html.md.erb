---
title: pg_type
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

The `pg_type` system catalog table stores information about data types. Base types (scalar types) are created with `CREATE TYPE`, and domains with `CREATE DOMAIN`. A composite type is automatically created for each table in the database, to represent the row structure of the table. It is also possible to create composite types with `CREATE TYPE AS`.

<a id="topic1__hz156260"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_type</span>

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
<td><code class="ph codeph">typname</code></td>
<td>name</td>
<td> </td>
<td>Data type name.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typnamespace</code></td>
<td>oid</td>
<td>pg_namespace.oid</td>
<td>The OID of the namespace that contains this type.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typowner</code></td>
<td>oid</td>
<td>pg_authid.oid</td>
<td>Owner of the type.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typlen</code></td>
<td>smallint</td>
<td> </td>
<td>For a fixed-size type, <code class="ph codeph">typlen</code> is the number of bytes in the internal representation of the type. But for a variable-length type, <code class="ph codeph">typlen</code> is negative. <code class="ph codeph">-1</code> indicates a 'varlena' type (one that has a length word), <code class="ph codeph">-2</code> indicates a null-terminated C string.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typbyval</code></td>
<td>boolean</td>
<td> </td>
<td>Determines whether internal routines pass a value of this type by value or by reference. <code class="ph codeph">typbyval </code>had better be false if <code class="ph codeph">typlen</code> is not 1, 2, or 4 (or 8 on machines where Datum is 8 bytes). Variable-length types are always passed by reference. Note that <code class="ph codeph">typbyval</code> can be false even if the length would allow pass-by-value; this is currently true for type <code class="ph codeph">float4</code>, for example.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typtype</code></td>
<td>char</td>
<td> </td>
<td><code class="ph codeph">b</code> for a base type, <code class="ph codeph">c</code> for a composite type, <code class="ph codeph">d</code> for a domain, or <code class="ph codeph">p</code> for a pseudo-type.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typisdefined</code></td>
<td>boolean</td>
<td> </td>
<td>True if the type is defined, false if this is a placeholder entry for a not-yet-defined type. When false, nothing except the type name, namespace, and OID can be relied on.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typdelim</code></td>
<td>char</td>
<td> </td>
<td>Character that separates two values of this type when parsing array input. Note that the delimiter is associated with the array element data type, not the array data type.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typrelid</code></td>
<td>oid</td>
<td>pg_class.oid</td>
<td>If this is a composite type, then this column points to the <code class="ph codeph">pg_class</code> entry that defines the corresponding table. (For a free-standing composite type, the <code class="ph codeph">pg_class</code> entry does not really represent a table, but it is needed anyway for the type's <code class="ph codeph">pg_attribute</code> entries to link to.) Zero for non-composite types.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typelem</code></td>
<td>oid</td>
<td>pg_type.oid</td>
<td>If not <code class="ph codeph">0</code> then it identifies another row in pg_type. The current type can then be subscripted like an array yielding values of type <code class="ph codeph">typelem</code>. A true array type is variable length (<code class="ph codeph">typlen</code> = <code class="ph codeph">-1</code>), but some fixed-length (<code class="ph codeph">tylpen</code> &gt; <code class="ph codeph">0</code>) types also have nonzero <code class="ph codeph">typelem</code>, for example <code class="ph codeph">name</code> and <code class="ph codeph">point</code>. If a fixed-length type has a <code class="ph codeph">typelem</code> then its internal representation must be some number of values of the <code class="ph codeph">typelem</code> data type with no other data. Variable-length array types have a header defined by the array subroutines.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typinput</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>Input conversion function (text format).</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typoutput</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>Output conversion function (text format).</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typreceive</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>Input conversion function (binary format), or 0 if none.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typsend</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>Output conversion function (binary format), or 0 if none.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typanalyze</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>Custom <code class="ph codeph">ANALYZE</code> function, or 0 to use the standard function.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typalign</code></td>
<td>char</td>
<td> </td>
<td>The alignment required when storing a value of this type. It applies to storage on disk as well as most representations of the value inside HAWQ. When multiple values are stored consecutively, such as in the representation of a complete row on disk, padding is inserted before a datum of this type so that it begins on the specified boundary. The alignment reference is the beginning of the first datum in the sequence. Possible values are:
<p><code class="ph codeph">c</code> = char alignment (no alignment needed).</p>
<p><code class="ph codeph">s</code> = short alignment (2 bytes on most machines).</p>
<p><code class="ph codeph">i</code> = int alignment (4 bytes on most machines).</p>
<p><code class="ph codeph">d</code> = double alignment (8 bytes on many machines, but not all).</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typstorage</code></td>
<td>char</td>
<td> </td>
<td>For varlena types (those with <code class="ph codeph">typlen</code> = -1) tells if the type is prepared for toasting and what the default strategy for attributes of this type should be. Possible values are:
<p><code class="ph codeph">p</code>: Value must always be stored plain.</p>
<p><code class="ph codeph">e</code>: Value can be stored in a secondary relation (if relation has one, see <code class="ph codeph">pg_class.reltoastrelid</code>).</p>
<p><code class="ph codeph">m</code>: Value can be stored compressed inline.</p>
<p><code class="ph codeph">x</code>: Value can be stored compressed inline or stored in secondary storage.</p>
<p>Note that <code class="ph codeph">m</code> columns can also be moved out to secondary storage, but only as a last resort (<code class="ph codeph">e</code> and <code class="ph codeph">x</code> columns are moved first).</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">typnotnull</code></td>
<td>boolean</td>
<td> </td>
<td>Represents a not-null constraint on a type. Used for domains only.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typbasetype</code></td>
<td>oid</td>
<td>pg_type.oid</td>
<td>Identifies the type that a domain is based on. Zero if this type is not a domain.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typtypmod</code></td>
<td>integer</td>
<td> </td>
<td>Domains use typtypmod to record the typmod to be applied to their base type (-1 if base type does not use a typmod). -1 if this type is not a domain.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typndims</code></td>
<td>integer</td>
<td> </td>
<td>The number of array dimensions for a domain that is an array (if <code class="ph codeph">typbasetype</code> is an array type; the domain's <code class="ph codeph">typelem</code> will match the base type's <code class="ph codeph">typelem</code>). Zero for types other than array domains.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">typdefaultbin</code></td>
<td>text</td>
<td> </td>
<td>If not null, it is the <code class="ph codeph">nodeToString()</code> representation of a default expression for the type. This is only used for domains.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">typdefault</code></td>
<td>text</td>
<td> </td>
<td>Null if the type has no associated default value. If not null, typdefault must contain a human-readable version of the default expression represented by typdefaultbin. If typdefaultbin is null and typdefault is not, then typdefault is the external representation of the type's default value, which may be fed to the type's input converter to produce a constant.</td>
</tr>
</tbody>
</table>


