from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class Random01Gem(ComponentSpec):
    name: str = "Random01Gem"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class Random01GemProperties(ComponentProperties):
        # properties for the component with default values
        my_property: SString = SString("default value of my property")

    def dialog(self) -> Dialog:
        # Define the UI dialog structure for the component
        return Dialog("Random01Gem")

    def validate(self, context: WorkflowContext, component: Component[Random01GemProperties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def onChange(self, context: WorkflowContext, oldState: Component[Random01GemProperties], newState: Component[Random01GemProperties]) -> Component[
    Random01GemProperties]:
        # Handle changes in the component's state and return the new state
        return newState


    class Random01GemCode(ComponentCode):
        def __init__(self, newProps):
            self.props: Random01Gem.Random01GemProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            # This method contains logic used to generate the spark code from the given inputs.
            return in0
