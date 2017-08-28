---
title: Troubleshooting Connection Problems
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

A number of things can prevent a client application from successfully connecting to HAWQ. This topic explains some of the common causes of connection problems and how to correct them.

|Problem|Solution|
|-------|--------|
|No pg\_hba.conf entry for host or user|To enable HAWQ to accept remote client connections, you must configure your HAWQ master instance so that connections are allowed from the client hosts and database users that will be connecting to HAWQ. This is done by adding the appropriate entries to the pg\_hba.conf configuration file \(located in the master instance's data directory\). For more detailed information, see [Allowing Connections to HAWQ](client_auth.html).|
|HAWQ is not running|If the HAWQ master instance is down, users will not be able to connect. You can verify that the HAWQ system is up by running the `hawq state` utility on the HAWQ master host.|
|Network problems<br/><br/>Interconnect timeouts|If users connect to the HAWQ master host from a remote client, network problems can prevent a connection \(for example, DNS host name resolution problems, the host system is down, and so on.\). To ensure that network problems are not the cause, connect to the HAWQ master host from the remote client host. For example: `ping hostname`. <br/><br/>If the system cannot resolve the host names and IP addresses of the hosts involved in HAWQ, queries and connections will fail. For some operations, connections to the HAWQ master use `localhost` and others use the actual host name, so you must be able to resolve both. If you encounter this error, first make sure you can connect to each host in your HAWQ array from the master host over the network. In the `/etc/hosts` file of the master and all segments, make sure you have the correct host names and IP addresses for all hosts involved in the HAWQ array. The `127.0.0.1` IP must resolve to `localhost`.|
|Too many clients already|By default, HAWQ is configured to allow a maximum of 1280 concurrent user connections on the master and 3000 connections on a segment. A connection attempt that causes that limit to be exceeded will be refused. This limit is controlled by the `max_connections` parameter on the master instance and by the `seg_max_connections` parameter on the segment instances.|
|Query failure|Reverse DNS must be configured in your HAWQ cluster network. In cases where reverse DNS has not been configured, failing queries will generate "Failed to reverse DNS lookup for ip \<ip-address\>" warning messages to the HAWQ master node log file. |
