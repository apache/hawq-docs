---
title: HDFS Configuration Reference
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

This reference page describes HDFS configuration values that are configured for HAWQ either within `hdfs-site.xml`, `core-site.xml`, or `hdfs-client.xml`.

## <a id="topic_ixj_xw1_1w"></a>HDFS Site Configuration (hdfs-site.xml and core-site.xml)

This topic provides a reference of the HDFS site configuration values recommended for HAWQ installations. These parameters are located in either `hdfs-site.xml` or `core-site.xml` of your HDFS deployment.

This table describes the configuration parameters and values that are recommended for HAWQ installations. Only HDFS parameters that need to be modified or customized for HAWQ are listed.

| Parameter                                 | Description                                                                                                                                                                                                        | Recommended Value for HAWQ Installs                                   | Comments                                                                                                                                                               |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dfs.allow.truncate`                      | Allows truncate.                                                                                                                                                                                                   | true                                                                  | HAWQ requires that you enable `dfs.allow.truncate`. The HAWQ service will fail to start if `dfs.allow.truncate` is not set to `true`.                                  |
| `dfs.block.access.token.enable`           | If `true`, access tokens are used as capabilities for accessing DataNodes. If `false`, no access tokens are checked on accessing DataNodes.                                                                        | *false* for an unsecured HDFS cluster, or *true* for a secure cluster |                                                                                                                                                                        |
| `dfs.block.local-path-access.user`        | Comma separated list of the users allowed to open block files on legacy short-circuit local read.                                                                                                                  | gpadmin                                                               |                                                                                                                                                                        |
| `dfs.client.read.shortcircuit`            | This configuration parameter turns on short-circuit local reads.                                                                                                                                                   | true                                                                  | In Ambari, this parameter corresponds to **HDFS Short-circuit read**. The value for this parameter should be the same in `hdfs-site.xml` and HAWQ's `hdfs-client.xml`. |
| `dfs.client.socket-timeout`               | The amount of time before a client connection times out when establishing a connection or reading. The value is expressed in milliseconds.                                                                         | 300000000                                                             |                                                                                                                                                                        |
| `dfs.client.use.legacy.blockreader.local` | Setting this value to false specifies that the new version of the short-circuit reader is used. Setting this value to true means that the legacy short-circuit reader would be used.                               | false                                                                 |                                                                                                                                                                        |
| `dfs.datanode.data.dir.perm`              | Permissions for the directories on on the local filesystem where the DFS DataNode stores its blocks. The permissions can either be octal or symbolic.                                                              | 750                                                                   | In Ambari, this parameter corresponds to **DataNode directories permission**                                                                                           |
| `dfs.datanode.handler.count`              | The number of server threads for the DataNode.                                                                                                                                                                     | 60                                                                    |                                                                                                                                                                        |
| `dfs.datanode.max.transfer.threads`       | Specifies the maximum number of threads to use for transferring data in and out of the DataNode.                                                                                                                   | 40960                                                                 | In Ambari, this parameter corresponds to **DataNode max data transfer threads**                                                                                        |
| `dfs.datanode.socket.write.timeout`       | The amount of time before a write operation times out, expressed in milliseconds.                                                                                                                                  | 7200000                                                               |                                                                                                                                                                        |
| `dfs.domain.socket.path`                  | (Optional.) The path to a UNIX domain socket to use for communication between the DataNode and local HDFS clients. If the string "\_PORT" is present in this path, it is replaced by the TCP port of the DataNode. |                                                                       | If set, the value for this parameter should be the same in `hdfs-site.xml` and HAWQ's `hdfs-client.xml`.                                                               |
| `dfs.namenode.accesstime.precision`       | The access time for HDFS file is precise up to this value. Setting a value of 0 disables access times for HDFS.                                                                                                    | 0                                                                     | In Ambari, this parameter corresponds to **Access time precision**                                                                                                     |
| `dfs.namenode.handler.count`              | The number of server threads for the NameNode.                                                                                                                                                                     | 600                                                                   |                                                                                                                                                                        |
| `dfs.support.append`                      | Whether HDFS is allowed to append to files.                                                                                                                                                                        | true                                                                  |                                                                                                                                                                        |
| `ipc.client.connection.maxidletime`       | The maximum time in milliseconds after which a client will bring down the connection to the server.                                                                                                                | 3600000                                                               | In core-site.xml                                                                                                                                                       |
| `ipc.client.connect.timeout`              | Indicates the number of milliseconds a client will wait for the socket to establish a server connection.                                                                                                           | 300000                                                                | In core-site.xml                                                                                                                                                       |
| `ipc.server.listen.queue.size`            | Indicates the length of the listen queue for servers accepting client connections.                                                                                                                                 | 3300                                                                  | In core-site.xml                                                                                                                                                       |

## <a id="topic_l1c_zw1_1w"></a>HDFS Client Configuration (hdfs-client.xml)

This topic provides a reference of the HAWQ configuration values located in `$GPHOME/etc/hdfs-client.xml`.

This table describes the configuration parameters and their default values:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
<th>Default Value</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">dfs.client.failover.max.attempts</code></td>
<td>The maximum number of times that the DFS client retries issuing a RPC call when multiple NameNodes are configured.</td>
<td>15</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">dfs.client.log.severity</code></td>
<td>The minimal log severity level. Valid values include: FATAL, ERROR, INFO, DEBUG1, DEBUG2, and DEBUG3.</td>
<td>INFO</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">dfs.client.read.shortcircuit</code></td>
<td>Determines whether the DataNode is bypassed when reading file blocks, if the block and client are on the same node. The default value, true, bypasses the DataNode.</td>
<td>true</td>
<td>The value for this parameter should be the same in <code class="ph codeph">hdfs-site.xml</code> and HAWQ's <code class="ph codeph">hdfs-client.xml</code>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">dfs.client.use.legacy.blockreader.local</code></td>
<td>Determines whether the legacy short-circuit reader implementation, based on HDFS-2246, is used. Set this property to true on non-Linux platforms that do not have the new implementation based on HDFS-347.</td>
<td>false</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">dfs.default.blocksize</code></td>
<td>Default block size, in bytes.</td>
<td>134217728</td>
<td>Default is equivalent to 128 MB. </td>
</tr>
<tr class="even">
<td><code class="ph codeph">dfs.default.replica</code></td>
<td>The default number of replicas.</td>
<td>3</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">dfs.domain.socket.path</code></td>
<td>(Optional.) The path to a UNIX domain socket to use for communication between the DataNode and local HDFS clients. If the string &quot;_PORT&quot; is present in this path, it is replaced by the TCP port of the DataNode.</td>
<td> </td>
<td>If set, the value for this parameter should be the same in <code class="ph codeph">hdfs-site.xml</code> and HAWQ's <code class="ph codeph">hdfs-client.xml</code>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">dfs.prefetchsize</code></td>
<td>The number of blocks for which information is pre-fetched.</td>
<td>10</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">hadoop.security.authentication</code></td>
<td>Specifies the type of RPC authentication to use. A value of <code class="ph codeph">simple</code> indicates no authentication. A value of <code class="ph codeph">kerberos</code> enables authentication by Kerberos.</td>
<td>simple</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">input.connect.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the input stream is setting up a connection to a DataNode.</td>
<td>600000</td>
<td> Default is equal to 1 hour.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">input.localread.blockinfo.cachesize</code></td>
<td>The size of the file block path information cache, in bytes.</td>
<td>1000</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">input.localread.default.buffersize</code></td>
<td>The size of the buffer, in bytes, used to hold data from the file block and verify the checksum. This value is used only when <code class="ph codeph">dfs.client.read.shortcircuit</code> is set to true.</td>
<td>1048576</td>
<td>Default is equal to 1MB. Only used when is set to true.
<p>If an older version of <code class="ph codeph">hdfs-client.xml</code> is retained during upgrade, to avoid performance degradation, set the <code class="ph codeph">input.localread.default.buffersize</code> to 2097152. </p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">input.read.getblockinfo.retry</code></td>
<td>The maximum number of times the client should retry getting block information from the NameNode.</td>
<td>3</td>
<td></td>
</tr>
<tr class="even">
<td><code class="ph codeph">input.read.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the input stream is reading from a DataNode.</td>
<td>3600000</td>
<td>Default is equal to 1 hour.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">input.write.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the input stream is writing to a DataNode.</td>
<td>3600000</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">output.close.timeout</code></td>
<td>The timeout interval for closing an output stream, in milliseconds.</td>
<td>900000</td>
<td>Default is equal to 1.5 hours.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">output.connect.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the output stream is setting up a connection to a DataNode.</td>
<td>600000</td>
<td>Default is equal to 10 minutes.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">output.default.chunksize</code></td>
<td>The chunk size of the pipeline, in bytes.</td>
<td>512</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">output.default.packetsize</code></td>
<td>The packet size of the pipeline, in bytes.</td>
<td>65536</td>
<td>Default is equal to 64KB. </td>
</tr>
<tr class="even">
<td><code class="ph codeph">output.default.write.retry</code></td>
<td>The maximum number of times that the client should reattempt to set up a failed pipeline.</td>
<td>10</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">output.packetpool.size</code></td>
<td>The maximum number of packets in a file's packet pool.</td>
<td>1024</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">output.read.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the output stream is reading from a DataNode.</td>
<td>3600000</td>
<td>Default is equal to 1 hour. </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">output.replace-datanode-on-failure</code></td>
<td>Determines whether the client adds a new DataNode to pipeline if the number of nodes in the pipeline is less than the specified number of replicas.</td>
<td>false (if # of nodes less than or equal to 4), otherwise true</td>
<td>When you deploy a HAWQ cluster, the <code class="ph codeph">hawq init</code> utility detects the number of nodes in the cluster and updates this configuration parameter accordingly. However, when expanding an existing cluster to 4 or more nodes, you must manually set this value to true. Set to false if you remove existing nodes and fall under 4 nodes.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">output.write.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the output stream is writing to a DataNode.</td>
<td>3600000</td>
<td>Default is equal to 1 hour.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rpc.client.connect.retry</code></td>
<td>The maximum number of times to retry a connection if the RPC client fails connect to the server.</td>
<td>10</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">rpc.client.connect.tcpnodelay</code></td>
<td>Determines whether TCP_NODELAY is used when connecting to the RPC server.</td>
<td>true</td>
<td> </td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rpc.client.connect.timeout</code></td>
<td>The timeout interval for establishing the RPC client connection, in milliseconds.</td>
<td>600000</td>
<td>Default equals 10 minutes.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">rpc.client.max.idle</code></td>
<td>The maximum idle time for an RPC connection, in milliseconds.</td>
<td>10000</td>
<td>Default equals 10 seconds.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rpc.client.ping.interval</code></td>
<td>The interval which the RPC client send a heart beat to server. 0 means disable.</td>
<td>10000</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">rpc.client.read.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the RPC client is reading from the server.</td>
<td>3600000</td>
<td>Default equals 1 hour.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rpc.client.socket.linger.timeout</code></td>
<td>The value to set for the SO_LINGER socket when connecting to the RPC server.</td>
<td>-1</td>
<td> </td>
</tr>
<tr class="even">
<td><code class="ph codeph">rpc.client.timeout</code></td>
<td>The timeout interval of an RPC invocation, in milliseconds.</td>
<td>3600000</td>
<td>Default equals 1 hour.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rpc.client.write.timeout</code></td>
<td>The timeout interval, in milliseconds, for when the RPC client is writing to the server.</td>
<td>3600000</td>
<td>Default equals 1 hour.</td>
</tr>
</tbody>
</table>


