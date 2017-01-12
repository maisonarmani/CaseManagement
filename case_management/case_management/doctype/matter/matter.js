// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
	refresh: function(frm) {
		//if (frm.doc.docstatus==1){
			frm.add_custom_button(__('Make Invoice'),function() {
//                alert(1);
                frappe.model.open_mapped_doc({
                        method: "case_management.case_management.doctype.matter.matter.make_invoice",
                        frm: cur_frm
                });
			});
			frm.add_custom_button(__('Make Timesheet'),function() {
//                alert(1);
                frappe.model.open_mapped_doc({
                        method: "case_management.case_management.doctype.matter.matter.make_timesheet",
                        frm: cur_frm
                });
			});
		//}
		frm.add_custom_button(__('Show Invoice'),function() {
//                alert(1);
                frappe.set_route("List", "Sales Invoice", {'matter_id': frm.doc.name});
			});
		frm.add_custom_button(__('Show Timesheet'),function() {
//                alert(1);
                frappe.set_route("List", "Timesheet", {'matter': frm.doc.name});
			});
	},
	start_timer : function (frm) {
    	frm.doc.from = get_Today();
    	refresh_form("from");
	},
});
//cur_frm.cscript.make_invoice= function() {
//		alert(1);
//		frappe.model.open_mapped_doc({
//			method: "case_management.case_management.doctype.matter.matter.make_invoice",
//			frm: cur_frm
//		});
//	}
