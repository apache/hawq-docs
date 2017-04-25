---
title: gpfdists Protocol
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

The `gpfdists://` protocol is a secure version of the `gpfdist://         protocol`. To use it, you run the `gpfdist` utility with the `--ssl` option. When specified in a URI, the `gpfdists://` protocol enables encrypted communication and secure identification of the file server and the HAWQ to protect against attacks such as eavesdropping and man-in-the-middle attacks.

`gpfdists` implements SSL security in a client/server scheme with the following attributes and limitations:

-   Client certificates are required.
-   Multilingual certificates are not supported.
-   A Certificate Revocation List (CRL) is not supported.
-   The `TLSv1` protocol is used with the `TLS_RSA_WITH_AES_128_CBC_SHA` encryption algorithm.
-   SSL parameters cannot be changed.
-   SSL renegotiation is supported.
-   The SSL ignore host mismatch parameter is set to `false`.
-   Private keys containing a passphrase are not supported for the `gpfdist` file server (server.key) and for the HAWQ (client.key).
-   Issuing certificates that are appropriate for the operating system in use is the user's responsibility. Generally, converting certificates as shown in [https://www.sslshopper.com/ssl-converter.html](https://www.sslshopper.com/ssl-converter.html) is supported.

    **Note:** A server started with the `gpfdist --ssl` option can only communicate with the `gpfdists` protocol. A server that was started with `gpfdist` without the `--ssl` option can only communicate with the `gpfdist` protocol.

-   The client certificate file, client.crt
-   The client private key file, client.key

Use one of the following methods to invoke the `gpfdists` protocol.

-   Run `gpfdist` with the `--ssl` option and then use the `gpfdists` protocol in the `LOCATION` clause of a `CREATE EXTERNAL TABLE` statement.
-   Use a `hawq load` YAML control file with the `SSL` option set to true.

Using `gpfdists` requires that the following client certificates reside in the `$PGDATA/gpfdists` directory on each segment.

-   The client certificate file, `client.crt`
-   The client private key file, `client.key`
-   The trusted certificate authorities, `root.crt`

For an example of loading data into an external table security, see [Example 3 - Multiple gpfdists instances](creating-external-tables-examples.html#topic47).


