# SOC 2 Type II Audit Readiness — Gap Analysis
**Author:** Anél Henning | GRC Analyst Portfolio  
**Framework:** AICPA SOC 2 Trust Services Criteria (TSC) — Security (CC Series)  
**Assessment Date:** May 2026  
**Organization Type:** Mid-size SaaS company  
**Audit Target:** SOC 2 Type II — 12-month observation period

---

## Executive Summary

This gap analysis assesses readiness for a SOC 2 Type II audit against the Security Trust Services Criteria (CC1–CC9). Controls are rated by current implementation status and assigned remediation priority.

| TSC Category | Controls Assessed | Fully Implemented | Partially Implemented | Not Implemented |
|---|---|---|---|---|
| CC1 — Control Environment | 5 | 2 | 2 | 1 |
| CC2 — Communication & Information | 3 | 1 | 2 | 0 |
| CC3 — Risk Assessment | 4 | 1 | 1 | 2 |
| CC4 — Monitoring Activities | 3 | 0 | 2 | 1 |
| CC5 — Control Activities | 4 | 2 | 1 | 1 |
| CC6 — Logical & Physical Access | 8 | 3 | 3 | 2 |
| CC7 — System Operations | 5 | 2 | 2 | 1 |
| CC8 — Change Management | 4 | 2 | 1 | 1 |
| CC9 — Risk Mitigation | 3 | 1 | 1 | 1 |
| **TOTAL** | **39** | **14 (36%)** | **15 (38%)** | **11 (28%)** |

**Overall SOC 2 Readiness: 36% fully implemented — significant work required before audit**

---

## Detailed Control Assessment

### CC1 — Control Environment

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC1.1 | COSO principles — demonstrates commitment to integrity and ethical values | 🟡 Partial | Code of conduct exists | Code of conduct not formally signed by all staff; no ethics training documented |
| CC1.2 | Board oversight of internal controls | 🟡 Partial | Board meeting minutes | No formal cybersecurity reporting to board; recommend quarterly security briefing |
| CC1.3 | Organizational structure with defined authority | ✅ Implemented | Org chart; job descriptions | — |
| CC1.4 | Commitment to competence | ✅ Implemented | Hiring records; role requirements | — |
| CC1.5 | Accountability for internal control responsibilities | 🔴 Not Implemented | None | No formal RACI for security controls; draft and approve |

### CC2 — Communication & Information

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC2.1 | Information to support internal controls | 🟡 Partial | Policy documents | Policies exist but not systematically communicated to all staff |
| CC2.2 | Internal communication of control objectives | 🟡 Partial | All-hands emails | No formal security awareness program with documented completion |
| CC2.3 | External communication of commitments | ✅ Implemented | Privacy policy; DPA templates | — |

### CC3 — Risk Assessment

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC3.1 | Risk assessment process established | 🟡 Partial | Informal risk spreadsheet | No formal risk assessment methodology; implement documented process |
| CC3.2 | Fraud risk assessment | 🔴 Not Implemented | None | No fraud risk assessment performed; add to annual risk review |
| CC3.3 | Changes affecting risk identified and assessed | 🔴 Not Implemented | None | No change-triggered risk assessment process; link to change management |
| CC3.4 | Third-party risk assessed | ✅ Implemented | Vendor contracts with DPAs | Basic vendor risk; formalize with security questionnaires |

### CC4 — Monitoring Activities

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC4.1 | Controls evaluated through ongoing monitoring | 🟡 Partial | Informal IT checks | No continuous control monitoring; implement automated compliance checks |
| CC4.2 | Deficiencies communicated and remediated | 🟡 Partial | Email threads | No formal deficiency tracking system; implement GRC tool or ticketing workflow |
| CC4.3 | Evaluation of controls by external parties | 🔴 Not Implemented | None | No third-party assessment or pen test in last 12 months; schedule immediately |

### CC5 — Control Activities

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC5.1 | Controls selected and developed | ✅ Implemented | Security policies; IT procedures | — |
| CC5.2 | Technology controls implemented | 🟡 Partial | Firewall, AV configs | No centralized evidence of all technology control configurations |
| CC5.3 | Policies and procedures deployed | ✅ Implemented | Policy library | — |
| CC5.4 | Segregation of duties enforced | 🔴 Not Implemented | None | No SoD matrix; admin roles not separated; develop SoD controls |

