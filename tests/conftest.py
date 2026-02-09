import socket

import pytest
import requests
from requests import HTTPError

from wazzup.drivers import whatsapp_abstract_driver


@pytest.fixture(autouse=True)
def you_shall_not_pass(monkeypatch):
    """Disable ability to make HTTP requests"""
    def http_block(host, port, *args):
        raise RuntimeError(f"Network blocked: {host}:{port}")

    monkeypatch.setattr(socket, "getaddrinfo", http_block)


@pytest.fixture
def requests_mock(mocker):
    """Mock the requests library for testing"""
    mock = mocker.patch.object(
        whatsapp_abstract_driver, "requests", spec=requests,
    )
    mock.request = mocker.MagicMock()
    mock.HTTPError = HTTPError
    return mock
