---
title: hawq ssh
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

Provides SSH access to multiple hosts at once.

## <a id="topic1__section2"></a>Synopsis

``` pre
hawq ssh -f <hostfile_hawqssh>) | (-h <hostname> [-h <hostname> ...]
    [-e]
    [-u <username>]
    [-v]
    [<bash_command>]

hawq ssh [-? | --help]

hawq ssh --version
```

## <a id="topic1__section3"></a>Description

The `hawq ssh` utility allows you to run bash shell commands on multiple hosts at once using SSH (secure shell). You can execute a single command by specifying it on the command-line, or omit the command to enter into an interactive command-line session.

To specify the hosts involved in the SSH session, use the `-f` option to specify a file containing a list of host names, or use the `-h` option to name single host names on the command-line. At least one host name (`-h`) or a host file (`-f`) is required. Note that the current host is ***not*** included in the session by default — to include the local host, you must explicitly declare it in the list of hosts involved in the session.

Before using `hawq ssh`, you must have a trusted host setup between the hosts involved in the SSH session. You can use the utility `hawq ssh-exkeys` to update the known host files and exchange public keys between hosts if you have not done so already.

If you do not specify a command on the command-line, `hawq ssh` will go into interactive mode. At the `hawq ssh` command prompt (`=>`), you can enter a command as you would in a regular bash terminal command-line, and the command will be executed on all hosts involved in the session. To end an interactive session, press `CTRL`+`D` on the keyboard or type `exit` or `quit`.

If a user name is not specified in the host file or via the `-u` option, `hawq ssh` will execute commands as the currently logged in user. To determine the currently logged in user, do a `whoami` command. By default, `hawq ssh` goes to `$HOME` of the session user on the remote hosts after login. To ensure commands are executed correctly on all remote hosts, you should always enter absolute paths.

## <a id="args"></a>Arguments
<dt>-f \<hostfile\_hawqssh\>  </dt>
<dd>Specifies the name of a file that contains a list of hosts that will participate in this SSH session. The host name is required, and you can optionally specify an alternate user name and/or SSH port number per host. The syntax of the host file is one host per line as follows:

``` pre
[username@]hostname[:ssh_port]
```
</dd>

<dt>-h \<hostname\>  </dt>
<dd>Specifies a single host name that will participate in this SSH session. You can use the `-h` option multiple times to specify multiple host names.</dd>


## <a id="topic1__section4"></a>Options

<dt>\<bash\_command\>   </dt>
<dd>A bash shell command to execute on all hosts involved in this session (optionally enclosed in quotes). If not specified, `hawq ssh` will start an interactive session.</dd>

<dt>-e (echo)  </dt>
<dd>Optional. Echoes the commands passed to each host and their resulting output while running in non-interactive mode.</dd>

<dt>-u \<username\>  </dt>
<dd>Specifies the userid for the SSH session.</dd>

<dt>-v (verbose mode)  </dt>
<dd>Reports additional messages in addition to the command output when running in non-interactive mode.</dd>

<dt>-\\\-version  </dt>
<dd>Displays the version of this utility.</dd>

<dt>-?, -\\\-help </dt>
<dd>Displays the online help.</dd>

## <a id="topic1__section5"></a>Examples

Start an interactive group SSH session with all hosts listed in the file `hostfile_hawqssh`:

``` shell
$ hawq ssh -f hostfile_hawqssh
```

At the `hawq ssh` interactive command prompt, run a shell command on all the hosts involved in this session.

``` pre
=> ls -a /data/path-to-masterdd/*
```

Exit an interactive session:

``` pre
=> exit
=> quit
```

Start a non-interactive group SSH session with the hosts named `sdw1` and `sdw2` and pass a file containing several commands named `command_file` to `hawq ssh`:

``` shell
$ hawq ssh -h sdw1 -h sdw2 -v -e < command_file
```

Execute single commands in non-interactive mode on hosts `sdw2` and `localhost`:

``` shell
$ hawq ssh -h sdw2 -h localhost -v -e 'ls -a /data/primary/*'
$ hawq ssh -h sdw2 -h localhost -v -e 'echo $GPHOME'
$ hawq ssh -h sdw2 -h localhost -v -e 'ls -1 | wc -l'
```

## See Also

[hawq ssh-exkeys](hawqssh-exkeys.html#topic1), [hawq scp](hawqscp.html#topic1)


