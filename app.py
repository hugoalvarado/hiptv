#!/usr/bin/env python3

from aws_cdk import core as cdk

from backend.infrastructure.stacks.chaliceapp import ChaliceApp
from frontend.infrastructure.frontend_app import FrontEndApp
from hiptv_pipeline.pipeline_stack import PipelineStack


app = cdk.App()

ChaliceApp(app, "backend-stack")
FrontEndApp(app, "web-stack", "dev")

PipelineStack(app, "pipeline-stack")

app.synth()
