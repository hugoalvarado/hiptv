import os
import boto3
from chalice import Chalice


app = Chalice(app_name="hiptv")
dynamodb = boto3.resource("dynamodb")
dynamodb_table = dynamodb.Table(os.environ.get("APP_TABLE_NAME", ""))


# sources for channels:
# http://www.reloltv.com/ Playerjs
# ustvgo.la ..
# http://123tv.live/
# https://github.com/iptv-restream/iptv-channels
#
# @app.route('/update_keys')
# def update_keys():
#     import copy
#     response = dynamodb_table.query(
#         KeyConditionExpression=Key('pk').eq('channels')
#     )
#     for item in response['Items']:
#         new_item = copy.deepcopy(item)
#
#         dynamodb_table.delete_item(
#             Key={
#                 'pk': item['pk'],
#                 'sk': item['sk']
#             }
#         )
#
#         new_item['category'] = new_item['sk'].split('#')[1]
#         new_item['title'] = new_item['sk'].split('#')[3]
#
#         print(new_item)
#
#         dynamodb_table.put_item(Item=new_item)


def get_all_channels():
    response = dynamodb_table.query(KeyConditionExpression=Key("pk").eq("channels"))
    return response["Items"]


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/channels", cors=True)
def channels():
    return get_all_channels()
