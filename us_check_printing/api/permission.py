import frappe


def has_app_permission():
	"""Only show the US Check Printing icon on the Apps screen to users
	who actually have access to the US Check Print Template doctype."""
	if frappe.session.user == "Administrator":
		return True

	allowed_roles = {"System Manager", "Accounts Manager", "Accounts User"}
	user_roles = set(frappe.get_roles(frappe.session.user))

	return bool(allowed_roles & user_roles)