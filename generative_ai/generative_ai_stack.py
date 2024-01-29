from constructs import Construct
from aws_cdk import (
    Stack
)
from generative_ai.grammarly_stack import GrammarlyStack
from generative_ai.ideal_girl_stack import IdealGirlStack
from helper.helper import get_env


class GenerativeAiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        env = get_env()

        # GrammarlyStack
        GrammarlyStack(self, "GrammarlyStack", stack_name="grammarly-stack", env=env)

        # IdealGirlStack
        IdealGirlStack(self, "IdealGirlStack", stack_name="ideal-girl-stack", env=env)