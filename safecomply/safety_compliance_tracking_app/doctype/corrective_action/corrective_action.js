// Copyright (c) 2025, Vinay Mishra and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Corrective Action", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Corrective Action', {
    onload: function(frm) {
        frm.set_query("reference_type", function() {
            return {
                filters: [
                    ["name", "in", ["Safety Incident", "Safety Audit Log"]]
                ]
            };
        });
    }
});