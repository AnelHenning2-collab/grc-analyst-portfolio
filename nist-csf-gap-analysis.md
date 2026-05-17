# NIST Cybersecurity Framework (CSF) Gap Analysis
## Mock Audit — Acme Corp (Fictional Organization)

**Prepared By:** [Your Name]  
**Date:** [Date]  
**Framework Version:** NIST CSF 2.0  
**Assessment Scope:** Enterprise IT environment (excluding OT/ICS)  
**Overall Maturity Score:** 2.1 / 5.0 (Partial → Risk-Informed transition)

---

## Executive Summary

This gap analysis assesses Acme Corp's cybersecurity posture against the NIST Cybersecurity Framework (CSF) 2.0. The assessment identified significant gaps primarily in the **Govern**, **Detect**, and **Respond** functions. The organization has foundational controls in place for **Protect** and **Identify**, but lacks formalized policies, incident response capability, and continuous monitoring.

**Key Findings:**
- No formal cybersecurity governance program or documented risk appetite
- Asset inventory is incomplete and not maintained regularly
- Security monitoring is reactive with no SIEM or centralized logging
- Incident response plan exists but has never been tested
- Recovery planning is limited to IT disaster recovery with no documented BCP

**Priority Recommendations:**
1. Establish a cybersecurity steering committee and define risk appetite (Govern)
2. Complete and automate asset inventory (Identify)
3. Deploy centralized logging and SIEM (Detect)
4. Conduct tabletop exercise against the IR plan (Respond)
5. Develop and test a full Business Continuity Plan (Recover)

---

## Scoring Methodology

Each subcategory is scored on the NIST CSF Implementation Tier scale:

| Tier | Name | Description |
|---|---|---|
| 1 | Partial | Ad hoc, reactive, limited awareness |
| 2 | Risk-Informed | Practices exist but not organization-wide |
| 3 | Repeatable | Formal policies, consistent execution |
| 4 | Adaptive | Data-driven, continuously improving |

---

## Function 1: GOVERN (GV)

*New in CSF 2.0 — establishes cybersecurity strategy, governance, and risk management.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| GV.OC-01 | Organizational mission understood | Partially defined | 2 | No formal cybersecurity mission statement | Medium |
| GV.OC-02 | Internal/external stakeholders identified | Informal only | 1 | No stakeholder register | High |
| GV.RM-01 | Risk management policy established | Draft exists | 2 | Not approved or enforced | High |
| GV.RM-02 | Risk appetite defined | Not defined | 1 | No documented risk tolerance | High |
| GV.RM-03 | Senior leadership accountable for risk | Informal | 1 | No CISO or security steering committee | High |
| GV.PO-01 | Policy established and communicated | Some policies exist | 2 | Inconsistent, not all employees trained | Medium |

**Function Score: 1.5 / 4** — Critical gaps in governance structure and risk oversight.

**Remediation Actions:**
- Appoint a security owner or establish a virtual CISO function
- Conduct risk appetite workshop with executive leadership
- Formalize and ratify the risk management policy

---

## Function 2: IDENTIFY (ID)

*Understanding the organization's assets, risks, and vulnerabilities.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| ID.AM-01 | Hardware asset inventory | Spreadsheet, 60% complete | 2 | Incomplete, manually maintained | High |
| ID.AM-02 | Software asset inventory | Incomplete | 1 | No software management tool | High |
| ID.AM-03 | Network flows documented | Not documented | 1 | No network diagram or flow mapping | Medium |
| ID.AM-07 | Data inventory maintained | Partial | 2 | No data classification scheme applied | High |
| ID.RA-01 | Vulnerabilities identified | Quarterly scans | 2 | Not continuous, no CVE tracking | Medium |
| ID.RA-03 | Threats identified and assessed | Ad hoc | 1 | No threat intelligence program | Medium |
| ID.RA-05 | Threats, vulnerabilities, likelihoods consolidated | Not performed | 1 | No formal risk register | High |
| ID.IM-01 | Improvements identified from assessments | Informal | 2 | No formal tracking or remediation program | Medium |

**Function Score: 1.6 / 4** — Asset management and risk assessment need significant improvement.

**Remediation Actions:**
- Implement automated asset discovery tool (e.g., Lansweeper, Qualys CSAM)
- Deploy and maintain a formal risk register
- Apply the Data Classification Policy to all known data stores

---

