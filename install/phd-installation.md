---
title: Installing Pivotal HD 3.3.2 and Pivotal HDB 2.0 Beta Using Ambari
---

This document contains the information and procedures required for installing Ambari 2.1.2.2, Pivotal HD 3.3.2, and Pivotal HDB 2.0 Beta using the Ambari user interface.

**Note:** For manual installation instructions \(not using Ambari\), see [\(Optional\) Install Pivotal HDB 2.0 Beta from the Command Line](HAWQBetaInstallation.html).

## Prerequisites <a name="topic_b5r_gmc_b5"></a>

### System Requirements

|Operating System Requirements|Red Hat Enterprise Linux \(RHEL\) 6.4+ \(64-bit\)**Note:** The installer uses many packages from the base OS repositories. All machines in the cluster should have access to a complete set of base OS repositories. The repositories can be either installed locally or be proxied / mirrored from another location.

|
|Browser Requirements|The Ambari Cluster Creation Wizard is a web-based tool running in a browser. You must have a machine that can run a graphical web browser to use the Ambari Cluster Creation Wizard. The machine can either be the same or have a network connectivity to the machine where the Ambari server is installed.-   Windows \(Vista, 7\)
    -   Internet Explorer 9.0 and higher \(for Vista + Windows 7\)
    -   Firefox latest stable release
    -   Safari latest stable release
    -   Google Chrome latest stable release
-   Mac OS X \(10.6 or later\)
    -   Firefox latest stable release
    -   Safari latest stable release
    -   Google Chrome latest stable release
-   Linux \(RHEL, CentOS, SLES\)
    -   Firefox latest stable release
    -   Google Chrome latest stable release

|
|Software Requirements|The following packages must be installed on all your hosts:-   yum and rpm \(RHEL/CentOS\)
-   scp, curl, and wget
-   python \(2.6 or later\)

|
|JDK Requirement|Oracle jdk-8u40-linux-x64.tar.gz|
|Database Requirements|Ambari, Hive/HCatalog and Oozie require their own databases.-   Ambari: by default uses PostgreSQL 8.x server instance installed by Ambari. It is also possible to use an existing instance ofPostgreSQL 9.x, MySQL 5.x, or Oracle 11g.
-   Hive/HCatalog: Ambari will install an instance of MySQL on the Hive Metastore host. It is also possible to use an existing instance of PostgreSQL 9.x, MySQL 5.x, or Oracle 11g.
-   Oozie: by default uses Derby instance installed by Ambari. It is also possible to use an existing instance of PostgreSQL 9.x, MySQL 5.x, or Oracle 11g.

|
|OpenSSL Requirement|openssl-1.0.1e-16.el6.x86\_64 or above is required on all nodes|

### Password-less SSH \(Ambari Server to Cluster Hosts\)

Ambari requires ambari-agents be installed on all the cluster hosts. Ambari server communicates with agents to perform the PHD cluster installation and management tasks. The agents can either be installed automatically by the Ambari Server or manually by the system administrator.

To have the Ambari Server install the Ambari Agents automatically on each cluster host, a password-less ssh connection must be established between the Ambari Server host and all other hosts. For manual install, refer to the “Ambari Agents Manual Install” section.

### Synchronize clocks across all cluster hosts

The clocks on all cluster hosts and the machine that runs the browser must be synchronized. Enable NTP service to make sure synchronization happens automatically.

### Check DNS settings

All hosts in the cluster must be configured for DNS and Reverse DNS. Alternatively, you can manage host resolution in /etc/hosts file. The hostname command should return Fully Qualified Domain name \(FQDN\) of your host.

### Disable or Configure iptables

A number of network ports need to be open on the cluster hosts for Ambari to be able to provision and manage them during setup. The easiest way to open the ports is to temporarily disable the iptables process:

```
$ service iptables stop
```

The service can be restarted after the setup is complete.

### Disable SELinux and PackageKit and Check umask Value

Temporarily disable SELinux during the Ambari setup:

```
$ setenforce 0
```

-   If PackageKit is installed, open /etc/yum/pluginconf.d/refresh-packagekit.conf in a test editor and make this change: enabled=0
-   Make sure umask is set to 022

### Disable IPv6

Enter the following commands to disable IPv6:

```
$ mkdir -p /etc/sysctl.d
$ ( cat > /etc/sysctl.d/99-hadoop-ipv6.conf <<-'EOF'
## Disabled ipv6
## Provided by Ambari Bootstrap
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
EOF
    )
$ sysctl -e -p /etc/sysctl.d/99-hadoop-ipv6.conf

```

### Disable Transparent Huge Pages \(THP\)

