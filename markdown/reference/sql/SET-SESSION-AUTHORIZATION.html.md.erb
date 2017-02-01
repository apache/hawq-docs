---
title: SET SESSION AUTHORIZATION
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

Sets the session role identifier and the current role identifier of the current session.

## <a id="topic1__section2"></a>Synopsis

``` pre
SET [SESSION | LOCAL] SESSION AUTHORIZATION <rolename>
SET [SESSION | LOCAL] SESSION AUTHORIZATION DEFAULT
RESET SESSION AUTHORIZATION
```

## <a id="topic1__section3"></a>Description

This command sets the session role identifier and the current role identifier of the current SQL-session context to \<rolename\> . The role name may be written as either an identifier or a string literal. Using this command, it is possible, for example, to temporarily become an unprivileged user and later switch back to being a superuser.

The session role identifier is initially set to be the (possibly authenticated) role name provided by the client. The current role identifier is normally equal to the session user identifier, but may change temporarily in the context of setuid functions and similar mechanisms; it can also be changed by [SET ROLE](SET-ROLE.html). The current user identifier is relevant for permission checking.

The session user identifier may be changed only if the initial session user (the authenticated user) had the superuser privilege. Otherwise, the command is accepted only if it specifies the authenticated user name.

The `DEFAULT` and `RESET` forms reset the session and current user identifiers to be the originally authenticated user name. These forms may be executed by any user.

## <a id="topic1__section4"></a>Parameters

<dt>SESSION  </dt>
<dd>Specifies that the command takes effect for the current session. This is the default.</dd>

<dt>LOCAL  </dt>
<dd>Specifies that the command takes effect for only the current transaction. After `COMMIT` or `ROLLBACK`, the session-level setting takes effect again. Note that `SET LOCAL` will appear to have no effect if it is executed outside of a transaction.</dd>

<dt> \<rolename\>   </dt>
<dd>The name of the role to assume.</dd>

<dt>NONE  
RESET  </dt>
<dd>Reset the session and current role identifiers to be that of the role used to log in.</dd>

## <a id="topic1__section5"></a>Examples

``` sql
SELECT SESSION_USER, CURRENT_USER;
```
``` pre
 session_user | current_user 
--------------+--------------
 peter        | peter
```
``` sql
SET SESSION AUTHORIZATION 'paul';
SELECT SESSION_USER, CURRENT_USER;
```
``` pre
 session_user | current_user 
--------------+--------------
 paul         | paul
```

## <a id="topic1__section6"></a>Compatibility

The SQL standard allows some other expressions to appear in place of the literal \<rolename\>, but these options are not important in practice. HAWQ allows identifier syntax (\<rolename\>), while SQL does not. SQL does not allow this command during a transaction; HAWQ does not make this restriction. The `SESSION` and `LOCAL` modifiers are a HAWQ extension, as is the `RESET` syntax.

## <a id="topic1__section7"></a>See Also

[SET ROLE](SET-ROLE.html)
