# 🛡️ Web Application Penetration Testing Report

**Target:** VulnFlask (Local Test Application)
**Tester:** Hari Ragavendiran R
**Environment:** Localhost (127.0.0.1)
**Testing Type:** Educational / Self-Hosted Application
**Authorization:** Fully Authorized (Self-developed application)

---

## 1️⃣ Executive Summary

This report documents a **manual web application security assessment** performed on a self-developed Flask-based web application named **VulnFlask**.
The purpose of this assessment was to **simulate real-world web pentesting scenarios**, understand how common vulnerabilities arise during development, and practice exploitation using professional tools and methodologies.

The application was intentionally designed with security flaws to study vulnerabilities from both **attacker and developer perspectives**.

---
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 01-24-47" src="https://github.com/user-attachments/assets/fca5897e-358b-4f11-9219-4398497f9c61" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 01-25-33" src="https://github.com/user-attachments/assets/b35592ee-c3d6-447a-8365-388ecdde580c" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 01-25-58" src="https://github.com/user-attachments/assets/f5268735-a8c4-4bbe-987c-14a2be52823e" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 13-06-10" src="https://github.com/user-attachments/assets/789ed09f-a6bb-41b5-a924-68a901df32ba" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 13-07-30" src="https://github.com/user-attachments/assets/332e4884-ba6e-47b2-adf9-055613eedd38" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 13-07-42" src="https://github.com/user-attachments/assets/f612f153-5577-45e9-af69-2996c8b8b674" />
<img width="1920" height="1080" alt="Screenshot at 2026-01-07 13-07-55" src="https://github.com/user-attachments/assets/3423037a-1bdb-4c88-96ef-a7452ca5c465" />


## 2️⃣ Scope of Testing

### ✅ In Scope

* Web application hosted on `http://127.0.0.1:5000`
* Login functionality
* User profile endpoint
* Search functionality
* Application database interactions

### ❌ Out of Scope

* Network infrastructure
* Host operating system
* Denial-of-Service testing

---

## 3️⃣ Tools & Methodology

### 🧰 Tools Used

* Burp Suite (Proxy, Repeater)
* Web Browser
* SQLmap (Controlled, local testing)
* SQLite3
* Flask (Python)

---

### 🧭 Methodology Followed

1. Application mapping
2. Input identification
3. Manual vulnerability testing
4. Exploitation validation
5. Impact analysis
6. Documentation

This methodology aligns with **OWASP Web Security Testing Guide (WSTG)** principles.

---

## 4️⃣ Findings Summary

| ID    | Vulnerability                           | Severity |
| ----- | --------------------------------------- | -------- |
| VF-01 | SQL Injection (Authentication Bypass)   | High     |
| VF-02 | Insecure Direct Object Reference (IDOR) | High     |
| VF-03 | Reflected Cross-Site Scripting (XSS)    | Medium   |

---

## 5️⃣ Detailed Findings

---

### 🔴 VF-01: SQL Injection – Authentication Bypass

**Severity:** High
**OWASP Category:** A03 – Injection

#### Description

The login functionality constructs SQL queries using unsanitized user input, allowing an attacker to manipulate the query logic.

#### Vulnerable Code

```python
query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
```

#### Proof of Concept

Login request with payload:

```
Username: ' OR '1'='1
Password: anything
```

#### Impact

* Authentication bypass
* Unauthorized access to application
* Potential database compromise

#### Recommendation

* Use parameterized queries (prepared statements)
* Avoid string concatenation in SQL queries

---

### 🔴 VF-02: Insecure Direct Object Reference (IDOR)

**Severity:** High
**OWASP Category:** A01 – Broken Access Control

#### Description

The application exposes user profile data based solely on a user-controlled `id` parameter without authorization checks.

#### Vulnerable Endpoint

```
GET /profile?id=1
```

#### Proof of Concept

Changing the parameter:

```
/profile?id=2
```

#### Impact

* Unauthorized access to other users’ data
* Privacy violations
* Potential data leakage

#### Recommendation

* Implement authorization checks
* Validate user ownership of resources

---

### 🟠 VF-03: Reflected Cross-Site Scripting (XSS)

**Severity:** Medium
**OWASP Category:** A07 – Cross-Site Scripting

#### Description

User input is reflected directly into the HTML response without encoding or sanitization.

#### Vulnerable Endpoint

```
GET /search?q=<script>alert(1)</script>
```

#### Impact

* Execution of arbitrary JavaScript
* Session hijacking (in real-world scenarios)
* Client-side attacks

#### Recommendation

* Encode output
* Use templating with auto-escaping
* Validate and sanitize user input

---

## 6️⃣ Risk Assessment

| Risk Area            | Impact |
| -------------------- | ------ |
| Authentication       | High   |
| Authorization        | High   |
| Client-Side Security | Medium |

The vulnerabilities identified demonstrate **critical weaknesses in core security controls**.

---

## 7️⃣ Conclusion

This assessment successfully demonstrated how common web application vulnerabilities can be introduced during development when secure coding practices are not followed.
The exercise improved understanding of:

* How SQL Injection, IDOR, and XSS vulnerabilities arise
* How attackers exploit insecure logic
* How to document findings professionally

This project provided **hands-on, real-world pentesting experience** beyond lab environments.

---

## 8️⃣ Disclaimer

This application was developed and tested **solely for educational purposes** in a controlled environment.
No real user data or external systems were involved.

---

## 9️⃣ Author

**Hari Ragavendiran R**
Junior Web Application Pentester (Aspiring)
Skills: Web Pentesting, OWASP Top 10, Burp Suite, Secure Coding Awareness
Date: 07/01/2026

---

