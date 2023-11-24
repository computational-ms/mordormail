from email.mime.multipart import MIMEMultipart
from pathlib import Path

import pytest

pytest._test_path = Path(__file__).parent


@pytest.fixture
def sample_mime_message():
    return MIMEMultipart()
