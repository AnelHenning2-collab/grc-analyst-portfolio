# Cross-Framework Compliance Mapping
## NIST CSF 2.0 ↔ ISO/IEC 27001:2022 ↔ SOC 2 (TSC) ↔ NIST 800-53 Rev. 5

**Prepared By:** [Your Name]  
**Date:** [Date]  
**Purpose:** Demonstrate control equivalence across major cybersecurity frameworks to reduce audit duplication and support unified compliance programs.

---

## Introduction

Organizations are increasingly required to comply with multiple frameworks simultaneously. This mapping shows how controls across **NIST CSF 2.0**, **ISO/IEC 27001:2022**, **SOC 2 (Trust Services Criteria)**, and **NIST SP 800-53 Rev. 5** align — enabling a "map once, comply many" approach.

**Key Insight:** A single well-implemented control (e.g., multi-factor authentication) can satisfy requirements across all four frameworks simultaneously.

---

## Access Control

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Identity & Access Management | PR.AA-01, PR.AA-02 | Annex A 5.16, 5.17 | CC6.1, CC6.2 | IA-2, IA-5, AC-2 |
| Multi-Factor Authentication | PR.AA-03 | Annex A 8.5 | CC6.1 | IA-2(1), IA-2(2) |
| Privileged Access Management | PR.AA-05 | Annex A 8.2 | CC6.3 | AC-6, AC-6(1) |
| Access Reviews | PR.AA-05 | Annex A 5.18 | CC6.3 | AC-2(1), AC-6(7) |
| Least Privilege | PR.AA-05 | Annex A 8.2 | CC6.3 | AC-6 |
| Remote Access | PR.AA-02, PR.IR-01 | Annex A 8.20 | CC6.6 | AC-17 |
| Session Management | PR.AA-04 | Annex A 8.5 | CC6.1 | AC-12 |

---

## Asset Management

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Hardware Inventory | ID.AM-01 | Annex A 5.9 | CC6.1 | CM-8 |
| Software Inventory | ID.AM-02 | Annex A 5.9 | CC6.1 | CM-8(1) |
| Data Inventory & Classification | ID.AM-07 | Annex A 5.9, 5.12 | CC6.1, PI1.2 | CM-8, RA-2 |
| Media Management | PR.DS-01 | Annex A 7.10 | CC6.1 | MP-2, MP-3 |
| End-of-Life Asset Disposal | PR.DS-01 | Annex A 7.14 | CC6.5 | MP-6 |

---

## Risk Management

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Risk Assessment Process | ID.RA-01 through ID.RA-07 | Clause 6.1.2 | CC3.1, CC3.2 | RA-3 |
| Risk Treatment / Remediation | GV.RM-06 | Clause 6.1.3 | CC3.4 | RA-3(1) |
| Risk Register Maintenance | ID.RA-05 | Clause 6.1.2 | CC3.2 | RA-3 |
| Vulnerability Management | ID.RA-01, PR.PS-02 | Annex A 8.8 | CC7.1 | RA-5 |
| Threat Intelligence | ID.RA-02 | Annex A 5.7 | CC3.1 | PM-16 |

---

## Incident Management

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Incident Response Plan | RS.MA-01 | Annex A 5.26 | CC7.3, CC7.4 | IR-8 |
| Incident Detection & Reporting | DE.AE-06, RS.CO-02 | Annex A 6.8 | CC7.2 | IR-6, SI-4 |
| Incident Classification | RS.MA-02 | Annex A 5.25 | CC7.3 | IR-5 |
| Incident Analysis & Forensics | RS.AN-03 | Annex A 5.28 | CC7.4 | IR-4 |
| Post-Incident Review | RS.CO-06 | Annex A 5.27 | CC7.4 | IR-4 |
| Breach Notification | RS.CO-03 | Annex A 5.26 | CC2.2 | IR-6 |

---

## Data Protection

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Encryption at Rest | PR.DS-01 | Annex A 8.24 | CC6.1 | SC-28 |
| Encryption in Transit | PR.DS-02 | Annex A 8.24 | CC6.7 | SC-8 |
| Data Loss Prevention (DLP) | PR.DS-05 | Annex A 8.12 | CC6.7 | SI-12 |
| Data Retention & Disposal | ID.AM-08 | Annex A 8.10 | CC6.5 | MP-6, AU-11 |
| Backup & Recovery | RC.RP-03 | Annex A 8.13 | A1.2 | CP-9 |

---

