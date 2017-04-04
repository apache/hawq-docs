---
title: Using the Ambari REST API
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

You can monitor and manage the resources in your HAWQ cluster using the Ambari REST API.  In addition to providing access to the metrics information in your cluster, the API supports viewing, creating, deleting, and updating cluster resources.

This section will provide an introduction to using the Ambari REST APIs for HAWQ-related cluster management activities.

Refer to [Ambari API Reference v1](https://github.com/apache/ambari/blob/trunk/ambari-server/docs/api/v1/index.md) for the official Ambari API documentation, including full REST resource definitions and response semantics. *Note*: These APIs may change in new versions of Ambari.


## <a id="ambari-rest-uri"></a>Manageable HAWQ Resources

HAWQ provides several REST resources to support starting and stopping services, executing service checks, and viewing configuration information among other activities. HAWQ resources you can manage using the Ambari REST API include:

| Ambari Resource      | Description     |
|----------------------|------------------------|
| cluster | The HAWQ cluster. |
| service | The HAWQ and PXF service. You can manage other Hadoop services as well. |
| component | A specific HAWQ/PXF service component, i.e. the HAWQ Master, PXF. |
| configuration | A specific HAWQ/PXF configuration entity, for example the hawq-site or pxf-profiles configuration files, or a specific single HAWQ or PXF configuration property. |
| request | A group of tasks. |

## <a id="ambari-rest-uri"></a>URI Structure

The Ambari REST API provides access to HAWQ cluster resources via URI (uniform resource identifier) paths. To use the Ambari REST API, you will send HTTP requests and parse JSON-formatted HTTP responses.

The Ambari REST API supports standard HTTP request methods including:

- `GET` - read resource properties, metrics
- `POST` - create new resource
- `PUT` - update resource
- `DELETE` - delete resource (use with care)

**Note**: Be careful when using `DELETE` or `PUT` requests; typos or other incorrect usage may leave your cluster in an inoperable state.

URIs for Ambari REST API resources have the following structure:

``` shell
http://<ambari-server-host>:<port>/api/v1/<resource-path>
```

The Ambari REST API supports the following HAWQ-related \<resource-paths\>:

| REST Resource Path              | Description     |
|----------------------|------------------------|
| clusters/\<cluster\-name\> | The HAWQ cluster name. |
| clusters/\<cluster\-name\>/services/PXF | The PXF service. |
| clusters/\<cluster\-name\>/services/HAWQ | The HAWQ service. |
| clusters/\<cluster\-name\>/services/HAWQ/components | All HAWQ service components. |
| clusters/\<cluster\-name\>/services/HAWQ/components/\<name\> | A specific HAWQ service component, i.e. HAWQMASTER. |
| clusters/\<cluster\-name\>/configurations | Cluster configurations. |
| clusters/\<cluster\-name\>/requests | Group of tasks that run a command. |

## <a id="ambari-rest-curl"></a>Submitting Requests with cURL

Your HTTP request to the Ambari REST API should include the following information:

- User name and password for basic authentication.
- An HTTP request header.
- The HTTP request method.
- JSON-formatted request data, if required.
- The URI identifying the Ambari REST resource.

You can use the `curl` command to transfer HTTP request data to, and receive data from, the Ambari server using the HTTP protocol.

Use the following syntax to issue a `curl` command for Ambari HAWQ/PXF management operations:

``` shell
$ curl -u <user>:<passwd> -H <header> -X GET|POST|PUT|DELETE -d <data> <URI>
```

`curl` options relevant to Ambari REST API communication include:

| Option              | Description     |
|----------------------|------------------------|
| -u \<user\>:\<passwd\> | Identify the username and password for basic authentication to the HTTP server. |
| -H \<header\>   | Identify an extra header to include in the HTTP request. \<header\> must specify `'X-Requested-By:ambari'`.   |
| -X \<command\>   | Identify the request method. \<command\> may specify `GET` (the default), `POST`, `PUT`, and `DELETE`. |
| -d \<data\>     | Send the specified \<data\> to the HTTP server along with the request. The \<command\> and \<URI\> determine if \<data\> is required, and if so, its content.  |
| \<URI\>    | Path to the Ambari REST resource.  |


## <a id="ambari-rest-api-auth"></a>Authenticating with the Ambari REST API

The first step in using the Ambari REST API is to authenticate with the Ambari server. The Ambari REST API supports HTTP basic authentication. With this authentication method, you provide a username and password that is internally encoded and sent in the HTTP header.

Example: Testing Authentication

1. Set up some environment variables; replace the values with those appropriate for your operating environment.  For example:

    ``` shell
    $ export AMBARI_USER=admin
    $ export AMBARI_PASSWD=admin
    $ export AMBARI_HOST=<ambari-server>
    $ export AMBARI_PORT=8080
    ```

2. Submit a `curl` request to the Ambari server:

    ``` shell
    $ curl -u $AMBARI_USER:$AMBARI_PASSWD http://$AMBARI_HOST:$AMBARI_PORT
    ```
    
    If authentication succeeds, Apache license information is displayed.


## <a id="ambari-rest-using"></a>Using the Ambari REST API for HAWQ Management


### <a id="ambari-rest-ex-clustname"></a>Example: Retrieving the HAWQ Cluster Name

1. Set up an additional environment variables:

    ``` shell
    $ export AMBARI_CREDS="$AMBARI_USER:$AMBARI_PASSWD"
    $ export AMBARI_URLBASE="http://${AMBARI_HOST}:${AMBARI_PORT}/api/v1/clusters"
    ```
    
    You will use these variables in upcoming examples to simplify `curl` calls.
    
2. Use the Ambari REST API to determine the name of your HAWQ cluster; also set `$AMBARI_URLBASE` to include the cluster name:

    ``` shell
    $ export CLUSTER_NAME="$(curl -u ${AMBARI_CREDS} -i -H 'X-Requested-By:ambari' $AMBARI_URLBASE | sed -n 's/.*"cluster_name" : "\([^\"]*\)".*/\1/p')"
    $ echo $CLUSTER_NAME
    TestCluster
    $ export AMBARI_URLBASE=$AMBARI_URLBASE/$CLUSTER_NAME
    ```

### <a id="ambari-rest-ex-mgmt"></a>Examples: Managing the HAWQ and PXF Services

The following subsections provide `curl` commands for common HAWQ cluster management activities.

Refer to [API usage scenarios, troubleshooting, and other FAQs](https://cwiki.apache.org/confluence/display/AMBARI/API+usage+scenarios%2C+troubleshooting%2C+and+other+FAQs) for additional Ambari REST API usage examples.


#### <a id="ambari-rest-ex-get"></a>Viewing HAWQ Cluster Service and Configuration Information

| Task              |Command           |
|----------------------|------------------------|
| View HAWQ service information. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' $AMBARI_URLBASE/services/HAWQ` |
| List all HAWQ components. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' $AMBARI_URLBASE/services/HAWQ/components` |
| View information about the HAWQ master. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' $AMBARI_URLBASE/services/HAWQ/components/HAWQMASTER` |
| View the `hawq-site` configuration settings. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' "$AMBARI_URLBASE/configurations?type=hawq-site&tag=TOPOLOGY_RESOLVED"` |
| View the initial `core-site` configuration settings. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' "$AMBARI_URLBASE/configurations?type=core-site&tag=INITIAL"` |
| View the `pxf-profiles` configuration file. | `curl -u $AMBARI_CREDS -X GET -H 'X-Requested-By:ambari' "$AMBARI_URLBASE/configurations?type=pxf-profiles&tag=INITIAL"` |
| View all components on node. | `curl -u $AMBARI_CREDS -i  -X GET -H 'X-Requested-B:ambari' $AMBARI_URLBASE/hosts/<hawq-node>` |


#### <a id="ambari-rest-ex-put"></a>Starting/Stopping HAWQ and PXF Services

| Task              |Command           |
|----------------------|------------------------|
| Start the HAWQ service. | `curl -u $AMBARI_CREDS -X PUT -H 'X-Requested-By:ambari' -d '{"RequestInfo": {"context" :"Start HAWQ via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' $AMBARI_URLBASE/services/HAWQ` |
| Stop the HAWQ service. | `curl -u $AMBARI_CREDS -X PUT -H 'X-Requested-By:ambari' -d '{"RequestInfo": {"context" :"Stop HAWQ via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' $AMBARI_URLBASE/services/HAWQ` |
| Start the PXF service. | `curl -u $AMBARI_CREDS -X PUT -H 'X-Requested-By:ambari' -d '{"RequestInfo": {"context" :"Start PXF via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' $AMBARI_URLBASE//services/PXF` |
| Stop the PXF service. | `curl -u $AMBARI_CREDS -X PUT -H 'X-Requested-By:ambari' -d '{"RequestInfo": {"context" :"Stop PXF via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' $AMBARI_URLBASE/services/PXF` |

#### <a id="ambari-rest-ex-post"></a>Invoking HAWQ and PXF Service Actions

| Task              |Command           |
|----------------------|------------------------|
| Run a HAWQ service check. | `curl -u $AMBARI_CREDS -X POST -H 'X-Requested-By:ambari' -d '{"RequestInfo":{"context":"HAWQ Service Check","command":"HAWQ_SERVICE_CHECK"}, "Requests/resource_filters":[{ "service_name":"HAWQ"}]}'  $AMBARI_URLBASE/requests` |
| Run a PXF service check. | `curl -u $AMBARI_CREDS -X POST -H 'X-Requested-By:ambari' -d '{"RequestInfo":{"context":"PXF Service Check","command":"PXF_SERVICE_CHECK"}, "Requests/resource_filters":[{ "service_name":"PXF"}]}'  $AMBARI_URLBASE/requests` |
