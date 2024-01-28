# generative-ai

generative-ai

documentation: <>

api url: <>

## Requirement

- install python (v3.12.1)
- install cdk-cli

The cdk.json file tells the CDK Toolkit how to execute your app.

## Testing and run

```zsh
// create virtualenv
$ python -m venv .venv

// activate virtualenv
$ source .venv/bin/activate

// install dependencies
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt

// install lambda layer dependencies
$ cd lambda/layer/python
$ pip install -r requirements.txt

// run test case
$ pytest
```

```zsh
// copy .env file
$ cp .env.sample .env

// list all stacks in the app
$ cdk ls

// deploys the CDK toolkit stack into an AWS environment
$ cdk bootstrap

// compare deployed stack with current state
$ cdk diff

// synthesize the CloudFormation template
$ cdk synth

// deploy specific stack to your default AWS account/region
$ cdk deploy <stackName>

// deploy all stack
$ cdk deploy --all

// destroy specific stack
$ cdk destroy <stackName>

// destroy all stack
$ cdk destroy --all

// check more command
$ cdk --help
```
