from dataclasses import asdict
from urllib.parse import urljoin

from ..models import messages, utils
from .whatsapp_abstract_driver import WhatsAppAbstractDriver


class WhatsAppMessagingDriver(WhatsAppAbstractDriver):
    RESOURCE_PATH = "{phone_number}/messages"

    def __init__(
        self, access_token, phone_number_id, *, api_version=None, enabled: bool = True
    ):
        super().__init__(api_version=api_version, enabled=enabled)
        self.access_token = access_token
        self.url = urljoin(
            self.base_url,
            self.RESOURCE_PATH.format(phone_number=phone_number_id),
        )

    def send_text_message(self, text_message: messages.TextMessage):
        payload = asdict(text_message)

        response = self._make_request(
            method="POST",
            url=self.url,
            data=payload,
        )

        return response

    def reply_message(
        self,
        text_message: messages.TextMessage,
        message_id,
    ):
        payload = asdict(text_message)
        payload["context"] = {"message_id": message_id}

        response = self._make_request(
            method="POST",
            url=self.url,
            data=payload,
        )

        return response

    def react_to_message(
        self,
        message_reaction: messages.MessageReaction,
    ):
        payload = asdict(message_reaction)
        response = self._make_request(
            method="POST",
            url=self.url,
            data=payload,
        )

        return response

    def send_image_message(self, image_message: messages.ImageMessage):
        payload = asdict(image_message)

        response = self._make_request(
            method="POST",
            url=self.url,
            data=payload,
        )

        return response

    def send_location_message(self, location_message: messages.LocationMessage):
        payload = asdict(location_message)

        response = self._make_request(
            method='POST',
            url=self.url,
            data=payload,
        )

        return response

    def send_template_message(self, template: messages.TemplateMessage):
        payload = asdict(template, dict_factory=utils.skip_none_factory)

        response = self._make_request(
            method='POST',
            url=self.url,
            data=payload,
        )

        return response
