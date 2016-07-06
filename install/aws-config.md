---
title: Amazon EC2 Configuration
---

Amazon Elastic Compute Cloud (EC2) is a service provided by Amazon Web Services (AWS).  You can install and configure HAWQ on virtual servers provided by Amazon EC2. The following information describes some considerations when installing a HAWQ cluster in an Amazon EC2 environment.

## <a id="topic_wqv_yfx_y5"></a>About Amazon EC2 

Amazon EC2 can be used to launch as many virtual servers as you need, configure security and networking, and manage storage. An EC2 *instance* is a virtual server in the AWS cloud virtual computing environment.

EC2 instances are managed by AWS. AWS isolates your EC2 instances from other users in a virtual private cloud (VPC) and lets you control access to the instances. You can configure instance features such as operating system, network connectivity (network ports and protocols, IP addresses), access to the Internet, and size and type of disk storage. 

For information about Amazon EC2, see the [EC2 User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

## <a id="topic_nhk_df4_2v"></a>Create and Launch HAWQ Instances

Use the *Amazon EC2 Console* to launch instances and configure, start, stop, and terminate (delete) virtual servers. When you launch a HAWQ instance, you select and configure key attributes via the EC2 Console.


### <a id="topic_amitype"></a>Choose AMI Type

An Amazon Machine Image (AMI) is a template that contains a software configuration including the operating system, application server, and applications that best suit your purpose. When configuring a HAWQ virtual instance, select an AMI that runs an operating system supported by HAWQ. Refer to the Release Notes for the HAWQ version that you are installing for a list of supported OS platforms. 


### <a id="topic_selcfgstorage"></a>Consider Storage
**HAWQ** supports either EC2 instance store or Amazon EBS in production environments.

 - EC2 *instance store* provides temporary block-level storage. This storage is located on disks that are physically attached to the host computer. Powering off the instance causes data loss when using instance store storage. Soft reboots preserve instance store data. 
     
     Virtual devices for instance store volumes for HAWQ EC2 instance store instances are named `ephemeralN` (where *N* is between 0 and 23). CentOS instance store block device names appear as `/dev/xvdletter` (where *letter* is a lower case letter of the alphabet).
       
 - Amazon *Elastic Block Store* (EBS) provides block level storage volumes with long-term persistence. When using Amazon EBS, HAWQ supports only EBS-Optimized instance types.  EBS provides block level storage volumes with long-term persistence. HAWQ supported configurations using EBS must be a RAID of Amazon EBS volumes mounted with the XFS file system. All other file systems are explicitly not supported.  
 
    Select an EBS volume type of `gp2` or `io1` when configuring a virtual HAWQ server.


### <a id="topic_selinsttype"></a>Select EC2 Instance Type

An EC2 instance types is a specific combination of CPU, memory, default storage, and networking capacity.  Two EC2 instance types configured with instance store showed acceptable performance for HAWQ nodes.  These include the `d2.8xlarge` instance type configured with four `raid0` volumes of 6 disks each, and the `i2.8xlarge`  instance type configured with two `raid0` volumes of 4 disks. 

Select an EC2 instance type of ??x1 r3??  for your HAWQ EBS node.  ??DESCRIBE FURTHER HERE??

For sufficient network performance, the chosen instance type must support EC2 enhanced networking. To enable enhanced networking on your Red Hat and CentOS RHEL/CentOS HAWQ instance, you must ensure that the kernel has the `ixgbevf` module version 2.14.2 or higher installed and that the `sriovNetSupport` attribute is set. 


### <a id="topic_cfgnetw"></a>Configure Networking 

The HAWQ cluster instances should be in a single VPC and subnet. Instances are always assigned a VPC internal IP address and may be assigned a public IP address for external and Internet access.  You may choose to assign an Elastic IP Address to your instance.

The internal IP address is used for HAWQ communication between hosts. You can also use the internal IP address to access an instance from another instance within the EC2 VPC. 

Both a public IP address for the instance and an Internet gateway configured for the EC2 VPC are required to access the HAWQ instance from an external source and for the instance to access the Internet.


###Configure Security Groups<a id="topic_cfgsecgrp"></a>

A security group is a set of rules that control network traffic to and from your HAWQ instance.  One or more rules may be associated with a security group, and one or more security groups may be associated with an instance.

To allow access to/from a source external to the HAWQ cluster, include and open the following ports in the appropriate security group.

?? PROVIDE SPECIFIC type/protocol/portrange/source settings from EC2 console ??

| Port  | Application |
|-------|-------------------------------------|
| 22    | ssh - secure connect to other hosts |
| 8080  | Ambari - HAWQ admin/config web console |  

UDP network traffic must be permitted between each HAWQ cluster node.  Enable this access by creating or modifying a security group to include rules for inbound and outbound UDP protocol traffic.  Be sure to specify a complete range of port numbers in these rules.

###Generate Key Pair<a id="topic_cfgkeypair"></a>
AWS uses public-key cryptography to secure the login information for your instance. You use the EC2 console to generate and name a key pair when you launch your instance.  

A key pair for an EC2 instance consists of a *public key* that AWS stores, and a *private key file* that you maintain. Together, they allow you to connect to your instance securely. The private key file name typically has a `.pem` suffix

This example logs into an into EC2 instance from an external location with the private key file `my-test.pem` as user `ec2-user`. (`ec2-user` is the default user for some Linux AMI templates.) In this example, the instance is configured with the public IP address `52.36.113.82` and the private key file resides in the current directory.

```shell
$ ssh -i my-test.pem ec2-user@52.36.113.82
```

##Additional HAWQ Considerations <a id="topic_mj4_524_2v"></a>

After launching your HAWQ instance, you will connect to and configure the instance. The  *Instances* page of the EC2 Console lists the running instances and their associated network access information. If the instance does not have a public IP address, you can allocate an Elastic IP address and associate it with the instance.

Before installing HAWQ, set up the EC2 instances as you would local host server machines. Configure the host operating system, configure host network information (for example, update the `/etc/hosts` file), set operating system parameters, and install operating system packages. For information about how to prepare your operating system environment for HAWQ, see [Select HAWQ Host Machines](../install/select-hosts.html).

  
##References<a id="topic_hgz_zwy_bv"></a>

Links to related Amazon Web Services and EC2 features and information.

- [Amazon Web Services](https://aws.amazon.com)
- [Amazon Machine Image \(AMI\)](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [EC2 Instance Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Elastic Block Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)
- [Enhanced Networking on Linux Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [Subnet Public IP Addressing](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html#subnet-public-ip)
- [Elastic IP Address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [Virtual Private Cloud](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
- [Internet Gateways] (http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html)
