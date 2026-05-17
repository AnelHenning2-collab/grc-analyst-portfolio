# Security Awareness Training Guide
## Protecting Yourself and [Organization Name] from Cyber Threats

**Audience:** All Employees  
**Estimated Time:** 30–45 minutes  
**Review Frequency:** Annual (or after major incidents)  
**Owner:** Information Security Team

---

## Welcome

Cybersecurity is everyone's responsibility — not just IT's. Attackers frequently target employees directly because it's often easier to trick a person than to hack a system. This training will help you recognize threats, respond correctly, and protect yourself and the organization.

---

## Module 1: Phishing — The #1 Threat

### What Is Phishing?

Phishing is a cyberattack where criminals send fraudulent messages — usually emails — that appear to come from a trusted source (your bank, your company, a colleague, or a vendor) to trick you into:
- Clicking a malicious link
- Downloading malware
- Entering your username and password
- Transferring money or sharing sensitive data

**By the numbers:**
- 91% of cyberattacks begin with a phishing email
- The average cost of a phishing attack on a mid-sized company is $1.6 million
- Attackers craft emails in under 5 minutes using AI tools

---

### Types of Phishing

| Type | Description | Example |
|---|---|---|
| **Phishing** | Mass emails sent to thousands of people | "Your account will be suspended — click here" |
| **Spear Phishing** | Targeted email using personal details | "Hi [Your Name], please review the attached invoice" |
| **Whaling** | Targeting executives (CEO, CFO) | Fake board communication or legal notice |
| **Smishing** | Phishing via SMS/text message | "Your package is delayed — verify your address" |
| **Vishing** | Phishing via phone call | Fake IT support asking for your password |
| **Business Email Compromise (BEC)** | Impersonating an executive to authorize wire transfers | "I need you to process this payment urgently — CEO" |

---

### How to Spot a Phishing Email

Look for these red flags:

**Sender Address**
- ✅ Legitimate: `support@microsoft.com`
- ❌ Suspicious: `support@micros0ft-help.com` or `noreply@microsoft.support-portal.net`
- Always hover over the sender name to see the actual email address

**Urgency and Pressure**
- "Act now or your account will be deleted"
- "You have 24 hours to respond"
- "Don't tell anyone — this is confidential"

**Generic Greetings**
- "Dear Customer" or "Dear User" instead of your actual name

**Suspicious Links**
- Hover over links before clicking — the URL shown should match the expected domain
- Short URLs (bit.ly, tinyurl) are often used to hide malicious destinations

**Unexpected Attachments**
- Unexpected Word docs, Excel files, or ZIP archives (even from known contacts)
- Files named things like `Invoice_2024.exe` or `Urgent_Review.docm`

**Requests for Sensitive Info**
- Legitimate companies never ask for passwords, SSNs, or credit cards via email
- IT will never email you asking for your password

---

### What to Do If You Suspect a Phishing Email

1. **Do NOT click any links or open attachments**
2. **Do NOT reply to the email**
3. **Report it** using the phishing report button in your email client, or forward to: `security@[organization].com`
4. **Delete the email** after reporting
5. If you already clicked — **report it immediately** and disconnect your device from the network. You will not be in trouble for reporting quickly.

---

## Module 2: Password Security

### Why Passwords Matter

Credentials are the keys to your organization's data. Attackers use:
- **Brute force:** Trying millions of passwords automatically
- **Credential stuffing:** Using passwords leaked from other breaches
- **Password spraying:** Trying common passwords against many accounts

### Creating Strong Passwords

| Weak | Strong |
|---|---|
| `password123` | `correct-horse-battery-staple` |
| `Summer2024!` | `J9#mP2@xQ7!rLvKn` |
| `[YourName]2024` | Use a password manager to generate |

**Rules:**
- Minimum 12 characters (16+ is better)
- Mix of uppercase, lowercase, numbers, and symbols
- Never reuse passwords across accounts
- Never use personal info (birthdate, pet name, address)

### Use a Password Manager

A password manager securely stores all your passwords so you only need to remember one master password. Approved options may include:
- 1Password
- Bitwarden (open source)
- LastPass
- KeePass

Ask IT for the organization's approved password manager.

### Multi-Factor Authentication (MFA)

MFA requires a second verification step beyond your password. Even if an attacker steals your password, they cannot log in without the second factor.

**MFA methods (most to least secure):**
1. **Hardware key** (YubiKey) — Most secure
2. **Authenticator app** (Google Authenticator, Microsoft Authenticator) — Recommended
3. **SMS/Text code** — Better than nothing, but SIM-swapping is a risk
4. **Email code** — Weakest form of MFA

