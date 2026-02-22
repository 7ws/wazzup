from dataclasses import asdict
from urllib.parse import urljoin

import requests

from ..models import templates, utils
from .whatsapp_abstract_driver import WhatsAppAbstractDriver


class WhatsAppTemplateDriver(WhatsAppAbstractDriver):
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

    def create_template(self, template: templates.Template) -> requests.Response:
        """
        Create a new template in WhatsApp.

        :param template: The template to be created.
        :return: Response from the WhatsApp API.
        """
        payload = asdict(template, dict_factory=utils.skip_none_factory)

        response = self._make_request(
            method="POST",
            url=self.url,
            data=payload,
        )

        return response

    def update_template(
        self,
        template_id: str,
        template: templates.Template,
    ) -> requests.Response:
        """
        Update an existing template in WhatsApp.

        :param template_id: The ID of the template to be updated.
        :param template: The updated template data.
        :return: Response from the WhatsApp API.
        """
        url = urljoin(self.base_url, template_id)
        payload = asdict(template, dict_factory=utils.skip_none_factory)

        response = self._make_request(
            method="POST",
            url=url,
            data=payload,
        )

        return response

    def delete_template(
        self, template_id: str, template_name: str
    ) -> requests.Response:
        """
        Delete a template in WhatsApp.

        :param template_id: The ID of the template to be deleted.
        :param template_name: The name of the template to be deleted.
        :return: Response from the WhatsApp API.
        """
        url = urljoin(
            self.url,
            f"?hsm_id={template_id}&name={template_name}",
        )

        response = self._make_request(
            method="DELETE",
            url=url,
            data={},
        )

        return response
