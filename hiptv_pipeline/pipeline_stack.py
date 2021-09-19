# Based on  https://cdkworkshop.com/30-python/70-advanced-topics/200-pipelines/3000-new-pipeline.html
from aws_cdk import (
    core, aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_lambda as lambda_)
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction

from .app_stage import AppStage


class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, repo_name: str = None,
                 lambda_code: lambda_.CfnParametersCode = None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # source artifact represents the source code
        source_artifact = codepipeline.Artifact()
        # cloud assembly artifact represent the result of synthesizing the CDK app
        cloud_assembly_artifact = codepipeline.Artifact("CdkBuildOutput")

        gh_owner = "hugoalvarado"
        gh_repo = "hiptv"
        gh_branch = "master"

        pipeline = CdkPipeline(
            self,
            "Pipeline",
            cross_account_keys=False,
            # important: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.pipelines/README.html#a-note-on-cost
            pipeline_name="HipTvPipeline",
            cloud_assembly_artifact=cloud_assembly_artifact,

            source_action=codepipeline_actions.GitHubSourceAction(
                action_name="GitHub",
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager("github-hiptv-pipeline"),
                # Replace these with your actual GitHub project name
                owner=gh_owner,
                repo=gh_repo,
                branch=gh_branch
            ),

            synth_action=SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                # Optionally specify a VPC in which the action runs
                # vpc=ec2.Vpc(self, "NpmSynthVpc"),
                install_command='npm install -g aws-cdk && pip install -r requirements-backend.txt',
                # Use this if you need a build step (if you're not using ts-node
                # or if you have TypeScript Lambdas that need to be compiled).
                build_command="",
                synth_command="npx cdk synth"
            )
        )

        pipeline.add_application_stage(AppStage(self, 'QA'))
