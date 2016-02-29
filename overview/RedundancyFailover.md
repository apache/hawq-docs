# Redundancy and Fault Tolerance {#hawqarchitecture}

HAWQ uses a fault tolerance service based on heartbeats and on-demand probe protocols. It can identify newly added node dynamically and remove node from the cluster when it becomes unusable.

## About Segment Fault Tolerance {#aboutsegmentfailover}

In HAWQ, the segments are stateless. This ensures faster recovery and better availability.

When a segment fails, the segment is removed from the resource pool. Queries are no longer dispatched to the segment. When the segment is operational again, the Fault Tolerance Service verifies its state and adds the segment back to the resource pool.

## About Interconnect Redundancy {#aboutinterconnectredundancy}

The *interconnect* refers to the inter-process communication between the segments and the network infrastructure on which this communication relies. You can achieve a highly available interconnect by deploying dual Gigabit Ethernet switches on your network and deploying redundant Gigabit connections to the HAWQ host \(master and segment\) servers.

In order to use multiple NICs in HAWQ, NIC bounding is required.

