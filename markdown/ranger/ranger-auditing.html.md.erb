---
title: Auditing Authorization Events
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

The HAWQ Ranger Plug-in Service supports storing auditing records in any of the Ranger auditing framework audit destinations, referred to as *audit sink*s. The `/usr/local/hawq/ranger/etc/ranger-hawq-audit.xml` file specifies the audit configuration. It contains sample definitions for the HDFS, Solr, and Log4j audit sinks.

As a best practice, configure one or more audit sinks in `ranger-hawq-audit.xml` before you register the HAWQ Ranger Plug-in Service. By default only the Log4j sink is enabled. Production deployments should use both a Solr and an HDFS audit sink, with the Solr destination configured to automatically purge audit records after some period of time.  This configuration enables you to search the most recent audit records, while keeping a full history of auditing records in HDFS.

If you modify `ranger-hawq-audit.xml` after you have registered the HAWQ Ranger Plug-in, you must restart the plug-in for the changes to take effect. See [Custom Configuration](ranger-integration-config.html#customconfig) for instructions.

Full documentation for the Ranger auditing configuration properties and the Ranger auditing framework is available at [Ranger 0.5 Audit Configuration](https://cwiki.apache.org/confluence/display/RANGER/Ranger+0.5+Audit+Configuration).

## <a id="solr"></a>Configuring Solr Auditing
To configure a Solr audit sink, you define a different set of properties in `ranger-hawq-audit.xml` depending on whether you use Zookeeper or a direct URL connect to your Solr destination. For a production environment, use Zookeeper instead of a direct URL.

If you use Zookeeper to connect to Solr, configure these auditing properties in `ranger-hawq-audit.xml`:

Table 1. Properties for Zookeeper Configuration

| Property | Value | Description |
| -------- | ----- | ----------- |
| xasecure.audit.destination.solr | true | Use this property to enable or disable the Solr sink. |
| xasecure.audit.destination.solr.zookeepers | &lt;zookeeper connect string&gt; | Specify the Zookeeper connection string for the Solr destination. |
| xasecure.audit.destination.solr.collection | &lt;collection name&gt; | Specify the Solr collection name to use for indexing the HAWQ audit records. By default HAWQ uses the `ranger_audits` collection. |
| xasecure.audit.destination.solr.batch.filespool.* | Multiple Properties | See [Configuration related to File spooling](https://cwiki.apache.org/confluence/display/RANGER/Ranger+0.5+Audit+Configuration#Ranger0.5AuditConfiguration-ConfigurationrelatedtoFilespooling) in the Ranger documentation if you want to configure spooling of auditing events to disk when the in-memory buffer is full. |
| xasecure.audit.destination.solr.urls | NONE | Leave this property value empty or set it to `NONE` when using Zookeeper to connect to Solr. |

For example:

```
<!-- ********************************* -->
<!-- SOLR audit provider configuration -->
<!-- ********************************* -->
<property>
    <name>xasecure.audit.destination.solr</name>
    <value>true</value>
</property>

<property>
    <name>xasecure.audit.destination.solr.zookeepers</name>
    <value>zkhost1:2181,zkhost2:2181/infra-solr</value>
</property>

<property>
    <name>xasecure.audit.destination.solr.collection</name>
    <value>ranger_audits</value>
</property>

<property>
    <name>xasecure.audit.destination.solr.urls</name>
    <value>NONE</value>
</property>

<property>
    <name>xasecure.audit.destination.solr.batch.filespool.enabled</name>
    <value>true</value>
</property>

<property>
    <name>xasecure.audit.destination.solr.batch.filespool.dir</name>
    <value>/usr/local/hawq_<version>/ranger/plugin-service/logs/spool/audit/solr</value>
</property>
```

## <a id="hdfs"></a>Configuring HDFS Auditing
To configure an HDFS audit sink, define these auditing properties in `ranger-hawq-audit.xml`:

Table 2. Properties for HDFS Configuration

| Property | Value | Description |
| -------- | ----- | ----------- |
| xasecure.audit.destination.hdfs | true | Use this property to enable or disable the HDFS sink. |
| xasecure.audit.destination.hdfs.dir | &lt;HDFS directory&gt; | Specify the HDFS directory in which the plug-in records audit events. | 
| xasecure.audit.destination.hdfs.batch.filespool.* | Multiple Properties | See [Configuration related to File spooling](https://cwiki.apache.org/confluence/display/RANGER/Ranger+0.5+Audit+Configuration#Ranger0.5AuditConfiguration-ConfigurationrelatedtoFilespooling) in the Ranger documentation if you want to configure spooling of auditing events to disk when the in-memory buffer is full. |

For example:

```
<!-- ********************************* -->
<!-- HDFS audit provider configuration -->
<!-- ********************************* -->
<property>
    <name>xasecure.audit.destination.hdfs</name>
    <value>true</value>
</property>

<property>
    <name>xasecure.audit.destination.hdfs.dir</name>
    <value>hdfs://localhost:8020/ranger/audit</value>
</property>

<property>
    <name>xasecure.audit.destination.hdfs.batch.filespool.enabled</name>
    <value>true</value>
</property>

<property>
    <name>xasecure.audit.destination.hdfs.batch.filespool.dir</name>
    <value>/usr/local/hawq_<version>/ranger/plugin-service/logs/spool/audit/hdfs</value>
</property>
```
## <a id="log4j"></a>Configuring Log4j Auditing
To configure a Log4j audit sink, define these auditing properties in `ranger-hawq-audit.xml`:

Table 3. Properties for Log4j Configuration

| Property | Value | Description |
| -------- | ----- | ----------- |
| xasecure.audit.destination.log4j | true | Use this property to enable or disable the Log4j sink. |
| xasecure.audit.destination.log4j.logger | &lt;Logger Name&gt; | Specify the name of the logger to use for sending audit events. | 
| xasecure.audit.destination.log4j.batch.filespool.* | Multiple Properties | See [Configuration related to File spooling](https://cwiki.apache.org/confluence/display/RANGER/Ranger+0.5+Audit+Configuration#Ranger0.5AuditConfiguration-ConfigurationrelatedtoFilespooling) in the Ranger documentation if you want to configure spooling of auditing events to disk when the in-memory buffer is full. |

For example:

```
<!-- ********************************** -->
<!-- Log4j audit provider configuration -->
<!-- ********************************** -->
<property>
    <name>xasecure.audit.destination.log4j</name>
    <value>true</value>
</property>

<property>
    <name>xasecure.audit.destination.log4j.logger</name>
    <value>ranger_audit_logger</value>
</property>
```
