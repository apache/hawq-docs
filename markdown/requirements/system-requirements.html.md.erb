---
title: Apache HAWQ System Requirements
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

Follow these guidelines to configure each host machine that will run an Apache HAWQ or PXF service.


## <a id="topic_d3f_vlz_g5"></a>Host Memory Configuration

In order to prevent data loss or corruption in an Apache HAWQ cluster, you must configure the memory on each host machine so that the Linux Out-of-Memory \(OOM\) killer process never kills a HAWQ process due to OOM conditions. \(HAWQ applies its own rules to enforce memory restrictions.\)

**For mission critical deployments of HAWQ, perform these steps on each host machine to configure memory:**

1.  Set the operating system `vm.overcommit_memory` parameter to 2. With this setting, the OOM killer process reports an error instead of killing running processes. To set this parameter:
    1.  Open the `/etc/sysctl.conf` file with a text editor.
    2.  Add or change the parameter definition so that the file includes these lines:

        ```
        kernel.threads-max=798720
        vm.overcommit_memory=2
        ```

    3.  Save and close the file, then execute this command to apply your change:

        ``` shell
        $ sysctl -p
        ```

    4.  To view the current `vm.overcommit_memory` setting, execute the command:

        ``` shell
        $ sysctl -a | grep overcommit_memory
        ```

    5.  To view the runtime overcommit settings, execute the command:

        ``` shell
        $ cat /proc/meminfo | grep Commit
        ```

2.  Set the Linux swap space size and `vm.overcommit_ratio` parameter according to the available memory on each host. For hosts having 2GB-8GB of memory, set swap space = physical RAM and set `vm.overcommit_ratio=50`. For hosts having more than 8GB up to 64GB of memory, set swap space = 0.5 \* physical RAM and set `vm.overcommit_ratio=50`. For hosts having more than 64GB memory, set swap space = 4GB and set `vm.overcommit_ratio=100`

    To set the `vm.overcommit_ratio` parameter:

    1.  Open the `/etc/sysctl.conf` file with a text editor.
    2.  Add or change the parameter definition so that the file includes the line:

           ```
       vm.overcommit_ratio=50
       ```

           \(Use `vm.overcommit_ratio=100` for hosts with more than 64GB RAM.\)
    3.  Save and close the file, then execute this command to apply your change:

        ``` shell
        $ sysctl -p
        ```

    4.  To view the current `vm.overcommit_ratio` setting, execute the command:

        ``` shell
        $ sysctl -a | grep overcommit_ratio
        ```
        You can choose to use a dedicated swap partition, a swap file, or a combination of both. View the current swap settings using the command:

        ``` shell
        $ cat /proc/meminfo | grep Swap
        ```
