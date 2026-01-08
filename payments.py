import os
from flask import Blueprint, render_template, flash, redirect, url_for

# -------------------- Blueprint --------------------
payments = Blueprint('payments', __name__)

# -------------------- Hosted Buttons --------------------
# Instead of creating payments via SDK, we now rely on PayPal Hosted Buttons
# These IDs come from your PayPal dashboard
MODULE_BUTTON_ID = "25ZB5B5M2Z9F8"   # Hosted button ID for single module unlock
COURSE_BUTTON_ID = "E4QRSZMBN6Q4E"   # Hosted button ID for full course unlock

# -------------------- Routes --------------------
@payments.route('/unlock-module')
def unlock_module():
    """Render modal or page with PayPal Hosted Button for single module."""
    return render_template(
        "unlock_module.html",
        hosted_button_id=MODULE_BUTTON_ID
    )

@payments.route('/unlock-course')
def unlock_course():
    """Render modal or page with PayPal Hosted Button for full course."""
    return render_template(
        "unlock_course.html",
        hosted_button_id=COURSE_BUTTON_ID
    )

@payments.route('/paypal-success')
def paypal_success():
    flash("PayPal payment successful. Subscription activated.", "success")
    return redirect(url_for('dashboard'))

@payments.route('/paypal-cancel')
def paypal_cancel():
    flash("PayPal payment cancelled.", "warning")
    return redirect(url_for('dashboard'))
