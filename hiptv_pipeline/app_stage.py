from aws_cdk import core

from .app_stack import AppStack

class AppStage(core.Stage):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = AppStack(self, 'TvService')

    self.bucket_name = service.bucket_name