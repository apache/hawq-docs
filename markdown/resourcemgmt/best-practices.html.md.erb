---
title: Best Practices for Configuring Resource Management
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

When configuring resource management, you can apply certain best practices to ensure that resources are managed both efficiently and for best system performance.

The following is a list of high-level best practices for optimal resource management:

-   Make sure segments do not have identical IP addresses. See [Segments Do Not Appear in gp\_segment\_configuration](../troubleshooting/Troubleshooting.html) for an explanation of this problem.
-   Configure all segments to have the same resource capacity. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html).
-   To prevent resource fragmentation, ensure that your deployment's segment resource capacity \(standalone mode\) or YARN node resource capacity \(YARN mode\) is a multiple of all virtual segment resource quotas. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html) \(HAWQ standalone mode\) and [Setting HAWQ Segment Resource Capacity in YARN](YARNIntegration.html).
-   Ensure that enough registered segments are available and usable for query resource requests. If the number of unavailable or unregistered segments is higher than a set limit, then query resource requests are rejected. Also ensure that the variance of dispatched virtual segments across physical segments is not greater than the configured limit. See [Rejection of Query Resource Requests](../troubleshooting/Troubleshooting.html).
-   Use multiple master and segment temporary directories on separate, large disks (2TB or greater) to load balance writes to temporary files (for example, `/disk1/tmp /disk2/tmp`). For a given query, HAWQ will use a separate temp directory (if available) for each virtual segment to store spill files. Multiple HAWQ sessions will also use separate temp directories where available to avoid disk contention. If you configure too few temp directories, or you place multiple temp directories on the same disk, you increase the risk of disk contention or running out of disk space when multiple virtual segments target the same disk. 
-   Configure minimum resource levels in YARN, and tune the timeout of when idle resources are returned to YARN. See [Tune HAWQ Resource Negotiations with YARN](YARNIntegration.html).
-   Make sure that the property `yarn.scheduler.minimum-allocation-mb` in `yarn-site.xml` is an equal subdivision of 1GB. For example, 1024, 512. See [Setting HAWQ Segment Resource Capacity in YARN](YARNIntegration.html#topic_pzf_kqn_c5).
