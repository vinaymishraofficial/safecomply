# app_name = "safecomply"
# app_title = "Safety Compliance Tracking App"
# app_publisher = "Vinay Mishra"
# app_description = "SafeComply is a robust Safety Compliance Tracking App built on the Frappe framework to help organizations effectively monitor, document, and manage workplace safety, audits, and regulatory compliance."
# app_email = "Vinay.alwar89@gmail.com"
# app_license = "mit"
# # Apps
# # ------------------

# # required_apps = []

# # Each item in the list will be shown as an app in the apps page
# # add_to_apps_screen = [
# # 	{
# # 		"name": "safecomply",
# # 		"logo": "/assets/safecomply/logo.png",
# # 		"title": "Safety Compliance Tracking App",
# # 		"route": "/safecomply",
# # 		"has_permission": "safecomply.api.permission.has_app_permission"
# # 	}
# # ]

# doctype_js = {
#     "Corrective Action": "safety_compliance_tracking_app/doctype/corrective_action/corrective_action.js"
# }

# fixtures = [
#     "Report",
#     "Dashboard",
#     "Dashboard Chart",
#     "Number Card",
#     "Workspace",
#     "Role",
#     "Role Profile",

# ]

# # Includes in <head>
# # ------------------

# # include js, css files in header of desk.html
# app_include_css = "/assets/safecomply/css/safecomply.css"
# app_include_js = "/assets/safecomply/js/safecomply.js"

# # include js, css files in header of web template
# # web_include_css = "/assets/safecomply/css/safecomply.css"
# # web_include_js = "/assets/safecomply/js/safecomply.js"

# # include custom scss in every website theme (without file extension ".scss")
# # website_theme_scss = "safecomply/public/scss/website"

# # include js, css files in header of web form
# # webform_include_js = {"doctype": "public/js/doctype.js"}
# # webform_include_css = {"doctype": "public/css/doctype.css"}

# # # include js in page
# # page_js = {"page" : "public/js/file.js"}

# # # include js in doctype views
# # doctype_js = {"doctype" : "public/js/doctype.js"}
# # doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# # doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# # doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# # Svg Icons
# # ------------------
# # include app icons in desk
# # app_include_icons = "/assets/safecomply/logo.png"

# # Home Pages
# # ----------

# # application home page (will override Website Settings)
# # home_page = "login"

# # website user home page (by Role)
# # role_home_page = {
# # 	"Role": "home_page"
# # }

# # Generators
# # ----------

# # automatically create page for each record of this doctype
# # website_generators = ["Web Page"]

# # Jinja
# # ----------

# # add methods and filters to jinja environment
# # jinja = {
# # 	"methods": "safecomply.utils.jinja_methods",
# # 	"filters": "safecomply.utils.jinja_filters"
# # }

# # Installation
# # ------------

# # before_install = "safecomply.install.before_install"
# # after_install = "safecomply.install.after_install"

# # Uninstallation
# # ------------

# # before_uninstall = "safecomply.uninstall.before_uninstall"
# # after_uninstall = "safecomply.uninstall.after_uninstall"

# # Integration Setup
# # ------------------
# # To set up dependencies/integrations with other apps
# # Name of the app being installed is passed as an argument

# # before_app_install = "safecomply.utils.before_app_install"
# # after_app_install = "safecomply.utils.after_app_install"

# # Integration Cleanup
# # -------------------
# # To clean up dependencies/integrations with other apps
# # Name of the app being uninstalled is passed as an argument

# # before_app_uninstall = "safecomply.utils.before_app_uninstall"
# # after_app_uninstall = "safecomply.utils.after_app_uninstall"

# # Desk Notifications
# # ------------------
# # See frappe.core.notifications.get_notification_config

# # notification_config = "safecomply.notifications.get_notification_config"

# # Permissions
# # -----------
# # Permissions evaluated in scripted ways

# # permission_query_conditions = {
# # 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# # }
# #
# # has_permission = {
# # 	"Event": "frappe.desk.doctype.event.event.has_permission",
# # }

# # DocType Class
# # ---------------
# # Override standard doctype classes

# # override_doctype_class = {
# # 	"ToDo": "custom_app.overrides.CustomToDo"
# # }

# # Document Events
# # ---------------
# # Hook on document methods and events

# # doc_events = {
# # 	"*": {
# # 		"on_update": "method",
# # 		"on_cancel": "method",
# # 		"on_trash": "method"
# # 	}
# # }

# # Scheduled Tasks
# # ---------------

# # scheduler_events = {
# # 	"all": [
# # 		"safecomply.tasks.all"
# # 	],
# # 	"daily": [
# # 		"safecomply.tasks.daily"
# # 	],
# # 	"hourly": [
# # 		"safecomply.tasks.hourly"
# # 	],
# # 	"weekly": [
# # 		"safecomply.tasks.weekly"
# # 	],
# # 	"monthly": [
# # 		"safecomply.tasks.monthly"
# # 	],
# # }

# # Testing
# # -------

# # before_tests = "safecomply.install.before_tests"

# # Overriding Methods
# # ------------------------------
# #
# # override_whitelisted_methods = {
# # 	"frappe.desk.doctype.event.event.get_events": "safecomply.event.get_events"
# # }
# #
# # each overriding function accepts a `data` argument;
# # generated from the base implementation of the doctype dashboard,
# # along with any modifications made in other Frappe apps
# # override_doctype_dashboards = {
# # 	"Task": "safecomply.task.get_dashboard_data"
# # }

# # exempt linked doctypes from being automatically cancelled
# #
# # auto_cancel_exempted_doctypes = ["Auto Repeat"]

# # Ignore links to specified DocTypes when deleting documents
# # -----------------------------------------------------------

# # ignore_links_on_delete = ["Communication", "ToDo"]

# # Request Events
# # ----------------
# # before_request = ["safecomply.utils.before_request"]
# # after_request = ["safecomply.utils.after_request"]

# # Job Events
# # ----------
# # before_job = ["safecomply.utils.before_job"]
# # after_job = ["safecomply.utils.after_job"]

# # User Data Protection
# # --------------------

# # user_data_fields = [
# # 	{
# # 		"doctype": "{doctype_1}",
# # 		"filter_by": "{filter_by}",
# # 		"redact_fields": ["{field_1}", "{field_2}"],
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_2}",
# # 		"filter_by": "{filter_by}",
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_3}",
# # 		"strict": False,
# # 	},
# # 	{
# # 		"doctype": "{doctype_4}"
# # 	}
# # ]

# # Authentication and authorization
# # --------------------------------

# # auth_hooks = [
# # 	"safecomply.auth.validate"
# # ]

# # Automatically update python controller files with type annotations for this app.
# # export_python_type_annotations = True

# # default_log_clearing_doctypes = {
# # 	"Logging DocType Name": 30  # days to retain logs
# # }

