import socket

import pytest
import requests
from requests import HTTPError

from src.wazzup import whatsapp


@pytest.fixture(autouse=True)
def you_shall_not_pass(monkeypatch):
    """
    Desable ability to make HTTP requests
    """
    def http_block(host, port, *args):
        raise RuntimeError(f"Network blocked: {host}:{port}")

    monkeypatch.setattr(socket, "getaddrinfo", http_block)


@pytest.fixture
def requests_mock(mocker):
    """
    Mock the requests library for testing
    """
    requests_mock = mocker.patch.object(whatsapp, "requests", spec=requests)
    requests_mock.request = mocker.MagicMock()
    requests_mock.HTTPError = HTTPError
    return requests_mock
