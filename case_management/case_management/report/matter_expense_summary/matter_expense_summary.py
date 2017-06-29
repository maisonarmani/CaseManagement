# Copyright (c) 2013, masonarmani38@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _

import frappe

def execute(filters=None):
	return get_column(), get_data(filters)


def get_data(filters):
	# Expense Claims|
	pi_conditions = ec_conditions = "(1=1) "
	if filters.get('date_from') and filters.get('date_to'):
		ec_conditions += " and posting_date  BETWEEN DATE('{0}') and DATE('{1}')" .format(filters.get("date_from"),filters.get('date_to'))
		pi_conditions += " and posting_date  BETWEEN DATE('{0}') and DATE('{1}')" .format(filters.get("date_from"),filters.get('date_to'))

	if filters.get('matter'):
		ec_conditions += " and matter = '{0}'" .format(filters.get("matter"))
		pi_conditions += " and matter = '{0}'" .format(filters.get("matter"))


	# Expense Claims
	sql = "select posting_date, matter, name, remark, owner, exp_approver ,total_claimed_amount from `tabExpense Claim` WHERE {0} and (docstatus = 1 and status='Paid')"
	ec_sql = sql.format(ec_conditions)

	# Purchase Invoice
	sql = "select posting_date, matter, name, supplier ,owner, 'Approver' , base_grand_total from `tabPurchase Invoice` WHERE {0} and (docstatus = 1 and status='Paid')"
	pi_sql = sql.format(pi_conditions)

	data = frappe.db.sql("{0} UNION {1}".format(ec_sql, pi_sql))
	return  data


def get_column():
	# Examples:
	# "Link:Link/Accident:150", "Data:Data:200", "Currency:Currency:100", "Float:Float:100"
	return [
		"Transaction Date:Date:100",
		"Matter:Link/Matter:100",
		"Document ID:Data:150",
		"Description:Data:250",
		"Created by:Link/User:200",
		"Approver:Link/User:150",
		"Amount:Currency:150",
	]
