---
title: hawq scp
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

Copies files between multiple hosts at once.

## <a id="topic1__section2"></a>Synopsis

``` pre
hawq scp -f <hostfile_hawqssh> | -h <hostname> [-h <hostname> ...] 
    [--ignore-bad-hosts] [-J <character>] [-r] [-v] 
    [[<user>@]<hostname>:]<file_to_copy> [...]
    [[<user>@]<hostname>:]<copy_to_path>

hawq scp -? 

hawq scp --version
```

## <a id="topic1__section3"></a>Description

The `hawq scp` utility allows you to copy one or more files from the specified hosts to other specified hosts in one command using SCP (secure copy). For example, you can copy a file from the HAWQ master host to all of the segment hosts at the same time.

To specify the hosts involved in the SCP session, use the `-f` option to specify a file containing a list of host names, or use the `-h` option to name single host names on the command-line. At least one host name (`-h`) or a host file (`-f`) is required. The `-J` option allows you to specify a single character to substitute for the *hostname* in the `<file_to_copy>` and `<copy_to_path>` destination strings. If `-J` is not specified, the default substitution character is an equal sign (`=`). For example, the following command will copy `.bashrc` from the local host to `/home/gpadmin` on all hosts named in `hostfile_gpssh`:

``` shell
$ hawq scp -f hostfile_hawqssh .bashrc =:/home/gpadmin
```

If a user name is not specified in the host list or with *user*`@` in the file path, `hawq scp` will copy files as the currently logged in user. To determine the currently logged in user, invoke the `whoami` command. By default, `hawq scp` copies to `$HOME` of the session user on the remote hosts after login. To ensure the file is copied to the correct location on the remote hosts, use absolute paths.

Before using `hawq scp`, you must have a trusted host setup between the hosts involved in the SCP session. You can use the utility `hawq ssh-exkeys` to update the known host files and exchange public keys between hosts if you have not done so already.

## <a id="topic1__section9"></a>Arguments
<dt>-f \<hostfile\_hawqssh\>  </dt>
<dd>Specifies the name of a file that contains a list of hosts that will participate in this SCP session. The syntax of the host file is one host per line as follows:

``` pre
<hostname>
```
</dd>

<dt>-h \<hostname\>  </dt>
<dd>Specifies a single host name that will participate in this SCP session. You can use the `-h` option multiple times to specify multiple host names.</dd>

<dt>\<file\_to\_copy\>  </dt>
<dd>The name (or absolute path) of a file or directory that you want to copy to other hosts (or file locations). This can be either a file on the local host or on another named host.</dd>

<dt>\<copy\_to\_path\>  </dt>
<dd>The path where you want the file(s) to be copied on the named hosts. If an absolute path is not used, the file will be copied relative to `$HOME` of the session user. You can also use the equal sign '`=`' (or another character that you specify with the `-J` option) in place of a \<hostname\>. This will then substitute in each host name as specified in the supplied host file (`-f`) or with the `-h` option.</dd>

## <a id="topic1__section4"></a>Options

<dt>
-\\\-ignore-bad-hosts 
</dt>
<dd>
Overrides copying configuration files to a host on which SSH validation fails. If SSH to a skipped host is reestablished, make sure the files are re-synched once it is reachable.
</dd>

<dt>-J \<character\>  </dt>
<dd>The `-J` option allows you to specify a single character to substitute for the \<hostname\> in the `<file_to_copy\>` and `<copy_to_path\>` destination strings. If `-J` is not specified, the default substitution character is an equal sign (`=`).</dd>


<dt>-v (verbose mode)  </dt>
<dd>Reports additional messages in addition to the SCP command output.</dd>

<dt>-r (recursive mode)  </dt>
<dd>If \<file\_to\_copy\> is a directory, copies the contents of \<file\_to\_copy\> and all subdirectories.</dd>

<dt>-? (help)  </dt>
<dd>Displays the online help.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

## <a id="topic1__section5"></a>Examples

Copy the file named `installer.tar` to `/` on all the hosts in the file `hostfile_hawqssh`.

``` shell
$ hawq scp -f hostfile_hawqssh installer.tar =:/
```

Copy the file named *myfuncs.so* to the specified location on the hosts named `sdw1` and `sdw2`:

``` shell
$ hawq scp -h sdw1 -h sdw2 myfuncs.so =:/usr/local/-db/lib
```

## See Also

[hawq ssh](hawqssh.html#topic1), [hawq ssh-exkeys](hawqssh-exkeys.html#topic1)


