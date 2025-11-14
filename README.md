# 🔥 Blind XSS Training Lab — Realistic Admin Bot + OOB Exploitation

A fully-featured, realistic **Blind XSS training environment** designed for bug bounty hunters, pentesters, and security enthusiasts.  

This lab simulates a real SaaS admin panel where attacker-supplied payloads are **stored**, later **reviewed by an admin**, and executed **in the background** using a headless browser — just like real blind XSS bugs seen in the wild.

---

## 🏴 Blind XSS Challenge — Steal the Admin Flag

Your mission is to exploit a blind stored XSS vulnerability in this lab and use it to steal a secret flag that only the admin bot can access.
🎯 Objective

Gain access to the protected endpoint:

/secret

This page contains the main challenge flag, but:

Normal users cannot view it

Only the admin bot has the required session cookie

The bot loads untrusted user submissions automatically

You must execute JavaScript inside the admin’s browser context

Your goal:

Trigger a blind XSS payload that runs inside the admin bot and exfiltrates the flag from /secret.


---

## 🚀 Features

### ✔ Fully Isolated Blind XSS Environment
You submit **raw payloads**, not URLs.  
The server stores them silently, and only the admin bot loads them.

### ✔ Realistic Admin Bot (Headless Chromium)
The bot automatically:
- Logs in using a **real admin cookie**
- Visits stored payloads in a vulnerable review page
- Executes JavaScript like a real browser user
- Triggers your OOB callbacks instantly

### ✔ No Manual Reflection Needed
Just submit the payload.  
The admin bot wraps it in a review page and executes it.  
This mirrors real SaaS “admin reviews” that trigger blind XSS.

### ✔ Perfect for OOB XSS Testing
Works seamlessly with:
- **Burp Collaborator**
- **Interactsh**
- **Cloudflare Worker-based callback collectors**
- **Custom OOB dashboards**

### ✔ One-Command Setup
Includes `setup.sh` to automatically install:
- Chromium
- Chromedriver
- Virtual environment
- All dependencies

Just clone and run.

---

## 📦 Installation

```bash
./setup.sh
source venv/bin/activate
python3 app.py
---
## Usage:
Visit http://127.0.0.1:5000 and submit a payload by using my OOB XSS payload creator and listener (completely free so I'd really appreciate a sub on yt for this one):
OOB XSS listener and payload generator: https://aged-cloud-b431.0days.workers.dev/
My YouTube: https://youtube.com/@0dayscyber
---

## 🛡 Safety Disclaimer

This project is **intentionally vulnerable** and meant strictly for **educational, research, and training purposes**.  
Do **NOT** deploy publicly, expose on the internet, or use outside controlled environments.

---

## ❤️ For Bug Bounty Hunters

This lab helps hunters understand:

- Why blind XSS often fires **hours or days** after submission  
- How admin dashboards inadvertently trigger stored XSS  
- Crafting stealthy payloads for **OOB (Out-of-Band) XSS**  
- Debugging silent / external callback failures  
- Real-world exploitation paths

Perfect for training before hunting on:

- SaaS dashboards  
- Moderation panels  
- Internal admin systems  
- Customer support backends  
- Content review workflows

