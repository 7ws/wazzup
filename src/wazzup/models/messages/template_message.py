from dataclasses import asdict, dataclass

from .template_componenets import TemplateComponent


@dataclass
class TemplateMessage:
    to: str
    template: dict[str, str | dict | list[dict[str, str]]] | None = None
    messaging_product: str = 'whatsapp'
    type: str = 'template'

    def __init__(
        self,
        to: str,
        template_name: str,
        components: list[TemplateComponent] | None = None,
    ):
        self.to = to
        self.template = {
            'name': template_name,
            'language': {'code': 'pt_BR'},
        }
        if components:
            self.template['components'] = [
                asdict(component) for component in components
            ]
