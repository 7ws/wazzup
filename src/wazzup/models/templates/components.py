from dataclasses import asdict, dataclass
from enum import StrEnum

from ..utils import skip_none_factory


@dataclass
class Component:
    class TypeChoices(StrEnum):
        HEADER = 'HEADER'
        BODY = 'BODY'
        FOOTER = 'FOOTER'
        BUTTONS = 'BUTTONS'

    class FormatChoices(StrEnum):
        TEXT = 'TEXT'
        IMAGE = 'IMAGE'
        VIDEO = 'VIDEO'
        DOCUMENT = 'DOCUMENT'
        LOCATION = 'LOCATION'


@dataclass
class HeaderTemplate(Component):
    text: str
    type: Component.TypeChoices = Component.TypeChoices.HEADER
    # NOTE: for media formats we need to use hader_handle
    format: Component.FormatChoices = Component.FormatChoices.TEXT
    header_text_named_params: list[dict[str, str]] = None

    def __init__(
        self,
        text: str,
        text_named_params: list[dict[str, str]] | None = None,
    ) -> None:
        """
        Args:
            text: The header text.
            text_named_params: List of dictionaries with named parameters for the header text.
        """
        self.text = text
        self.header_text_named_params = text_named_params


@dataclass
class BodyTemplate(Component):
    text: str
    type: Component.TypeChoices = Component.TypeChoices.BODY
    body_text_named_params: list[dict[str, str]] = None

    def __init__(
        self,
        text: str,
        text_named_params: list[dict[str, str]] | None = None,
    ) -> None:
        """
        Args:
            text: The body text.
            text_named_params: List of dictionaries with named parameters for the body text.
        """
        self.text = text
        self.body_text_named_params = text_named_params


@dataclass
class FooterTemplate(Component):
    text: str
    type: Component.TypeChoices = Component.TypeChoices.FOOTER


@dataclass
class Button(Component):
    class TypeChoices(StrEnum):
        COPY_CODE = 'COPY_CODE'
        FLOW = 'FLOW'
        MPM = 'MPM'
        PHONE_NUMBER = 'PHONE_NUMBER'
        QUICK_REPLY = 'QUICK_REPLY'
        URL = 'URL'

    type: TypeChoices
    phone_number: str = None
    url: str = None
    text: str = None
    example: list[str] | str = None

    def __init__(
        self,
        button_type: TypeChoices,
        text: str,
        phone_number: str | None = None,
        url: str | None = None,
        example: list[str] | None = None,
        copy_code: str | None = None,
    ) -> None:
        """
        Args:
            button_type: The type of the button.
            text: The text to be displayed on the button.
            phone_number: The phone number for PHONE_NUMBER type.
            url: The URL for URL type.
            example: Example values for URL variables.
            copy_code: The code to be copied for COPY_CODE type.
        """
        self.type = button_type
        self.text = text
        self.phone_number = phone_number
        self.url = url
        self.example = example
        self.example = copy_code


@dataclass
class ButtonsTemplate(Component):
    buttons: list[dict[str, str]]
    type: Component.TypeChoices = Component.TypeChoices.BUTTONS

    def __init__(self, buttons: list[Button]):
        self.buttons = [
            asdict(button, dict_factory=skip_none_factory) for button in buttons
        ]
