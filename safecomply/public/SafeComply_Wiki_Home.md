
# 🧭 Welcome to the SafeComply Wiki

This documentation will help you understand, install, and extend the **SafeComply** app – your all-in-one solution for tracking safety audits, incidents, and compliance.

---

## 📦 Modules

- ✅ Safety Audit Log
- ✅ Safety Incidents
- ✅ Corrective Actions
- ✅ Departmental Checklists
- ✅ Compliance Reports & Charts

---

## 🛠 Setup Steps

1. Clone the app repository into your bench:
   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/vinaymishraofficial/safecomply.git
   ```

2. Add to `apps.txt`:
   ```bash
   echo "safecomply" >> ../sites/apps.txt
   ```

3. Install on your site:
   ```bash
   bench --site yoursite.com install-app safecomply
   bench migrate
   ```

4. Visit the `/app/safecomply` workspace in your Frappe UI.

---

## 📊 Reports & Dashboards

- **Compliance Summary Report**
- **Audits Passed vs Failed**
- **Incident Count by Type**
- **Monthly Compliance %**

---

## 🔐 Roles & Permissions

- Safety Officer
- Auditor
- System Manager

---

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests.  
Your feedback and improvements are always welcome!

---

📄 Created by [Vinay Mishra](https://github.com/vinaymishraofficial)
