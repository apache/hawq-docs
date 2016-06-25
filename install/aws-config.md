---
title: Amazon EC2 Configuration
---

Amazon Elastic Compute Cloud (EC2) is a service provided by Amazon Web Services (AWS).  You can install and configure HAWQ on virtual servers provided by Amazon EC2. The following overview information describes some considerations when installing HAWQ in an Amazon EC2 environment.

## About Amazon EC2 <a id="topic_wqv_yfx_y5"></a>

Amazon EC2 can be used to launch as many virtual servers as you need, configure security and networking, and manage storage. An EC2 *instance* is a virtual server in the AWS cloud virtual computing environment.

EC2 instances are managed by AWS. AWS isolates your EC2 instances from other users in a virtual private cloud (VPC) and lets you control access to the instances. You can configure instance features such as operating system, network connectivity (network ports and protocols, IP addresses), access to the Internet, and size and type of disk storage.

When you launch an instance, you use a preconfigured template known as an Amazon Machine Image (AMI). The AMI packages the bits you need for your server, including the operating system and additional software components. Amazon provides several AMIs from which to choose, or you can create and customize your own. 

You launch instances in an Availability Zone of an AWS region. An *Availability Zone* is a distinct location within a region that is engineered to be insulated from failures in other Availability Zones.

For information about Amazon EC2, see the [EC2 User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

## Launching Instances<a id="topic_nhk_df4_2v"></a>

Use the *Amazon EC2 Console* to launch instances and configure, start, stop, and terminate (delete) virtual servers. When you launch an instance, you select, configure, and view the following features in the EC2 Console.

| Feature                      | Description                                                                                                                                                                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Amazon Machine Image (AMI) | A template that contains a software configuration including the operating system, application server, and applications that best suit your purpose.  |
| Instance Type | Varying combinations of CPU, memory, default storage, and networking capacity. |
| Instance Details | Information about starting, running, and stopping EC2 instances, including number of instances of the same AMI, network information, and EC2 VPC and subnet membership.|
| Storage Configuration | Tools to adjust and add storage. For example, you can change the size of the root volume or add volumes.|
| Tagging | An optional (set of) case-sensitive key-value pairs  used for managing or organizing a large number of EC2 resources.|
| Security Groups | A set of firewall rules that control the network traffic for instances. For external access to an instance with `ssh`, you will create a rule that enables `ssh` for inbound network traffic. |


### Select AMI Type
When Configuring a HAWQ virtual instance, select an AMI that runs an operating system supported by HAWQ. Refer to the Release Notes for the HAWQ version that you are installing for a list of supported OS platforms. 

**Note**: To create and launch a customized AMI, see [About Amazon Machine Images](#topic_n3y_4gx_y5)


### Select and Configure EC2 Instance Type
When using Amazon Elastic Block Store (EBS), HAWQ supports only EBS-Optimized instance types. See [Configure Storage](#hawq_storage) for information about HAWQ storage requirements. For information about EBS-Optimized instances, see the Amazon [EBS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) documentation.

For sufficient network performance, the instance type must also support EC2 enhanced networking. For information about this feature, see [Amazon Enhanced Networking on Linux Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html).

The HAWQ cluster instances should be in a single VPC and subnet. Instances are always assigned a VPC internal IP address and can be assigned a public IP address for external and Internet access.

The internal IP address is used for HAWQ communication between hosts. You can also use the internal IP address to access an instance from another instance within the EC2 VPC. For information about configuring launched instances to communicate with each other, see [Working with EC2 Instances](#topic_mj4_524_2v).

Both a public IP address for the instance and an Internet gateway configured for the EC2 VPC are required to access the instance from an external source and for the instance to access the Internet. (Internet access is required when installing Linux packages.) 

When you launch a set of instances, you can enable or disable the automatic assignment of public IP addresses when the instances are started.  If automatic assignment of public IP addresses is enabled, instances are always assigned a public IP address when started. If automatic assignment of public IP addresses is disabled, you can temporarily associate an [EC2 Elastic IP Address](#task_yd3_sd4_2v) with the instance.

To control whether a public IP address is assigned when launching an instance, see the Amazon documentation on [Subnet Public IP Addressing](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html#subnet-public-ip).


###Configure Storage<a id="hawq_storage"></a>
**HAWQ** supports either EC2 instance store or Amazon EBS in production environments.

 - EC2 *instance store* provides temporary block-level storage. This storage is located on disks that are physically attached to the host computer. Powering off the instance causes data loss when using instance store storage. Soft reboots preserve instance store data. EC2 instance store can provide higher and more consistent I/O performance.
 
    For additional information about EC2 instance store, see [Amazon EC2 Instance Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html).
 - *EBS* provides block level storage volumes with long-term persistence. HAWQ supported configurations using EBS must be a RAID of Amazon EBS volumes mounted with the XFS file system. All other file systems are explicitly not supported.  
There are several classes of EBS. For HAWQ, select an EBS volume type of `gp2` or `io1`. See the Amazon [Block Device Mapping](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) documentation for more information.

For additional information about HAWQ requirements on the Amazon storage types, see the [Notes](#topic_kwk_ygx_y5).



##Working with EC2 Instances <a id="topic_mj4_524_2v"></a>

After launching an EC2 instance, connect to and configure the instance. The  *Instances* page of the EC2 Console lists the running instances and their associated network access information. If the instance does not have a public IP address, you can create an Elastic IP address and associate it with the instance. See [About Elastic IP Addresses](#task_yd3_sd4_2v) below.

To access EC2 instances, AWS uses public-key cryptography to secure the login information for your instance. A Linux instance has no password; you use a key pair to log in to your instance securely. You identify the name of the key pair when you launch your instance, and then provide the private key when you log in using SSH. See the Amazon [EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) documentation for more detailed information.

A key pair for an EC2 instance consists of a *public key* that AWS stores, and a *private key file* that you maintain. Together, they allow you to connect to your instance securely.  The private key file name typically has a `.pem` suffix.

This example logs into an into EC2 instance from an external location with the private key file `my-test.pem` as user `ec2-user`. (`ec2-user` is the default user for some Linux AMI templates.) In this example, the instance is configured with the public IP address `52.36.113.82` and the private key file resides in the current directory.

```shell
$ ssh -i my-test.pem ec2-user@52.36.113.82
```

Before installing HAWQ, set up the EC2 instances as you would local host server machines. Configure the host operating system, configure host network information (for example, update the `/etc/hosts` file), set operating system parameters, and install operating system packages. For information about how to prepare your operating system environment for HAWQ, see [Select HAWQ Host Machines](../install/select-hosts.html).

These example commands log in to an EC2 instance and use `yum` to install the `ed`, `unzip`, and `vim` Linux packages on the instance.

```shell
$ ssh -i my-test.pem ec2-user@52.36.113.82
ec2inst$ sudo yum install -y ed unzip vim
```

##About Amazon Machine Images (AMIs)   <a id="topic_n3y_4gx_y5"></a>

An Amazon Machine Image (AMI) is a template for a specific software configuration (for example, the collection of an operating system, application servers, and applications). From an AMI, you launch an *instance*, which is a copy of the AMI running as a virtual server in the cloud. You can launch multiple instances of an AMI.

After you launch an instance, it acts like a traditional host; you can interact with it as you would any computer. You have complete control of your instances.  For example, you can use `sudo` to run commands that require root privileges.

You can create a new Amazon EBS-backed Linux AMI from an instance that you've already launched and customized to your needs. First, create and register a new AMI based on the customized AMI.  You can then use the new AMI to launch instances with these customizations.

For information about AMIs, see the Amazon [AMI User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) documentation.


## About Amazon Elastic IP Addresses<a id="task_yd3_sd4_2v"></a>

An EC2 Elastic IP address is a public IP address that you can create for your account. You can associate it to and disassociate it from instances as you require; it's allocated to your account until you choose to release it.

Your default VPC is configured with an Internet gateway. When you allocate an EC2 Elastic IP address, AWS configures the VPC to allow internet access to the IP address using the gateway.

To enable an instance in your VPC to communicate with the Internet, it must have a public IP address or an EC2 Elastic IP address that's associated with a private IP address on your instance.

To ensure that your instances can communicate with the Internet, you must also attach an Internet gateway to your EC2 VPC. For information about VPC Internet Gateways, see the Amazon [Internet Gateways] (http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) documentation.

For more detailed information about EC2 Elastic IP addresses and how to use them, see the [Amazon Elastic IP Address](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html).


##Notes<a id="topic_kwk_ygx_y5"></a>

- Supported HAWQ storage configurations with Amazon EBS include a RAID of Amazon EBS volumes mounted with the XFS file system.  
  
- Virtual devices for instance store volumes for HAWQ EC2 instance store instances are named `ephemeralN` (where *N* is between 0 and 23). CentOS instance store block device names appear as `/dev/xvdletter` (where *letter* is a lower case letter of the alphabet).
  
    Two EC2 instance types configured with instance store showed acceptable performance.  These include the `d2.8xlarge` instance type configured with four `raid0` volumes of 6 disks each, and the `i2.8xlarge`  instance type configured with two `raid0` volumes of 4 disks.  
  
- To allow access to/from a source external to a VPC, include and open the following ports in the appropriate security group.

    | Port  | Application |
    |-------|-------------------------------------|
    | 22    | ssh - secure connect to other hosts |
    | 8080  | Ambari - HAWQ admin/config web console |  

- You can configure a non-default VPC with an internet gateway and allocate an Elastic IP address for the VPC. AWS will automatically configure the Elastic IP for internet access.
 
- A *placement group* is a logical grouping of instances within a single Availability Zone. Using placement groups enables applications to participate in a low-latency, 10 Gbps network. Placement groups are recommended for applications that benefit from low network latency, high network throughput, or both. 
 
    Placement Groups could be used to separate EC2 instances from other instances. While configuring instances in different placement groups can improve performance, it may create a configuration where an instance in a placement group cannot be replaced.  
   
    See [Amazon Placement Group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) for additional information.

- Amazon EC2 provides enhanced networking capabilities on some instance types by using single root I/O virtualization (SR-IOV). Enabling enhanced networking on your instance results in higher performance (packets per second), lower latency, and lower jitter.

    To enable enhanced networking on your Red Hat and CentOS RHEL/CentOS instance, you must ensure that the kernel has the `ixgbevf` module version 2.14.2 or higher installed and that the `sriovNetSupport` attribute is set.  
  
##Additional References<a id="topic_hgz_zwy_bv"></a>

Links to related AWS and EC2 features and information.

- [Amazon Web Services](https://aws.amazon.com)
- [Connecting to an EC2 instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- [Amazon VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
- [Amazon EC2 best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html)
- [Amazon EC2 and VPC command line interface](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/Welcome.html)
- [Amazon S3 \(secure, durable, scalable object storage\)](https://aws.amazon.com/s3)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation) - With AWS CloudFormation, you can create templates to simplify provisioning and management of related AWS resources.