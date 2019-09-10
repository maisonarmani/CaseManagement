// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Matter', {
  
    refresh: function (frm) {
        var open_mapped_doc = function (method) {
            frappe.model.open_mapped_doc({
                method: method,
                frm: cur_frm
            });
        };

        if (!cur_frm.doc.__islocal){
            if (cur_frm.doc.status != "Closed") {
                // frm.add_custom_button(__('Add Case File'), function () {
                //     frappe.set_route("List", "File", "Home", "Case Files")
                // }).css({"background-color": "rgb(20, 33, 100)", "color": 'white', "font-weight": 'bolder'});

                // Make
                frm.add_custom_button(__('Add Invoice'), function () {
                    open_mapped_doc("case_management.case_management.doctype.matter.matter.make_invoice");
                }).css({"background-color": "rgb(20, 33, 22)", "color": 'white', "font-weight": 'bolder'});

                frm.add_custom_button(__('Add Expense Claim'), function () {
                    open_mapped_doc("case_management.case_management.doctype.matter.matter.make_expense");
                }).css({"background-color": "rgb(20, 122, 22)", "color": 'white', "font-weight": 'bolder'});

                // frm.add_custom_button(__('Add Employee Advance'), function () {
                //     open_mapped_doc("case_management.case_management.doctype.matter.matter.make_advance");
                // }).css({"background-color": "rgb(20, 122, 22)", "color": 'white', "font-weight": 'bolder'});

                frm.add_custom_button(__('Add Timesheet'), function () {
                    open_mapped_doc("case_management.case_management.doctype.matter.matter.make_timesheet");
                }).css({"background-color": "rgb(20, 62, 22)", "color": 'white', "font-weight": 'bolder'});
                //
                // frm.add_custom_button(__('Add Task'), function () {
                //     open_mapped_doc("case_management.case_management.doctype.matter.matter.make_task");
                // }).css({"background-color": "rgb(20, 100, 122)", "color": 'white', "font-weight": 'bolder'});
            }
             // Close Matter
            if (frappe.user.name == cur_frm.doc.owner) {
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
                    }).css({"background-color": "rgb(197, 22, 22)", "color": 'white', "font-weight": 'bold'});
                }

                if (cur_frm.doc.status == "Closed") {
                    frm.add_custom_button(__('Reopen'), function () {
                        frappe.call({
                            method: "case_management.case_management.doctype.matter.matter.reopen",
                            args: {
                                doctype: cur_frm.doctype,
                                docname: cur_frm.docname
                            },
                            callback: function (message) {
                                cur_frm.reload_doc()
                            }
                        })
                    }).css({"background-color": "rgb(17,122, 22)", "color": 'white', "font-weight": 'bold'});
                }
            }

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
            frm.add_custom_button(__('Employee Advance'), function () {
                frappe.set_route("List", "Employee Advance", {'matter': frm.doc.name});
            }, "View");
            frm.add_custom_button(__('Task'), function () {
                frappe.set_route("List", "Task", {'matter': frm.doc.name});
            }, "View");
            frm.add_custom_button(__('Case Files'), function () {
                frappe.set_route("List", "File", "Home", "Case Files", cur_frm.doc.name);
            }, "View");

            frm.add_custom_button(__('Events/Calendar'), function () {
                frappe.set_route("List", "Event", {'matter': frm.doc.name});
            },"View");

            frm.add_custom_button(__('Contact'), function () {
                frappe.set_route("List", "Address", {'link_name': frm.doc.client});
            },"View");


            frm.page.set_inner_btn_group_as_primary(__("View"));
        }
    },
    start_timer: function (frm) {
        frm.doc.from = get_Today();
        refresh_form("from");
    },
});
