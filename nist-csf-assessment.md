# NIST CSF 2.0 Maturity Assessment — Sample Organization
**Author:** Anél Henning | GRC Analyst Portfolio  
**Framework:** NIST Cybersecurity Framework 2.0  
**Assessment Date:** May 2026  
**Organization Type:** Mid-size enterprise (~500 employees)

---

## Executive Summary

This assessment evaluates the sample organization's cybersecurity posture against the NIST Cybersecurity Framework 2.0 (CSF 2.0) six core functions. Maturity levels are rated on a 1–4 scale (Initial → Managed → Defined → Optimizing).

| CSF Function | Current Maturity | Target Maturity | Gap |
|---|---|---|---|
| **GV — Govern** | 1 — Initial | 3 — Defined | 🔴 High |
| **ID — Identify** | 2 — Managed | 3 — Defined | 🟡 Medium |
| **PR — Protect** | 2 — Managed | 3 — Defined | 🟡 Medium |
| **DE — Detect** | 1 — Initial | 3 — Defined | 🔴 High |
| **RS — Respond** | 2 — Managed | 3 — Defined | 🟡 Medium |
| **RC — Recover** | 1 — Initial | 3 — Defined | 🔴 High |

**Overall Maturity: 1.5 / 4 — Significant gaps in Govern, Detect, and Recover functions**

---

## Maturity Scale

| Level | Name | Description |
|---|---|---|
| 1 | Initial | Ad hoc; undocumented; reactive |
| 2 | Managed | Partially documented; inconsistently applied |
| 3 | Defined | Fully documented; consistently applied; reviewed periodically |
| 4 | Optimizing | Metrics-driven; continuously improved; integrated with risk management |

---

## GV — Govern (Current: 1 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| GV.OC-01: Organizational context understood | Partial — no formal risk appetite statement | 🔴 | Define and document risk appetite; approve at board level |
| GV.OC-02: Legal/regulatory requirements tracked | Partial — compliance spreadsheet, not systematic | 🟡 | Implement compliance obligation register |
| GV.RM-01: Risk management policy established | No formal policy | 🔴 | Draft and approve enterprise risk management policy |
| GV.RM-02: Risk management strategy documented | Undocumented | 🔴 | Develop 3-year cybersecurity strategy aligned to business goals |
| GV.PO-01: Cybersecurity policies established | AUP exists; other policies missing | 🟡 | Complete policy library (IRP, ACP, Data Classification) |
| GV.RR-01: Roles and responsibilities defined | Informal; not documented | 🔴 | Create RACI matrix for cybersecurity responsibilities |

---

## ID — Identify (Current: 2 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| ID.AM-01: Asset inventory maintained | Informal spreadsheet | 🟡 | Formalize asset inventory; include cloud assets |
| ID.AM-02: Software inventory maintained | Not maintained | 🔴 | Deploy software asset management tool |
| ID.RA-01: Vulnerabilities identified | Quarterly scans | 🟡 | Move to continuous scanning; integrate with patch management |
| ID.RA-02: Threat intelligence consumed | CISA alerts only | 🟡 | Subscribe to ISAC feeds relevant to industry |
| ID.RA-05: Risk register maintained | Not formal | 🔴 | Implement enterprise risk register (see risk-register.xlsx) |

---

## PR — Protect (Current: 2 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| PR.AA-01: Identities managed | Active Directory; no PAM | 🟡 | Implement privileged access management (PAM) |
| PR.AA-03: Users authenticated | MFA available, not enforced | 🔴 | Mandate MFA for all accounts; enforce via policy and technical control |
| PR.AA-05: Access permissions reviewed | Annual review only | 🟡 | Move to semi-annual access certification campaigns |
| PR.AT-01: Awareness training provided | Annual CBT; <80% completion | 🟡 | Mandate completion; add phishing simulations quarterly |
| PR.DS-01: Data-at-rest protected | Encryption on servers; not laptops | 🟡 | Enable full-disk encryption on all endpoints |
| PR.PS-01: Config baselines maintained | Partial — servers only | 🟡 | Extend CIS benchmarks to all endpoint types |

---

## DE — Detect (Current: 1 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| DE.CM-01: Networks monitored | Firewall logs; no SIEM | 🔴 | Implement SIEM with alerting for high-priority events |
| DE.CM-03: User activity monitored | Not in place | 🔴 | Deploy user activity monitoring for privileged accounts |
| DE.CM-06: External service activity monitored | Not in place | 🔴 | Enable cloud security posture management (CSPM) |
| DE.AE-02: Anomalies analyzed | Manual review only | 🔴 | Define alert thresholds; implement automated anomaly detection |

---

## RS — Respond (Current: 2 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| RS.MA-01: Incident response executed | IRP exists; untested | 🟡 | Conduct tabletop exercise Q3 2026 |
| RS.CO-02: Incidents reported | Internal only; no regulatory process | 🟡 | Define regulatory notification thresholds and timelines |
| RS.AN-03: Incident analysis performed | Ad hoc post-incident review | 🟡 | Standardize post-incident review template; track lessons learned |

---

## RC — Recover (Current: 1 | Target: 3)

| Subcategory | Current State | Gap | Recommendation |
|---|---|---|---|
| RC.RP-01: Recovery plan executed | BCP outdated (2023) | 🔴 | Update BCP; align RTO/RPO with business requirements |
| RC.RP-02: Recovery plan tested | Never tested | 🔴 | Schedule BCP tabletop exercise; validate backup restoration |
| RC.CO-03: Recovery communicated | No communication plan | 🔴 | Draft crisis communications plan including customer and regulatory notifications |

---

## Prioritized Remediation Roadmap

### Immediate (0–30 days)
1. Enforce MFA on all privileged accounts
2. Escalate critical vulnerabilities (R-001, R-006 in risk register)
3. Assign risk register ownership

### Short-Term (30–90 days)
4. Draft missing policies (IRP, ACP, Data Classification)
5. Conduct IRP tabletop exercise
6. Implement SIEM baseline alerting
7. Formalize asset inventory

### Medium-Term (90–180 days)
8. Launch semi-annual access certification
9. Develop vendor risk assessment process
10. Update BCP; test backup restoration
11. Define regulatory breach notification process

---

## References
- NIST Cybersecurity Framework 2.0 (February 2024)
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls
- NIST SP 800-30 Rev. 1 — Risk Assessments
- CIS Controls v8
