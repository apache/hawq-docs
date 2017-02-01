---
title: SET
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

Changes the value of a HAWQ configuration parameter.

## <a id="topic1__section2"></a>Synopsis

``` pre
SET [SESSION | LOCAL] <configuration_parameter> {TO | =} {<value> | '<value>' | DEFAULT}
SET [SESSION | LOCAL] TIME ZONE {<timezone> | LOCAL | DEFAULT}
```

## <a id="topic1__section3"></a>Description

The `SET` command changes server configuration parameters. Any configuration parameter classified as a *session* parameter can be changed on-the-fly with `SET`. See [About Server Configuration Parameters](../guc/guc_config.html#topic1). `SET` only affects the value used by the current session.

If `SET` or `SET SESSION` is issued within a transaction that is later aborted, the effects of the `SET` command disappear when the transaction is rolled back. Once the surrounding transaction is committed, the effects will persist until the end of the session, unless overridden by another `SET`.

The effects of `SET LOCAL` only last till the end of the current transaction, whether committed or not. A special case is `SET` followed by `SET LOCAL` within a single transaction: the `SET                LOCAL` value will be seen until the end of the transaction, but afterwards (if the transaction is committed) the `SET` value will take effect.

## <a id="topic1__section4"></a>Parameters

<dt>SESSION  </dt>
<dd>Specifies that the command takes effect for the current session. This is the default.</dd>

<dt>LOCAL  </dt>
<dd>Specifies that the command takes effect for only the current transaction. After `COMMIT` or `ROLLBACK`, the session-level setting takes effect again. Note that `SET LOCAL` will appear to have no effect if it is executed outside of a transaction.</dd>

<dt> \<configuration\_parameter\>  </dt>
<dd>The name of a HAWQ configuration parameter. Only parameters classified as *session* can be changed with `SET`. See [About Server Configuration Parameters](../guc/guc_config.html#topic1).</dd>

<dt> \<value\>  </dt>
<dd>New value of parameter. Values can be specified as string constants, identifiers, numbers, or comma-separated lists of these. `DEFAULT` can be used to specify resetting the parameter to its default value. If specifying memory sizing or time units, enclose the value in single quotes.</dd>

<dt>TIME ZONE  </dt>
<dd>`SET TIME ZONE` value is an alias for `SET timezone TO                         value`.

<dt>LOCAL,  
DEFAULT  </dt>
<dd>Set the time zone to your local time zone (the one that the server's operating system defaults to).</dd>

<dt> \<timezone\>  </dt>
<dd>The \<timezone\> specification. Examples of syntactically valid values:

`'PST8PDT'`

`'Europe/Rome'`

`-7` (time zone 7 hours west from UTC)

`INTERVAL '-08:00' HOUR TO MINUTE` (time zone 8 hours west from UTC).</dd>
</dd>

## <a id="topic1__section5"></a>Examples

Set the schema search path:

``` sql
SET search_path TO my_schema, public;
```

Set the style of date to traditional POSTGRES with "day before month" input convention:

``` sql
SET datestyle TO postgres, dmy;
```

Set the time zone for San Mateo, California (Pacific Time):

``` sql
SET TIME ZONE 'PST8PDT';
```

Set the time zone for Italy:

``` sql
SET TIME ZONE 'Europe/Rome';
```

## <a id="topic1__section6"></a>Compatibility

`SET TIME ZONE` extends the syntax defined in the SQL standard. The standard allows only numeric time zone offsets while HAWQ allows more flexible time-zone specifications. All other `SET` features are HAWQ extensions.

## <a id="topic1__section7"></a>See Also

[RESET](RESET.html), [SHOW](SHOW.html)
