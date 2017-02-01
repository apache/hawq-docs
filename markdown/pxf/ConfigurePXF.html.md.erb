---
title: Configuring PXF
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

This topic describes how to configure the PXF service.

**Note:** After you make any changes to a PXF configuration file (such as `pxf-profiles.xml` for adding custom profiles), propagate the changes to all nodes with PXF installed, and then restart the PXF service on all nodes.

## <a id="settingupthejavaclasspath"></a>Setting up the Java Classpath

The classpath for the PXF service is set during the plug-in installation process. Administrators should only modify it when adding new PXF connectors. The classpath is defined in two files:

1.  `/etc/pxf/conf/pxf-private.classpath` – contains all the required resources to run the PXF service, including pxf-hdfs, pxf-hbase, and pxf-hive plug-ins. This file must not be edited or removed.
2.  `/etc/pxf/conf/pxf-public.classpath` – plug-in jar files and any dependent jar files for custom plug-ins and custom profiles should be added here. The classpath resources should be defined one per line. Wildcard characters can be used in the name of the resource, but not in the full path. See [Adding and Updating Profiles](ReadWritePXF.html#addingandupdatingprofiles) for information on adding custom profiles.

After changing the classpath files, the PXF service must be restarted. 

## <a id="settingupthejvmcommandlineoptionsforpxfservice"></a>Setting up the JVM Command Line Options for the PXF Service

The PXF service JVM command line options can be added or modified for each pxf-service instance in the `/var/pxf/pxf-service/bin/setenv.sh` file:

Currently the `JVM_OPTS` parameter is set with the following values for maximum Java heap size and thread stack size:

``` shell
JVM_OPTS="-Xmx512M -Xss256K"
```

After adding or modifying the JVM command line options, the PXF service must be restarted.

(Refer to [Addressing PXF Memory Issues](TroubleshootingPXF.html#pxf-memcfg) for a related discussion of the configuration options available to address memory issues in your PXF deployment.)

## <a id="topic_i3f_hvm_ss"></a>Using PXF on a Secure HDFS Cluster

You can use PXF on a secure HDFS cluster. Read, write, and analyze operations for PXF tables on HDFS files are enabled. It requires no changes to preexisting PXF tables from a previous version.

### <a id="requirements"></a>Requirements

-   Both HDFS and YARN principals are created and are properly configured.
-   HAWQ is correctly configured to work in secure mode.

Please refer to [Troubleshooting PXF](TroubleshootingPXF.html) for common errors related to PXF security and their meaning.

## <a id="credentialsforremoteservices"></a>Credentials for Remote Services

Credentials for remote services allows a PXF plug-in to access a remote service that requires credentials.

### <a id="inhawq"></a>In HAWQ

Two parameters for credentials are implemented in HAWQ:

-   `pxf_remote_service_login` – a string of characters detailing information regarding login (i.e. user name).
-   `pxf_remote_service_secret` – a string of characters detailing information that is considered secret (i.e. password).

Currently, the contents of the two parameters are stored in memory, without any security, for the whole session. Leaving the session will insecurely drop the contents of the parameters.

**Important:** These parameters are temporary and could soon be deprecated, in favor of a complete solution for managing credentials for remote services in PXF.

### <a id="inapxfplugin"></a>In a PXF Plug-in

In a PXF plug-in, the contents of the two credentials parameters is available through the following InputData API functions:

``` java
string getLogin()
string getSecret()
```

Both functions return 'null' if the corresponding HAWQ parameter was set to an empty string or was not set at all. 