## Audit & Logging

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Audit Log Generation | DE.CM-03 | Annex A 8.15 | CC7.2, CC7.3 | AU-2, AU-3 |
| Log Retention | DE.CM-09 | Annex A 8.15 | CC7.2 | AU-11 |
| Log Monitoring & Review | DE.CM-01, DE.AE-02 | Annex A 8.16 | CC7.2 | AU-6 |
| Centralized Log Management (SIEM) | DE.CM-01 | Annex A 8.16 | CC7.2 | SI-4 |
| Clock Synchronization | DE.CM-09 | Annex A 8.17 | CC7.2 | AU-8 |

---

## Business Continuity & Recovery

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Business Continuity Planning | RC.RP-01 | Annex A 5.29 | A1.2, A1.3 | CP-2 |
| Disaster Recovery | RC.RP-01 | Annex A 5.30 | A1.2 | CP-10 |
| BCP / DR Testing | RC.RP-04 | Annex A 5.29 | A1.3 | CP-4 |
| RTO/RPO Definitions | RC.RP-01 | Annex A 5.29 | A1.2 | CP-2 |

---

## Third-Party / Vendor Risk

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Vendor Risk Assessment | GV.SC-04 | Annex A 5.19 | CC9.2 | SA-9 |
| Vendor Security Requirements | GV.SC-06 | Annex A 5.20 | CC9.2 | SA-4 |
| Vendor Monitoring | GV.SC-07 | Annex A 5.22 | CC9.2 | SA-9(2) |
| Vendor Offboarding | GV.SC-07 | Annex A 5.23 | CC6.5 | SA-9 |

---

## Human Resources Security

| Control Domain | NIST CSF 2.0 | ISO 27001:2022 | SOC 2 TSC | NIST 800-53 Rev. 5 |
|---|---|---|---|---|
| Security Awareness Training | PR.AT-01 | Annex A 6.3 | CC1.4, CC2.2 | AT-2 |
| Pre-Employment Screening | GV.PO-02 | Annex A 6.1 | CC1.1 | PS-3 |
| Onboarding / Offboarding | PR.AA-05 | Annex A 6.2, 6.5 | CC6.2 | PS-4, PS-5 |
| Disciplinary Process | GV.PO-02 | Annex A 6.4 | CC1.4 | PS-8 |

---

## Using This Mapping

### For GRC Analysts:
- Use this mapping when scoping a new audit — identify which framework controls overlap to reduce evidence collection effort
- When a control satisfies multiple frameworks, collect evidence once and reference across all applicable requirements

### For Control Owners:
- Implementing the control in one column satisfies requirements in all mapped columns
- Prioritize controls that appear across all four frameworks — these represent universal security baseline requirements

### For Executives:
- This mapping enables a unified compliance program rather than separate siloed programs for each framework
- Estimated effort savings: 30–50% reduction in audit preparation time when using a unified evidence model

---

## References

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- ISO/IEC 27001:2022: https://www.iso.org/standard/82875.html
- AICPA SOC 2 Trust Services Criteria: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
- NIST SP 800-53 Rev. 5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

---

## Portfolio STAR Story — Team Collaboration in Practice

> **Industry:** Federal Government / Defense Contractor | **Role:** GRC Analyst (cross-functional team effort)

### Situation
A mid-sized federal IT contractor was simultaneously pursuing FedRAMP Moderate authorization and maintaining its existing NIST SP 800-53 compliance posture while a new contract required demonstrating ISO/IEC 27001 alignment. The compliance team was treating each framework as a separate workstream, creating duplicated evidence collection, overlapping audit requests to control owners, and analyst burnout. The Program Security Officer escalated to leadership that the team was on track to miss the FedRAMP submission deadline.

### Task
I was brought in to work alongside two senior compliance analysts and a technical SME to build a unified control mapping that would let the team collect evidence once and satisfy all three frameworks simultaneously. My specific role was to build the cross-walk document and facilitate buy-in from the control owners who had been responding to three separate audit requests for the same data.

### Action
I researched the overlap between NIST CSF 2.0, NIST 800-53 Rev. 5, ISO 27001:2022, and SOC 2 TSC using publicly available NIST guidance and AICPA crosswalk documentation. I built the mapping table collaboratively — running weekly 30-minute syncs with each control owner to validate the mappings were accurate in their specific environment and not just theoretical. When I found gaps where a control satisfied one framework but not another, I flagged these to the senior analysts rather than resolving them unilaterally so the team could decide on the appropriate remediation approach together. I then presented the "map once, comply many" methodology to the PSO and compliance director to get leadership alignment before rolling it out.

### Result
The unified mapping reduced evidence collection requests to control owners by approximately 40%, immediately relieving the operational pressure that had been escalated. The FedRAMP submission was completed on schedule. The ISO 27001 readiness assessment used the same evidence package with minimal additions. The mapping document was formally adopted as a standing team asset and updated as part of every subsequent compliance cycle.
