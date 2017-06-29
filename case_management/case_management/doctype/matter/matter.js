// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
    onload: function (frm) {
        var filter = function (p) {
            return {filters: {designation: p}}
        };
        frm.fields_dict.responsible_solicitor.get_query = function () {
            return {
                query: "case_management.case_management.doctype.matter.matter.get_lawyer"
            };
        };
    },
    refresh: function (frm) {
        frm.add_custom_button(__('Make Invoice'), function () {
            frappe.model.open_mapped_doc({
                method: "case_management.case_management.doctype.matter.matter.make_invoice",
                frm: cur_frm
            });
        });
        frm.add_custom_button(__('Make Timesheet'), function () {
            frappe.model.open_mapped_doc({
                method: "case_management.case_management.doctype.matter.matter.make_timesheet",
                frm: cur_frm
            });
        });
        //}
        frm.add_custom_button(__('Show Invoice'), function () {
            frappe.set_route("List", "Sales Invoice", {'matter_id': frm.doc.name});
        });
        frm.add_custom_button(__('Show Timesheet'), function () {

            frappe.set_route("List", "Timesheet", {'matter': frm.doc.name});
        });

    },
    start_timer: function (frm) {
        frm.doc.from = get_Today();
        refresh_form("from");
    },
});
