import requests
import boto3

def main(event, context):
    r = requests.post('https://ustvgo.tv/data.php', data={'stream': 'TruTV'})
    token = r.text.split('wmsAuthSign=')[1]

    s3 = boto3.resource('s3')
    s3_object = s3.Object('tv.hugoalvarado.net', 'ustvgotoken.js')
    s3_object.put(Body='var ustvgotoken="{}";'.format(token))

    return token