**Enable MFA on every account that supports it — especially:**
- Work email and Microsoft 365 / Google Workspace
- VPN and remote access
- Cloud services (AWS, Azure, Salesforce)
- Financial accounts

---

## Module 3: Social Engineering

Social engineering is manipulating people into giving up information or access — no malware required.

### Common Tactics

**Pretexting**
An attacker creates a believable false scenario.
> *"Hi, this is Mike from IT. We're running an urgent security update on your machine. I'll need your login credentials to push the patch remotely."*

**Impersonation**
Pretending to be someone you trust — a colleague, IT staff, a vendor, or even your manager.

**Tailgating / Piggybacking**
Following an employee through a secure door without badging in by acting like they belong.

**Quid Pro Quo**
Offering something (fake tech support, prizes) in exchange for information.

---

### How to Defend Against Social Engineering

- **Verify identities** — If someone calls claiming to be IT, hang up and call IT using the number in the company directory
- **Never share credentials** — No legitimate IT staff member will ever ask for your password
- **When in doubt, slow down** — Urgency is a manipulation tactic; take time to verify
- **Badge in separately** — Never allow someone to tailgating behind you through a secure door, even if they look familiar
- **Report suspicious interactions** — If something feels off, report it to security

---

## Module 4: Safe Internet and Device Use

### Browsing Safety

- Only use company-approved browsers with security extensions enabled
- Don't install unauthorized browser extensions or plugins
- Avoid entering work credentials on personal or unfamiliar devices
- Do not download software from unofficial or pirated sources

### Public Wi-Fi

Public Wi-Fi (coffee shops, airports, hotels) is inherently insecure.

**Always:**
- Connect through the company VPN when on public Wi-Fi
- Avoid accessing sensitive systems (banking, HR, email) without VPN

**Never:**
- Conduct sensitive work on open public Wi-Fi without a VPN

### Removable Media (USB Drives)

**Never plug in a USB drive you didn't purchase yourself.**

Attackers commonly leave infected USB drives in parking lots or common areas hoping someone will plug them in ("USB drop attacks").

If you find a USB drive, hand it to IT — do not plug it in to "see what's on it."

---

## Module 5: Reporting and Incident Response

### The Golden Rule: Report Fast

If you think you've fallen for a phishing email, clicked a bad link, or noticed anything suspicious — **report it immediately.**

- **You will not get in trouble for reporting.** You may get in trouble for hiding it.
- The faster a security team responds, the less damage an attacker can do.
- Many breaches take months to discover because employees were afraid to report.

### How to Report

| Situation | How to Report |
|---|---|
| Suspicious email | Report button in email client or `security@[org].com` |
| Clicked a bad link | Call IT immediately: [Phone] |
| Saw something unusual on your computer | Call IT immediately: [Phone] |
| Someone asked for your password | Report to IT and your manager |
| Physical security concern | Report to Facilities or your manager |

---

## Module 6: Compliance and Your Responsibilities

By completing this training, you acknowledge that you understand and will comply with:

- **Acceptable Use Policy (AUP)** — Governs appropriate use of company systems
- **Data Classification Policy** — How to handle different types of data
- **Password Policy** — Requirements for password strength and MFA
- **Incident Response Policy** — Your obligation to report security incidents promptly

Violations of these policies may result in disciplinary action.

---

## Knowledge Check

Answer these questions to confirm your understanding:

1. You receive an email from your CEO asking you to urgently wire $15,000 to a new vendor. The sender address is `ceo@[yourcompany].biz`. What should you do?

2. A colleague who you don't recognize holds the secure door open for you and waves you through. What should you do?

3. You receive a pop-up saying your computer is infected and you should call a phone number immediately. What should you do?

4. IT sends you an email asking you to confirm your password to prevent your account from being suspended. What should you do?

**Answers:**
1. Do NOT transfer. Verify directly with your CEO via phone or in person. This is a Business Email Compromise (BEC) red flag — wrong domain.
2. Politely decline, badge in separately, and report the tailgating attempt to security.
3. Do NOT call the number. This is a fake alert (scareware). Close the pop-up and report to IT.
4. Do NOT provide your password. Legitimate IT will never ask for your password. Report the email.

---

## Summary: Your Security Checklist

- [ ] Enable MFA on all work accounts
- [ ] Use a password manager with unique passwords for every account
- [ ] Report suspicious emails using the phishing report button
- [ ] Connect through VPN on public Wi-Fi
- [ ] Never share credentials with anyone, including IT
- [ ] Lock your screen when stepping away from your desk
- [ ] Report security incidents immediately — no judgment

---

*Questions? Contact the Information Security Team at: security@[organization].com*  
*Training completion must be recorded in [LMS / HR System] by [Due Date].*
