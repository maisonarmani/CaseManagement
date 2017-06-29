// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt
frappe.views.calendar["Matter"] = {
    field_map: {
        "start": "open_date",
        "end": "close_date",
        "id": "name",
        "title": "title",
        "status": "status",
    },
    options: {
        header: {
            left: 'prev,next today',
            center: 'name',
            right: 'month'
        }
    },
    get_events_method: "case_management.case_management.doctype.matter.matter.get_events"
}