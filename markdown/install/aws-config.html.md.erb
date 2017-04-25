---
title: Amazon EC2 Configuration
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

Amazon Elastic Compute Cloud (EC2) is a service provided by Amazon Web Services (AWS).  You can install and configure HAWQ on virtual servers provided by Amazon EC2. The following information describes some considerations when deploying a HAWQ cluster in an Amazon EC2 environment.

## <a id="topic_wqv_yfx_y5"></a>About Amazon EC2 

Amazon EC2 can be used to launch as many virtual servers as you need, configure security and networking, and manage storage. An EC2 *instance* is a virtual server in the AWS cloud virtual computing environment.

EC2 instances are managed by AWS. AWS isolates your EC2 instances from other users in a virtual private cloud (VPC) and lets you control access to the instances. You can configure instance features such as operating system, network connectivity (network ports and protocols, IP addresses), access to the Internet, and size and type of disk storage. 

For information about Amazon EC2, see the [EC2 User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

## <a id="topic_nhk_df4_2v"></a>Create and Launch HAWQ Instances

Use the **Amazon EC2 Console** to launch instances and configure, start, stop, and terminate (delete) virtual servers. When you launch a HAWQ instance, you select and configure key attributes via the EC2 Console.


### <a id="topic_amitype"></a>Choose AMI Type

An Amazon Machine Image (AMI) is a template that contains a specific software configuration including the operating system, application server, and applications that best suit your purpose. When configuring a HAWQ virtual instance, use a *hardware virtualized* (HVM) AMI supporting enhanced 10Gbps networking. Ensure the AMI is running 64-bit Red Hat Enterprise Linux version 6.4 or 6.5 or 64-bit CentOS 6.4 or 6.5.  Obtain the licenses and instances directly from the OS provider.

### <a id="topic_selcfgstorage"></a>Consider Storage
You can launch EC2 instances as either Elastic Block Store (EBS)-backed or instance store-backed. Choose the storage type based on the expected lifetime of your cluster and data.

#### <a id="topic_selcfgstorage_instance"></a>Instance Store-Backed

Use instance store-backed storage for short lived or transient clusters that do not require long-term persistence of data. While instance store-backed storage is generally better performing than EBS, it is not recommended for use in a production environment.

**Warning**: EC2 instance store-backed storage provides *temporary* block-level storage. This storage is located on disks that are physically attached to the host computer. You will lose all instance store data when the AMI instance is powered off.


#### <a id="topic_selcfgstorage_ebs"></a>EBS-Backed
EBS volumes are reliable and highly-available. Use EBS-backed storage for longer running clusters where data must be quickly accessible and must remain available for a long period of time.


#### <a id="topic_selcfgstorage_volume"></a>Volume Types
When selecting between HDD and SSD volume types, the trade-offs are between speed, capacity, and cost. HDD volumes are less expensive and have greater disk capacity, but may be less performant. SSD (solid state drive) volumes are more performant, but costlier and typically have less disk capacity.

### <a id="topic_cfgplacegrp"></a>Configure Placement Group 

A placement group is a logical grouping of instances within a single availability zone that participate in a low-latency, 10 Gbps network. Your HAWQ master and segment cluster instances should support enhanced networking and reside in a single placement group (and subnet) for optimal network performance.

If your Ambari node is not a DataNode, locating the Ambari node instance in a subnet separate from the HAWQ master/segment placement group enables you to manage multiple HAWQ clusters from the single Ambari instance.

Amazon recommends that you use the same instance type for all instances in the placement group and that you launch all instances within the placement group at the same time.

Membership in a placement group has some implications for your HAWQ cluster.  Specifically, growing the cluster beyond the placement group capacity may require shutting down all HAWQ instances in the current placement group and restarting the instances in a new placement group. **Warning**: Instance store volumes are lost in this scenario.

**Note**: If cluster down time during expansion is not acceptable for your HAWQ deployment, do not use placement groups.

### <a id="topic_selinsttype"></a>Select EC2 Instance Type

An EC2 instance type is a specific combination of CPU, memory, default storage, and networking capacity.  

Several instance store-backed EC2 instance types have shown acceptable performance for HAWQ nodes in development and production environments: 

| Instance Type  | Env | vCPUs | Memory (GB) | Disk Capacity (GB) | Storage Type | Network Speed |
|-------|-----|------|--------|----------|--------|-------|
| d2.2xlarge  | Dev | 8 | 60 | 6 x 2000 | HDD | High |
| d2.4xlarge  | Dev/QA | 16 | 122 | 12 x 2000 | HDD | High |
| c3.8xlarge  | Dev/QA | 32 | 60 | 2 x 320 | SSD | 10 Gigabit |
| r3.8xlarge  | Dev/QA | 32 | 244 | 2 x 320 | SSD | 10 Gigabit |
| i2.8xlarge  | Prod | 32 | 244 | 8 x 800 | SSD | 10 Gigabit |
| d2.8xlarge  | Prod | 36 | 244 | 24 x 2000 | HDD | 10 Gigabit |
 
**Note**: This list is not exhaustive. You may find other instance types with similar specifications suitable for your HAWQ deployment.

For optimal network performance, the chosen HAWQ instance type should support EC2 enhanced networking. Enhanced networking results in higher performance, lower latency, and lower jitter. Refer to [Enhanced Networking on Linux Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) for detailed information on enabling enhanced networking in supported EC2 instance types.


### <a id="topic_cfgnetw"></a>Configure Networking and VPC

Place your HAWQ cluster instances in a single VPC and on the same subnet. Instances are always assigned a VPC internal IP address. Use this internal IP address for HAWQ communication between hosts. You can also use the internal IP address to access an instance from another instance within the HAWQ VPC.

You may choose to locate your Ambari node on a separate subnet in the VPC. Both a public IP address for the instance and an Internet gateway configured for the EC2 VPC are required to access the Ambari instance from an external source and for the instance to access the Internet. 

Ensure your Ambari and HAWQ master instances are each assigned a public IP address for external and internet access. Also assign an Elastic IP Address to the HAWQ master instance.


###Configure Security Groups<a id="topic_cfgsecgrp"></a>

A security group is a set of rules that control network traffic to and from your HAWQ instance.  One or more rules may be associated with a security group, and one or more security groups may be associated with an instance.

To configure HAWQ communication between nodes in a HAWQ cluster, include and open appropriate ports in the security group for the HAWQ master and segment nodes. For example, if you have a single VPC, you may create a single security group named `hawq-cluster-sg` for your cluster, and configure this security group to open the following ports:

| Port  | Protocol | Application | Source |
|-------|----------|--------------|-------------|
| -1    |  ICMP | `ping` | `hawq-cluster-sg` |
| 5432    | TCP     | HAWQ/Postgres | cidr 0.0.0.0/0 |
| 50700    |  TCP   | HDFS NameNode |  cidr 0.0.0.0/0 |
| 0-65535 | TCP | `ssh`, HAWQ segment communication  | `hawq-cluster-sg` |
| 0-65535 | UDP | HAWQ segment communication  | `hawq-cluster-sg` |

This configuration allows communication between the HAWQ segment nodes. It also allows `ping` on and `ssh` between all instances in the `hawq-cluster-sg`  security group. The HAWQ master and HDFS NameNode ports are open with the above settings.

Open and/or restrict these and any additional ports required for your HAWQ deployment environment.

Include and open the following ports in an appropriate security group for your Ambari node to allow access to/from a source external to this node:

| Port  | Protocol | Application |
|-------|-----------------|--------------------|
| 22    | TCP | `ssh` - secure shell to/from other hosts |
| 8080  | TCP | Ambari - HAWQ admininstration web console |


###Generate Key Pair<a id="topic_cfgkeypair"></a>
AWS uses public-key cryptography to secure the login information for your instance. You use the EC2 console to generate and name a key pair when you launch your instance.  

A key pair for an EC2 instance consists of a *public key* that AWS stores, and a *private key file* that you maintain. Together, they allow you to connect to your instance securely. The private key file name typically has a `.pem` suffix.

The following example logs into an into EC2 instance from an external location with the private key file `my-test.pem` as user `user1`.  In this example, the instance is configured with the public IP address `192.0.2.0` and the private key file resides in the current directory.

```shell
$ ssh -i ./my-test.pem user1@192.0.2.0
```

##Additional HAWQ Considerations <a id="topic_mj4_524_2v"></a>

After launching your HAWQ instance, you will connect to and configure the instance. The **Instances** page of the EC2 Console lists the running instances and their associated network access information.

Before installing HAWQ, set up the EC2 instances as you would local host server machines. Configure the host operating system, configure host network information (for example, update the `/etc/hosts` file), set operating system parameters, and install operating system packages. [Apache HAWQ System Requirements](../requirements/system-requirements.html) and [Select HAWQ Host Machines](../install/select-hosts.html) provide the information necessary to prepare your operating system environment for HAWQ.

###Passwordless SSH Configuration<a id="topic_pwdlessssh_cc"></a>

HAWQ hosts are configured during the installation process to use passwordless SSH for intra-cluster communications. Temporary password-based authentication must be enabled on each HAWQ host in preparation for this configuration.

Password authentication is typically disabled by default in cloud images. Update the cloud configuration in `/etc/cloud/cloud.cfg` to enable password authentication in your AMI(s). Set `ssh_pwauth: True` in this configuration file. If desired, set the property back to `False` after HAWQ installation to disable password authentication.
  
##References<a id="topic_hgz_zwy_bv"></a>

Links to related Amazon Web Services and EC2 features and information.

- [Amazon Web Services](https://aws.amazon.com)
- [Amazon Machine Image \(AMI\)](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [EC2 Instance Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Elastic Block Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)
- [EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [Elastic IP Address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Enhanced Networking on Linux Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [Internet Gateways] (http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html)
- [Subnet Public IP Addressing](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html#subnet-public-ip)
- [Virtual Private Cloud](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
