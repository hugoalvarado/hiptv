from aws_cdk import (core,
                     aws_s3_deployment as s3deploy,
                     aws_s3 as s3)


class HiptvStack(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs):
        super().__init__(app, id, **kwargs)

        bucket = s3.Bucket(
            self, "bucket-tv-web",
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

        bucket_name = core.CfnOutput(
            self, "BucketURL",
            description="The message that came back from the Custom Resource",
            value=bucket.bucket_website_domain_name
        )
