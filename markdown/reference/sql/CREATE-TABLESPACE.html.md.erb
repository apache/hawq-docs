---
title: CREATE TABLESPACE
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

Defines a new tablespace.

## <a id="topic1__section2"></a>Synopsis

``` pre
CREATE TABLESPACE <tablespace_name> [OWNER <username>]
       FILESPACE <filespace_name>
         
```

## <a id="topic1__section3"></a>Description

`CREATE TABLESPACE` registers a new tablespace for your HAWQ system. The tablespace name must be distinct from the name of any existing tablespace in the system.

A tablespace allows superusers to define an alternative location on the file system where the data files containing database objects (such as tables) may reside.

A user with appropriate privileges can pass a tablespace name to [CREATE DATABASE](CREATE-DATABASE.html) or [CREATE TABLE](CREATE-TABLE.html) to have the data files for these objects stored within the specified tablespace.

In HAWQ, there must be a file system location defined for the master and each segment in order for the tablespace to have a location to store its objects across an entire HAWQ system. This collection of file system locations is defined in a filespace object. A filespace must be defined before you can create a tablespace. See [hawq filespace](../cli/admin_utilities/hawqfilespace.html#topic1) for more information.

## <a id="topic1__section4"></a>Parameters

<dt> \<tablespacename\>   </dt>
<dd>The name of a tablespace to be created. The name cannot begin with `pg_`, as such names are reserved for system tablespaces.</dd>

<dt>OWNER \<username\>   </dt>
<dd>The name of the user who will own the tablespace. If omitted, defaults to the user executing the command. Only superusers may create tablespaces, but they can assign ownership of tablespaces to non-superusers.</dd>

<dt>FILESPACE \<filespace\_name\>   </dt>
<dd>The name of a HAWQ filespace that was defined using the `hawq filespace` management utility.</dd>

## <a id="topic1__section5"></a>Notes

You must first create a filespace to be used by the tablespace. See [hawq filespace](../cli/admin_utilities/hawqfilespace.html#topic1) for more information.

Tablespaces are only supported on systems that support symbolic links.

`CREATE TABLESPACE` cannot be executed inside a transaction block.

## <a id="topic1__section6"></a>Examples

Create a new tablespace by specifying the corresponding filespace to use:

``` pre
CREATE TABLESPACE mytblspace FILESPACE myfilespace;
```

## <a id="topic1__section7"></a>Compatibility

`CREATE TABLESPACE` is a HAWQ extension.

## <a id="topic1__section8"></a>See Also

[CREATE DATABASE](CREATE-DATABASE.html), [CREATE TABLE](CREATE-TABLE.html), [DROP TABLESPACE](DROP-TABLESPACE.html)
