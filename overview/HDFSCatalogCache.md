---
title: HDFS Catalog Cache
---

HDFS catalog cache is a caching service used by HAWQ master to determine the distribution information of table data on HDFS.

HDFS is slow at RPC handling, especially when the number of concurrent requests is high. In order to decide which segments handle which part of data, HAWQ needs data location information from HDFS NameNodes. HDFS catalog cache is used to cache the data location information and accelerate HDFS RPCs.
