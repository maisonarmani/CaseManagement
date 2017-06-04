from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Accounts"),
			"items": [
				{
					"type": "report",
					"name": "Accounts Receivable",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Accounts Payable",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name":"General Ledger",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Trial Balance",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Balance Sheet",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Cash Flow",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Profit and Loss Statement",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Petty Cash Log Report",
					"is_query_report": True,
					"doctype": "Petty Cash Log"
				},
				{
					"type": "report",
					"name": "Bank Reconciliation Statement",
					"is_query_report": True,
					"doctype": "Journal Entry"
				},
				{
					"type": "report",
					"name": "Bank Clearance Summary",
					"is_query_report": True,
					"doctype": "Journal Entry"
				},
				{
					"type": "report",
					"name": "Sales Register",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Purchase Register",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Budget Variance Report",
					"is_query_report": True,
					"doctype": "Cost Center"
				},
				{
					"type": "report",
					"name": "Ordered Items To Be Billed",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"name": "Delivered Items To Be Billed",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"name": "Purchase Order Items To Be Billed",
					"is_query_report": True,
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"name": "Received Items To Be Billed",
					"is_query_report": True,
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"name": "Gross Profit",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Purchase Invoice Trends",
					"is_query_report": True,
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"name": "Sales Invoice Trends",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase by Items Report Summary",
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase by Items Report Details",
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"name": "Fixed Asset Register Report",
					"doctype": "Asset",
					"is_query_report": True,
				},{
					"type": "report",
					"name": "Payment Entry Report",
					"doctype": "Payment Entry",
					"is_query_report": True,
				},{
					"type": "report",
					"name": "Overdue Sales Invoice",
					"doctype": "Sales Invoice",
					"is_query_report": True,
				},{
					"type": "report",
					"name": "Overdue Purchase Invoice",
					"doctype": "Purchase Invoice",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Asset Depreciation Ledger",
					"doctype": "Asset",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Asset Depreciations and Balances",
					"doctype": "Asset",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Trial Balance for Party",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Sales Partners Commission",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
				{
					"type": "report",
					"name": "Accounts Receivable Summary",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Accounts Payable Summary",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Credit Balance",
					"doctype": "Customer"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Payment Voucher Report",
					"doctype": "Payment Voucher Form"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Bank Balance Report",
					"doctype": "Journal Entry"
				},
			]
		},
		{
			"label": _("Purchasing"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase Order Status Report",
					"doctype": "Purchase Order Status"
				},{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase by Items Report Summary",
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase by Items Report Details",
					"doctype": "Purchase Invoice"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Requested Items To Be Ordered",
					"doctype": "Material Request"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Item-wise Purchase History",
					"doctype": "Item"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Supplier Addresses and Contacts",
					"doctype": "Supplier"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase Order Summary Report",
					"doctype": "Purchase Order"
				}
			]
		},
		{
			"label": _("CRM"),
			"items": [
				{
					"type": "page",
					"name": "sales-funnel",
					"label": _("Sales Funnel"),
					"icon": "icon-bar-chart",
				},
				{
					"type": "report",
					"name": "Minutes to First Response for Opportunity",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Details",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Addresses and Contacts",
					"doctype": "Contact"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Inactive Customers",
					"doctype": "Sales Order"
				},
			]
		},
		{
			"label": _("Human Resources"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Leave Balance",
					"doctype": "Leave Application"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Birthday",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employees working on a holiday",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"name": "Employee Information",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Monthly Salary Register",
					"doctype": "Salary Slip"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Monthly Attendance Sheet",
					"doctype": "Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Expense Claim Report",
					"doctype": "Expense Claim"
				},
			]
		},
		{
			"label": _("Logistics"),
			"items": [
				{
					"type": "report",
					"name": "Vehicle Fuel Consumption log Report",
					"route": "query-report/Vehicle Fuel Consumption log Report",
					"doctype": "Vehicle Fuel Consumption log",
				},
				{
					"type": "report",
					"name": "Vehicle Allocation Schedule Report",
					"route": "query-report/Vehicle Allocation Schedule Report",
					"doctype": "Vehicle Schedule",
				},
				{
					"type": "report",
					"name": "Goods Tracking Report",
					"route": "query-report/Goods Tracking Report",
					"doctype": "Vehicle Schedule",
				},
				{
					"type": "report",
					"name": "Vehicle Maintenance Log Report",
					"route": "query-report/Vehicle Maintenance Log Report",
					"doctype": "Vehicle Maintenance Log",
				},
				{
					"type": "report",
					"name": "Vehicle Mileage Report",
					"route": "query-report/Vehicle Mileage Report",
					"doctype": "Daily Vehicle Mileage Log",
				},
				#{
				#	"type": "report",
				#	"name": "Logistics Expense Report",
				#	"route": "query-report/Logistics Expense Report",
				#	"doctype": "Logistics Expense",
				#},
			]
		},
		{
			"label": _("Manufacture"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Open Production Orders",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Production Orders in Progress",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Issued Items Against Production Order",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Completed Production Orders",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Search",
					"doctype": "BOM"
				},
			]
		},
		{
			"label": _("Projects"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Daily Timesheet Summary",
					"doctype": "Timesheet"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Project wise Stock Tracking",
					"doctype": "Project"
				},
				{
					"type": "report",
					"route": "Gantt/Task",
					"doctype": "Task",
					"name": "Gantt Chart",
					"description": _("Gantt chart of all tasks.")
				},
			]
		},
		{
			"label":_("Selling"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Territory Target Variance (Item Group-Wise)",
					"route": "query-report/Territory Target Variance Item Group-Wise",
					"doctype": "Territory"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Person Target Variance (Item Group-Wise)",
					"route": "query-report/Sales Person Target Variance Item Group-Wise",
					"doctype": "Sales Person",
				},
				{
					"type": "report",
					"name": "Call Log Report",
					"is_query_report": True,
					"doctype": "Call Log",
				},
				{
					"type": "report",
					"name": "Daily Route Activity Report",
					"route": "query-report/Daily Route Activity Report",
					"doctype": "Daily Route Activity",
				},
				{
					"type": "report",
					"name": "Outlet Survey Report",
					"route": "query-report/Outlet Survey Report",
					"doctype": "Outlet Survey",
				},
				{
					"type": "report",
					"name": "Sales by Product Report",
					"route": "query-report/Sales by Product Report",
					"doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Customer Commission Report",
					"route": "query-report/Customer Commission Report",
					"doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Sales Rep Scorecard Report",
					"route": "query-report/Sales Rep Scorecard Report",
					"doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Product Delivery & Distribution Schedule Report",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales By Product Report Summary",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Addresses And Contacts",
					"doctype": "Contact"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Ordered Items To Be Delivered",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Inactive Customers",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Credit Balance",
					"doctype": "Customer"
				},
				{
					"type": "report",
					"name": "Sales Person-wise Transaction Summary",
					"doctype": "Sales Order",
					"is_query_report": True,
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Variance Report",
					"doctype": "Sales order"
				},
			]
		},
		{
			"label":_("Stock"),
			"items":[
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger",
					"doctype": "Stock Ledger Entry",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger Simplified",
					"doctype": "Stock Ledger Entry",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Raw material re-order Report",
					"doctype": "Item",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Balance",
					"doctype": "Stock Ledger Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Projected Qty",
					"doctype": "Item",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ageing",
					"doctype": "Item",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Store Bin Cards Report",
					"doctype": "Store Bin Card",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name":"Material Receipt List Report",
					"doctype": "Purchase Receipt",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Ordered Items To Be Delivered",
					"doctype": "Delivery Note"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase Order Items To Be Received",
					"doctype": "Purchase Receipt"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Itemwise Recommended Reorder Level",
					"doctype": "Item"
				},
			]
		},
		{
			"label":"Support",
			"items":[
				{
					"type": "page",
					"name": "support-analytics",
					"label": _("Support Analytics"),
					"icon": "icon-bar-chart"
				},
				{
					"type": "report",
					"name": "Minutes to First Response for Issues",
					"doctype": "Issue",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "HelpDesk Report",
					"doctype": "Helpdesk Ticket",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Job Card Status Report",
					"doctype": "Job Card",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Job Card Cost Report",
					"doctype": "Job Card",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Job Card Completion Report",
					"doctype": "Job Card",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Computing Asset Inspection Checklist Report",
					"doctype": "Computing Asset Inspection Checklist",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Fixed Asset Inspection Checklist Report",
					"doctype": "Fixed Asset Inspection Checklist",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Generator Fuel Consumption Log Report",
					"doctype": "Generator Fuel Consumption Log",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Daily Generator Activity Log Report",
					"doctype": "Daily Generator Activity Log",
					"is_query_report": True
				},
			]
		}
	]