## Function 3: PROTECT (PR)

*Implementing safeguards to limit cybersecurity event impact.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| PR.AA-01 | Identities managed | AD in place | 3 | No privileged access management (PAM) | Medium |
| PR.AA-02 | Authentication managed | Passwords + some MFA | 2 | MFA not enforced org-wide | High |
| PR.AA-05 | Access permissions managed | RBAC partially applied | 2 | No periodic access reviews | Medium |
| PR.AT-01 | Security awareness training | Annual training | 2 | Not phishing-simulated, completion not tracked | Medium |
| PR.DS-01 | Data-at-rest protected | Partial encryption | 2 | Laptops not all encrypted | High |
| PR.DS-02 | Data-in-transit protected | TLS on web apps | 3 | Internal traffic not consistently encrypted | Low |
| PR.IR-01 | Networks segmented | Basic VLANs | 2 | No micro-segmentation, flat internal network | Medium |
| PR.PS-01 | Config management practices | Informal baselines | 1 | No CIS benchmark hardening applied | Medium |

**Function Score: 2.4 / 4** — Best function; basic controls exist but have consistency gaps.

**Remediation Actions:**
- Enforce MFA for all users, starting with privileged accounts
- Enable full-disk encryption on all endpoints (BitLocker/FileVault)
- Implement quarterly access reviews
- Apply CIS Benchmark Level 1 hardening to servers and endpoints

---

## Function 4: DETECT (DE)

*Identifying cybersecurity events in a timely manner.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| DE.CM-01 | Networks monitored | Firewall logs only | 1 | No SIEM, no centralized log aggregation | Critical |
| DE.CM-03 | Personnel activity monitored | Not performed | 1 | No user behavior analytics (UEBA) | Medium |
| DE.CM-06 | External services monitored | Not performed | 1 | No cloud security monitoring | Medium |
| DE.CM-09 | Computing hardware monitored | Basic antivirus | 2 | No EDR solution deployed | High |
| DE.AE-02 | Events analyzed | Manual, ad hoc | 1 | No correlation, no alert triage process | High |
| DE.AE-06 | Alerts communicated to responders | Email only | 1 | No ticketing integration or escalation path | Medium |

**Function Score: 1.2 / 4** — Most critical gap area. Detection capability is minimal.

**Remediation Actions:**
- Deploy a SIEM solution (e.g., Microsoft Sentinel, Elastic SIEM, Splunk)
- Implement EDR on all endpoints (e.g., CrowdStrike, SentinelOne, Defender for Endpoint)
- Establish a log retention policy (minimum 12 months)
- Define and document alert triage and escalation procedures

---

## Function 5: RESPOND (RS)

*Taking action regarding a detected cybersecurity incident.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| RS.MA-01 | Incident response plan exists | Draft plan | 2 | Never tested; not all stakeholders aware | High |
| RS.MA-02 | Incidents triaged and categorized | Ad hoc | 1 | No severity matrix or triage playbooks | High |
| RS.CO-02 | Incidents reported internally | Informal | 2 | No formal internal notification process | Medium |
| RS.CO-03 | Regulatory reporting capability | Unknown | 1 | No legal/compliance review of obligations | High |
| RS.AN-03 | Analysis performed | Not formalized | 1 | No forensic capability or chain of custody | Medium |
| RS.MI-01 | Incidents contained | Case-by-case | 2 | No documented containment playbooks | High |

**Function Score: 1.5 / 4** — IR plan exists on paper but lacks operational readiness.

**Remediation Actions:**
- Conduct a tabletop exercise against the current IR plan within 90 days
- Develop at least 3 response playbooks (ransomware, phishing, insider threat)
- Engage legal counsel to determine regulatory breach notification obligations
- Establish a formal chain-of-custody procedure for evidence handling

---

## Function 6: RECOVER (RC)

*Restoring capabilities after a cybersecurity incident.*

| Subcategory | Description | Current State | Score | Gap | Priority |
|---|---|---|---|---|---|
| RC.RP-01 | Recovery plan in place | IT DR plan only | 2 | No business-aligned BCP | High |
| RC.RP-02 | Recovery strategy updated post-incident | Not performed | 1 | No lessons-learned process | Medium |
| RC.CO-03 | Recovery communicated to stakeholders | Not formalized | 1 | No communications plan for incidents | Medium |

**Function Score: 1.3 / 4** — Recovery capability limited to IT systems; no holistic BCP.

