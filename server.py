from flask import Flask, request, jsonify
from bkash_api import BkashAPI
from mikrotik_api import MikroTikAPI
import os

app = Flask(__name__)

bkash = BkashAPI()
mikrotik = MikroTikAPI()

# Sample packages mapping
PACKAGES = {
    "5": "2hr",
    "10": "1Day",
    "50": "7Day",
    "80": "15Day",
    "100": "30Day"
}

@app.route('/payment-callback', methods=['POST'])
def payment_callback():
    data = request.json
    trx_id = data.get("trxID")
    amount = str(data.get("amount"))
    phone = data.get("customerMsisdn")

    if not trx_id or not amount or not phone:
        return jsonify({"error": "Missing data"}), 400

    # Verify the payment with bKash
    if not bkash.verify_payment(trx_id, amount, phone):
        return jsonify({"error": "Payment verification failed"}), 400

    profile = PACKAGES.get(amount)
    if not profile:
        return jsonify({"error": "Invalid package"}), 400

    username = phone[-6:]  # Use last 6 digits as username
    password = phone[-6:]

    success = mikrotik.create_hotspot_user(username, password, profile)
    if success:
        return jsonify({"message": f"User {username} activated for {profile}"}), 200
    else:
        return jsonify({"error": "Failed to create user"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
