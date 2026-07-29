# Copyright (c) 2026, UnifyXperts and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase

from us_check_printing.us_check_printing.doctype.us_check_print_template.us_check_print_template import (
	create_or_update_cheque_print_format,
)

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class IntegrationTestUSCheckPrintTemplate(IntegrationTestCase):
	"""
	Integration tests for USCheckPrintTemplate.
	Use this class for testing interactions between multiple components.
	"""

	def make_template(self, bank_name="_Test Bank For Cheque Printing"):
		if frappe.db.exists("US Check Print Template", bank_name):
			return frappe.get_doc("US Check Print Template", bank_name)

		template = frappe.get_doc(
			{
				"doctype": "US Check Print Template",
				"bank_name": bank_name,
				"cheque_size": "Regular",
				"cheque_width": 21.50,
				"cheque_height": 9.00,
			}
		)
		template.insert(ignore_permissions=True)
		return template

	def test_creates_print_format_on_first_call(self):
		template = self.make_template()
		self.assertFalse(frappe.db.exists("Print Format", template.name))

		result = create_or_update_cheque_print_format(template.name)

		self.assertEqual(result.doctype, "Print Format")
		self.assertEqual(result.name, template.name)
		self.assertEqual(result.doc_type, "Payment Entry")
		self.assertEqual(result.print_format_type, "Jinja")
		self.assertIn(f"width:{template.cheque_width}cm", result.html)

		# has_print_format should now be flagged on the template
		self.assertEqual(frappe.db.get_value("US Check Print Template", template.name, "has_print_format"), 1)

	def test_updates_existing_print_format_instead_of_duplicating(self):
		template = self.make_template("_Test Bank For Cheque Printing Update")
		create_or_update_cheque_print_format(template.name)

		# change a layout value and re-run - should update the same Print Format, not create a new one
		frappe.db.set_value("US Check Print Template", template.name, "cheque_width", 25.00)
		template.reload()

		result = create_or_update_cheque_print_format(template.name)

		self.assertEqual(frappe.db.count("Print Format", {"name": template.name}), 1)
		self.assertIn("width:25.0cm", result.html)

	def test_unauthorized_user_cannot_generate_print_format(self):
		template = self.make_template("_Test Bank For Cheque Printing Permission")

		unauthorized_user = "test_no_access@example.com"
		if not frappe.db.exists("User", unauthorized_user):
			frappe.get_doc(
				{
					"doctype": "User",
					"email": unauthorized_user,
					"first_name": "No Access",
					"send_welcome_email": 0,
					"roles": [{"role": "Sales User"}],
				}
			).insert(ignore_permissions=True)

		with self.set_user(unauthorized_user):
			self.assertRaises(
				frappe.PermissionError,
				create_or_update_cheque_print_format,
				template.name,
			)

		# confirm nothing was created by the blocked call
		self.assertFalse(frappe.db.exists("Print Format", template.name))