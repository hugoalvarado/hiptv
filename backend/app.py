import os
import boto3

from chalice import Chalice
from boto3.dynamodb.conditions import Key

app = Chalice(app_name='hiptv-backend')

dynamodb = boto3.resource('dynamodb')
dynamodb_table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE_NAME', 'channels'))

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
    response = dynamodb_table.query(
        KeyConditionExpression=Key('pk').eq('channels')
    )
    return response['Items']

@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/channels', cors=True)
def channels():
    return get_all_channels()


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
