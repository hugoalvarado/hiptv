#!/usr/bin/env python3

from aws_cdk import core as cdk

from hiptv_pipeline.app_stack import AppStack
from hiptv_pipeline.pipeline_stack import PipelineStack
from backend.infrastructure.stacks.chaliceapp import ChaliceApp

app = cdk.App()
ChaliceApp(app, "backend-stack")
AppStack(app, "web-stack", "dev")

PipelineStack(app, "pipeline-stack")

app.synth()
