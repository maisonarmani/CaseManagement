# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cint, flt


class Matter(Document):
    pass

    def before_submit(self):
        self.status = "Close"
        self.close_date = frappe.utils.nowdate()

    def get_custom_field(self):
        if self.custom_field:
            data = frappe.db.sql(
                """select title from `tabMatter Custom Check List Item` where parent="{}" """.format(self.custom_field),
                as_list=1)
            self.check_list = []
            for row in data:
                dt = self.append('check_list', {})
                dt.title = row[0]
        else:
            frappe.throw("""Please select a Custom Field Preset. """)

@frappe.whitelist()
def get_events(start, end, filters=None):
    """Returns events for Gantt / Calendar view rendering.

    :param start: Start date-time.
    :param end: End date-time.
    :param filters: Filters (JSON).
    """
    from frappe.desk.calendar import get_event_conditions
    conditions = get_event_conditions("Matter", filters)

    data = frappe.db.sql("""select name,CONCAT(name," ",client) as title , open_date,
		close_date, status from `tabMatter` where 
		((ifnull(open_date, '0000-00-00') != '0000-00-00')  and (open_date <= %(end)s and open_date >= %(start)s)) 
		{conditions}
		""".format(conditions=conditions), {
        "start": start,
        "end": end
    }, as_dict=True)
    return data


@frappe.whitelist()
def make_invoice(source_name, target_doc=None):
    def set_missing_values(source, target):
        pass

    def update_item(source, target, source_parent):
        pass

    target_doc = get_mapped_doc("Matter", source_name, {
        "Matter": {
            "doctype": "Sales Invoice",
            "field_map": {
                "client": "customer",
                "matter_id": "name",
            }
        },

    }, target_doc, set_missing_values)

    return target_doc


@frappe.whitelist()
def make_timesheet(source_name, target_doc=None):
    def set_missing_values(source, target):
        pass

    def update_item(source, target, source_parent):
        pass

    target_doc = get_mapped_doc("Matter", source_name, {
        "Matter": {
            "doctype": "Timesheet",
            "field_map": {
                "matter": "name",
            }
        },

    }, target_doc, set_missing_values)

    return target_doc


def invoice_update(doc, method):
    if not doc.matter_id:
        return
    if method == "on_submit":
        record = frappe.new_doc("Matter Invoice")
        # frappe.throw(doc.name)
        record.update({"parent": doc.matter_id, "parenttype": "Matter", "parentfield": "invoice", "status": doc.status,
                       "invoice": doc.name, "total": flt(doc.grand_total)})
        record.insert()
        record.save()
    # elif method == "after_update":
    # frappe.throw("tes")
    # frappe.db.sql("""update `tabMatter Invoice` set status="{}" where parent="{}" and sales_invoice="{}" """.format(doc.status,doc.matter_id,doc.name))
    else:
        frappe.db.sql(
            """delete from `tabMatter Invoice` where parent="{}" and invoice="{}" """.format(doc.matter_id, doc.name))


def timesheet_update(doc, method):
    if not doc.matter:
        return
    # frappe.throw(method)
    if method == "on_submit":
        record = frappe.new_doc("Matter Timesheet")
        record.update(
            {"parent": doc.matter, "parenttype": "Matter", "parentfield": "activities", "time_sheet": doc.name,
             "total_hours": flt(doc.total_hours), "employee": doc.employee, "employee_name": doc.employee_name})
        record.insert()
        record.save()
    else:
        frappe.db.sql(
            """delete from `tabMatter Timesheet` where parent="{}" and time_sheet="{}" """.format(doc.matter, doc.name))


def invoice_payment_update(doc, method):
    for row in doc.references:
        if row.allocated_amount == row.outstanding_amount and row.reference_doctype == "Sales Invoice":
            frappe.db.sql(
                """update `tabMatter Invoice` set status="Paid" where invoice="{}" """.format(row.reference_name))


def invoice_payment_cancel(doc, method):
    for row in doc.references:
        if row.reference_doctype == "Sales Invoice":
            frappe.db.sql(
                """update `tabMatter Invoice` set status="Unpaid" where  invoice="{}" """.format(row.reference_name))
