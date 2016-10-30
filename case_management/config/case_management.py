from __future__ import unicode_literals
from frappe import _

def get_data():
	return []
def get_x():
	return [
		{
			"label": _("Case Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Matter",
					"description": _("Matter Documents")
				}
			]
		},
		{
			"label":_("Setup"),
			"items": [
                                {
                                        "type": "doctype",
                                        "name": "Practice Area",
                                        "description": _("Practice Area")
                                },
                                {
                                        "type": "doctype",
                                        "name": "Matter Custom Check List",
                                        "description": _("Matter Custom Check List")
                                },
			]
		}
	]
