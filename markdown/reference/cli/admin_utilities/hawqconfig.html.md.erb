---
title: hawq config
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

Sets server configuration parameters on all nodes (master and segments) for HAWQ systems that are managed using command-line utilities.

**Note:** If you install and manage HAWQ using Ambari, do not use `hawq config` to configure HAWQ properties. Ambari will overwrite any changes that were made by `hawq config` when it restarts the cluster. For Ambari-managed HAWQ clusters, always use the Ambari administration interface to set or change HAWQ configuration properties.

## <a id="topic1__section2"></a>Synopsis

``` pre
hawq config -c <hawq_property> | --change <hawq_property> 
    -v <hawq_property_value> | --value <hawq_property_value> 
    [--skipvalidation] [--ignore-bad-hosts]
       
hawq config -r <hawq_property> | --remove <hawq_property> 
    [--skipvalidation] [--ignore-bad-hosts]  
  
hawq config -l | --list 
    [--ignore-bad-hosts] 
    
hawq config -s <hawq_property> | --show <hawq_property> 
    [--ignore-bad-hosts] 
    
hawq config --help
```

## <a id="topic1__section3"></a>Description

The `hawq config` utility allows you to set, unset, or view configuration properties from the `hawq-site.xml` files of all instances in your HAWQ system.

**Note:** The `hawq config` utility makes configuration properties identical and consistent across all nodes, including the master and segments. Using the utility will override any unique configurations that were defined manually in `hawq-site.xml`.

`hawq config` can only be used to manage specific properties. For example, you cannot use it to set properties such as `port`, which is required to be distinct for every segment instance. Use the `-l` (list) option to see a complete list of configuration properties supported by `hawq config`.

When `hawq config` sets a configuration property in a `hawq_site.xml` file, the new property setting always displays at the bottom of the file. When you use `hawq config` to remove a configuration property setting, `hawq config` comments out the property in all `hawq-site.xml` files, thereby restoring the system default setting. For example, if you use `hawq config `to remove (comment out) a property and later add it back (set a new value), there will be two instances of the property; one that is commented out, and one that is enabled and inserted at the bottom of the `hawq-site.xml` file.

After setting a property, you must restart your HAWQ system or reload the `hawq-site.xml` file for the change to take effect. Whether you require a restart or a reload depends on the property being set. To reload the configuration files, use `hawq stop cluster -u`. To restart the system, use `hawq restart` .

To show the currently set values for a property across the system, use the `-s` option.

`hawq config` uses the following environment variables to connect to the HAWQ master instance and obtain system configuration information:

-   `PGHOST`
-   `PGPORT`
-   `PGUSER`
-   `PGPASSWORD`
-   `PGDATABASE`

## <a id="topic1__section4"></a>Options

<dt>
-c, -\\\-change \<hawq\_property\>
</dt> 
<dd>Changes a HAWQ property setting by adding the new setting to the bottom of the `hawq-site.xml` files.</dd>

<dt>
-v, -\\\-value \<hawq\_property\_value\>  
</dt>
<dd>
Set the value of the HAWQ property setting in the `hawq-site.xml` files.
</dd>

<dt>
-r, -\\\-remove \<hawq\_property\> 
</dt>
<dd>
Removes a HAWQ property setting by commenting out the entry in the `hawq-site.xml` files.
</dd>

<dt>
-s, -\\\-show \<hawq\_property\> 
</dt>
<dd>
Shows the value for a HAWQ property name used on all instances (master and segments) in the HAWQ system. If there is a discrepancy in a parameter value between segment instances, the `hawq config` utility displays an error message. Note that the `hawq config` utility reads property values directly from the database, and not the `hawq-site.xml` file. If you are using `hawq config` to set properties across all segments, then running `hawq               config -s` to verify the changes, you might still see the previous (old) values. You must reload the configuration files (`hawq stop cluster -u`) or restart the system (`hawq restart`) for changes to take effect.
</dd>

<dt>
-l, -\\\-list
</dt>
<dd>
Lists all HAWQ property settings supported by the `hawq config` utility.
</dd>

<dt>
-\\\-skipvalidation 
</dt>
<dd>
Overrides the system validation checks of `hawq config` and allows you to operate on any server property, including hidden parameters and restricted parameters that cannot be changed by `hawq config`. Do not modify hidden or restricted parameters unless you are aware of all potential consequences. 
</dd>

<dt>
-\\\-ignore-bad-hosts 
</dt>
<dd>
Overrides copying configuration files to a host on which SSH validation fails. If ssh to a skipped host is reestablished, make sure the configuration files are re-synched once it is reachable.
</dd>

<dt>
-h, -\\\-help  
</dt>
<dd>
Displays the online help.
</dd>

## <a id="topic1__section5"></a>Examples

Set the `max_connections` setting to 100:

``` shell
$ hawq config -c max_connections -v 100
```

Comment out all instances of the `default_statistics_target` property, and restore the system default:

``` shell
$ hawq config -r default_statistics_target
```

List all properties supported by `hawq config`:

``` shell
$ hawq config -l
```

Show the values of a particular property across the system:

``` shell
$ hawq config -s max_connections
```

## <a id="topic1__section6"></a>See Also

[hawq stop](hawqstop.html#topic1)
