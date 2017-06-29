// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Matter Expense Summary"] = {
	"filters": [
        {
            "fieldname": "date_from",
            "label": __("Transactions From"),
            "fieldtype": "Date",
            "width": "80",
            "reqd": 1,
            "default": dateutil.year_start()
        },
        {
            "fieldname": "date_to",
            "label": __("Transactions To"),
            "fieldtype": "Date",
            "width": "80",
            "reqd": 1,
            "default": dateutil.year_end()
        },
        {
            "fieldname": "matter",
            "label": __("Matter"),
            "fieldtype": "Link",
            "options":"Matter",
            "width": "80",
            "reqd": 0,
        }
	]
}
