// Copyright (c) 2026, UnifyXperts and contributors
// For license information, please see license.txt

frappe.provide("us_check_printing.us_check_print");

frappe.ui.form.on("US Check Print Template", {
	refresh: function (frm) {
		if (!frm.doc.__islocal) {

			frm.add_custom_button(
                
				frm.doc.has_print_format ? __("Update Print Format") : __("Create Print Format"),
				function () {
					us_check_printing.us_check_print.view_check_print(frm);
				}
			).addClass("btn-primary");
			$(frm.fields_dict.cheque_print_preview.wrapper).empty();

			let template = `
			<div style="position: relative; overflow-x: scroll;">
				<div id="cheque_preview"
					style="width: ${frm.doc.cheque_width}cm;
					height: ${frm.doc.cheque_height}cm;
					background-repeat: no-repeat;
					background-size: cover;">

					<span style="top: ${frm.doc.date_dist_from_top_edge}cm;
						left: ${frm.doc.date_dist_from_left_edge}cm;
						position: absolute;">
						Date
					</span>

					<span style="top: ${frm.doc.check_ref_dist_from_top_edge}cm;
						left: ${frm.doc.check_ref_dist_from_left_edge}cm;
						position: absolute;">
						12345
					</span>

					<span style="top: ${frm.doc.payer_name_from_top_edge}cm;
						left: ${frm.doc.payer_name_from_left_edge}cm;
						position: absolute;">
						Payer Name
					</span>

					<span style="top: ${frm.doc.amt_in_words_from_top_edge}cm;
						left: ${frm.doc.amt_in_words_from_left_edge}cm;
						position: absolute;">
						Amount in Words
					</span>

					<span style="top: ${frm.doc.amt_in_figures_from_top_edge}cm;
						left: ${frm.doc.amt_in_figures_from_left_edge}cm;
						position: absolute;">
						1000
					</span>

				</div>
			</div>`;

			$(template).appendTo(frm.fields_dict.cheque_print_preview.wrapper);

			if (frm.doc.scanned_cheque) {
				$(frm.fields_dict.cheque_print_preview.wrapper)
					.find("#cheque_preview")
					.css("background-image", "url(" + frm.doc.scanned_cheque + ")");
			}
		}
	},
});

us_check_printing.us_check_print.view_check_print = function (frm) {
	frappe.call({
		method: "us_check_printing.us_check_printing.doctype.us_check_print_template.us_check_print_template.create_or_update_cheque_print_format",
		args: {
			template_name: frm.doc.name,
		},
		callback: function (r) {
			if (!r.exc && !frm.doc.has_print_format) {
				let doc = frappe.model.sync(r.message);
				frappe.set_route("Form", r.message.doctype, r.message.name);
			} else {
				frappe.msgprint(__("Print settings updated"));
			}
		},
	});
};