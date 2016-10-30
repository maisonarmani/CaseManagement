// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
	refresh: function(frm) {
		if (frm.doc.docstatus==1){
			frm.add_custom_button(__('Make Invoice'),function() {
//                alert(1);
                frappe.model.open_mapped_doc({
                        method: "case_management.case_management.doctype.matter.matter.make_invoice",
                        frm: cur_frm
                });
});
		}
	},
});
//cur_frm.cscript.make_invoice= function() {
//		alert(1);
//		frappe.model.open_mapped_doc({
//			method: "case_management.case_management.doctype.matter.matter.make_invoice",
//			frm: cur_frm
//		});
//	}
