#!/usr/bin/env python3

from constructs import Construct
import aws_cdk as cdk
from aws_cdk import App, Stack

from backend.infrastructure.stacks.chaliceapp import ChaliceApp
from frontend.infrastructure.frontend_app import FrontEndApp
from hiptv_pipeline.pipeline_stack import PipelineStack


app = cdk.App()

app_name = "hiptv"

ChaliceApp(app, "{}-{}".format(app_name, "backend-stack"))
FrontEndApp(app,  "{}-{}".format(app_name, "web-stack"), "dev")
PipelineStack(app,  "{}-{}".format(app_name, "pipeline-stack"))

app.synth()
