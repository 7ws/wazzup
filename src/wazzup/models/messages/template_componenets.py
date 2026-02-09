from dataclasses import asdict, dataclass


@dataclass
class ComponentHeader:
    parameters: list[dict[str, str]]
    type: str = 'header'

    def __init__(self, parameters):
        self.parameters = [asdict(parameter) for parameter in parameters]


@dataclass
class ComponentBody:
    parameters: list[dict[str, str]]
    type: str = 'body'

    def __init__(self, parameters):
        self.parameters = [asdict(parameter) for parameter in parameters]


@dataclass
class ComponentFooter:
    parameters: list[dict[str, str]]
    type: str = 'footer'

    def __init__(self, parameters):
        self.parameters = [asdict(parameter) for parameter in parameters]


@dataclass
class ComponentButton:
    parameters: list[dict[str, str]]
    sub_type: str = 'quick_reply'
    index: str = '0'
    type: str = 'button'

    def __init__(self, parameters):
        self.parameters = [asdict(parameter) for parameter in parameters]


@dataclass
class TemplateComponent:
    type: str
    parameters: list[dict[str, str]] | None = None

    def __init__(self, cathegory: str, parameters=None):
        self.type = cathegory
        if parameters:
            self.parameters = [asdict(parameter) for parameter in parameters]
