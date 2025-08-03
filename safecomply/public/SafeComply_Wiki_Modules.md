
# 🧩 SafeComply Modules Overview

Here’s a breakdown of each module included in the SafeComply application to help you understand the workflow and data relationships.

---

## 📝 1. Safety Audit Log

Tracks audit records conducted within the organization.

- Linked to: Department, Auditor
- Contains: Checklist results, Audit Status (Pass/Fail)
- Can be submitted
- Used in compliance reports & dashboards

---

## 🚨 2. Safety Incidents

Logs any reported safety incidents across departments.

- Linked to: Department, Reported By
- Fields: Incident Type, Description, Severity, Corrective Action
- Dashboard summary: Incident Type distribution

---

## ✅ 3. Corrective Actions

Captures follow-up actions for audits or incidents.

- Dynamic Link: Links to either an Audit Log or Incident
- Fields: Assigned To, Due Date, Status (Open, In Progress, Closed)

---

## 📋 4. Departmental Checklist

Manages the checklist template for each department.

- Fields: Checklist Item, Description, Expected Outcome
- Used during audit creation

---

## 📈 5. Reports & Dashboards

Visualize data and performance over time:

- **Compliance Summary Report**
- **Audit Pass/Fail Chart**
- **Incident Count by Type**
- **Monthly Compliance %**
- Number Cards for total audits, incidents, etc.

---

## 🔒 6. User Roles

| Role            | Permissions                           |
|-----------------|----------------------------------------|
| Safety Officer  | Full access to audit and incidents     |
| Auditor         | Can log audits, view incidents         |
| System Manager  | Full administrative access             |

---

For setup help, visit the [Home Wiki Page](https://github.com/vinaymishraofficial/safecomply/wiki)