When installing Ambari, one or more host checks may fail if you have not disabled Transparent Huge Pages on all hosts. To disable THP:

1.  Add the following commands to your /etc/rc.local file:

    ```
    if test -f /sys/kernel/mm/redhat_transparent_hugepage/enabled; then
       echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled; fi
    if test -f /sys/kernel/mm/redhat_transparent_hugepage/defrag; then
       echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag; fi

    ```

2.  To confirm, reboot the host and then run the command:

    ```
    $ cat /sys/kernel/mm/redhat_transparent_hugepage/enabled
        always madvise [never]
    $ cat /sys/kernel/mm/redhat_transparent_hugepage/defrag
        always madvise [never]

    ```


## Installing Ambari Server <a name="topic_lpx_2nc_b5"></a>

You must configure a YUM repository server in order to install Ambari. The repository must reside on a host that is accessible from all the cluster hosts. You can use a dedicated host for that purpose or set up the YUM repository server on the admin host where the Ambari Server will be installed.

Follow this procedure to set up the YUM repository and install the Ambari server:

1.  Make sure that the httpd server is running on the host that will serve as a YUM repo:

    ```
    $ service httpd status
    ```

    If the service is not running, install and start it:

    ```
    $ yum install httpd
    $ service httpd start
    ```

2.  Create a staging directory where you will extract the tarballs for the Ambari, PHD, HDB, and other stacks. The staging directory and all the directories above it must be readable and executable by the system user that runs the httpd process \(typically `apache`\). Pivotal recommends that you make the directory readable and executable by all users. For example:

    ```
    $ mkdir /staging
    $ chmod a+rx /staging
    ```

    **Note:** Do not use the /tmp directory as a staging directory because files under /tmp can be removed at any time.

