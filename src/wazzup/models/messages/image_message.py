from dataclasses import dataclass


@dataclass
class ImageMessage:
    to: str
    image: dict[str, str]
    messaging_product: str = 'whatsapp'
    recipient_type: str = 'individual'
    type: str = 'image'

    def __init__(self, image_id: str, to: str):
        """
        Args:
            image_id: The ID of the image to send.
            to: The recipient's phone number in the format 1234567890'.
        """
        self.to = to
        self.image = {
            'uuid': image_id,
        }
