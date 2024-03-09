# generative-ai

This project intends to use aws cdk with aws bedrock to make API with generative ai, there are two API for `text-to-text` and `text-to-image`

The model uses `amazon titan text express v1` and `stable diffusion XL 1.0`

Web ui uses streamlit

documentation: <https://documenter.getpostman.com/view/3827865/2s9YyqjNqN>

grammarly api url: <https://ii5m356p5f.execute-api.us-east-1.amazonaws.com/prod>

ideal-girl api url: <https://ev6tfvtw2g.execute-api.us-east-1.amazonaws.com/prod>

get-ideal-girls api url: <https://edw2m22scb.execute-api.us-east-1.amazonaws.com/prod>

grammarly web url: <https://generative-ai-grammarly.streamlit.app>

ideal-girl web url: <https://generative-ai-ideal-girl.streamlit.app>

ideal-girl-listing web url: <https://generative-ai-ideal-girl-listing.streamlit.app>

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

```zsh
// install dependencies
$ cd web
$ pip install -r requirements.txt

// open grammarly web
$ streamlit run grammarly.py

// open ideal girl web
$ streamlit run ideal_girl.py

// open ideal girl listing web
$ streamlit run ideal_girl_listing.py
```
