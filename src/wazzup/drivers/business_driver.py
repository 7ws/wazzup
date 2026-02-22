from urllib.parse import urljoin

import requests

from .whatsapp_abstract_driver import WhatsAppAbstractDriver


class WhatsAppBusinessDriver(WhatsAppAbstractDriver):
    RESOURCE_PATH = "{waba_id}/message_templates"

    def __init__(
        self, access_token, waba_id, *, api_version=None, enabled: bool = True
    ):
        super().__init__(api_version=api_version, enabled=enabled)
        self.access_token = access_token
        self.url = urljoin(
            self.base_url,
            self.RESOURCE_PATH.format(waba_id=waba_id),
        )

    def list_templates(self) -> requests.Response:
        """
        List all message templates for the WhatsApp Business Account.

        :return: Response from the WhatsApp API.
        """
        if not self.enabled:
            response = requests.Response()
            response.status_code = 200
            response._content = b'{"data": []}'
            return response

        headers = self._get_common_headers()
        response = requests.get(self.url, headers=headers)

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        return response
