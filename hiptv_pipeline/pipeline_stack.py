# Based on  https://cdkworkshop.com/30-python/70-advanced-topics/200-pipelines/3000-new-pipeline.html
import aws_cdk as cdk
from aws_cdk import (
    aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_lambda as lambda_)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct


# from .app_stage import AppStage


class PipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, *, repo_name: str = None,
                 lambda_code: lambda_.CfnParametersCode = None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # source artifact represents the source code
        source_artifact = codepipeline.Artifact()
        # cloud assembly artifact represent the result of synthesizing the CDK app
        cloud_assembly_artifact = codepipeline.Artifact("CdkBuildOutput")

        gh_owner = "hugoalvarado"
        gh_repo = "hiptv"
        gh_branch = "master"

        source = CodePipelineSource.git_hub(
            "{}/{}".format(gh_owner, gh_repo),
            gh_branch,
            authentication=cdk.SecretValue.secrets_manager("hiptv-github-token"),
        )

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="HipTvPipeline",
            # important: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.pipelines/README.html#a-note-on-cost
            synth=ShellStep("Synth",
                            input=source,
                            commands=[
                                "npm install -g aws-cdk",
                                "python -m pip install -r requirements-dev.txt",
                                "cdk synth"
                            ],
                            env={}
                            ),
        )

