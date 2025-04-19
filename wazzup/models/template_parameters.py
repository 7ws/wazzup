from dataclasses import dataclass


@dataclass
class PayloadParameter:
    payload: str
    type: str = 'payload'

    def __init__(self, payload: str):
        self.payload = payload


@dataclass
class ImageParameter:
    image: dict[str, str]
    type: str = 'image'

    def __init__(self, image_link: str):
        self.image = {'link': image_link}


@dataclass
class TextParameter:
    text: dict[str, str]
    type: str = 'text'

    def __init__(self, text_content: str):
        self.text = text_content
