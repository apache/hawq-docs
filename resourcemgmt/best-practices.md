---
title: Best Practices for Configuring Resource Management
---

When configuring resource management, you can apply certain best practices to ensure that resources are managed both efficiently and for best system performance.

The following is a list of high-level best practices for optimal resource management:

-   Make sure segments do not have identical IP addresses. See [Segments Do Not Appear in gp\_segment\_configuration](/200/hawq/troubleshooting/Troubleshooting.html) for an explanation of this problem.
-   Configure all segments to have the same resource capacity. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html).
-   To prevent resource fragmentation, ensure that your deployment's segment resource capacity \(standalone mode\) or YARN node resource capacity \(YARN mode\) is a multiple of all virtual segment resource quotas. See [Configuring Segment Resource Capacity](ConfigureResourceManagement.html) \(HAWQ standalone mode\) and [Setting HAWQ Segment Resource Capacity in YARN](YARNIntegration.html).
-   Ensure that enough registered segments are available and usable for query resource requests. If the number of unavailable or unregistered segments is higher than a set limit, then query resource requests are rejected. Also ensure that the variance of dispatched virtual segments across physical segments is not greater than the configured limit. See [Rejection of Query Resource Requests](/200/hawq/troubleshooting/Troubleshooting.html).
-   Use multiple segment temporary directories on separate, large disks (2TB or greater) to load balance writes to temporary files (for example, `/disk1/tmp /disk2/tmp`). For a given query, HAWQ will use a separate temp directory (if available) for each virtual segment to store spill files. Multiple HAWQ sessions will also use separate temp directories where available to avoid disk contention. If you configure too few temp directories, or you place multiple temp directories on the same disk, you increase the risk of disk contention or running out of disk space when multiple virtual segments target the same disk. 
-   Configure minimum resource levels in YARN, and tune the timeout of when idle resources are returned to YARN. See [Tune HAWQ Resource Negotiations with YARN](YARNIntegration.html).
-   Make sure that the property `yarn.scheduler.minimum-allocation-mb` in `yarn-site.xml` is an equal subdivision of 1GB. For example, 1024, 512. See [Setting HAWQ Segment Resource Capacity in YARN](YARNIntegration.html#topic_pzf_kqn_c5).