3.  On the host that you will use as the YUM repo, download the Pivotal Ambari tarball from [https://network.pivotal.io/products/pivotal-hd](https://network.pivotal.io/products/pivotal-hd) into the staging directory that you set up in the previous step \(for example, /staging\).
4.  Extract the tarball into the staging directory:

    ```
    $ tar -xvzf /staging/AMBARI-2.1.2.2-163-centos6.tar.gz -C /staging/
    ```

5.  Each tarball is an archived yum repository and has a setup\_repo.sh script. The script creates a symlink from the document root of the httpd server \(/var/www/html\) to the directory where the tarball was extracted. On the host that will be used as a YUM repo, execute the setup\_repo.sh script that is shipped as a part of the ambari tarball:

    ```
    $ /staging/AMBARI-2.1.2.2/setup_repo.sh
    ```

    The script also creates an Ambari repo definition and places it in the /etc/yum.repos.d/ambari.repo file. This file must be available on the admin host where the Ambari Server will be installed.

6.  Verify that the ambari YUM repo is now available from the YUM web server:

    ```
    $ curl http://localhost/AMBARI-2.1.2.2/repodata/repomd.xml
    ```

    Also verify that you can access the following URL from the admin and cluster hosts:

    ```
    http://<yum.repo.fqdn>/AMBARI-2.1.2.2
    ```

7.  After the YUM repo is configured, execute this command to install the Ambari Server:

    ```
    $ yum install ambari-server
    ```

    This command installs the Ambari Server, which is a web application server listening on port 8080. It also installs a PostgreSQL server instance that listens on port 5432.

8.  The Ambari application server requires the Java JDK 1.8 framework to run. Execute this command to download the Oracle JDK 1.7 tarball:

    ```
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn/java/jdk/8u40-b26/jdk-8u40-linux-x64.tar.gz
    ```

    **Note:** The name of the Java JDK tarball is hardcoded in the Ambari setup script, which means you need to download the exact same version from Oracle. If you use a browser to download the file, ensure that the final downloaded filename remains jdk-7u67-linux-x64.tar.gz.

    After downloading the JDK tarball, you have 2 options:

    1.  **Rely on Ambari to install and distribute the Oracle JDK to the cluster hosts.** Copy the downloaded tarball to the /var/lib/ambari-server/resources/ directory. The setup script for the Ambari server will detect the presence of the tarball in this location and will install the JDK on the admin host. The Ambari Server will also distribute and install this JDK on all cluster hosts during cluster creation. Ensure that the file has READ permission for all.
    2.  **Manually install the Oracle JDK on all cluster hosts.** If you prefer this option, write down the value of JAVA\_HOME for your Java installation as you will need it when setting up the Ambari Server.
9.  The Ambari application server also requires Java Unlimited JCE policies when used to manage a Kerberos-enabled cluster. After you have configured the Oracle JDK, download the Java Cryptography Extension \(JCE\) Unlimited Strength Jurisdiction Policy Files for Java 7 directly from Oracle site: [http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html) . Copy the file to the /var/lib/ambari-server/resources/ directory. The setup script for Ambari server will detect the presence of the JCE archive in this location and distribute the files to the cluster hosts automatically. Ensure that the file has READ permission for all.
10. If your PostgreSQL instance is configured to listen on the default port number, simply run the following command to set up the Ambari server:

    ```
    $ ambari-server setup
    ```

    This command prompts for user input to make several decisions:

    -   **User Account** – You can choose to use another user \(other than root\) to run the daemon process ambari-server on the admin node. If you decide to use a different user and the user does not yet exist, it will be created.
    -   **Java JDK** – Choose the Oracle JDK 1.8 option to use the JDK tarball that you have downloaded and copied to the /var/lib/ambari-server/resources/ directory. If you want to install a custom JDK on all hosts manually, choose “Custom JDK” option and provide the value of the JAVA\_HOME. ***Do not choose the Oracle JDK 1.6 option as it is no longer supported.***
    -   **Database** – If you would like to use an existing database server instead of the new PostgreSQL instance provisioned by Ambari, answer “y” to “Enter advanced database configuration” question and provide connection parameters to the existing database.
    **Note:** If your PostgreSQL instance is configured to listen on a non-default port number, perform these alternate steps to configure postgres and Ambari:

    1.  Open the PostgreSQL /var/lib/pgsql/data/pg\_hba.conf configuration file in a text editor. Append the following lines to the end of the file to allow the `ambari` user to connect to the database:

        ```
        local  all  ambari md5
        host  all   ambari 0.0.0.0/0  md5
        host  all   ambari ::/0 md5
        ```

    2.  Open the /etc/sysconfig/pgsql/postgresql to enable the non-default port. For example, to use port 10432 the file would need the line:

        ```
        PGPORT=10432
        ```

    3.  Restart the PostgreSQL database:

        ```
        $ service postgresql restart
        ```

    4.  Connect to the database as `postgres` \(superuser\) and configure the database for Ambari:

        ```
        $ psql -U postgres -p 10432;
        postgres=# CREATE DATABASE ambari;
        postgres=# CREATE USER ambari WITH ENCRYPTED PASSWORD 'bigdata';
        postgres=# \c ambari
        ambari=# CREATE SCHEMA ambari AUTHORIZATION ambari;
        ambari=# ALTER SCHEMA ambari OWNER TO ambari;
        ambari=# ALTER ROLE ambari SET search_path to 'ambari','public';
        ambari=# \q
        ```

    5.  Execute this command to setup Ambari:

        ```
        $ ambari-server setup --database=postgres --databasehost=localhost --databaseport=10432 --databasename=ambari --databaseusername=ambari --databasepassword=bigdata
        ```

        **Note:** Use the following command to verify that `postgres` is listening on the hostname value assigned to `--databasehost`:

        ```
        $ netstat -anp | egrep <port>
        ```

    6.  Execute the Ambari-DDL-Postgres-CREATE.sql file in PostgreSQL to complete the configuration:

        ```
        $ psql -f /var/lib/ambari-server/resources/Ambari-DDL-Postgres-CREATE.sql -U ambari -p 10432 -d ambari

        ```

        Enter the password bigdata when prompted.

    7.  Continue with the next step to start the Ambari server.
11. After the Ambari server is set up, start it with the command:

    ```
    $ ambari-server start
    ```

    To check the status of the server, use the command:

    ```
    $ ambari-server status
    ```

    To stop the server, use the command:

    ```
    $ ambari-server stop
    ```


## Installing the Pivotal HD and Pivotal HDB with Ambari <a name="topic_mkv_lpc_b5"></a>

The Ambari server installation process creates the local YUM repository server that you can now use to install Pivotal HD 3.3.2, Pivotal HDB 2.0 Beta, and related software. Follow these steps to install the software using Ambari.

### Download and extract PHD stack tarballs

The PHD stack tarballs should be installed on the machine that hosts the YUM server. Unless you’re using a dedicated machine for the YUM repository server, this will be the same admin host you used for installing the Ambari Server.

Download the following tarballs and extract them in your staging directory \(avoid using /tmp directory\).

|Stack Name|Download URL|Description|
|PHD-3.3.2.0\(PHD-3.3.2.0-2950-centos6.tar.gz\)

|[Pivotal Network](https://network.pivotal.io/products/pivotal-hd)|Pivotal Hadoop stack contains RPMs for Hadoop Services such as HDFS, YARN, HBASE, HIVE, OOZIE, ZOOKEEPER.|
|PHD-UTILS-1.1.0.20\(PHD-UTILS-1.1.0.20-centos6.tar.gz\)

|[Pivotal Network](https://network.pivotal.io/products/pivotal-hd)|Pivotal Hadoop Utilities stack contains optional services and libraries such as Ganglia and Nagios used for monitoring and alerting of core cluster services.|
|HDB-2.0.0.0 Beta\(pivotal-hdb-2.0.0.0-18407.tar.gz\)

|[Pivotal Network](https://network.pivotal.io/products/pivotal-hawq)|Pivotal HDB is a parallel SQL query engine that includes features from Apache HAWQ \(Incubating\) such as PXF.|
|HAWQ-PLUGIN-2.0.0\(hawq-plugin-2.0.0-phd-356.tar.gz\)

|[Pivotal Network](https://network.pivotal.io/products/pivotal-hawq)|The HAWQ plug-in provides Ambari installation and monitoring functionality for Apache HAWQ \(Incubating\).|

Assuming you downloaded the tarballs to the /tmp directory and want to stage them in /staging directory:

```
$ tar -xzf /tmp/{stack"></a>.tar.gz -C /staging/
```

### Setup local YUM repositories

PHD stacks are shipped as archived YUM repositories that need to be deployed in your YUM repository server to be accessible by the Ambari Server and all cluster hosts.

Each stack repository contains the setup\_repo.sh script that assumes:

-   the YUM repository server is accessible by all hosts in the cluster
-   the document root of your YUM server is /var/www/html/

Each stack’s script creates a symbolic link in the YUM repository server document root to point to the location of the extracted stack tarball and creates a repo definition file in /etc/yum.repos.d/ directory so that your local yum command can find the repository. It is essential that the hostnames in the repo definition files use the Fully Qualified Domain Name \(FQDN\) of the YUM server host that is accessible from all cluster hosts.

For each stack, run the local repo setup script:

```
$ /staging/{stack"></a>/setup_repo.sh
```

**If the repository setup was successful, the script will print out the repository URL. Write down the URL as you will need it later when installing a PHD cluster using Ambari Sever UI.**

**Note:** If your YUM repository server runs on a different host than the admin host where the Amabri Server is installed, copy the generated repository definition files in /etc/yum.repos.d/ to /etc/yum.repos.d on the admin host where you installed the Ambari Sever.

Test that the repositories are properly configured – run the following command from the admin host:

```
$ yum repolist
```

You should see the repositories for the stacks listed.

### Login to Ambari Server

Once the Ambari Server is started:

1.  Open http://\{ambari.server.host\"></a>:8080 in the web browser
2.  Login to the server using user `admin` and the password `admin`. These credentials can be changed later.
3.  Click on “Launch Install Wizard” button to enter into cluster creation wizard. The wizard is self-explanatory and guides you through the steps necessary to provision a new PHD cluster. A few actions requiring particular attention are listed below:
    1.  In the **Select Stack** section, click **Advanced Repository Options** to reveal a list of YUM repositories Ambari will search to get PHD stacks RPMs from. The values provided here out-of-the box need to be replaced with the URLs of the stack repositories you have installed previously. Replace[http://SET\_REPO\_URL](http://set_repo_url/) with the appropriate repository URL you have noted down earlier when you ran setup\_repo.sh script for the stack. If you don’t have the links handy, you can always get them from the /etc/yum.repos.d/-.repo file.

        **Note:** After you deploy the cluster, you can update repositories via the Ambari UI \(**Admin \> Repositories**\).

    2.  In the **Install Options** section, you need to provide FQDN names for the hosts that will comprise your cluster. You can use the range expression using square brackets – for example, host\[01-10\].domain will describe 10 hosts.

        If you want Ambari to automatically provision and register Ambari Agents on the cluster hosts, you will need to provide a private key that you used to setup password-less SSH on your cluster. You can either pick and choose a file or copy&paste the file content into the screen form.

        **Note:** If you do not want to provide the private key or setup password-less SSH you will have to provision and configure the Ambari Agents manually. In this you have to:

        1.  Setup Ambari Repository by copying /etc/yum.repos.d/ambari.repo file from the YUM repository server
        2.  Install the Ambari Agent:

            ```
            ~> yum install ambari-agent
            ```

        3.  Edit the Ambari Agent configuration \(/etc/ambari-agent/conf/ambari-agent.ini\) to point it to the Ambari Server:

            ```
            [server]
            hostname={ambari.server.hostname"></a>
            url_port=8440
            secured_url_port=8441

            ```

        4.  Start the agent:

            ```
            ~> ambari-agent start
            ```

        The agent will register itself with the server when it starts.
