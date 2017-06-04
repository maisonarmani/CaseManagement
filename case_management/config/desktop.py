# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "module_name": "Case Management",
            "color": "#934bec",
            "doctype": "File",
            "icon": "octicon octicon-file-directory",
            "label": _("Case Management"),
            "link": "modules/Case Management",
            "type": "module",
            "hidden": 0
        },
        {
            "module_name": "Reports",
            "color": "#bdc3c7",
            "icon": "octicon octicon-checklist",
            "type": "module",
            "label": _("Reports")
        },
        {
            "module_name": "Matter",
            "_doctype": "Matter",
            "color": "teal",
            "icon": "octicon octicon-briefcase",
            "type": "link",
            "link": "List/Matter"
        },
    ]
