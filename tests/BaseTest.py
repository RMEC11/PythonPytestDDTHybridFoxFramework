from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    def random_email_generator(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        email_gen = "rmec" + time_stamp + "@gmail.com"
        return email_gen