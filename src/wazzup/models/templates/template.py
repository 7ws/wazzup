from dataclasses import asdict, dataclass
from enum import StrEnum

from ..utils import skip_none_factory
from .components import Component


@dataclass
class Template:
    class CategoryChoices(StrEnum):
        MARKETING = 'MARKETING'
        UTILITY = 'UTILITY'

    name: str
    components: list[dict]
    language: str = 'pt_BR'
    category: CategoryChoices = CategoryChoices.UTILITY

    def __init__(
        self,
        name: str,
        components: list[Component],
        language: str = 'pt_BR',
        category: CategoryChoices = CategoryChoices.UTILITY,
    ):
        """
        Args:
            components: List of components that make up the template.
        """
        self.name = name
        self.language = language
        self.category = category
        self.components = [
            asdict(component, dict_factory=skip_none_factory)
            for component in components
        ]
