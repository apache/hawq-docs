---
title: Administering HAWQ and PXF Using Ambari
---

Ambari provides an easy interface to perform some of the most common HAWQ and PXF Administration Tasks, such as:

* Add a HAWQ Standby Master

## Add a HAWQ Standby Master

A HAWQ Standby Master serves as a backup of the HAWQ Master host, and is an important part of providing high availability for the HAWQ cluster. When your cluster uses a standby master, you can activate the standby if the active HAWQ Master host fails or becomes unreachable.

### When to Perform
* Execute this procedure during a scheduled maintenance period, because it requires a restart of the HAWQ service.
* A HAWQ standby master is recommended as a best practice for most clusters for high availability.
* Add a new standby master after you activate an existing standby master.

### Procedure
To add a HAWQ Standby Master to your cluster:

1.  Select an existing host in the HAWQ cluster to run the HAWQ standby master. You cannot run the standby master on the same host that runs the HAWQ master.
1. Login to the HAWQ host that you chose to run the standby master and determine if there is an existing HAWQ master data directory (for example, /data/hawq/master) on the machine. If the directory exists, rename the directory. For example:
   ```
   $ mv /data/hawq/master /data/hawq/master-old
   ```

   **Note:**  If a HAWQ master data directory exists on the host when you configure the HAWQ standby master, then the standby master may be initialized with stale data. Rename any existing master data directory before you proceed.
1.  Access the Ambari web console at http://ambari.server.hostname:8080, and login as the "admin" user. \(The default password is also "admin".\)
2.  Click **HAWQ** in the list of installed services.
3.  Select **Service Actions > Add HAWQ Standby Master** to start the Add HAWQ Standby Master Wizard.
4.  Read the Get Started page for information about HAWQ the standby master and to acknowledge that the procedure requries a service restart. Click **Next** to display the Select Host page.
5.  Use the HAWQ Standby Master menu to select a host to use for the standby service. Click **NExt** to display the Review page.

    **Note:**
    * The Current HAWQ Master host is shown only for reference. You cannot change the HAW Master host when you configure a standby master.
    * You cannot place the standby master on the same host as the HAWQ master.
6. Review the information to verify the host on which the HAWQ Standby Master will be installed. Click **Back** to change your selection or **Next** to continue.
7.
