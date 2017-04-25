---
title: Understanding the Fault Tolerance Service
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

The fault tolerance service (FTS) enables HAWQ to continue operating in the event that a segment node fails. The fault tolerance service runs automatically and requires no additional configuration requirements.

Each segment runs a resource manager process that periodically sends (by default, every 30 seconds) the segment’s status to the master's resource manager process. This interval is controlled by the `hawq_rm_segment_heartbeat_interval` server configuration parameter.

When a segment encounters a critical error-- for example, a temporary directory on the segment fails due to a hardware error-- the segment reports that there is temporary directory failure to the HAWQ master through a heartbeat report. When the master receives the report, it marks the segment as DOWN in the `gp_segment_configuration` table. All changes to a segment's status are recorded in the `gp_configuration_history` catalog table, including the reason why the segment is marked as DOWN. When this segment is set to DOWN, master will not run query executors on the segment. The failed segment is fault-isolated from the rest of the cluster.

Besides disk failure, there are other reasons why a segment can be marked as DOWN. For example, if HAWQ is running in YARN mode, every segment should have a NodeManager (Hadoop’s YARN service) running on it, so that the segment can be considered a resource to HAWQ. However, if the NodeManager on a segment is not operating properly, this segment will also be marked as DOWN in `gp_segment_configuration table`. The corresponding reason for the failure is recorded into `gp_configuration_history`.

**Note:** If a disk fails in a particular segment, the failure may cause either an HDFS error or a temporary directory error in HAWQ. HDFS errors are handled by the Hadoop HDFS service.

##Viewing the Current Status of a Segment <a id="view_segment_status"></a>

To view the current status of the segment, query the `gp_segment_configuration` table.

If the status of a segment is DOWN, the "description" column displays the reason. The reason can include any of the following reasons, as single reasons or as a combination of several reasons, split by a semicolon (";").

**Reason: heartbeat timeout**

Master has not received a heartbeat from the segment. If you see this reason, make sure that HAWQ is running on the segment.

If the segment reports a heartbeat at a later time, the segment is marked as UP.

**Reason: failed probing segment**

Master has probed the segment to verify that it is operating normally, and the segment response is NO.

While a HAWQ instance is running, the Query Dispatcher finds that some Query Executors on the segment are not working normally. The resource manager process on master sends a message to this segment. When the segment resource manager receives the message from master, it checks whether its PostgreSQL postmaster process is working normally and sends a reply message to master. When master gets a reply message that indicates that this segment's postmaster process is not working normally, then the master marks the segment as DOWN with the reason "failed probing segment."

Check the logs of the failed segment and try to restart the HAWQ instance.

**Reason: communication error**

Master cannot connect to the segment.

Check the network connection between the master and the segment.

**Reason: resource manager process was reset**

If the timestamp of the segment resource manager process doesn’t match the previous timestamp, it means that the resource manager process on segment has been restarted. In this case, HAWQ master needs to return the resources on this segment and marks the segment as DOWN. If the master receives a new heartbeat from this segment, it will mark it back to UP. 

**Reason: no global node report**

HAWQ is using YARN for resource management. No cluster report has been received for this segment. 

Check that NodeManager is operating normally on this segment. 

If not, try to start NodeManager on the segment. 
After NodeManager is started, run `yarn node --list` to see if the node is in list. If so, this segment is set to UP.
