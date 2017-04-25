---
title: About Server Configuration Parameters
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

There are many HAWQ server configuration parameters that affect the behavior of the HAWQ system. Many of these configuration parameters have the same names, settings, and behaviors as in a regular PostgreSQL database system.

-   [Parameter Types and Values](#topic_vsn_22l_z4) describes the parameter data types and values.
-   [Setting Parameters](#topic_cyz_p2l_z4) describes limitations on who can change them and where or when they can be set.
-   [Configuration Parameter Categories](guc_category-list.html#guc-cat-list) organizes parameters by functionality.
-   [Configuration Parameters](parameter_definitions.html) lists the parameter descriptions in alphabetic order.

## <a id="topic_vsn_22l_z4"></a>Parameter Types and Values

All parameter names are case-insensitive. Every parameter takes a value of one of four types: `Boolean`, `integer`, `floating point`, or `string`. Boolean values may be written as `ON`, `OFF`, `TRUE`, `FALSE`, `YES`, `NO`, `1`, `0` (all case-insensitive).

Some settings specify a memory size or time value. Each of these has an implicit unit, which is either kilobytes, blocks (typically eight kilobytes), milliseconds, seconds, or minutes. Valid memory size units are `kB` (kilobytes), `MB` (megabytes), and `GB` (gigabytes). Valid time units are `ms` (milliseconds), `s` (seconds), `min` (minutes), `h` (hours), and `d` (days). Note that the multiplier for memory units is 1024, not 1000. A valid time expression contains a number and a unit. When specifying a memory or time unit using the `SET` command, enclose the value in quotes. For example:

``` pre
SET hawq_rm_stmt_vseg_memory TO '4GB';
```

**Note:** There is no space between the value and the unit names.

## <a id="topic_cyz_p2l_z4"></a>Setting Parameters

Many of the configuration parameters have limitations on who can change them and where or when they can be set. For example, to change certain parameters, you must be a HAWQ superuser. Other parameters require a restart of the system for the changes to take effect. A parameter that is classified as *session* can be set at the system level (in the `hawq-site.xml` file), at the database-level (using `ALTER DATABASE`), at the role-level (using `ALTER ROLE`), or at the session-level (using `SET`). System parameters can only be set by using the `hawq config` utility or by directly modifying a `hawq-site.xml` file.

By design, all HAWQ instances (including master and segments) host identical `hawq-site.xml` files. Using a common `hawq-site.xml` file across all HAWQ instances simplifies configuration of the cluster. Within each `hawq-site.xml` configuration file, some parameters are considered *segment* parameters, meaning that each segment instance looks to its own `hawq-site.xml` file to get the value of that parameter. By convention, these parameter names begin with the string `hawq_segment`. Others parameters are considered *master* parameters. By convention, these parameter names begin with the string `hawq_master`. Master parameters are only applied at the master instance and ignored by segments.

**Note:** If you use the `hawq config` utility to set configuration parameter values in `hawq-site.xml`, the utility synchronizes all configuration files. Any manual modifications that you made to individual `hawq-site.xml` files may be lost. Additionally, if you install and manage HAWQ using Ambari, do not use `hawq config` to configure HAWQ properties. If the cluster is restarted, Ambari will overwrite any changes made by `hawq config` For Ambari-managed HAWQ clusters, only  use the Ambari administration interface to set or change HAWQ configuration properties.

This table describes the values in the Set Classifications column of the table in the description of a server configuration parameter.

<a id="topic_cyz_p2l_z4__ih389119"></a>

<table>
<caption><span class="tablecap">Table 1. Set Classifications</span></caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Set Classification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>master or local</td>
<td>A <em>master</em> parameter must be set in the <code class="ph codeph">hawq-site.xml</code> file of the HAWQ master instance. The value for this parameter is then either passed to (or ignored by) the segments at run time.
<p>A <em>local</em> parameter is also defined in the <code class="ph codeph">hawq-site.xml</code> file of the master AND every segment instance. Each HAWQ instance looks to its own configuration to get the value for the parameter.</p>
<p>We recommend that you use the same configuration parameter values across all HAWQ instances to maintain a single, consistent <code class="ph codeph">hawq-site.xml</code> configuration file. The <code class="ph codeph">hawq                     config</code> utility will enforce this consistency.</p>
<p>Changes to master or local parameters always require a system restart for changes to take effect.</p></td>
</tr>
<tr class="even">
<td>session or system</td>
<td><em>Session</em> parameters can be changed on the fly within a database session, and can have a hierarchy of settings: at the system level (through <code class="ph codeph">hawq-site.xml</code>or <code class="ph codeph">hawq config</code> utility), at the database level (<code class="ph codeph">ALTER DATABASE...SET</code>), at the role level (<code class="ph codeph">ALTER ROLE...SET</code>), or at the session level (<code class="ph codeph">SET</code>). If the parameter is set at multiple levels, then the most granular setting takes precedence (for example, session overrides role, role overrides database, and database overrides system).
<p>A <em>system</em> parameter can only be changed via <code class="ph codeph">hawq config</code> utility or the <code class="ph codeph">hawq-site.xml</code> file(s).</p></td>
</tr>
<tr class="odd">
<td>restart or reload</td>
<td>When changing parameter values in the <code class="ph codeph">hawq-site.xml</code> file(s), some require a <em>restart</em> of HAWQ for the change to take effect. Other parameter values can be refreshed by just reloading the configuration file (using <code class="ph codeph">hawq stop object -u</code>), and do not require stopping the system.</td>
</tr>
<tr class="even">
<td>superuser</td>
<td>These session parameters can only be set by a database superuser. Regular database users cannot set this parameter.</td>
</tr>
<tr class="odd">
<td>read only</td>
<td>These parameters are not settable by database users or superusers. The current value of the parameter can be shown but not altered.</td>
</tr>
</tbody>
</table>