3.  Ensure that all Java services that run on the machine use the `-Xmx` switch to allocate only their required heap.
4.  Ensure that no other services \(such as Puppet\) or automated processes attempt to reset the overcommit settings on cluster hosts.
5.  During the installation process, configure HAWQ memory by setting YARN or HAWQ configuration parameters, as described in [HAWQ Memory Configuration](#topic_uzf_flz_g5).

## <a id="topic_uzf_flz_g5"></a>HAWQ Memory Configuration

You must configure the memory used by HAWQ according to whether you plan to use YARN or HAWQ to manage system resources.

After you configure the `vm.overcommit_ratio` and swap space according to [Host Memory Configuration](#topic_d3f_vlz_g5), the total memory available to a Linux host machine can be represented by the equation:

```
TOTAL_MEMORY = RAM * overcommit_ratio_percentage + SWAP
```

`TOTAL_MEMORY` comprises both HAWQ memory and `NON_HAWQ_MEMORY`, which is the memory used by components such as:

-   Operating system
-   DataNode
-   NodeManager
-   PXF
-   All other software you run on the host machine.

To configure the HAWQ memory for a given host, first determine the amount of `NON_HAWQ_MEMORY` that is used on the machine. Then configure HAWQ memory by setting the correct parameter according to whether you use the HAWQ default resource manager or YARN to manage resources:

-   If you are using YARN for resource management, set `yarn.nodemanager.resource.memory-mb` to the smaller of `TOTAL_MEMORY - NON_HAWQ_MEMORY` or `RAM`.
-   If you are using the HAWQ default resource manager, set `hawq_rm_memory_limit_perseg = RAM - NON_HAWQ_MEMORY`.

You can set either parameter using Ambari when configuring YARN or when installing HAWQ with Ambari.

### Example 1 - Large Host Machine

An example large host machine uses the memory configuration:

>RAM: 256GB
>
>SWAP: 4GB

>NON\_HAWQ\_MEMORY:

>> 2GB for Operating System

>> 2GB for DataNode

>> 2GB for NodeManager

>> 1GB for PXF

>overcommit\_ratio\_percentage:1 \(`vm.overcommit_ratio` = 100\)

For this machine, `TOTAL_MEMORY = 256GB * 1 + 4GB = 260GB`.

If this system uses YARN for resource management, you would set `yarn.nodemanager.resource.memory-mb` to `TOTAL_MEMORY - NON_HAWQ_MEMORY` = 260GB - 7GB = 253 \(because 253GB is smaller than the available amount of RAM\).

If this system uses the default HAWQ resource manager, you would set `hawq_rm_memory_limit_perseg` = `RAM - NON_HAWQ_MEMORY` = 256 GB - 7GB = 249.

### Example 2 - Medium Host Machine

An example medium host machine uses the memory configuration:

>RAM: 64GB

>SWAP: 32GB

>NON\_HAWQ\_MEMORY:

>>2GB for Operating System

>>2GB for DataNode

>>2GB for NodeManager

>>1GB for PXF

>overcommit\_ratio\_percentage: .5 \(`vm.overcommit_ratio` = 50\)

For this machine, `TOTAL_MEMORY = 64GB * .5 + 32GB = 64GB`.

If this system uses YARN for resource management, you would set `yarn.nodemanager.resource.memory-mb` to `TOTAL_MEMORY - NON_HAWQ_MEMORY` = 64GB - 7GB = 57 \(because 57GB is smaller than the available amount of RAM\).

If this system uses the default HAWQ resource manager, you would set `hawq_rm_memory_limit_perseg` = `RAM - NON_HAWQ_MEMORY` = 64 GB - 11GB = 57.

### Example 3 - Small Host Machine \(Not recommended for production use\)

An example small machine uses the memory configuration:

>RAM: 8GB

>SWAP: 8GB

>NON\_HAWQ\_MEMORY:

>>2GB for Operating System

>>2GB for DataNode

>>2GB for NodeManager

>>1GB for PXF

>overcommit\_ratio\_percentage:  .5 \(`vm.overcommit_ratio` = 50\)

For this machine, `TOTAL_MEMORY = 8GB * .5 + 8GB = 12GB`.

If this system uses YARN for resource management, you would set `yarn.nodemanager.resource.memory-mb` to `TOTAL_MEMORY - NON_HAWQ_MEMORY` = 12GB - 7GB = 5 \(because 5GB is smaller than the available amount of RAM\).

If this system uses the default HAWQ resource manager, you would set `hawq_rm_memory_limit_perseg` = `RAM - NON_HAWQ_MEMORY` = 8 GB - 7GB = 1.

## <a id="topic_pwdlessssh"></a>Passwordless SSH Configuration

HAWQ hosts will be configured to use passwordless SSH for intra-cluster communications during the installation process. Temporary password-based authentication must be enabled on each HAWQ host in preparation for this configuration.

1. Install the SSH server if not already configured on the HAWQ system:

    ``` shell
    $ yum list installed | grep openssh-server
    $ yum -y install openssh-server
    ```

2. Update the host's SSH configuration to allow password-based authentication. Edit the SSH config file and change the `PasswordAuthentication` configuration value from `no` to `yes`:

    ``` shell
    $ sudo vi /etc/ssh/sshd_config
    ```

    ```
    PasswordAuthentication yes
    ```

3. Restart SSH:

    ``` shell
    $ sudo service sshd restart
    ```

*After installation is complete*, you may choose to turn off the temporary password-based authentication configured in the previous steps:

1. Open the SSH `/etc/ssh/sshd_config` file in a text editor and update the configuration option you enabled in step 2 above:
    
    ```
    PasswordAuthentication no
    ```

2.  Restart SSH:
    
    ``` shell
    $ sudo service sshd restart
    ```
 

## <a id="topic_bsm_hhv_2v"></a>Disk Requirements

-   2GB per host for HAWQ installation. 
-   Approximately 300MB per segment instance for metadata.
-   Multiple large (2TB or greater) disks are recommended for HAWQ master and segment temporary directories. For a given query, HAWQ will use a separate temp directory (if available) for each virtual segment to store spill files. Multiple HAWQ sessions will also use separate temp directories where available to avoid disk contention. If you configure too few temp directories, or you place multiple temp directories on the same disk, you increase the risk of disk contention or running out of disk space when multiple virtual segments target the same disk. Each HAWQ segment node can have 6 virtual segments.  
-   Appropriate free space for data: disks should have at least 30% free space \(no more than 70% capacity\).
-   High-speed, local storage

## <a id="topic_rdb_jhv_2v"></a>Network Requirements

-   Gigabit Ethernet within the array. For a production cluster, 10 Gigabit Ethernet recommended.
-   Dedicated, non-blocking switch.
-   Systems with multiple NICs require NIC bonding to utilize all available network bandwidth.
-   Communication between the HAWQ master and segments requires reverse DNS lookup be configured in your cluster network.

## <a id="port-req"></a>Port Requirements
Individual PXF plug-ins, which you install after adding the HAWQ and PXF services, require that you Tomcat on the host machine. Tomcat reserves ports 8005, 8080, and 8009.

If you have configured Oozie JXM reporting on a host that will run a PXF plug-in, make sure that the reporting service uses a port other than 8005. This helps to prevent port conflict errors from occurring when you start the PXF service.

## <a id="umask"></a>Umask Requirement
Set the OS file system umask to 022 on all cluster hosts. This ensure that users can read the HDFS block files.
