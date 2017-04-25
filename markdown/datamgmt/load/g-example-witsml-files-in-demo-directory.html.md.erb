---
title: Example using WITSML™ Files (In demo Directory)
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

This example demonstrates loading sample data describing an oil rig using a Joost STX transformation. The data is in the form of a complex XML file downloaded from energistics.org.

The Wellsite Information Transfer Standard Markup Language (WITSML™) is an oil industry initiative to provide open, non-proprietary, standard interfaces for technology and software to share information among oil companies, service companies, drilling contractors, application vendors, and regulatory agencies. For more information about WITSML™, see [http://www.witsml.org](http://www.witsml.org).

The oil rig information consists of a top level `<rigs>` element with multiple child elements such as `<documentInfo>,                             <rig>`, and so on. The following excerpt from the file shows the type of information in the `<rig>` tag.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="../stylesheets/rig.xsl" type="text/xsl" media="screen"?>
<rigs 
 xmlns="http://www.witsml.org/schemas/131" 
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
 xsi:schemaLocation="http://www.witsml.org/schemas/131 ../obj_rig.xsd" 
 version="1.3.1.1">
 <documentInfo>
 ... misc data ...
 </documentInfo>
 <rig uidWell="W-12" uidWellbore="B-01" uid="xr31">
     <nameWell>6507/7-A-42</nameWell>
     <nameWellbore>A-42</nameWellbore>
     <name>Deep Drill #5</name>
     <owner>Deep Drilling Co.</owner>
     <typeRig>floater</typeRig>
     <manufacturer>Fitsui Engineering</manufacturer>
     <yearEntService>1980</yearEntService>
     <classRig>ABS Class A1 M CSDU AMS ACCU</classRig>
     <approvals>DNV</approvals>
 ... more data ...
```

The goal is to import the information for this rig into HAWQ.

The sample document, *rig.xml*, is about 11KB in size. The input does not contain tabs so the relevant information can be converted into records delimited with a pipe (|).

`W-12|6507/7-A-42|xr31|Deep Drill #5|Deep Drilling Co.|John                             Doe|John.Doe@example.com|`

With the columns:

-   `well_uid text`, -- e.g. W-12
-   `well_name text`, -- e.g. 6507/7-A-42
-   `rig_uid text`, -- e.g. xr31
-   `rig_name text`, -- e.g. Deep Drill \#5
-   `rig_owner text`, -- e.g. Deep Drilling Co.
-   `rig_contact text`, -- e.g. John Doe
-   `rig_email text`, -- e.g. John.Doe@example.com
-   `doc xml`

Then, load the data into HAWQ.


