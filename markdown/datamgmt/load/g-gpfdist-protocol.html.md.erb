---
title: gpfdist Protocol
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

The `gpfdist://` protocol is used in a URI to reference a running `gpfdist` instance. The `gpfdist` utility serves external data files from a directory on a file host to all HAWQ segments in parallel.

`gpfdist` is located in the `$GPHOME/bin` directory on your HAWQ master host and on each segment host.

Run `gpfdist` on the host where the external data files reside. `gpfdist` uncompresses `gzip` (`.gz`) and `bzip2` (.`bz2`) files automatically. You can use the wildcard character (\*) or other C-style pattern matching to denote multiple files to read. The files specified are assumed to be relative to the directory that you specified when you started the `gpfdist` instance.

All virtual segments access the external file(s) in parallel, subject to the number of segments set in the `gp_external_max_segments` parameter, the length of the `gpfdist` location list, and the limits specified by the `hawq_rm_nvseg_perquery_limit` and `hawq_rm_nvseg_perquery_perseg_limit` parameters. Use multiple `gpfdist` data sources in a `CREATE EXTERNAL TABLE` statement to scale the external table's scan performance. For more information about configuring `gpfdist`, see [Using the HAWQ File Server (gpfdist)](g-using-the-hawq-file-server--gpfdist-.html#topic13).

See the `gpfdist` reference documentation for more information about using `gpfdist` with external tables.


