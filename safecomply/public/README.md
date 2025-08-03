
# 🛡️ SafeComply – Safety Compliance Tracking App

**SafeComply** is a Frappe-based app designed to help organizations track and manage safety audits, incidents, and compliance processes with structured dashboards, detailed reports, and guided onboarding.

![SafeComply Logo](https://raw.githubusercontent.com/vinaymishraofficial/safecomply/main/public/logo.png)

---

## 🚀 Features

- 📝 Log safety incidents and audits
- ✅ Manage corrective actions and checklists
- 📊 Charts: Audit Results, Compliance %, Incident Types
- 📋 Compliance Summary Reports
- 📦 Dashboard with cards & shortcuts
- 🧭 Onboarding for new users
- 🔐 Role-based access (Safety Officer, Auditor, Manager)

---

## 🛠️ Installation

Follow these steps to install SafeComply into your Frappe bench:

```bash
# Go to your apps folder
cd ~/frappe-bench/apps

# Clone the repo
git clone https://github.com/vinaymishraofficial/safecomply.git

# Add to apps.txt
echo "safecomply" >> ../sites/apps.txt

# Install on site
bench --site yoursite.com install-app safecomply
bench migrate
```

Then login and visit the **SafeComply** workspace to get started.

---

## 🧰 Tech Stack

- [Frappe Framework](https://frappeframework.com/) v14+
- Python, MariaDB, Redis
- REST-ready (via Frappe)
- Full export via fixtures

---

## 📘 Documentation

📚 [**SafeComply Wiki**](https://github.com/vinaymishraofficial/safecomply/wiki)  
Includes setup guide, user flow, and module overview.

---

## 🖼️ App Structure

```txt
safecomply/
├── fixtures/           # Charts, Reports, Cards, Dashboard
├── public/             # Assets like logo.png
├── config/             # Workspace definition
├── safecomply/
│   └── safety_compliance_tracking_app/
│       └── doctype/    # Core doctypes
├── README.md
```

---

## 🙌 Developed By

Made with ❤️ by [Vinay Mishra](https://github.com/vinaymishraofficial)  
📍 [Alwar, Rajasthan, India](https://maps.google.com/?q=Alwar)

---

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) file for details.
