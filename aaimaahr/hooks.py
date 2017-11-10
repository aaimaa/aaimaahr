# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aaimaahr"
app_title = "Aaimaa HR"
app_publisher = "Aaimaa Web Solutions"
app_description = "Aaimaa HR"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@aaimaa.in"
app_license = "MIT"
fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aaimaahr/css/aaimaahr.css"
# app_include_js = "/assets/aaimaahr/js/aaimaahr.js"

# include js, css files in header of web template
# web_include_css = "/assets/aaimaahr/css/aaimaahr.css"
# web_include_js = "/assets/aaimaahr/js/aaimaahr.js"

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
# get_website_user_home_page = "aaimaahr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aaimaahr.install.before_install"
# after_install = "aaimaahr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aaimaahr.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aaimaahr.tasks.all"
# 	],
# 	"daily": [
# 		"aaimaahr.tasks.daily"
# 	],
# 	"hourly": [
# 		"aaimaahr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aaimaahr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aaimaahr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aaimaahr.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aaimaahr.event.get_events"
# }

