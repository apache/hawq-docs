---
title: pg_window
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

The `pg_window` table stores information about window functions. Window functions are often used to compose complex OLAP (online analytical processing) queries. Window functions are applied to partitioned result sets within the scope of a single query expression. A window partition is a subset of rows returned by a query, as defined in a special `OVER()` clause. Typical window functions are `rank`, `dense_rank`, and `row_number`. Each entry in `pg_window` is an extension of an entry in [pg\_proc](pg_proc.html#topic1). The [pg\_proc](pg_proc.html#topic1) entry carries the window function's name, input and output data types, and other information that is similar to ordinary functions.

<a id="topic1__ic143898"></a>
<span class="tablecap">Table 1. pg\_catalog.pg\_window</span>

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
<td><code class="ph codeph">winfnoid</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>The OID in <code class="ph codeph">pg_proc</code> of the window function.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">winrequireorder</code></td>
<td>boolean</td>
<td> </td>
<td>The window function requires its window specification to have an <code class="ph codeph">ORDER BY</code> clause.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">winallowframe</code></td>
<td>boolean</td>
<td> </td>
<td>The window function permits its window specification to have a <code class="ph codeph">ROWS</code> or <code class="ph codeph">RANGE</code> framing clause.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">winpeercount</code></td>
<td>boolean</td>
<td> </td>
<td>The peer group row count is required to compute this window function, so the Window node implementation must 'look ahead' as necessary to make this available in its internal state.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">wincount</code></td>
<td>boolean</td>
<td> </td>
<td>The partition row count is required to compute this window function.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">winfunc</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>The OID in <code class="ph codeph">pg_proc</code> of a function to compute the value of an immediate-type window function.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">winprefunc</code></td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>The OID in <code class="ph codeph">pg_proc</code> of a preliminary window function to compute the partial value of a deferred-type window function.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">winpretype</code></td>
<td>oid</td>
<td>pg_type.oid</td>
<td>The OID in <code class="ph codeph">pg_type</code> of the preliminary window function's result type.</td>
</tr>
<tr class="odd">
<td>winfinfunc</td>
<td>regproc</td>
<td>pg_proc.oid</td>
<td>The OID in <code class="ph codeph">pg_proc</code> of a function to compute the final value of a deferred-type window function from the partition row count and the result of <code class="ph codeph">winprefunc</code>.</td>
</tr>
<tr class="even">
<td>winkind</td>
<td>char</td>
<td> </td>
<td>A character indicating membership of the window function in a class of related functions:
<p><code class="ph codeph">w</code> - ordinary window functions</p>
<p><code class="ph codeph">n</code> - NTILE functions</p>
<p><code class="ph codeph">f</code> - FIRST_VALUE functions</p>
<p><code class="ph codeph">l</code> - LAST_VALUE functions</p>
<p><code class="ph codeph">g</code> - LAG functions</p>
<p><code class="ph codeph">d</code> - LEAD functions</p></td>
</tr>
</tbody>
</table>




