# Risk Register Template

**Framework Alignment:** NIST SP 800-30 Rev. 1 / ISO/IEC 27005  
**Methodology:** Qualitative Risk Assessment (Likelihood × Impact)

---

## Overview

This risk register template is designed for use in small-to-medium organizations establishing or maturing their risk management program. It is aligned to NIST Special Publication 800-30 Rev. 1 (*Guide for Conducting Risk Assessments*) and ISO/IEC 27005 risk management principles.

---

## Scoring Methodology

### Likelihood Scale (1–5)

| Score | Rating | Description |
|---|---|---|
| 1 | Very Low | Unlikely to occur; no known history; strong controls |
| 2 | Low | Unlikely but possible; some historical incidents |
| 3 | Moderate | Reasonably likely; known threat actor interest |
| 4 | High | Likely to occur; frequently attempted |
| 5 | Very High | Near-certain; actively exploited in the wild |

### Impact Scale (1–5)

| Score | Rating | Description |
|---|---|---|
| 1 | Negligible | Minimal disruption; no data loss; no regulatory impact |
| 2 | Minor | Limited disruption; minor data exposure; low cost |
| 3 | Moderate | Significant disruption; sensitive data affected; regulatory notice |
| 4 | Major | Major operational impact; large data breach; regulatory fines |
| 5 | Catastrophic | Business-threatening; severe legal liability; reputational destruction |

### Risk Score = Likelihood × Impact

| Score Range | Risk Level | Recommended Action |
|---|---|---|
| 20–25 | **Critical** | Immediate action required; escalate to executive leadership |
| 12–19 | **High** | Address within 30–90 days; assign named owner |
| 6–11 | **Medium** | Address within 90–180 days; track in risk program |
| 1–5 | **Low** | Monitor and review annually; accept if within risk appetite |

---

## Risk Treatment Options

| Treatment | Description |
|---|---|
| **Mitigate** | Implement controls to reduce likelihood or impact |
| **Transfer** | Shift risk via insurance, contracts, or third parties |
| **Avoid** | Eliminate the activity or asset creating the risk |
| **Accept** | Document and accept the risk within defined risk appetite |

---

## Files

- `risk-register.csv` — Working risk register with 10 example risks scored
- `README.md` — This file (methodology and instructions)

---

## How to Use

1. Open `risk-register.csv` in Excel, Google Sheets, or any CSV viewer
2. Review existing example risks and customize for your organization
3. Score each risk using the Likelihood × Impact methodology above
4. Assign a Risk Owner for each identified risk
5. Document current controls and assess their effectiveness
6. Determine residual risk (risk remaining after controls)
7. Select a treatment option and assign a target remediation date
8. Review and update the register at least quarterly

---

## References

- NIST SP 800-30 Rev. 1: https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final
- ISO/IEC 27005:2022: https://www.iso.org/standard/80585.html
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
