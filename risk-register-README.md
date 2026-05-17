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

---

## Portfolio STAR Story — Team Collaboration in Practice

> **Industry:** Federal Health Agency (e.g., CMS / VA adjacent contractor) | **Role:** GRC Analyst (working with IT, Program Managers, and Risk Officers)

### Situation
A federal health IT contractor supporting a CMS-adjacent program had never maintained a formal risk register. Risk decisions were being made informally by IT leads and program managers without a documented process, scoring methodology, or executive visibility. When a new Program Security Officer joined, she found that several known high-severity risks — including an unpatched vulnerability on a public-facing portal handling beneficiary data — had been informally accepted with no documentation trail. This created significant exposure ahead of an upcoming ATO reauthorization.

### Task
I was assigned to build the organization's first formal risk register from scratch, working alongside the PSO, two IT leads, the Privacy Officer, and a program manager from the business side. My role was to design the scoring methodology, facilitate the initial risk identification sessions, and produce a register that the PSO could present to the Authorizing Official as part of the ATO package. I needed buy-in from IT leads who were skeptical of the process and a program manager who was worried that documenting risks would reflect poorly on her program.

### Action
Before building anything, I met individually with the IT leads and the program manager to understand their concerns. For the IT leads, I explained that the register would document what they already knew — getting it on paper actually protected them by showing awareness and a treatment plan. For the program manager, I reframed the register as evidence of mature risk governance rather than a list of failures. I designed the scoring methodology collaboratively — sharing draft likelihood and impact scales with the team for feedback before finalizing, so the scales reflected what "catastrophic" actually meant in their specific program context (beneficiary data exposure, CMS contract penalties). I facilitated two half-day risk identification workshops structured as open working sessions rather than interviews so the IT leads felt like co-authors, not subjects. Every risk treatment decision was made by the relevant risk owner, not by me.

### Result
The initial register captured 14 risks, including the previously undocumented unpatched portal vulnerability, which was formally accepted with a documented treatment plan and escalated to the Authorizing Official's attention. The ATO reauthorization was approved. The PSO reported that the Authorizing Official specifically noted the risk register as demonstrating program maturity. The two IT leads who had been most skeptical at the start became the register's most consistent updaters, submitting quarterly updates without prompting. The methodology document was included in the contractor's proposal library as a repeatable asset for future federal engagements.
