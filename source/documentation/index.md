---
title: EMCS API technical interface specification
weight: 1
description: Software developers, designers, product owners or business analysts. Integrate your software with the EMCS service
---

# EMCS technical interface specification

Version 0.35.0 issued October 2025
***


## Document summary

This document is the first part of the technical interface specification (TIS) for direct trader input (DTI) to Excise Movement and Control System (EMCS).

It shows the processes involved in the exchange of messages between traders and EMCS during excise movements, and provides definitions, formats and validations of those messages.


## Introduction

Excise Movement and Control System (EMCS) is a UK and EU-wide computer system that's used to record duty suspended movements of excise goods taking place within the UK and the EU.

EMCS captures and processes information about the movements online, validates the data entered and allows real time notification of the dispatch and receipt of duty suspended excise goods.

It allows the exchange of secure online messages containing specific consignment and movement information between UK and EU trading partners.


## Current technical specifications

The Excise Movement Control System (EMCS) support documents for software developers, used from Monday 19 August 2024, can be found below.

[Design Document for National Excise Applications (DDNEA) v3.14 for phase 4.1](<../downloads/phase-4.1/Design Document for National Excise Applications (DDNEA) v3.14 for phase 4.1.zip>)

ZIP, 11 MB

[Functional Excise System Specifications (FESS) v4.12 for phase 4.1](<../downloads/phase-4.1/Functional Excise System Specifications (FESS) v4.12 for phase 4.1.zip>)

ZIP, 23 MB

[Release Scope Document (RSD) v2.10 for phase 4.1](<../downloads/phase-4.1/Release Scope Document (RSD) v2.10 for phase 4.1.zip>)

ZIP, 653 kB


## New technical specifications

The new Excise Movement Control System (EMCS) support documents for software developers, that will be in use from Thursday 12 February 2026, can be found below.

[Design Document for National Excise Applications (DDNEA) v3.23 for phase 4.2](<../downloads/phase-4.2/Design Document for National Excise Applications (DDNEA) v3.23 for phase 4.2.zip>)

ZIP, 6.4 MB

[Functional Excise System Specifications (FESS) v4.22 for phase 4.2](<../downloads/phase-4.2/Functional Excise System Specifications (FESS) v4.22 for phase 4.2.zip>)

ZIP, 18 MB

[Release Scope Document (RSD) v2.00 for phase 4.2](<../downloads/phase-4.2/Release Scope Document (RSD) v2.00 for phase 4.2.zip>)

ZIP, 1.6 MB

The following references taken from the Release Scope Document (RSD) is a list of the changes HMRC aim to deliver for the FS4.2 release on Thursday 12 February 2026.

| DDNEA RFC    | FESS RFC | Description                                                                                                                                                  |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DDNEA-P4-363 | FESS-324 | Update of rules R271 - R276                                                                                                                                  |
| DDNEA-P4-364 | FESS-325 | Removal of 'SAD' from Common Specifications/Rev1                                                                                                             |
| DDNEA-P4-365 | FESS-326 | Minor Updates in the description of EMCS Code lists/Rev1Rev2                                                                                                 |
| DDNEA-P4-366 | FESS-328 | Update the description of IE839 in TC60 and TC64                                                                                                             |
| DDNEA-P4-369 | FESS-333 | Update of the multiplicity of the IE839 data group NEGATIVE CROSS-CHECK VALIDATION RESULTS from 99x to 999x                                                  |
| DDNEA-P4-371 | n/a      | Update of the wording of the technical rule TR0104/Rev1                                                                                                      |
| DDNEA-P4-372 | FESS-335 | Change the Condition C066 to a Rule/Rev1                                                                                                                     |
| DDNEA-P4-378 | FESS-341 | Filling of the Data Group (CONSIGNEE) TRADER in the IE829, IE839 messages                                                                                    |
| DDNEA-P4-379 | n/a      | Update of the DDNEA XSDs regarding the multiplicity defined as maxOccurs="unbounded"/Rev1                                                                    |
| DDNEA-P4-380 | FESS-342 | Moving the Data Item "Export Declaration Acceptance or Goods Released for Export" under the Data Group "EXPORT DECLARATION ACCEPTANCE/RELEASE" of IE829/Rev1 |
| DDNEA-P4-381 | FESS-343 | New business validation on the "Date of Arrival of Excise  Products” data item of the IE818 - Accepted or Rejected Report of Receipt/Export                  |
| DDNEA-P4-383 | FESS-345 | Validations regarding the usage of temporary authorisations in e-AD/e-SAD/Rev1                                                                               |
| DDNEA-P4-387 | FESS-349 | Deprecation of MVS messages                                                                                                                                  |
| n/a          | FESS-310 | Updates in relation to Code list TC72 - Diagnosis Code/Rev1                                                                                                  |
| n/a          | FESS-312 | Removal of NA-NL from CL National Administration - Degree Plato/Rev1                                                                                         |
| n/a          | FESS-318 | Updates in relation to the Alcoholic Strength by Volume in Percentage (ABV)/Rev1                                                                             |
| n/a          | FESS-319 | Change of Destination with unchanged Consignee and changed Destination Type Code/Rev1Rev2                                                                    |
| n/a          | FESS-323 | Addition of the new data item 'Independent Small Producers Declaration_LNG' in the IE815/IE801 messages/Rev1                                                 |
| n/a          | FESS-330 | Inclusion of CN Code '24041100' in the business code list BC37/Rev1                                                                                          |


## Related documentation

The TIS should be read with the following related documentation:

- [API specification](/api-documentation/docs/api/service/excise-movement-control-system-api/1.0/oas/page)
- [Service guide](/guides/emcs-api-service-guide/)
- [Testing guide](/guides/emcs-api-testing-guide/)

## Changelog

You can find the changelog in the [excise-movement-control-system-api-tis GitHub wiki](https://github.com/hmrc/excise-movement-control-system-api-tis/wiki/Excise-Movement-Control-System-API-TIS-changelog).
