import frappe
from frappe import _

def get_context(context):
    # Fetch available hotel rooms
    context.rooms = frappe.get_all(
        "Hotel Room",
        filters={"status": "Available"},  # Assuming you have a status field
        fields=["*"]
    )
    context.no_cache = 1  # Ensure the page updates dynamically