### CC6 — Logical and Physical Access Controls *(Most Audited Section)*

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC6.1 | Logical access security controls | 🟡 Partial | AD config; MFA on some systems | MFA not enforced on all systems; access request process informal |
| CC6.2 | Prior to access provisioned — new user access | 🔴 Not Implemented | None | No documented provisioning workflow with manager approval tracking |
| CC6.3 | Role-based access and least privilege | 🟡 Partial | Role definitions exist | Access granted outside roles without formal exception process |
| CC6.4 | Access removed on termination | ✅ Implemented | HR offboarding checklist | — |
| CC6.5 | Logical access reviewed periodically | 🔴 Not Implemented | None | **HIGH PRIORITY** — No formal access certification; implement semi-annual review |
| CC6.6 | External party access restricted | ✅ Implemented | Vendor access policy | — |
| CC6.7 | Transmission of data protected | ✅ Implemented | TLS certs; encryption in transit | — |
| CC6.8 | Malicious software prevention | 🟡 Partial | AV deployed | No EDR; no formal malware response procedure |

### CC7 — System Operations

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC7.1 | Vulnerabilities identified and managed | 🟡 Partial | Quarterly scan reports | Scans not continuous; patch SLA not enforced |
| CC7.2 | Anomalies and incidents identified | 🔴 Not Implemented | None | No SIEM; no formal alerting process; **implement SIEM baseline** |
| CC7.3 | Security incidents evaluated and responded to | ✅ Implemented | IRP document | IRP untested; conduct tabletop before audit |
| CC7.4 | Security incidents contained and remediated | ✅ Implemented | Post-incident documentation | — |
| CC7.5 | Disclosures of security incidents | 🟡 Partial | IRP includes notification section | No documented regulatory notification thresholds tested |

### CC8 — Change Management

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC8.1 | Infrastructure, data, software changes authorized | ✅ Implemented | Change request tickets | — |
| CC8.2 | Changes reviewed for risk | 🟡 Partial | Informal review | No formal risk assessment step in change process |
| CC8.3 | Emergency changes managed | ✅ Implemented | Emergency change procedure | — |
| CC8.4 | Changes tested prior to implementation | 🔴 Not Implemented | None | No documented test results for changes; require QA sign-off |

### CC9 — Risk Mitigation

| Control | Description | Status | Evidence Available | Gap / Remediation |
|---|---|---|---|---|
| CC9.1 | Risk mitigation activities — vendor risk | 🟡 Partial | Vendor contracts | No vendor risk assessment questionnaire |
| CC9.2 | Business disruption risk — BCP/DR | 🔴 Not Implemented | Outdated BCP | BCP not tested; no DR runbook; **critical gap for Type II** |
| CC9.3 | Risk management — insurance | ✅ Implemented | Cyber insurance policy | — |

---

## Prioritized Remediation Plan

### 🔴 Critical (Fix Before Audit Window Opens)
1. **CC6.5** — Implement semi-annual access certification; document first cycle results
2. **CC7.2** — Deploy SIEM; establish alert baseline; document alert response process
3. **CC6.2** — Implement formal provisioning workflow with manager approval audit trail
4. **CC9.2** — Update and test BCP; create DR runbook

### 🟠 High (Address in First 60 Days of Audit Period)
5. **CC4.3** — Schedule and complete annual penetration test
6. **CC5.4** — Develop separation of duties matrix; implement compensating controls
7. **CC3.2/3.3** — Conduct fraud risk assessment; link change management to risk assessment
8. **CC1.5** — Publish and distribute RACI matrix for security controls

### 🟡 Medium (Complete During Audit Period)
9. **CC2.1/2.2** — Launch formal security awareness program; track completion
10. **CC8.4** — Require QA sign-off documentation for all production changes
11. **CC7.1** — Move to continuous vulnerability scanning; enforce patch SLAs

---

## Evidence Collection Guide

For each implemented control, auditors will request evidence of **consistent operation over the 12-month audit period**. Key evidence types:

| Control Area | Evidence to Collect |
|---|---|
| Access provisioning | Ticketing system records showing manager approval for each access grant |
| Access reviews | Signed access certification reports (semi-annual) |
| Offboarding | IT ticket closure records showing termination date vs. access disable date |
| Vulnerability management | Scan reports (monthly); patch records with dates |
| Incident response | Incident tickets; post-incident reports; IRP tabletop exercise documentation |
| Change management | Change request tickets with approval, test results, and closure |
| Security awareness | Training completion reports (by employee, by date) |
| MFA enforcement | Configuration screenshots; admin reports showing MFA enrollment |

---

## References
- AICPA SOC 2 Trust Services Criteria (2017 with 2022 updates)
- AICPA Description Criteria for a SOC 2 Report
- NIST SP 800-53 Rev. 5
- ISO/IEC 27001:2022
