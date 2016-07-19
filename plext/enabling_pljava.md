---
title: Enabling and Removing PL/Java Support
---

The PL/Java extension is embedded in the HAWQ distribution.  This extension must be explicitly enabled on each database in which it will be used.


## <a id="pljavaprereq"></a>Prerequisites 

Before you enable PL/Java:

1. Ensure that the `$JAVA_HOME` variable is set to the same path on the master and all segment nodes.

2. Perform the following step on all machines to set up ldconfig for JDK:

	``` shell
	$ echo "$JAVA_HOME/jre/lib/amd64/server" > /etc/ld.so.conf.d/libjdk.conf
	$ ldconfig
	```
4. Make sure that your HAWQ cluster is running, you have sourced `greenplum_path.sh` and that your `$GPHOME` environment variable is set.


## <a id="enablepljava"></a>Enable PL/Java and Install JAR Files 

To use PL/Java:

1. Enable the language for each database.
1. Install user-created JAR files containing Java methods on all HAWQ hosts.
1. Add the name of the JAR file to the HAWQ `pljava_classpath` server configuration parameter in `hawq-site.xml`. This parameter value should contain a list of the installed JAR files.

### <a id="enablepljava"></a>Enable PL/Java and Install JAR Files 

Perform the following steps as the `gpadmin` user:

1. Enable PL/Java by running the `$GPHOME/share/postgresql/pljava/install.sql` SQL script in the databases that use PL/Java. For example, this example enables PL/Java on a database named `testdb`:

	``` shell
	$ psql -d testdb -f $GPHOME/share/postgresql/pljava/install.sql
	```

	The `install.sql` script registers both the trusted and untrusted PL/Java.
	
2. Copy your Java archives (JAR files) to `$GPHOME/lib/postgresql/java/` on all the HAWQ hosts. This example uses the `hawq scp` utility to copy the `myclasses.jar` file:

	``` shell
	$ hawq scp -f hawq_hosts myclasses.jar =:$GPHOME/lib/postgresql/java/
	```
	The `hawq_hosts` file contains a list of the HAWQ hosts.

3. Set the `pljava_classpath` server configuration parameter in the `hawq-site.xml` configuration file. The parameter value is a colon (:) separated list of the JAR files containing the Java classes used in any PL/Java functions. For example:

	``` shell
	$ hawq config -c pljava_classpath -v \'examples.jar:myclasses.jar\' 
	```
	
4. Restart the HAWQ cluster:

	``` shell
	$ hawq restart cluster
	```

5. (Optional) Your HAWQ installation includes an `examples.sql` file.  This script contains sample PL/Java functions that you can use for testing. Run the commands in this file to create the test functions, which use the Java classes in `examples.jar`:

	``` shell
	$ psql -f $GPHOME/share/postgresql/pljava/examples.sql
	```
	
### Enabling PL/Java in the template1 Database


To enable the PL/Java extension in all new HAWQ databases, execute the following command: 

``` shell
$ psql template1 -f $GPHOME/share/postgresql/pljava/install.sql
```

Use this option only if you are certain you want to enable PL/Java in all new databases.

### Configuring PL/Java VM Options

PL/Java JVM options can be configured via the `pljava_vmoptions` parameter in `hawq-site.xml`. For example, `pljava_vmoptions=-Xmx512M` sets the maximum heap size of the JVM. The default Xmx value is set to `-Xmx64M`.

## <a id="installcustomjars"></a>Installing Custom JARS 

1. Copy the JAR file on the master host in `$GPHOME/lib/postgresql/java`.
1. Copy the JAR file on all segments in the same location using `hawq scp` from master:

 	``` shell
	$ cd $GPHOME/lib/postgresql/java
	$ hawq scp -f hawq_hosts myfunc.jar =:$GPHOME/lib/postgresql/java/
	```
1. Set `pljava_classpath` to include the newly-copied JAR file. From the `psql` session, execute set to affect the current session:

	``` sql
	psql> set pljava_classpath='myfunc.jar'; 
	```

1. To affect all sessions, use `hawq config`: 
	
	``` shell
	$ hawq config -c pljava_classpath -v \'myfunc.jar\' 
	```
	
## <a id="uninstallpljava"></a>Disable PL/Java 

To disable PL/Java, you should:

1. Remove PL/Java support from each database in which it was added.
2. Uninstall the Java JAR files.

### <a id="uninstallpljavasupport"></a>Remove PL/Java Support from Databases 

For a database that no long requires the PL/Java language, remove support for PL/Java by running the `uninstall.sql` file as the `gpadmin` user. For example, the following command disables the PL/Java language in the specified database:

``` shell
$ psql -d <dbname> -f $GPHOME/share/postgresql/pljava/uninstall.sql
```

Replace \<dbname\> with the name of the target database.


### <a id="uninstallpljavapackage"></a>Uninstall the Java JAR files 

When no databases have PL/Java as a registered language, remove the Java JAR files:

1. Remove the `pljava_classpath` server configuration parameter in the `hawq-site.xml` file.

1. Remove the JAR files from the `$GPHOME/lib/postgresql/java/` directory of each HAWQ host.

1. Restart the HAWQ cluster:

	``` shell
	$ hawq restart cluster
	```

