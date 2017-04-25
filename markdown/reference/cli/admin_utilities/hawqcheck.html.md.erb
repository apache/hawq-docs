---
title: hawq check
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

Verifies and validates HAWQ platform settings.

## <a id="topic1__section2"></a>Synopsis

``` pre
hawq check -f <hostfile_hawq_check> | (-h <hostname> | --host <hostname>)
    [--hadoop <hadoop_home> | --hadoop-home <hadoop_home>]
    [--config <config_file>] 
    [--stdout | --zipout]
    [--kerberos] 
    [--hdfs-ha] 
    [--yarn] 
    [--yarn-ha]
         
hawq check --zipin <hawq_check_zipfile>

hawq check --version

hawq check -?
```

## <a id="topic1__section3"></a>Description

The `hawq check` utility determines the platform on which you are running HAWQ and validates various platform-specific configuration settings as well as HAWQ and HDFS-specific configuration settings. In order to perform HAWQ configuration checks, make sure HAWQ has been already started and `hawq config` works. For HDFS checks, you should either set the `$HADOOP_HOME` environment variable or provide the full path to the hadoop installation location using the `--hadoop` option.

The `hawq check` utility can use a host file or a file previously created with the `--zipout `option to validate platform settings. If `GPCHECK_ERROR` displays, one or more validation checks failed. You can also use `hawq check` to gather and view platform settings on hosts without running validation checks. When running checks, `hawq check` compares your actual configuration setting with an expected value listed in a config file (`$GPHOME/etc/hawq_check.cnf` by default). You must modify your configuration values for "mount.points" and "diskusage.monitor.mounts" to reflect the actual mount points you want to check, as a comma-separated list. Otherwise, the utility only checks the root directory, which may not be helpful.

An example is shown below:

``` pre
[linux.mount] 
mount.points = /,/data1,/data2 

[linux.diskusage] 
diskusage.monitor.mounts = /,/data1,/data2
```
## <a id="args"></a>Arguments

<dt>-f \<hostfile\_hawq\_check\>  </dt>
<dd>The name of a file that contains a list of hosts that `hawq check` uses to validate platform-specific settings. This file should contain a single host name for all hosts in your HAWQ system (master, standby master, and segments).</dd>

<dt>-h, -\\\-host \<hostname\>  </dt>
<dd>Specifies a single host on which platform-specific settings will be validated.</dd>

<dt>-\\\-zipin \<hawq\_check\_zipfile\>  </dt>
<dd>Use this option to decompress and check a .zip file created with the `--zipout` option. If you specify the `--zipin` option, `hawq check` performs validation tasks against the specified file.</dd>


## <a id="topic1__section4"></a>Options


<dt>-\\\-config \<config\_file\>   </dt>
<dd>The name of a configuration file to use instead of the default file `$GPHOME/etc/hawq_check.cnf`.</dd>

<dt>-\\\-hadoop, -\\\-hadoop-home \<hadoop\_home\>  </dt>
<dd>Use this option to specify the full path to your hadoop installation location so that `hawq check` can validate HDFS settings. This option is not needed if the `$HADOOP_HOME` environment variable is set.</dd>

<dt>-\\\-stdout  </dt>
<dd>Send collected host information from `hawq check` to standard output. No checks or validations are performed.</dd>

<dt>-\\\-zipout  </dt>
<dd>Save all collected data to a .zip file in the current working directory. `hawq check` automatically creates the .zip file and names it `hawq_check_timestamp.tar.gz.` No checks or validations are performed.</dd>

<dt>-\\\-kerberos  </dt>
<dd>Use this option to check HDFS and YARN when running Kerberos mode. This allows `hawq check` to validate HAWQ/HDFS/YARN settings with Kerberos enabled.</dd>

<dt>-\\\-hdfs-ha  </dt>
<dd>Use this option to indicate that HDFS-HA mode is enabled, allowing `hawq               check` to validate HDFS settings with HA mode enabled.</dd>

<dt>-\\\-yarn  </dt>
<dd>If HAWQ is using YARN, enables yarn mode, allowing `hawq check` to validate the basic YARN settings.</dd>

<dt>-\\\-yarn-ha  </dt>
<dd>Use this option to indicate HAWQ is using YARN with High Availability mode enabled, to allow `hawq check` to validate HAWQ-YARN settings with YARN-HA enabled.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

<dt>-? (help)  </dt>
<dd>Displays the online help.</dd>

## <a id="topic1__section5"></a>Examples

Verify and validate the HAWQ platform settings by entering a host file and specifying the full hadoop install path:

``` shell
$ hawq check -f hostfile_hawq_check --hadoop /usr/hdp/<version>/hadoop
```

Verify and validate the HAWQ platform settings with HDFS HA enabled, YARN HA enabled and Kerberos enabled:

``` shell
$ hawq check -f hostfile_hawq_check --hadoop /usr/local/hadoop-<version> --hdfs-ha --yarn-ha --kerberos
```

Verify and validate the HAWQ platform settings with HDFS HA enabled, and Kerberos enabled:

``` shell
$ hawq check -f hostfile_hawq_check --hadoop /usr/hdp/<version>/hadoop --hdfs-ha --kerberos
```

Save HAWQ platform settings to a zip file, when the `$HADOOP_HOME` environment variable is set:

``` shell
$ hawq check -f hostfile_hawq_check --zipout  
```

Verify and validate the HAWQ platform settings using a zip file created with the `--zipout` option:

``` shell
$ hawq check --zipin hawq_check_timestamp.tar.gz
```

View collected HAWQ platform settings:

``` shell
$ hawq check -f hostfile_hawq_check --hadoop /usr/local/hadoop-<version> --stdout
```

## <a id="topic1__section6"></a>See Also

[hawq checkperf](hawqcheckperf.html#topic1)
