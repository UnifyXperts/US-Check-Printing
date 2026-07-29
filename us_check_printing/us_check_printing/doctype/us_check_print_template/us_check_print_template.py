# Copyright (c) 2026, UnifyXperts and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class USCheckPrintTemplate(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amt_in_figures_from_left_edge: DF.Float
		amt_in_figures_from_top_edge: DF.Float
		amt_in_word_width: DF.Float
		amt_in_words_from_left_edge: DF.Float
		amt_in_words_from_top_edge: DF.Float
		amt_in_words_line_spacing: DF.Float
		bank_name: DF.Data
		cheque_height: DF.Float
		cheque_size: DF.Literal["", "Regular", "A4", "Letter"]
		cheque_width: DF.Float
		date_dist_from_left_edge: DF.Float
		date_dist_from_top_edge: DF.Float
		has_print_format: DF.Check
		payer_name_from_left_edge: DF.Float
		payer_name_from_top_edge: DF.Float
		scanned_cheque: DF.Attach | None
		starting_position_from_top_edge: DF.Float
	# end: auto-generated types

	pass


@frappe.whitelist()
def create_or_update_cheque_print_format(template_name: str):
	if not frappe.has_permission("US Check Print Template", "write", doc=template_name):
		frappe.throw(
			_("You do not have permission to create or update a Print Format for {0}").format(template_name),
			frappe.PermissionError,
		)

	if not frappe.db.exists("Print Format", template_name):
		cheque_print = frappe.new_doc("Print Format")
		cheque_print.update(
			{
				"doc_type": "Payment Entry",
				"standard": "No",
				"custom_format": 1,
				"print_format_type": "Jinja",
				"name": template_name,
			}
		)
	else:
		cheque_print = frappe.get_doc("Print Format", template_name)

	doc = frappe.get_doc("US Check Print Template", template_name)

	cheque_print.html = """
<style>
@page {{
    size: auto;
    margin: 0mm !important;
}}

html, body {{
    margin: 0 !important;
    padding: 0 !important;
}}

.print-format {{
    margin: 0 !important;
    padding: 0 !important;
}}

.page-break {{
    margin: 0 !important;
    padding: 0 !important;
}}
</style>
<!-- TABLE 1(SUMMARY) -->
<div style="position:absolute; top:{table_1_distance_from_top_edge}cm; width:100%;">
	<table style="width:100%; border-collapse: collapse; font-size:11px;">
		
		<!-- HEADER -->
		<thead>
			<tr>
				<th style="text-align:left;"><b>Reference</b></th>
				<th style="text-align:left;"><b>Date</b></th>
				<th style="text-align:left;"><b>Description</b></th>
				<th style="text-align:right;"><b>Amount</b></th>
				<th style="text-align:right;"><b>Net Amount</b></th>
			</tr>
		</thead>

		<tbody>

			<!-- REFERENCE ROWS -->
			{{% for row in doc.references %}}
			<tr>
				<td>{{{{ row.reference_name or "" }}}}</td>
				<td>
					{{{{ frappe.db.get_value(row.reference_doctype, row.reference_name, "posting_date") or "" }}}}
				</td>
				<td>{{{{ row.reference_doctype }}}}</td>
				<td style="text-align:right;">{{{{ row.allocated_amount or "" }}}}</td>
				<td style="text-align:right;">{{{{ row.allocated_amount or "" }}}}</td>
			</tr>
			{{% endfor %}}

			<!-- SPACE ROW -->
			<tr>
				<td colspan="5" style="height:10px;"></td>
			</tr>

			<!-- SUMMARY HEADER -->
			<tr>
				<td><b>Check #</b></td>
				<td><b>Date</b></td>
				<td style="text-align:center;"></td>
				<td style="text-align:right;"><b>Gross</b></td>
				<td style="text-align:right;"><b>Check Amount</b></td>
			</tr>

			<!-- SUMMARY VALUES -->
			<tr>
				<td>{{{{ doc.reference_no or "" }}}}</td>
				<td>{{{{ frappe.utils.formatdate(doc.posting_date) or "" }}}}</td>
				<td style="text-align:center;">
					<b>Totals →</b>
				</td>
				<td style="text-align:right;">{{{{ doc.total_allocated_amount or ""}}}}</td>
				<td style="text-align:right;">
					{{{{ doc.paid_amount or "" }}}}
				</td>
			</tr>

	</table>
</div>

<div style="position: relative; top:{starting_position_from_top_edge}cm">
	<div style="width:{cheque_width}cm;height:{cheque_height}cm;">
		<span style="top:{date_dist_from_top_edge}cm; left:{date_dist_from_left_edge}cm;
			position: absolute;">
			{{{{ frappe.utils.formatdate(doc.reference_date) or '' }}}}
		</span>
		<span style="top:{check_ref_dist_from_top_edge}cm;left:{check_ref_dist_from_left_edge}cm;
			position: absolute;  min-width: 6cm;">
			{{{{ doc.reference_no or '' }}}}
		</span>
		<span style="top:{payer_name_from_top_edge}cm;left: {payer_name_from_left_edge}cm;
			position: absolute;  min-width: 6cm;">
			{{{{doc.party_name}}}}
		</span>
		<span style="top:{amt_in_words_from_top_edge}cm; left:{amt_in_words_from_left_edge}cm;
			position: absolute; display: block; width: {amt_in_word_width}cm;
			line-height:{amt_in_words_line_spacing}cm; word-wrap: break-word;">
				{{{{frappe.utils.money_in_words(doc.base_paid_amount or doc.base_received_amount)}}}}
		</span>
		<span style="top:{amt_in_figures_from_top_edge}cm;left: {amt_in_figures_from_left_edge}cm;
			position: absolute; min-width: 4cm;">
			{{{{doc.get_formatted("base_paid_amount") or doc.get_formatted("base_received_amount")}}}}
		</span>
		
	</div>
</div>
<!-- TABLE 2 (SUMMARY) -->
<div style="position:absolute; top:{table_2_distance_from_top_edge}cm; width: 100%">
	<table style="width:100%; border-collapse: collapse; font-size:11px;">

		<!-- HEADER -->
		<thead>
			<tr>
				<th style="text-align:left;"><b>Reference</b></th>
				<th style="text-align:left;"><b>Date</b></th>
				<th style="text-align:left;"><b>Description</b></th>
				<th style="text-align:right;"><b>Amount</b></th>
				<th style="text-align:right;"><b>Net Amount</b></th>
			</tr>
		</thead>

		<tbody>

			<!-- REFERENCE ROWS -->
			{{% for row in doc.references %}}
			<tr>
				<td>{{{{ row.reference_name or "" }}}}</td>
				<td>
					{{{{ frappe.db.get_value(row.reference_doctype, row.reference_name, "posting_date") or "" }}}}
				</td>
				<td>{{{{ row.reference_doctype or "" }}}}</td>
				<td style="text-align:right;">{{{{ row.allocated_amount or "" }}}}</td>
				<td style="text-align:right;">{{{{ row.allocated_amount or "" }}}}</td>
			</tr>
			{{% endfor %}}

			<!-- SPACE ROW -->
			<tr>
				<td colspan="5" style="height:10px;"></td>
			</tr>

			<!-- SUMMARY HEADER -->
			<tr>
				<td><b>Check #</b></td>
				<td><b>Date</b></td>
				<td style="text-align:center;"></td>
				<td style="text-align:right;"><b>Gross</b></td>
				<td style="text-align:right;"><b>Check Amount</b></td>
			</tr>

			<!-- SUMMARY VALUES -->
			<tr>
				<td>{{{{ doc.reference_no or "" }}}}</td>
				<td>{{{{ frappe.utils.formatdate(doc.posting_date) }}}}</td>
				<td style="text-align:center;">
					<b>Totals →</b>
				</td>
				<td style="text-align:right;">{{{{ doc.total_allocated_amount }}}}</td>
				<td style="text-align:right;">
					{{{{ doc.paid_amount }}}}
				</td>
			</tr>

	</table>
</div>
""".format(
		starting_position_from_top_edge=doc.starting_position_from_top_edge
		if doc.cheque_size in ["A4", "Letter"]
		else 0.0,
		cheque_width=doc.cheque_width,
		cheque_height=doc.cheque_height,
		date_dist_from_top_edge=doc.date_dist_from_top_edge,
		date_dist_from_left_edge=doc.date_dist_from_left_edge,
		payer_name_from_top_edge=doc.payer_name_from_top_edge,
		payer_name_from_left_edge=doc.payer_name_from_left_edge,
		amt_in_words_from_top_edge=doc.amt_in_words_from_top_edge,
		amt_in_words_from_left_edge=doc.amt_in_words_from_left_edge,
		amt_in_word_width=doc.amt_in_word_width,
		amt_in_words_line_spacing=doc.amt_in_words_line_spacing,
		amt_in_figures_from_top_edge=doc.amt_in_figures_from_top_edge,
		amt_in_figures_from_left_edge=doc.amt_in_figures_from_left_edge,
		check_ref_dist_from_top_edge=doc.check_ref_dist_from_top_edge,
		check_ref_dist_from_left_edge=doc.check_ref_dist_from_left_edge,
		table_1_distance_from_top_edge=doc.table_1_distance_from_top_edge,
		table_2_distance_from_top_edge=doc.table_2_distance_from_top_edge
	)

	cheque_print.save(ignore_permissions=True)

	frappe.db.set_value("US Check Print Template", template_name, "has_print_format", 1)

	return cheque_print