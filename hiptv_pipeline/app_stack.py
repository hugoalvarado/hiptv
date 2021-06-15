from aws_cdk import (core,
                     aws_s3_deployment as s3deploy,
                     aws_events as events,
                     aws_lambda as lambda_,
                     aws_events_targets as targets,
                     aws_s3 as s3)


class AppStack(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        bucket_name_parameter = core.CfnParameter(
            self,
            "tv-bucket-name",
            default="tv.hugoalvarado.net",
            type="String",
            description="The name of the Amazon S3 bucket where uploaded files will be stored.")

        # main tv static site
        bucket = s3.Bucket(
            self,
            "bucket-tv-web",
            bucket_name=bucket_name_parameter.value_as_string,
            public_read_access=True,
            removal_policy=core.RemovalPolicy.DESTROY,
            website_index_document="index.html",
            auto_delete_objects=True)

        s3deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./web")],
            destination_bucket=bucket,
            retain_on_delete=False
        )

            # # lambda function used to retrieve token for streams
            # with open("./token_lambda/lambda-handler.py", encoding="utf8") as fp:
            #     handler_code = fp.read()
            #
            # lambdaFn = lambda_.Function(
            #     self,
            #     "TokenLambda",
            #     code=lambda_.InlineCode(handler_code),
            #     handler="index.main",
            #     timeout=core.Duration.seconds(300),
            #     runtime=lambda_.Runtime.PYTHON_3_7,
            # )
            #
            # bucket.grant_put(lambdaFn)
            # bucket.grant_read(lambdaFn)

        # # Run every day at 6PM UTC
        # # See https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html
        # rule = events.Rule(
        #     self, "Rule",
        #     schedule=events.Schedule.cron(
        #         minute='0',
        #         hour='18',
        #         month='*',
        #         week_day='*',
        #         year='*'),
        # )
        # rule.add_target(targets.LambdaFunction(lambdaFn))

        self.bucket_name = core.CfnOutput(
            self, "BucketURL",
            description="The message that came back from the Custom Resource",
            value=bucket.bucket_website_domain_name
        )
