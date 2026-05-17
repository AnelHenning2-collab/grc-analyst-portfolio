# Access Control Policy (ACP)
**Document Owner:** GRC / Information Security  
**Version:** 1.0  
**Effective Date:** May 2026  
**Review Cycle:** Annual  
**Classification:** Internal

---

## 1. Purpose

This Access Control Policy establishes requirements for managing logical access to organizational information systems, applications, and data. It ensures that access is granted based on business need, consistently reviewed, and promptly removed when no longer required — supporting the principle of least privilege and alignment with NIST CSF PR.AA and ISO 27001 Annex A.5.15.

---

## 2. Scope

This policy applies to all:
- Information systems, applications, and databases owned or operated by the organization
- Cloud environments, SaaS platforms, and third-party systems hosting organizational data
- All users including employees, contractors, vendors, and service accounts

---

## 3. Guiding Principles

| Principle | Description |
|---|---|
| **Least Privilege** | Users are granted the minimum access required to perform their job function — no more |
| **Need to Know** | Access to sensitive data is restricted to those with a documented business requirement |
| **Separation of Duties** | No single individual should have end-to-end control over a critical process without oversight |
| **Default Deny** | Access is denied by default; explicit approval is required before access is provisioned |
| **Accountability** | All access is tied to a uniquely identified individual account; shared accounts are prohibited |

---

## 4. Access Request and Provisioning

### 4.1 New Access Requests
- All access requests must be submitted through the IT ticketing system
- Requests must include: user name, role, systems requested, business justification, and manager approval
- IT Security reviews requests against this policy before provisioning
- Access is provisioned within **3 business days** of approved request

### 4.2 Role-Based Access Control (RBAC)
- Access is assigned based on defined job roles, not individual negotiation
- Role definitions and associated permissions are maintained by IT Security and reviewed annually
- Users must not receive access outside their assigned role without written exception approval

### 4.3 Privileged Access
- Privileged (administrative) accounts are subject to enhanced controls:
  - Separate privileged account distinct from standard user account
  - Multi-factor authentication (MFA) mandatory — no exceptions
  - All privileged session activity is logged and retained for 12 months
  - Privileged accounts are reviewed quarterly by IT Security and GRC

---

## 5. Access Reviews (Access Certification)

| Review Type | Frequency | Owner |
|---|---|---|
| Standard user access review | Semi-annual (June, December) | IT Security + Manager |
| Privileged access review | Quarterly | IT Security + CISO |
| Vendor / third-party access review | Quarterly | IT Security |
| Dormant account review | Monthly | IT (automated) |

- Managers must certify that each of their direct reports requires the access assigned
- Revocations identified during review must be completed within **5 business days**
- Evidence of access reviews is retained for audit purposes (minimum 3 years)

---

## 6. Offboarding and Access Termination

### 6.1 Voluntary Resignation or Planned Departure
- HR notifies IT Security at least **5 business days** before last day
- All access is disabled on the employee's last working day, no later than close of business

### 6.2 Involuntary Termination
- HR notifies IT Security **immediately** prior to or concurrent with the termination meeting
- All access is disabled **before or during** the termination meeting — not after
- Physical access badges and credentials are collected on the day of termination

### 6.3 Contractor or Vendor Offboarding
- Contract end dates are tracked by Procurement and IT Security
- Access is disabled on or before the contract end date
- Accounts without confirmed end dates are reviewed quarterly

### 6.4 Dormant Accounts
- Accounts with no login activity for **90 days** are flagged for review
- After manager confirmation, dormant accounts are disabled; accounts inactive for **180 days** are deleted

---

## 7. Multi-Factor Authentication (MFA)

MFA is **mandatory** for:
- All remote access (VPN, remote desktop)
- All cloud platform access (Microsoft 365, AWS, Azure, GCP, etc.)
- All privileged and administrative accounts
- Any system storing or processing sensitive or regulated data

MFA is **strongly recommended** for all other systems where technically feasible.

---

## 8. Shared and Service Accounts

- Shared accounts are prohibited for human users. Individual accounts must be used.
- Service accounts (non-human) must be:
  - Named and documented in the service account register
  - Assigned to a named human owner responsible for the account
  - Subject to the same access review cycle as standard accounts
  - Granted the minimum permissions required for the service function

---

## 9. Remote and Third-Party Access

- All remote access must use organizational VPN with MFA
- Third-party vendor access must be:
  - Formally requested and approved prior to provisioning
  - Time-limited to the duration of the engagement
  - Monitored and logged for the duration of access
  - Reviewed quarterly regardless of contract status

---

## 10. Exceptions

Exceptions to this policy (e.g., temporary elevated access) must be:
- Requested in writing with business justification
- Approved by IT Security Manager and CISO
- Time-limited with a defined expiration date
- Documented and reviewed at expiration

---

## 11. Policy Violations

Violations of this policy — including granting unauthorized access, sharing credentials, or failing to complete access reviews — may result in disciplinary action up to and including termination and legal action.

---

## 12. Compliance Mapping

| Requirement | Framework Reference |
|---|---|
| Least privilege | NIST CSF PR.AA-05; ISO 27001 A.5.15; SOC 2 CC6.3 |
| MFA enforcement | NIST CSF PR.AA-03; ISO 27001 A.8.5; SOC 2 CC6.1 |
| Access reviews | NIST CSF PR.AA-05; ISO 27001 A.5.18; SOC 2 CC6.2 |
| Offboarding | NIST CSF PR.AA-05; ISO 27001 A.5.18; SOC 2 CC6.2 |
| Privileged access | NIST CSF PR.AA-05; ISO 27001 A.8.2; SOC 2 CC6.1 |

---

## 13. Related Documents

- Acceptable Use Policy
- Incident Response Policy
- Data Classification Policy
- Vendor Risk Management Policy

---

## 14. Policy Review and Approval

| Role | Name | Date |
|---|---|---|
| Author | GRC Analyst | May 2026 |
| Reviewer | IT Security Manager | |
| Approver | CISO | |

---

**Document Control:** Sample policy for portfolio demonstration. Adapt to your organization's regulatory environment and review with legal counsel before implementation.
