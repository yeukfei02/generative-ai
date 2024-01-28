import aws_cdk as cdk
import os

def get_env():
    account_id = os.getenv("account_id")
    env = cdk.Environment(account=account_id, region="us-east-1")

    return env