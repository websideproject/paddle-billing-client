import pytest


@pytest.fixture(autouse=True)
def vcr_config():
    return {"decode_compressed_response": True, "record_mode": "once"}
