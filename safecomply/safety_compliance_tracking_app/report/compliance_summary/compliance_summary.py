# Copyright (c) 2025, Vinay Mishra and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate

def execute(filters=None):
    columns = [
        {"label": "Department", "fieldname": "department", "fieldtype": "Link", "options": "Department", "width": 150},
        {"label": "Total Audits", "fieldname": "total", "fieldtype": "Int", "width": 120},
        {"label": "Passed", "fieldname": "passed", "fieldtype": "Int", "width": 100},
        {"label": "Failed", "fieldname": "failed", "fieldtype": "Int", "width": 100},
        {"label": "Compliance %", "fieldname": "compliance", "fieldtype": "Percent", "width": 120},
        {"label": "Incidents", "fieldname": "incidents", "fieldtype": "Int", "width": 100},
    ]

    data = []

    departments = frappe.get_all("Department", pluck="name")
    for dept in departments:
        audits = frappe.get_all("Safety Audit Log", filters={"department": dept}, fields=["status"])
        total = len(audits)
        passed = len([a for a in audits if a.status == "Passed"])
        failed = total - passed

        compliance = (passed / total) * 100 if total else 0

        incidents = frappe.db.count("Safety Incident", {"department": dept})

        data.append({
            "department": dept,
            "total": total,
            "passed": passed,
            "failed": failed,
            "compliance": compliance,
            "incidents": incidents,
        })

    return columns, data
