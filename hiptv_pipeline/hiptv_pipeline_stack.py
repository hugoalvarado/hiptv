from aws_cdk import (
    core, aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_lambda as lambda_)
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction


class HiptvPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, repo_name: str = None,
                 lambda_code: lambda_.CfnParametersCode = None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact("CdkBuildOutput")

        gh_owner = ""
        gh_repo = ""
        gh_branch = ""

        pipeline = CdkPipeline(
            self,
            "Pipeline",
            cross_account_keys=False,
            # important: https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.pipelines/README.html#a-note-on-cost
            pipeline_name="MyAppPipeline",
            cloud_assembly_artifact=cloud_assembly_artifact,

            source_action=codepipeline_actions.GitHubSourceAction(
                action_name="GitHub",
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager("GITHUB_TOKEN_NAME"),
                # Replace these with your actual GitHub project name
                owner=gh_owner,
                repo=gh_repo,
                branch=gh_branch
            ),

            synth_action=SimpleSynthAction.standard_npm_synth(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,

                # Optionally specify a VPC in which the action runs
                vpc=ec2.Vpc(self, "NpmSynthVpc"),

                # Use this if you need a build step (if you're not using ts-node
                # or if you have TypeScript Lambdas that need to be compiled).
                build_command="npm run build",
                synth_command=""
            )
        )

        # code = codecommit.Repository.from_repository_name(self, "ImportedRepo",
        #                                                   repo_name)
        #
        # cdk_build = codebuild.PipelineProject(self, "CdkBuild",
        #                                       build_spec=codebuild.BuildSpec.from_object(dict(
        #                                           version="0.2",
        #                                           phases=dict(
        #                                               install=dict(
        #                                                   commands=[
        #                                                       "npm install aws-cdk",
        #                                                       "npm update",
        #                                                       "python -m pip install -r requirements.txt"
        #                                                   ]),
        #                                               build=dict(commands=[
        #                                                   "npx cdk synth -o dist"])),
        #                                           artifacts={
        #                                               "base-directory": "dist",
        #                                               "files": [
        #                                                   "LambdaStack.template.json"]},
        #                                           environment=dict(buildImage=
        #                                                            codebuild.LinuxBuildImage.STANDARD_2_0))))
        #
        # lambda_build = codebuild.PipelineProject(self, 'LambdaBuild',
        #                                          build_spec=codebuild.BuildSpec.from_object(dict(
        #                                              version="0.2",
        #                                              phases=dict(
        #                                                  install=dict(
        #                                                      commands=[
        #                                                          "cd lambda",
        #                                                          "npm install",
        #                                                          "npm install typescript"]),
        #                                                  build=dict(
        #                                                      commands=[
        #                                                          "npx tsc index.ts"])),
        #                                              artifacts={
        #                                                  "base-directory": "lambda",
        #                                                  "files": [
        #                                                      "index.js",
        #                                                      "node_modules/**/*"]},
        #                                              environment=dict(buildImage=
        #                                                               codebuild.LinuxBuildImage.STANDARD_5_0))))
        #
        # source_output = codepipeline.Artifact()
        # cdk_build_output = codepipeline.Artifact("CdkBuildOutput")
        # lambda_build_output = codepipeline.Artifact("LambdaBuildOutput")
        #
        # lambda_location = lambda_build_output.s3_location
        #
        # codepipeline.Pipeline(self, "Pipeline",
        #                       stages=[
        #                           codepipeline.StageProps(stage_name="Source",
        #                                                   actions=[
        #                                                       codepipeline_actions.CodeCommitSourceAction(
        #                                                           action_name="CodeCommit_Source",
        #                                                           branch="main",
        #                                                           repository=code,
        #                                                           output=source_output)]),
        #                           codepipeline.StageProps(stage_name="Build",
        #                                                   actions=[
        #                                                       codepipeline_actions.CodeBuildAction(
        #                                                           action_name="Lambda_Build",
        #                                                           project=lambda_build,
        #                                                           input=source_output,
        #                                                           outputs=[lambda_build_output]),
        #                                                       codepipeline_actions.CodeBuildAction(
        #                                                           action_name="CDK_Build",
        #                                                           project=cdk_build,
        #                                                           input=source_output,
        #                                                           outputs=[cdk_build_output])]),
        #                           codepipeline.StageProps(stage_name="Deploy",
        #                                                   actions=[
        #                                                       codepipeline_actions.CloudFormationCreateUpdateStackAction(
        #                                                           action_name="Lambda_CFN_Deploy",
        #                                                           template_path=cdk_build_output.at_path(
        #                                                               "LambdaStack.template.json"),
        #                                                           stack_name="LambdaDeploymentStack",
        #                                                           admin_permissions=True,
        #                                                           parameter_overrides=dict(
        #                                                               lambda_code.assign(
        #                                                                   bucket_name=lambda_location.bucket_name,
        #                                                                   object_key=lambda_location.object_key,
        #                                                                   object_version=lambda_location.object_version)),
        #                                                           extra_inputs=[lambda_build_output])])
        #                       ]
        #                       )
