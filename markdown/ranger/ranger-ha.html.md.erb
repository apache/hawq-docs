---
title: High Availability and HAWQ Ranger
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

This topic describes specific HAWQ Ranger failover scenarios and procedures. You must have registered and configured a standby HAWQ Ranger Plug-in Service as described in [Register a Standby Ranger Plug-in Service](ranger-integration-config.html#enableha) for these failover scenarios to occur.


## Failover to Standby Ranger Plug-in Service <a id="rps_ha_cfg_rpsfailover"></a>

Should the HAWQ master node fail to communicate with the local Ranger Plug-in Service, the master automatically switches over to the Ranger Plug-in Service registered on the HAWQ master standby node. This operation should be transparent to all HAWQ users.

`hawq state cluster` command output identifies the master service state as `Down` when the Ranger Plug-in Service has failed over to the master standby node:

``` shell
20170515:01:15:26:045131 hawq_state:master:gpadmin-[INFO]:--   HAWQ master Ranger plugin service state      = Down
20170515:01:15:27:045131 hawq_state:master:gpadmin-[INFO]:--   HAWQ standby Ranger plugin service state     = Active
```

After failover to the standby Ranger Plug-in Service, the HAWQ master periodically attempts to re-establish contact with the service on the local node. The [`hawq_rps_check_local_interval`](../reference/guc/parameter_definitions.html#hawq_rps_check_local_interval) server configuration parameter identifies the polling time interval for this contact. When communication is restored with the Ranger Plug-in Service on the local node, the HAWQ master automatically switches back to the local service. This operation is similarly transparent to all HAWQ users.


## Failover to HAWQ Standby Master <a id="rps_ha_cfg_masterfailover"></a>

If the HAWQ master node goes down, you will activate the master standby node, at which time the standby becomes the new HAWQ master. When the HAWQ master fails over in this manner, the master Ranger Plug-in Service also fails over to the standby node.

After activating a HAWQ standby master node, you must manually update the Ranger HAWQ service definition with the new HAWQ master node connection information. Update this information via the Ranger Admin UI.
