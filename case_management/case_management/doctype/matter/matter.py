# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Matter(Document):
	pass
	def get_custom_field(self):
		if self.custom_field :
			data = frappe.db.sql("""select title from `tabMatter Custom Check List Item` where parent="{}" """.format(self.custom_field),as_list=1)
			self.check_list=[]
			for row in data:
				dt = self.append('check_list', {})
				dt.title=row[0]
		else:
			frappe.throw("""Please select a Custom Field Preset. """)