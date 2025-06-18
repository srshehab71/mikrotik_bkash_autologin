import os

class BkashAPI:
    def __init__(self):
        self.app_key = os.getenv("BKASH_APP_KEY")
        self.app_secret = os.getenv("BKASH_APP_SECRET")
        self.username = os.getenv("BKASH_USERNAME")
        self.password = os.getenv("BKASH_PASSWORD")

    def verify_payment(self, trx_id, amount, phone):
        # Simulate verification (Replace with real bKash verification logic)
        return True  # Always valid for now (mocked)
