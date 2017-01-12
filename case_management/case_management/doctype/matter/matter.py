# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cint,flt
class Matter(Document):
	pass
	def before_submit(self):
		self.status="Close"
		self.close_date=frappe.utils.nowdate()
	def get_custom_field(self):
		if self.custom_field :
			data = frappe.db.sql("""select title from `tabMatter Custom Check List Item` where parent="{}" """.format(self.custom_field),as_list=1)
			self.check_list=[]
			for row in data:
				dt = self.append('check_list', {})
				dt.title=row[0]
		else:
			frappe.throw("""Please select a Custom Field Preset. """)
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
def invoice_update(doc,method):
	if method == "on_submit":
		record = frappe.get_doc("Matter",doc.matter_id)
		record.append("invoice",{"sales_invoice":doc.name ,"total":flt(doc.grand_total)})
		record.insert()
	else:
		frappe.db.sql("""delete from `tabMatter Invoice` where parent="{}" and sales_invoice="{}" """.format(doc.matter_id,doc.name))
def timesheet_update(doc,method):
	if method == "on_submit":
		record = frappe.get_doc("Matter",doc.matter)
		record.append("activities",{"time_sheet":doc.name ,"total_hours":flt(doc.total_hours),"employee":doc.employee,"employee_name":doc.employee_name})
		record.insert()
	else:
		frappe.db.sql("""delete from `tabMatter Timesheet` where parent="{}" and time_sheet="{}" """.format(doc.matter,doc.name))
