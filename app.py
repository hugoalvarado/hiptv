#!/usr/bin/env python3

from aws_cdk import core as cdk

from hiptv_pipeline.app_stack import AppStack
from hiptv_pipeline.pipeline_stack import PipelineStack


app = cdk.App()
AppStack(app, "app-stack")
PipelineStack(app, "pipeline-stack")

app.synth()
