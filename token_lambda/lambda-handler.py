import requests

def main(event, context):
    r = requests.post('https://ustvgo.tv/data.php', {'stream': 'TruTV'})
    token = r.text.split('wmsAuthSign=')[1]
    return token