**Remediation Actions:**
- Develop a full Business Continuity Plan (BCP) with RTOs and RPOs
- Establish a post-incident lessons-learned process
- Test backups and recovery procedures quarterly

---

## Overall Maturity Summary

| Function | Score | Tier |
|---|---|---|
| Govern (GV) | 1.5 | Partial |
| Identify (ID) | 1.6 | Partial → Risk-Informed |
| Protect (PR) | 2.4 | Risk-Informed |
| Detect (DE) | 1.2 | **Partial (Critical)** |
| Respond (RS) | 1.5 | Partial |
| Recover (RC) | 1.3 | Partial |
| **Overall** | **1.8** | **Partial** |

---

## Remediation Roadmap

### Immediate (0–30 days)
- [ ] Enforce MFA for all privileged accounts
- [ ] Enable full-disk encryption on unencrypted endpoints
- [ ] Begin SIEM evaluation and procurement
- [ ] Schedule tabletop exercise

### Short-Term (30–90 days)
- [ ] Complete hardware and software asset inventory
- [ ] Implement EDR solution
- [ ] Develop risk register with top 10 risks scored
- [ ] Conduct tabletop exercise

### Medium-Term (90–180 days)
- [ ] Deploy SIEM and establish log retention policy
- [ ] Draft and ratify Risk Management Policy
- [ ] Develop BCP with RTO/RPO targets
- [ ] Implement quarterly access reviews

### Long-Term (180–365 days)
- [ ] Establish formal security governance committee
- [ ] Apply CIS Benchmark hardening to all critical systems
- [ ] Build 3+ IR playbooks
- [ ] Achieve Tier 2 (Risk-Informed) across all functions

---

## Appendix: Assessment Methodology

This assessment was conducted using the following methods:
- Document review (policies, procedures, previous assessments)
- Stakeholder interviews (IT, HR, Finance, Legal)
- Technical observation (network scans, configuration reviews)
- Self-assessment questionnaires mapped to NIST CSF 2.0 subcategories

All findings reflect the state of controls at the time of assessment. This report is intended for internal use only and classified as **Confidential**.

---

*Framework Reference: NIST Cybersecurity Framework 2.0 (February 2024)*  
*https://www.nist.gov/cyberframework*

---

## Portfolio STAR Story — Team Collaboration in Practice

> **Industry:** Federal Civilian Agency | **Role:** GRC Analyst (embedded in a joint government-contractor assessment team)

### Situation
A mid-size federal civilian agency was preparing for its annual FISMA assessment and wanted to use NIST CSF 2.0 as an overlay to communicate its security posture to non-technical leadership. The agency had not conducted a formal gap analysis in three years. The IT security team had deep technical knowledge but limited experience translating findings into risk language that program managers and the agency CIO could act on. The assessment team included two federal employees, a contractor SME for technical controls, and me as the GRC analyst responsible for framework alignment and the written assessment report.

### Task
My responsibility was to lead the structured gap analysis across all six CSF functions, facilitate stakeholder interviews with IT leads and program offices, score the subcategories consistently, and produce the written findings in language appropriate for both a technical audience and executive leadership. I also needed to ensure the assessment methodology was defensible — documented clearly enough that the agency could repeat it the following year without contractor support.

### Action
I developed the scoring rubric and interview guide before the first stakeholder session and shared drafts with the federal team leads for review, incorporating their feedback before use. During subcategory interviews, I deferred all technical judgments to the contractor SME and federal IT staff — my role was to ask the right questions and document findings accurately, not to impose conclusions. When I saw that the Detect function scores were significantly lower than the team's informal impression suggested, I raised this in our internal debrief and we agreed to schedule a follow-up session with the SOC team rather than accepting the initial scores. The remediation roadmap was built collaboratively: I drafted a priority ranking, the technical SME validated feasibility and timelines, and the federal team leads confirmed alignment with budget cycles before the roadmap was finalized.

### Result
The assessment report was accepted by the agency CIO without revision requests — the first time the team had achieved that outcome on this contract. The executive summary was specifically called out as clear and actionable by the agency's Deputy CIO. The documented methodology was handed off to the agency's internal team and used verbatim for the following year's self-assessment. Two of the immediate remediation actions — MFA enforcement for privileged accounts and endpoint encryption — were funded in the next budget cycle, with the gap analysis cited as the justification in the budget request.
