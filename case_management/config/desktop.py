# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "module_name": "Case Management",
            "color": "rgb(14, 96, 134)",
            "icon": "octicon octicon-file-directory",
            "label": _("Case Management"),
            "link": "modules/Case Management",
            "type": "module",
            "hidden": 0
        },
        {
            "module_name": "Matter",
            "_doctype":"Matter",
            "color": "rgb(14, 131, 52)",
            "icon": "octicon octicon-briefcase",
            "type": "list",
            "label":"Matter",
            "link": "List/Matter"
        },
        {
            "module_name": "Calendar",
            "color": "rgb(14, 131, 52)",
            "icon": "octicon octicon-calendar",
            "type": "page",
            "label":"Matter Calendar",
            "link": "List/Matter/Calendar"
        },
    ]
