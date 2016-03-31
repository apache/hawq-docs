---
title: Installing Additional HAWQ Components
---

This chapter describes how to install additional HAWQ components.

-   [Installing Cryptographic Functions for PostgreSQL](#)
    -   [Install pgcrypto](#)
    -   [Uninstalling pgcrypto](#)
-   [Installing PL/R](#)
    -   [Install PL/R](#)
    -   [Enable PL/R Language Support](#)
    -   [Uninstalling PL/R](#)
-   [Installing PL/Java](#)
    -   [Install the HAWQ PL/Java Extension](#)
    -   [Enable PL/Java and Install JAR Files](#)
    -   [Uninstalling PL/Java](#)
-   [Installing MADlib on HAWQ](#)
    -   [Pre-requisites for Installing MADlib on HAWQ](#)
    -   [Install MADlib on HAWQ](#)

## Installing Cryptographic Functions for PostgreSQL <a id="installingcryptographicfunctionsforpostgresql"></a>

pgcrypto is available as a package that you can download from the Pivotal Download Center and install using the Package Manager utility \(`gppkg`\). `gppkg` installs pgcrypto and other HAWQ extensions, along with any dependencies, on all hosts across a cluster. It will also automatically install extensions on new hosts in the case of system expansion and segment recovery.

**Note:** Before you install the pgcrypto software package, make sure that your HAWQ database is running, you have sourced greenplum\_path.sh, and that the `$MASTER_DATA_DIRECTORY` and `$GPHOME` variables are set.

### Install pgcrypto <a id="installpgcrypto"></a>

Download the pgcrypto package from the Pivotal Download Center, then copy it to the master host. Install the software package by running the following command:

```
gppkg -i pgcrypto-1.0-rhel5-x86_64.gppkg
```

You will see output similar to the following.

```
[gpadmin@gp-single-host ~]$ gppkg -i pgcrypto-1.0-rhel5-x86_64.gppkg
20120418:23:54:20:gppkg:gp-single-host:gpadmin-[INFO]:-Starting gppkg with args: -i pgcrypto-1.0-rhel5-x86_64.gppkg
20120418:23:54:20:gppkg:gp-single-host:gpadmin-[INFO]:-Installing package pgcrypto-1.0-rhel5-x86_64.gppkg
20120418:23:54:21:gppkg:gp-single-host:gpadmin-[INFO]:-Validating rpm installation cmdStr='rpm --test -i /usr/local/greenplum-db/./.tmp/pgcrypto-1.0-1.x86_64.rpm --dbpath /usr/local/greenplum-db/./share/packages/database --prefix /usr/local/greenplum-db/.'
20120418:23:54:22:gppkg:gp-single-host:gpadmin-[INFO]:-Please run psql -d mydatabase -f $GPHOME/share/postgresql/contrib/pgcrypto.sql to enable the package.
20120418:23:54:22:gppkg:gp-single-host:gpadmin-[INFO]:-pgcrypto-1.0-rhel5-x86_64.gppkg successfully installed.
```

### Uninstalling pgcrypto <a id="uninstallingpgcrypto"></a>

#### Uninstall pgcrypto support

To uninstall the pgcrypto objects, use uninstall\_pgcrypto.sql to remove pgcrypto support.

For each database on which you enabled pgcrypto support, execute the following:

```
psql -d dbname -f $GPHOME/share/postgresql/contrib/uninstall_pgcrypto.sql
```

**Note:** This script does not remove dependent user-created objects.

#### Uninstall the software package

You can uninstall the pgcrypto software using the Greenplum Package Manager \(gppkg\), as follows:

```
gppkg -r pgcrypto-1.0
```

## Installing PL/R <a id="installingplr"></a>

PL/R is available as a package that you can download from the Pivotal Download Center and install using the Package Manager utility \(`gppkg`\). `gppkg` installs PL/R and other Greenplum Database extensions, along with any dependencies, on all hosts across a cluster. It will also automatically install extensions on new hosts in the case of system expansion and segment recovery.

**Note:** Before you install the PL/R software package, make sure that your HAWQ database is running, you have sourced greenplum\_path.sh, and that the `$MASTER_DATA_DIRECTORY` and `$GPHOME` variables are set.

### Install PL/R <a id="installplr"></a>

1.  Download the PL/R package from the Pivotal Download Center, then copy it to the master host. Install the software package by running the following command:

    ```
    $ gppkg -i plr-1.0-rhel5-x86_64.gppkg
    ```

2.  Source the $GPHOME/greenplum\_path.sh file. The extension and the R environment are installed in the $GPHOME/ext/R-2.13.0/ directory.
3.  Restart the database:

    ```
    $ gpstop -r
    ```


### Enable PL/R Language Support <a id="enablingplrlanguagesupport"></a>

For each database that requires its use, register the PL/R language with the `CREATE LANGUAGE` SQL command or the `createlang` utility. For example, running the following command as the `gpadmin` user registers the language for a database named `testdb`:

```
$ createlang plr -d testdb
```

PL/R is registered as an untrusted language.

You are now ready to create new PLR functions. A library of convenient PLR functions may be found in $GPHOME/share/postgresql/contrib/plr.sql. These functions may be installed by using the `psql` utility to execute plr.sql, as follows:

```
psql -d <dbname> -f $GPHOME/share/postgresql/contrib/plr.sql
```

### Uninstalling PL/R <a id="uninstallingplr"></a>

When you remove PL/R language support from a database, the PL/R routines that you created in the database will no longer work.

#### Remove PL/R Support for a Database <a id="removeplrsupportforadatabase"></a>

For a database that no long requires the PL/R language, remove support for PL/R with the SQL command `DROP LANGUAGE`or the `droplang` utility. For example, running the following command as the `gpadmin` user removes support for PL/R from the database `testdb`:

```
$ droplang plr -d testdb
```

#### Uninstall the Software Package <a id="uninstallthesoftwarepackage"></a>

If no databases have PL/R as a registered language, uninstall the Greenplum PL/R extension with the `gppkg` utility. This example uninstalls PL/R package version 1.0:

```
$ gppkg -r plr-1.0
```

You can run the `gppkg` utility with the options `-q --all` to list the installed extensions and their versions.

Then, restart the database.

```
$ gpstop -r
```

##### Downloading and Installing R libraries

For a given R library, identify all dependent R libraries and each library's web URL.This can be found by selecting the specific package from the following page: [http://cran.r-project.org/web/packages/available\_packages\_by\_name.html](http://cran.r-project.org/web/packages/available_packages_by_name.html)

From the page for the arm library, you can see that this library requires the following R libraries:

-   Matrix
-   lattice
-   lme4
-   R2WinBUGS
-   coda
-   abind
-   foreign
-   MASS

From the command line, use `wget` to download the tar.gz files for the required libraries to the master node:

```
$ wget http://cran.r-project.org/src/contrib/arm_1.5-03.tar.gz
$ wget http://cran.r-project.org/src/contrib/Archive/Matrix/Matrix_1.0-1.tar.gz
$ wget http://cran.r-project.org/src/contrib/Archive/lattice/lattice_0.19-33.tar.gz
$ wget http://cran.r-project.org/src/contrib/lme4_0.999375-42.tar.gz
$ wget http://cran.r-project.org/src/contrib/R2WinBUGS_2.1-18.tar.gz
$ wget http://cran.r-project.org/src/contrib/coda_0.14-7.tar.gz
$ wget http://cran.r-project.org/src/contrib/abind_1.4-0.tar.gz
$ wget http://cran.r-project.org/src/contrib/foreign_0.8-49.tar.gz
$ wget http://cran.r-project.org/src/contrib/MASS_7.3-17.tar.gz
```

Using `gpscp` and the hostname file, copy the tar.gz files to the same directory on all nodes of the HAWQ cluster. You may require `root` access to do this.

```
$ gpscp -f /home/gpadmin/hosts_all lattice_0.19-33.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all Matrix_1.0-1.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all abind_1.4-0.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all coda_0.14-7.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all R2WinBUGS_2.1-18.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all lme4_0.999375-42.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all MASS_7.3-17.tar.gz =:/home/gpadmin
$ gpscp -f /home/gpadmin/hosts_all arm_1.5-03.tar.gz =:/home/gpadmin
```

Use `R CMD INSTALL` to install the packages from the command line. You may require `root` access to do this.

```
$ R CMD INSTALL lattice_0.19-33.tar.gz Matrix_1.0-1.tar.gz abind_1.4-0.tar.gz coda_0.14-7.tar.gz R2WinBUGS_2.1-18.tar.gz lme4_0.999375-42.tar.gz MASS_7.3-17.tar.gz arm_1.5-03.tar.gz
```

## Installing PL/Java <a id="installingpljava"></a>

The PL/Java extension is available as a package that you can download from the Pivotal Download Center and then install with the Package Manager utility \(`gppkg`\).

**Note:** Before you install PL/Java:

-   Ensure that the `$JAVA_HOME` variable is set to the same path on the master and all the segments.
-   Perform the following step on all machines to set up `ldconfig` for JDK:

    ```
    $ echo "$JAVA_HOME/jre/lib/amd64/server" > /etc/ld.so.conf.d/libjdk.conf
    $ ldconfig
    ```

-   If you are upgrading to the latest version of Java or installing it as part of the expansion process, follow the instructions in the chapter, *Expanding the HAWQ System* in the *HAWQ Administrator Guide*.
-   PL/Java is compatible with JDK 1.6 and 1.7.

The `gppkg` utility installs HAWQ extensions, along with any dependencies, on all hosts across a cluster. It also automatically installs extensions on new hosts in the case of system expansion and segment recovery.

To install and use PL/Java:

1.  Install the PL/Java extension.
2.  Enable the language for each database.
3.  Install user-created JAR files containing Java methods on all HAWQ hosts.
4.  Add the name of the JAR file to the HAWQ `pljava_classpath` environment variable. The variable lists the installed JAR files.

**Note:** Before you install the PL/Java extension, make sure that your Greenplum database is running, you have sourced greenplum\_path.sh, and that the `$MASTER_DATA_DIRECTORY` and `$GPHOME` variables are set.

### Install the HAWQ PL/Java Extension <a id="installingthehawqpljavaextension"></a>

1.  Download the PL/Java extension package from the Pivotal Download Center and copy it to the master host.
2.  Install the software extension package by running the `gppkg` command. This example installs the PL/Java extension package on a Linux system:

    ```
    $ gppkg -i pljava-1.1-rhel5-x86_64.gppkg
    ```

3.  Restart the database:

    ```
    $ gpstop -r
    ```

4.  Source the $GPHOME/greenplum\_path.sh file.

### Enable PL/Java and Install JAR Files <a id="enablingpljavaandinstallingjarfiles"></a>

Perform the following steps as the HAWQ administrator `gpadmin`:

1.  Enable PL/Java by running the $GPHOME/share/postgresql/pljava/install.sql SQL script in the databases that use PL/Java. For example, this example enables PL/Java on a database named `mytestdb`:

    ```
    $ psql -d mytestdb -f $GPHOME/share/postgresql/pljava/install.sql
    ```

    The install.sql script registers both the trusted and untrusted PL/Java.

2.  Copy your Java archives \(JAR files\) to $GPHOME/lib/postgresql/java/ on all the HAWQ hosts. This example uses the gpscp utility to copy the myclasses.jar file:

    ```
    $ gpscp -f gphosts_file myclasses.jar =:/usr/local/greenplum-db/lib/postgresql/java/
    ```

    The gphosts\_file file contains a list of the Greenplum Database hosts.

3.  Set the `pljava_classpath` server configuration parameter in the master postgresql.conf file. The parameter value is a colon \(`:`\) separated list of the JAR files containing the Java classes used in any PL/Java functions. For example:

    ```
    $ gpconfig -c pljava_classpath -v \'examples.jar:myclasses.jar\' --masteronly
    ```

4.  Restart the database:

    ```
    $ gpstop -r
    ```

5.  **\(Optional\)** Pivotal provides an examples.sql file containing sample PL/Java functions that you can use for testing. Run the commands in this file to create the test functions \(which use the Java classes in examples.jar\):

    ```
    $ psql -f $GPHOME/share/postgresql/pljava/examples.sql
    ```

    Enabling the PL/Java extension in the `template1` database enables PL/Java in any new Greenplum databases:

    ```
    $ psql template1 -f $GPHOME/share/postgresql/pljava/install.sql
    ```


#### Configuring PL/Java vmoptions <a id="configuringpljavavmoptions"></a>

PL/Java JVM options can be configured via the `pljava_vmoptions` parameter in the postgresql.conf file. For example, `pljava_vmoptions=-Xmx512M` sets the maximum heap size of the JVM. The default `Xmx` value is set to `-Xmx64M`.

### Uninstalling PL/Java <a id="uninstallingpljava"></a>

To uninstall PL/Java, you should:

1.  Remove PL/Java Support for a Database
2.  Uninstall the Java JAR files and Software Package

#### Remove PL/Java Support for a Database <a id="removepljavasupportforadatabase"></a>

For a database that no long requires the PL/Java language, remove support for PL/Java by running the uninstall.sql file as the `gpadmin` user. For example, the following command disables the PL/Java language in the specified database:

```
$ psql -d mydatabase -f $GPHOME/share/postgresql/pljava/uninstall.sql
```

#### Uninstall the Java JAR files and Software Package <a id="uninstallthejavajarfilesandsoftwarepackage"></a>

If no databases have PL/Java as a registered language, remove the Java JAR files and uninstall the Greenplum PL/Java extension with the `gppkg` utility:

1.  Remove the `pljava_classpath` server configuration parameter in the master postgresql.conf file.
2.  Remove the JAR files from the $GPHOME/lib/postgresql/java/ directory of the HAWQ hosts.
3.  Use the `gppkg` utility with the `-r` option to uninstall the PL/Java extension. The following example uninstalls the PL/Java extension on a Linux system:

    ```
    $ gppkg -r pljava-1.1
    ```

    You can run the `gppkg` utility with the options `-q --all` to list the installed extensions and their versions.

4.  After you uninstall the extension, restart the database:

    ```
    $ gpstop -r
    ```


#### Installing Custom JARS <a id="installingcustomjars"></a>

1.  Copy the jar file on the master host in $GPHOME/lib/postgresql/java.
2.  Copy the jar file on all segments in the same location using `gpscp` from master:

    ```
    $ cd $GPHOME/lib/postgresql/java
    $ gpscp -f ~/hosts.txt myfunc.jar =:$GPHOME/lib/postgresql/java/
    ```

3.  Set `pljava_classpath` to include the newly-copied jar file:  
    -   From the `psql` session, execute set to affect the current session:

        ```
        set pljava_classpath='myfunc.jar';
        ```

    -   To affect all sessions, use `gpconfig`: 

        ```
        gpconfig -c pljava_classpath -v \'myfunc.jar\'
        ```


## Installing MADlib on HAWQ <a id="installingmadlibonhawq1"></a>

The MADlib library adds statistical and machine learning functionality to HAWQ. MADlib is provided as a package that you can download from the Pivotal Download Center and install using the Package Manager utility \(`gppkg`\). `gppkg` installs MADlib and other Greenplum Database extensions, along with any dependencies, on all hosts across a cluster. It also automatically installs extensions on new hosts in the case of system expansion and segment recovery.

### Pre-requisites for Installing MADlib on HAWQ <a id="pre-requisitesforinstallingmadlibonhawq"></a>

**Note:** Before you install the MADlib software package, make sure that your HAWQ database is running, that you have sourced greenplum\_path.sh, and that the `$MASTER_DATA_DIRECTORY` and `$GPHOME` variables are set.

### Install MADlib on HAWQ <a id="installingmadlibonhawq2"></a>

1.  Download the MADlib package from the Pivotal Download Center, then copy it to the master host. Install the software package by running the command:

    ```
    $ gppkg -i madlib-ossv1.7.1_pv1.9.3_hawq1.3-rhel5-x86_64.gppkg
    ```

    The installation process begins and shows output similar to:

    ```
    20150330:21:28:33:021734 gppkg:gpdb11:gpdbchina-[INFO]:-Starting
    gppkg with args: -i /data/home/gpdbchina/pulse2-data/agents/agent1/work/
    MADlib%20TINC%20Feature%20Test%20on%20HAWQ%201.3/rhel5_x86_64/madlib/
    madlib-ossv1.7.1_pv1.9.3_hawq1.3-rhel5-x86_64.gppkg
    20150330:21:28:33:021734 gppkg:gpdb11:gpdbchina-[INFO]:-Installing package
    madlib-ossv1.7.1_pv1.9.3_hawq1.3-rhel5-x86_64.gppkgInstalled GPDB Version:
    pg_ctl (HAWQ) 1.3.0.0 build 12954
    [...]
    ```

2.  Restart the database:

    ```
    $ gpstop -r
    ```

3.  Source the $GPHOME/greenplum\_path.sh file.
4.  Deploy the MADlib objects to a database using the `GPHOME/madlib/bin/madpack` utility. The syntax for installing objects is:

    ```
    madpack install [-s schema\_name] -p hawq -c user@host:port/database
    ```

    The default schema name is `madlib`.

    For example, the following command install the objects to a database named "testdb" on server mdw:5432 using the gpadmin user:

    ```
    $ $GPHOME/madlib/bin/madpack install -s madlib -p hawq -c gpadmin@mdw:5432/testdb
    ```

    Enter the password for the specified user when prompted.

5.  To learn more about additional options for the `madpack` utility, enter:

    ```
    $GPHOME/madlib/bin/madpack --help
    ```

    See also the documentation available at [madlib.net](http://madlib.net/documentation/).
