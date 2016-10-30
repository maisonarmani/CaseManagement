from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Matter",
					"description": _("Matter Documents")
				},
                                {
                                        "type": "doctype",
                                        "name": "Practice Area"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Matter Custom Check List"
                                },
			]
		}
	]
