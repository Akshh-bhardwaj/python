import logging
import unittest
from unittest.mock import MagicMock, patch

# ----------------------------------------------------
# 1. Custom Exception Hierarchy and Exception Chaining
# ----------------------------------------------------
class ApplicationError(Exception):
    """Base application exception."""
    pass

class APIConnectionError(ApplicationError):
    """Custom exception raised when external API calls fail."""
    def __init__(self, message, endpoint):
        super().__init__(message)
        self.endpoint = endpoint

class ConnectionTimeoutError(Exception):
    pass

def call_third_party_api(endpoint):
    try:
        # Simulate a low-level socket timeout or HTTP error
        raise ConnectionTimeoutError("Connection timed out at socket layer.")
    except Exception as e:
        # Exception Chaining: Raising our custom exception 'from' the low-level exception
        raise APIConnectionError(f"Failed to fetch data from {endpoint}", endpoint) from e


# ----------------------------------------------------
# 2. Structured Logging Configuration
# ----------------------------------------------------
# Setup basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("AdvancedAppLogger")


# ----------------------------------------------------
# 3. Code Under Test (Using Dependency Injection & Global Calls)
# ----------------------------------------------------
def get_exchange_rate(currency):
    """Simulates an external HTTP request to get exchange rates."""
    # In real applications, this does requests.get("https://api.exchangerate.com/...")
    raise RuntimeError("External network resource unavailable.")

class PaymentService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_user_payment(self, user_id, amount, currency="USD"):
        logger.info(f"Processing payment of {amount} {currency} for User-{user_id}...")
        try:
            # If currency is not USD, we dynamically convert it
            if currency != "USD":
                rate = get_exchange_rate(currency)
                amount = amount * rate
                logger.info(f"Converted amount to USD: {amount:.2f}")

            response = self.payment_gateway.charge(user_id, amount)
            if response.get("status") == "success":
                logger.info(f"Payment successful. Transaction ID: {response['tx_id']}")
                return True
            else:
                logger.warning(f"Payment declined for User-{user_id}.")
                return False
        except Exception as e:
            logger.error(f"Payment failed due to error: {e}")
            raise ApplicationError("Payment process failed.") from e


# ----------------------------------------------------
# 4. Unit Tests
# ----------------------------------------------------
class TestPaymentService(unittest.TestCase):
    
    def test_mock_gateway_success(self):
        """Test charging USD using direct dependency injection mock."""
        mock_gateway = MagicMock()
        mock_gateway.charge.return_value = {"status": "success", "tx_id": "TX_99812"}

        service = PaymentService(mock_gateway)
        result = service.process_user_payment("user123", 100.0)

        self.assertTrue(result)
        mock_gateway.charge.assert_called_once_with("user123", 100.0)

    def test_mock_gateway_decline(self):
        """Test charging USD when the charge is declined."""
        mock_gateway = MagicMock()
        mock_gateway.charge.return_value = {"status": "declined", "tx_id": None}

        service = PaymentService(mock_gateway)
        result = service.process_user_payment("user456", 25.0)

        self.assertFalse(result)
        mock_gateway.charge.assert_called_once_with("user456", 25.0)

    @patch('__main__.get_exchange_rate')
    def test_payment_with_exchange_rate_patch(self, mock_get_rate):
        """Test international payment where the global get_exchange_rate function is patched."""
        # Setup mock behavior for patched function
        mock_get_rate.return_value = 0.85  # 1 EUR = 0.85 USD

        mock_gateway = MagicMock()
        mock_gateway.charge.return_value = {"status": "success", "tx_id": "TX_11223"}

        service = PaymentService(mock_gateway)
        result = service.process_user_payment("user_euro", 100.0, currency="EUR")

        self.assertTrue(result)
        # Verify exchange rate conversion logic was applied (100 * 0.85 = 85.0)
        mock_gateway.charge.assert_called_once_with("user_euro", 85.0)
        mock_get_rate.assert_called_once_with("EUR")


# Run example execution
if __name__ == "__main__":
    print("--- Running Log & Exception Demonstration ---")
    try:
        call_third_party_api("/v1/payments")
    except APIConnectionError as e:
        logger.exception("Application intercepted a critical API connection exception:")
    print()

    print("--- Running Unit Tests ---")
    unittest.main(exit=False)
