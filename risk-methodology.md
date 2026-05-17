# Risk Assessment Methodology
**Author:** Anél Henning | GRC Analyst Portfolio  
**Framework Reference:** NIST SP 800-37 (Risk Management Framework) · NIST SP 800-30  
**Version:** 1.0 | May 2026

---

## 1. Purpose

This document describes the methodology used to identify, assess, score, and prioritize risks in the accompanying risk register. It is designed to align with NIST SP 800-30 (Guide for Conducting Risk Assessments) and supports an organization's overall Risk Management Framework (RMF) implementation.

---

## 2. Risk Identification

Risks are identified through:
- **Asset inventory review** — identifying information systems, data stores, and critical processes
- **Threat intelligence** — referencing MITRE ATT&CK, CISA advisories, and industry threat reports
- **Vulnerability scanning results** — CVEs, misconfigurations, and patch gaps
- **Control gap analysis** — comparing current controls against NIST CSF or ISO 27001 baselines
- **Stakeholder interviews** — business owners, IT, legal, and operations

Each identified risk is assigned a unique Risk ID, an owner, and a category (Strategic, Operational, Compliance, Technology, Third-Party).

---

## 3. Risk Scoring

Risks are scored using a **5×5 likelihood × impact matrix** producing a composite Risk Score (1–25).

### 3.1 Likelihood Scale

| Score | Rating | Description |
|---|---|---|
| 1 | Rare | <5% probability in the next 12 months |
| 2 | Unlikely | 5–20% probability |
| 3 | Possible | 21–50% probability |
| 4 | Likely | 51–80% probability |
| 5 | Almost Certain | >80% probability |

### 3.2 Impact Scale

| Score | Rating | Description |
|---|---|---|
| 1 | Negligible | Minimal disruption; no regulatory impact |
| 2 | Minor | Limited impact; recoverable within 24 hours |
| 3 | Moderate | Significant operational disruption or data exposure |
| 4 | Major | Material financial loss, regulatory breach, or reputational damage |
| 5 | Critical | Business-threatening; potential loss of license or major litigation |

### 3.3 Risk Score Calculation

```
Risk Score = Likelihood × Impact
```

### 3.4 Risk Rating

| Score Range | Rating | Action Required |
|---|---|---|
| 20–25 | 🔴 Critical | Immediate escalation to executive leadership; treatment plan within 30 days |
| 15–19 | 🟠 High | Risk owner must develop treatment plan within 60 days |
| 8–14 | 🟡 Medium | Monitor; include in quarterly risk review |
| 1–7 | 🟢 Low | Accept or monitor; review annually |

---

## 4. Risk Treatment Options

Each risk is assigned one of four treatment strategies:

| Strategy | Description |
|---|---|
| **Mitigate** | Implement controls to reduce likelihood or impact |
| **Transfer** | Shift risk via insurance, contracts, or third-party agreements |
| **Accept** | Formally acknowledge and accept the residual risk (requires sign-off) |
| **Avoid** | Eliminate the activity or asset that introduces the risk |

---

## 5. Residual Risk

After treatment controls are applied, a **residual risk score** is calculated using the same likelihood × impact method against the post-control environment. Residual risks rated Medium or above require ongoing monitoring and quarterly review.

---

## 6. Risk Register Maintenance

- **Frequency:** Reviewed quarterly; updated following incidents, audits, or significant changes
- **Owner:** GRC Analyst / Risk Manager
- **Escalation:** Critical and High risks reported to CISO/executive leadership monthly
- **Retention:** Risk register maintained for 3 years minimum per compliance requirements

---

## 7. References

- NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments
- NIST SP 800-37 Rev. 2 — Risk Management Framework
- NIST Cybersecurity Framework 2.0
- ISO/IEC 27005:2022 — Information Security Risk Management
- MITRE ATT&CK Framework v14
