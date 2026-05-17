# Data Classification Policy

**Document ID:** GRC-POL-003  
**Version:** 1.0  
**Classification:** Internal  
**Effective Date:** [Date]  
**Review Date:** [Date + 1 Year]  
**Owner:** Information Security Team  
**Approved By:** [CISO / IT Director]

---

## 1. Purpose

This policy establishes a framework for classifying organizational data based on its sensitivity and business value. Proper classification ensures that data receives appropriate protection commensurate with the harm its unauthorized disclosure, modification, or loss would cause.

---

## 2. Scope

This policy applies to all data created, collected, processed, stored, or transmitted by [Organization Name] and all individuals who handle that data, including employees, contractors, and third-party partners.

---

## 3. Data Classification Levels

### Level 1 — Public

**Definition:** Information intended for public disclosure or that poses no risk if released publicly.

**Examples:**
- Marketing materials, press releases
- Published website content
- Job postings

**Handling Requirements:**
- No special handling required
- May be freely shared internally and externally

---

### Level 2 — Internal

**Definition:** Information intended for internal use only. Unauthorized disclosure would cause minimal harm but is not appropriate for public release.

**Examples:**
- Internal memos and announcements
- Non-sensitive project documentation
- Organizational charts

**Handling Requirements:**
- Do not share externally without a business need
- Store on approved internal systems only
- No special encryption required for storage, but use secure channels for transmission

---

### Level 3 — Confidential

**Definition:** Sensitive business information that could cause significant harm to the organization or individuals if disclosed without authorization.

**Examples:**
- Financial statements and forecasts
- Business strategies and contracts
- Employee HR records
- Customer account information
- Vendor agreements

**Handling Requirements:**
- Access on a need-to-know basis only
- Encrypt at rest and in transit
- Do not store on personal devices or unapproved cloud services
- Shred physical documents when no longer needed
- Label documents clearly as "Confidential"

---

### Level 4 — Restricted

**Definition:** The most sensitive category. Unauthorized disclosure would cause severe harm, legal liability, regulatory penalties, or significant reputational damage.

**Examples:**
- Social Security Numbers, government IDs
- Payment card data (PCI DSS scope)
- Protected Health Information (HIPAA scope)
- Intellectual property and trade secrets
- Authentication credentials (passwords, keys, tokens)
- Legal matters under attorney-client privilege

**Handling Requirements:**
- Strict access controls — authorized users only, with logging
- Encrypt at rest and in transit using approved strong encryption
- Never transmit via unencrypted email or messaging
- Never store on personal devices, removable media, or unapproved services
- Physical copies locked in secured storage
- Dispose of using approved secure destruction methods
- Audit access logs regularly

---

## 4. Classification Responsibilities

| Role | Responsibility |
|---|---|
| **Data Owners** | Assign classification levels to data they are responsible for |
| **Data Custodians** | Apply handling controls consistent with classification |
| **All Employees** | Follow handling requirements for data they access or process |
| **Information Security** | Provide guidance, conduct audits, and update this policy |

**Data Owners** are typically department heads or system owners. When in doubt about classification, users should treat data as one level higher and consult the Information Security team.

---

## 5. Labeling Requirements

| Classification | Document Label | Email Subject Prefix |
|---|---|---|
| Public | (none required) | (none required) |
| Internal | `[INTERNAL]` | `[INTERNAL]` |
| Confidential | `[CONFIDENTIAL]` | `[CONFIDENTIAL]` |
| Restricted | `[RESTRICTED]` | `[RESTRICTED]` |

---

## 6. Data Handling Matrix

| Activity | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Share externally | ✅ Allowed | ⚠️ Approval needed | ❌ Prohibited | ❌ Prohibited |
| Store on personal device | ✅ | ⚠️ Avoid | ❌ | ❌ |
| Send via email (unencrypted) | ✅ | ✅ | ⚠️ Encrypt | ❌ |
| Store in approved cloud | ✅ | ✅ | ✅ | ⚠️ Approved only |
| Print physical copies | ✅ | ✅ | ⚠️ Secure storage | ⚠️ Locked storage |
| Retain after use | As needed | Per retention schedule | Per retention schedule | Per retention + legal hold |

---

## 7. Data Retention and Disposal

Data must be retained per [Organization Name]'s Data Retention Schedule and disposed of securely when no longer required:

- **Electronic data:** Cryptographic erasure or certified secure wipe
- **Physical documents:** Cross-cut shredding or certified destruction service
- **Removable media:** Physical destruction or certified degaussing

---

## 8. Violations

Mishandling data in violation of its classification level may result in disciplinary action, up to and including termination and legal action, depending on the severity and intent of the violation.

---

## 9. Review and Maintenance

This policy will be reviewed annually and updated as necessary to reflect changes in business operations, technology, or regulatory requirements.

---

## 10. Related Policies

- Acceptable Use Policy
- Information Security Policy
- Incident Response Policy
- Data Retention and Disposal Policy
- Third-Party Vendor Management Policy

---

*For questions about this policy, contact: security@[organization].com*
