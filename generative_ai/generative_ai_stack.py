from constructs import Construct
from aws_cdk import (
    Stack
)
from generative_ai.correct_grammar_stack import CorrectGrammarStack
from helper.helper import get_env


class GenerativeAiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        env = get_env()

        CorrectGrammarStack(self, "CorrectGrammarStack", stack_name="correct-grammar-stack", env=env)

    