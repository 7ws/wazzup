from dataclasses import dataclass


@dataclass
class TextMessage:
    """
    Represents a text message in the WhatsApp application

    Attributes:
        to (str): The recipient of the message.
        message_content (str): The content of the message.
        messaging_product (str): The messaging product, default is "whatsapp".
        recipient_type (str): The type of recipient, default is "individual".
        type (str): The type of message, default is "text".
    """

    to: str
    text: dict[str, str]
    messaging_product: str = 'whatsapp'
    recipient_type: str = 'individual'
    type: str = 'text'

    def __init__(self, message_content: str, to: str):
        """
        Args:
            message_content: The content of the message.
            to: The recipient of the message.
        """
        self.to = to
        self.text = {'preview_url': False, 'body': message_content}
