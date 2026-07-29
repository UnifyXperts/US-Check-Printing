app_name = "us_check_printing"
app_title = "US Check Printing"
app_publisher = "UnifyXperts"
app_description = "Printing Style of US Checks"
app_email = "manan@unifyxperts.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "us_check_printing",
		"logo": "/assets/us_check_printing/images/logo_us_check_printing.png",
		"title": "US Check Printing",
		"route": "/app/us-check-print-template",
		"has_permission": "us_check_printing.api.permission.has_app_permission"
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/us_check_printing/css/us_check_printing.css"
# app_include_js = "/assets/us_check_printing/js/us_check_printing.js"

# include js, css files in header of web template
# web_include_css = "/assets/us_check_printing/css/us_check_printing.css"
# web_include_js = "/assets/us_check_printing/js/us_check_printing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "us_check_printing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "us_check_printing/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "us_check_printing.utils.jinja_methods",
# 	"filters": "us_check_printing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "us_check_printing.install.before_install"
# after_install = "us_check_printing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "us_check_printing.uninstall.before_uninstall"
# after_uninstall = "us_check_printing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "us_check_printing.utils.before_app_install"
# after_app_install = "us_check_printing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "us_check_printing.utils.before_app_uninstall"
# after_app_uninstall = "us_check_printing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "us_check_printing.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"us_check_printing.tasks.all"
# 	],
# 	"daily": [
# 		"us_check_printing.tasks.daily"
# 	],
# 	"hourly": [
# 		"us_check_printing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"us_check_printing.tasks.weekly"
# 	],
# 	"monthly": [
# 		"us_check_printing.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "us_check_printing.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "us_check_printing.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "us_check_printing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "us_check_printing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["us_check_printing.utils.before_request"]
# after_request = ["us_check_printing.utils.after_request"]

# Job Events
# ----------
# before_job = ["us_check_printing.utils.before_job"]
# after_job = ["us_check_printing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"us_check_printing.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

