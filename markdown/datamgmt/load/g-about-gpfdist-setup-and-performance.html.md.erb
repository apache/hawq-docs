---
title: About gpfdist Setup and Performance
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

Consider the following scenarios for optimizing your ETL network performance.

-   Allow network traffic to use all ETL host Network Interface Cards (NICs) simultaneously. Run one instance of `gpfdist` on the ETL host, then declare the host name of each NIC in the `LOCATION` clause of your external table definition (see [Creating External Tables - Examples](creating-external-tables-examples.html#topic44)).

<a id="topic14__du165872"></a>
<span class="figtitleprefix">Figure: </span>External Table Using Single gpfdist Instance with Multiple NICs

<img src="../../images/ext_tables_multinic.jpg" class="image" width="472" height="271" />

-   Divide external table data equally among multiple `gpfdist` instances on the ETL host. For example, on an ETL system with two NICs, run two `gpfdist` instances (one on each NIC) to optimize data load performance and divide the external table data files evenly between the two `gpfdists`.

<a id="topic14__du165882"></a>

<span class="figtitleprefix">Figure: </span>External Tables Using Multiple gpfdist Instances with Multiple NICs

<img src="../../images/ext_tables.jpg" class="image" width="467" height="282" />

**Note:** Use pipes (|) to separate formatted text when you submit files to `gpfdist`. HAWQ encloses comma-separated text strings in single or double quotes. `gpfdist` has to remove the quotes to parse the strings. Using pipes to separate formatted text avoids the extra step and improves performance.
