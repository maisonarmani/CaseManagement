// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
    onload: function (frm) {
        var filter = function (p) {
            return {filters: {designation: p}}
        };
    },
    refresh: function (frm) {
        var open_mapped_doc = function (method) {
            frappe.model.open_mapped_doc({
                method: method,
                frm: cur_frm
            });
        };

        if (cur_frm.doc.docstatus == 1) {
            if (cur_frm.doc.status != "Closed") {
                frm.add_custom_button(__('Close Matter'), function () {
                    frappe.confirm("Are you sure you want to close this this matter?", function () {
                        frappe.call({
                            method: "case_management.case_management.doctype.matter.matter.resolve",
                            args: {
                                doctype: cur_frm.doctype,
                                docname: cur_frm.docname
                            },
                            callback: function (message) {
                                cur_frm.reload_doc()
                            }
                        })
                    })
                });
            }
            // Make
            frm.add_custom_button(__('Invoice'), function () {
                open_mapped_doc("case_management.case_management.doctype.matter.matter.make_invoice");
            }, "Make");
            frm.add_custom_button(__('Expense Claim'), function () {
                open_mapped_doc("case_management.case_management.doctype.matter.matter.make_expense");
            }, "Make");
            frm.add_custom_button(__('Timesheet'), function () {
                open_mapped_doc("case_management.case_management.doctype.matter.matter.make_timesheet");
            }, "Make");

            // View
            frm.add_custom_button(__('Invoice'), function () {
                frappe.set_route("List", "Sales Invoice", {'matter_id': frm.doc.name});
            }, "View");
            frm.add_custom_button(__('Timesheet'), function () {
                frappe.set_route("List", "Timesheet", {'matter': frm.doc.name});
            }, "View");
            frm.add_custom_button(__('Expense Claim'), function () {
                frappe.set_route("List", "Expense Claim", {'matter': frm.doc.name});
            }, "View");

        }
    },
    start_timer: function (frm) {
        frm.doc.from = get_Today();
        refresh_form("from");
    },
});
