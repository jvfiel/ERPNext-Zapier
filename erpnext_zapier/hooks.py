# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_zapier"
app_title = "Erpnext Zapier"
app_publisher = "johnvincentfiel@gmail.com"
app_description = "Zapier"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "johnvincentfiel@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_zapier/css/erpnext_zapier.css"
# app_include_js = "/assets/erpnext_zapier/js/erpnext_zapier.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_zapier/css/erpnext_zapier.css"
# web_include_js = "/assets/erpnext_zapier/js/erpnext_zapier.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_zapier.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_zapier.install.before_install"
# after_install = "erpnext_zapier.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_zapier.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"validate": "erpnext_zapier.erpnext_zapier.doctype.zapier_item_hook.zapier_item_hook.validate",
		"on_trash": "erpnext_zapier.erpnext_zapier.doctype.zapier_item_hook.zapier_item_hook.on_trash",
		"after_insert": "erpnext_zapier.erpnext_zapier.doctype.zapier_item_hook.zapier_item_hook.after_insert"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_zapier.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_zapier.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_zapier.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_zapier.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_zapier.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_zapier.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_zapier.event.get_events"
# }

