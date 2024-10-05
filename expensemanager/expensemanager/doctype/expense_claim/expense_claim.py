# Copyright (c) 2024, Kumkum Tiwari and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def validate(self):
		amount = 0

		for item in self.expense_type:
			if item.price:
				amount += item.price

		self.amount = amount
