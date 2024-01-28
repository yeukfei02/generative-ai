#!/usr/bin/env python3

import aws_cdk as cdk
from dotenv import load_dotenv

from generative_ai.generative_ai_stack import GenerativeAiStack
from helper.helper import get_env

load_dotenv()

app = cdk.App()

env = get_env()

GenerativeAiStack(app, "GenerativeAiStack", stack_name="generative-ai-stack", env=env)

app.synth()
