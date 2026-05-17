# Incident Response Policy (IRP)
**Document Owner:** GRC / Information Security  
**Version:** 1.0  
**Effective Date:** May 2026  
**Review Cycle:** Annual (or post-incident)  
**Classification:** Internal — Restricted

---

## 1. Purpose

This Incident Response Policy establishes the organization's framework for detecting, reporting, classifying, responding to, and recovering from cybersecurity incidents. It ensures a coordinated, consistent, and documented response that minimizes harm, preserves evidence, and satisfies regulatory notification obligations.

---

## 2. Scope

This policy applies to all cybersecurity incidents affecting:
- Organizational information systems, networks, and endpoints
- Cloud-hosted environments and SaaS platforms
- Third-party systems that store, process, or transmit organizational data
- All employees, contractors, and vendors with access to organizational systems

---

## 3. Definitions

| Term | Definition |
|---|---|
| **Security Event** | Any observable occurrence on a system or network (not necessarily harmful) |
| **Security Incident** | A security event that compromises or threatens the confidentiality, integrity, or availability of organizational assets |
| **Breach** | Confirmed unauthorized access to or disclosure of sensitive or regulated data |
| **Incident Response Team (IRT)** | Cross-functional team responsible for managing security incidents |
| **RTO** | Recovery Time Objective — maximum acceptable downtime before restoration |
| **RPO** | Recovery Point Objective — maximum acceptable data loss measured in time |

---

## 4. Incident Classification

### Severity Levels

| Severity | Criteria | Response SLA |
|---|---|---|
| **P1 — Critical** | Active breach; ransomware; critical system unavailable; confirmed data exfiltration | Immediate — IRT activated within 1 hour |
| **P2 — High** | Suspected breach; unauthorized privileged access; malware detected; significant data exposure risk | IRT notified within 4 hours |
| **P3 — Medium** | Policy violation; failed access attempts; isolated malware; phishing click | IT Security response within 24 hours |
| **P4 — Low** | Suspicious activity; unusual login; minor policy breach | Logged and reviewed within 72 hours |

---

## 5. Roles and Responsibilities (RACI)

| Role | Responsibility |
|---|---|
| **CISO** | Executive authority; approves P1/P2 communications; engages legal and PR |
| **Incident Commander** | Leads IRT; coordinates response activities; owns incident timeline |
| **IT Security Analyst** | Technical investigation; containment and eradication; evidence preservation |
| **GRC Analyst** | Regulatory notification assessment; documentation; lessons learned |
| **Legal Counsel** | Legal hold; attorney-client privilege; regulatory counsel |
| **Communications / PR** | External communications; customer notifications (as directed by legal) |
| **All Employees** | Report suspected incidents immediately; cooperate with investigation |

---

## 6. Incident Response Lifecycle

### Phase 1 — Preparation
- Maintain and test this IRP annually via tabletop exercise
- Ensure IRT contact list is current and accessible offline
- Maintain forensic tools, backup systems, and recovery resources in a ready state
- Train all employees on incident identification and reporting procedures

### Phase 2 — Detection & Reporting
- **Employees** who suspect an incident must report immediately via:
  - IT Security Helpdesk: [security@organization.com] / [phone number]
  - Emergency escalation: [CISO direct contact]
- **Automated alerts** from SIEM, EDR, or monitoring tools are triaged by IT Security within 15 minutes of receipt during business hours; 1 hour outside business hours
- All reports are logged in the incident tracking system with a timestamp

### Phase 3 — Analysis & Classification
- IT Security performs initial triage to confirm whether a security event constitutes an incident
- Incident is classified by severity (P1–P4) within 2 hours of detection
- Scope is assessed: systems affected, data exposed, ongoing threat activity
- Evidence is preserved: system images, logs, memory captures (as appropriate)

### Phase 4 — Containment
**Short-term containment (immediate):**
- Isolate affected systems from the network to prevent lateral movement
- Disable compromised accounts
- Block malicious IPs or domains at the firewall

**Long-term containment (hours to days):**
- Apply emergency patches or configuration changes
- Implement compensating controls while root cause is addressed
- Maintain business continuity through backup systems where possible

### Phase 5 — Eradication
- Identify and remove the root cause (malware, unauthorized access, misconfiguration)
- Validate that all affected systems are clean before restoration
- Patch vulnerabilities exploited during the incident
- Reset credentials for all affected accounts

### Phase 6 — Recovery
- Restore systems from verified clean backups
- Validate system integrity and functionality before returning to production
- Monitor restored systems closely for 30 days post-recovery
- Confirm RTO and RPO obligations are met

### Phase 7 — Post-Incident Review (Lessons Learned)
- Conduct post-incident review within **5 business days** of incident closure
- Document: timeline, root cause, detection gap, response effectiveness, corrective actions
- Update IRP, playbooks, and controls based on lessons learned
- Report findings to CISO and risk register

---

## 7. Regulatory Notification Requirements

| Regulation | Notification Trigger | Deadline |
|---|---|---|
| **GDPR** | Personal data of EU residents breached | 72 hours to supervisory authority; without undue delay to individuals |
| **HIPAA** | PHI breach affecting ≥500 individuals | 60 days to HHS; without unreasonable delay to individuals |
| **State Breach Laws (e.g., FL § 501.171)** | FL residents' PI breached | 30 days to individuals; 30 days to AG if ≥500 FL residents |
| **PCI DSS** | Cardholder data compromised | Immediately to card brands and acquiring bank |

*Note: Notification obligations must be assessed by legal counsel for each incident.*

---

## 8. Evidence Preservation and Chain of Custody

- All digital evidence must be collected using forensically sound methods
- Chain of custody documentation is required for any evidence that may be used in legal proceedings
- Evidence is retained for a minimum of **3 years** or as directed by legal counsel
- No affected systems should be powered off, wiped, or rebuilt before forensic imaging is authorized

---

## 9. Communication Guidelines

- **Internal communications** during an active incident should use out-of-band channels (phone, Signal) if email systems may be compromised
- **External communications** (press, customers, regulators) require CISO and legal approval before release
- Employees must not discuss incident details publicly, on social media, or with unauthorized parties

---

## 10. Related Documents

- Acceptable Use Policy
- Business Continuity Plan
- Disaster Recovery Plan
- Data Classification Policy
- Vendor Risk Management Policy

---

## 11. Policy Review and Approval

| Role | Name | Date |
|---|---|---|
| Author | GRC Analyst | May 2026 |
| Reviewer | IT Security Manager | |
| Approver | CISO | |

---

**Document Control:** This is a sample policy created for portfolio demonstration purposes. Review with legal counsel and adapt to your regulatory environment before implementation.
