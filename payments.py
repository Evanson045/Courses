import os
from flask import Blueprint, render_template, flash, redirect, url_for

# -------------------- Blueprint --------------------
payments = Blueprint("payments", __name__, template_folder="templates")

# -------------------- Hosted Buttons --------------------
# PayPal Hosted Button IDs (configure via environment variables for flexibility)
MODULE_BUTTON_ID = os.getenv("PAYPAL_MODULE_BUTTON_ID", "25ZB5B5M2Z9F8")   # Single module unlock
COURSE_BUTTON_ID = os.getenv("PAYPAL_COURSE_BUTTON_ID", "E4QRSZMBN6Q4E")   # Full course unlock

# -------------------- Routes --------------------
@payments.route("/unlock-module")
def unlock_module():
    """Render page with PayPal Hosted Button for single module unlock."""
    return render_template(
        "unlock_module.html",
        hosted_button_id=MODULE_BUTTON_ID
    )

@payments.route("/unlock-course")
def unlock_course():
    """Render page with PayPal Hosted Button for full course unlock."""
    return render_template(
        "unlock_course.html",
        hosted_button_id=COURSE_BUTTON_ID
    )

@payments.route("/paypal-success")
def paypal_success():
    """Handle successful PayPal payment."""
    flash("✅ PayPal payment successful. Subscription activated.", "success")
    return redirect(url_for("dashboard"))

@payments.route("/paypal-cancel")
def paypal_cancel():
    """Handle cancelled PayPal payment."""
    flash("⚠️ PayPal payment cancelled. No changes made.", "warning")
    return redirect(url_for("dashboard"))
