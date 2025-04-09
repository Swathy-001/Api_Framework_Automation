import pytest
import logging
# from app.fuctions import get_user, create_user, update_user, delete_user
# from app.Base import User

class APITestRunner:
    def __init__(self):
        self.logger = logging.getLogger('APITestRunner')
        logging.basicConfig(level=logging.INFO)
        self.results = []

    def setup(self):
        self.logger.info("Setting up the test environment...")

    def teardown(self):
        self.logger.info("Tearing down the test environment...")

    def run_tests(self):
        self.setup()
        try:
            # Run each test function (you could also specify test names or collect dynamically)
            pytest.main(["-q", "--tb=short"])
        finally:
            self.teardown()

    def show_results(self):
        # Example: Display test results after completion
        if self.results == 0:
            self.logger.info("All API tests passed successfully!")
        else:
            self.logger.error(f"Some tests failed with exit code {self.results}.")


# Main script to run the tests
if __name__ == "__main__":
    runner = APITestRunner()
    runner.run_tests()