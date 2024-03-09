from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway
)
from aws_cdk.aws_iam import (
    ManagedPolicy
)
import os


class IdealGirlStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create infra
        self.create_infra()

    def create_infra(self):
        # create s3 bucket
        self.create_s3_bucket()

        # create ideal girl api
        self.create_ideal_girl_api()

        # create get ideal girl api
        self.create_get_ideal_girl_image_api()

    def create_s3_bucket(self):
        _s3.Bucket(
            self,
            "GenerativeAIIdealGirlBucket",
            bucket_name="ideal-girl",
            removal_policy=RemovalPolicy.RETAIN
        )

    def create_ideal_girl_api(self):
        # create lambda layer
        lambda_layer = self.create_lambda_layer(
            "GenerativeAIIdealGirlLambdaLayer")

        # create lambda
        lambda_func = self.create_lambda(
            "GenerativeAIIdealGirlLambdaFunc", "generative-ai-ideal-girl", "ideal_girl.handler", lambda_layer)

        # create api gateway
        self.create_api_gateway(
            "GenerativeAIIdealGirlApiGateway", lambda_func, 'ideal_girl')

    def create_get_ideal_girl_image_api(self):
        # create lambda layer
        lambda_layer = self.create_lambda_layer(
            "GenerativeAIGetIdealGirlsLambdaLayer")

        # create lambda
        lambda_func = self.create_lambda(
            "GenerativeAIGetIdealGirlsLambdaFunc", "generative-ai-get-ideal-girls", "get_ideal_girls.handler", lambda_layer)

        # create api gateway
        self.create_api_gateway(
            "GenerativeAIGetIdealGirlsApiGateway", lambda_func, 'get_ideal_girls')

    def create_lambda_layer(self, id):
        lambda_layer = _lambda.LayerVersion(
            self,
            id,
            code=_lambda.Code.from_asset("lambda/layer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_12],
            compatible_architectures=[_lambda.Architecture.ARM_64],
            removal_policy=RemovalPolicy.RETAIN,
        )
        return lambda_layer

    def create_lambda(self, id, function_name, handler, lambda_layer):
        lambda_func = _lambda.Function(
            self,
            id,
            function_name=function_name,
            runtime=_lambda.Runtime.PYTHON_3_12,
            memory_size=1000,
            code=_lambda.Code.from_asset("lambda"),
            handler=handler,
            architecture=_lambda.Architecture.ARM_64,
            timeout=Duration.minutes(5),
            tracing=_lambda.Tracing.ACTIVE,
            layers=[lambda_layer],
            environment={
                "PYTHON_ENV": os.getenv("PYTHON_ENV"),
            },
        )

        lambda_func.role.add_managed_policy(
            ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess"),
        )

        return lambda_func

    def create_api_gateway(self, id, lambda_func, type):
        api_gateway = _apigateway.LambdaRestApi(
            self,
            id,
            handler=lambda_func,
            default_cors_preflight_options=_apigateway.CorsOptions(
                allow_origins=_apigateway.Cors.ALL_ORIGINS,
                allow_methods=_apigateway.Cors.ALL_METHODS
            ),
            proxy=False,
            integration_options=_apigateway.LambdaIntegrationOptions(
                timeout=Duration.seconds(29)
            ),
            deploy_options=_apigateway.StageOptions(
                data_trace_enabled=True,
                tracing_enabled=True,
                metrics_enabled=True
            )
        )

        api = api_gateway.root.add_resource("generative-ai")
        api.add_method("GET")  # GET /generative-ai

        if type == 'ideal_girl':
            ideal_girl = api.add_resource("ideal-girl")
            ideal_girl.add_method("GET")  # GET /generative-ai/ideal-girl
        elif type == 'get_ideal_girls':
            ideal_girl = api.add_resource("get-ideal-girls")
            ideal_girl.add_method("GET")  # GET /generative-ai/get-ideal-girls
