import requests


def grab_token():
    r = requests.post('https://ustvgo.tv/data.php', data={'stream': 'TruTV'})
    return r.text.split('wmsAuthSign=')[1]


if __name__ == '__main__':
    token = grab_token()
    print('var ustvgotoken="{}";'.format(token))
