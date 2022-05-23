import os, sys
import aws_cdk as cdk

sys.path.append('../backend')
sys.path.append('../frontend')

from frontend.infrastructure.frontend_app import FrontEndApp
from backend.infrastructure.stacks.chaliceapp import ChaliceApp



class AppStage(cdk.Stage):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        backend_service = ChaliceApp(self, "HipTvBackEnd-" + id.upper())
        frontend_service = FrontEndApp(self, "HipTvWeb-" + id.upper(), stage=id.lower())

        self.bucket_name = frontend_service.bucket_name
