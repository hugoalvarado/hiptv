import os
import boto3
from chalice import Chalice
from boto3.dynamodb.conditions import Key

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


# @app.route("/channels", cors=True)
# def channels():
#     return get_all_channels()

@app.route('/channels', cors=True)
def channels():
    return all_channels


all_channels = {
    'news': [
        {
            'title': 'CNN',
            'url': 'https://cnn-cnninternational-1-de.samsung.wurl.com/manifest/playlist.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/cnn-269x151.png'
        },
        {
            'title': 'BBC',
            'url': 'http://ott-cdn.ucom.am/s24/04.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2020/01/bbc-america-269x151.png'
        },
        {
            'title': 'CBS',
            'url': 'https://cbsnewshd-lh.akamaihd.net/i/CBSNHD_7@199302/master.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/cbsn-269x151.jpg'
        },
        {
            'title': 'ABC',
            'url': 'https://content.uplynk.com/channel/3324f2467c414329b3b0cc5cd987b6be.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/abc-269x151.jpg'
        },
        {
            'title': 'SKY',
            'url': 'http://skydvn-sn-mobile-prod.skydvn.com/skynews/1404/latest.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvDZ6urGm3q1pjnKiNhEUDtD8AcHionSqY2g&usqp=CAU'
        },
        {
            'title': 'RT',
            'url': 'https://rt-usa.secure.footprint.net/1105.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY6T5mgkdBdd-cBGv8QnDmMLacXwg5FFTz6g&usqp=CAU'
        },
        {
            'title': 'FOX',
            'url': 'https://h1.ustvgo.la/FOX/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIREhISExIQFhITFxAVGBUVFRoVFRAYFRUWFxUYFhYYHigiGBolGxUWITEtJSkrLi4uGB8zODMsNygtOisBCgoKDg0OGxAQFy0mICUtLS8tLS0uLS0vLS0tLS0tLS0tLS0vLSstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBIgACEQEDEQH/xAAcAAABBAMBAAAAAAAAAAAAAAAAAQIGBwMEBQj/xABPEAABAwICBAoAEQkHBQAAAAABAAIDBBESIQUGBzETFCJBUWFicYGRFiUyQlJTVHOCkqGisbKz0uEXIzRDcpS0wtEkMzV0g9PwFURjk8H/xAAaAQADAQEBAQAAAAAAAAAAAAAAAQIDBAUG/8QANREAAgECAgYHBwUBAQAAAAAAAAECAxExoQQSIUFR0RMUFSIyUmEFFlNxgcHwBkJDkbHhov/aAAwDAQACEQMRAD8AqeyLJyF0HMNsssQTFmYMk0JioSoVEiISoQBjlWGyySHNNUstDbIsnISAbZPjakWdrbJoTBCVCokRZonXWJOabIQGZYZncyzOflda6pslIRCVCkoRYHNsVsJkjUmhpmCyLJyFJQ2yLJyEAZGHJPWOIrKqRLEQlQmIRYZRms6xyhJjRhsiychSUNsiychAC2RZOsiyYhAFsWWGMZrYsqQmNsiydZFkxDbJHZJ9limQBhRZOsiygobZFk6yLIAWJqzWQxtgnWVpE3G2RZOsiyAG2QnWWKU8yAEa/PqWSywLNGbpJ3GxbIsnWRZMQ2yLJ1kWQBqltikss8redYrKGrFIbZFk6yLIAG5FZ7LBZZo9ycRMWyLJ1kWVCG2TXjJZLIsgDUsiyUhFlBQlkWTrIsgB1kWSrp6K1eq6prn09PLK1pwlzBcB1gbHrsQfFN7BWOdC1ZrLuxalaRH/AGVT8X8U/wBBmkfcVT8X8U01xE0+D/oj9kWUg9BmkfcVT8X8VxqmmfG90b2lr2Etc05FpG8FNNPBis1ijBZYJMyth5sCU6g0XPPnDBPIOmONz2jvcBYIlsHHaadkWXVq9XayIEyUlU1o3kxPIHWSBYDvXLBupG1bESydE25W/orQdTVYuLwSS4LYsAvhvuv5FdaPUrSIH6FU/F/FF1faws7YHBsiy3tJ6KnpnBs8UkTnC4DxbEL2uOlYaOkkme2KJjnyPJDWNF3OIBJsO4E+Csg17JbLv+gzSPuKp+L+K1dIauVlOzhJqaaNlwMTxYXO4JXXEdnwZyHZLXK7dHqzW1LGyw0s0kTsQa9rbtdhJa62fMQR4LMdSNJe4qn4v4qXJcSlF2wI9ZKw2Skf86FtaN0bNUv4OCN8kli7CwXNhvPyhADAEWXci1L0kN9FU/F/Fa9Nq/VySSRMp5XSxW4Rgbd0d92Icyq64kuLW45dkWUg9BmkfcVT8X8UegzSPuKp+L+KLrigs+D/AKI/Zazm2Up9BmkfcVT8X8Vpu1WrXSGEUsxma0PdHh5Qa42DiOi6Ta4jSfBnCsiykXoH0l7hqfij+q4MjC0lpBBaSCDvBBsQfFJNMdrGOyyQroaK1eq6ppfBTyytacJLBcA2vbvsQsmkNWq2mZws1NNHGCBic2wBOQHii6uFmaFktkq7cWqGkHNDm0dQWuAIIbkQRcEeCt2WLIV3gjhWRZbWkKGWneY5mOjkABLXZEAi4v4LtaE1Hr6sB8cGGNwuJJXCNrhzWB5RHWG260m0ttxpNuyRFJG5ptlYk+yOutcSUhPRjePlwKI6d1dqqJwbUwujxEhrrhzH29i9pI3Z2yPUoUk3sZbi0tqOTZFk5CYh1lc2w39EqP8AMH7GJU3ZXFsTNqSo/wAwfsolNTwl0vEWTiRiWHEq21m2iVNNVTwMipyyNwALg/Ebsa7OzwOdYxi5OyNpTUVdln3VB66aPkk0rUwxtLpJJW4WjeS+Nr/AWN+qy7P5Vqz2mk+LJ99SzUKEzmXSczI2z1PIbhBs2OMBhIxEm7izPPc0LRKVPa0ZScalkmJqns4p6YNkqGsnqMjyheKI7xgYd5HS7wAU4bkABkBuA3DuCw4lDdrVY9mj3BjiOEkjY62RLTcuHcbAHqus9sntNdkVsJw2S+YPiCo/rLqdR1wPCxBstrCaMBsre825QudzrhVnsZrHsq3whxET4nvLPW4mlgDgOY2JCubEiUdV2CMtZFHU1NU6A0gxz+VE4EF7QcNRESMVhzPabG3MQOYq9KeobI1r2EOa4BzSNzgRcFcXW3Qra6mfCQMfqo3H1kgBwnuNyD1EqGbJ9YjY0MpsW4nRX6L3fH3g3I8ehU+9G+9ELuStueBKtoGrgr6YhoHDxXfEek+uZfocBbvDTzLgbI9WjFG6slaRJKC2MEWLI75utzFxHkB0qf4kuNTrO2qW4K9zLdUdtX1m41UcBGbw05Iy3Pk3Pd4epHj0qwdousvE6YhhtPNdrLb2D1z/AAGQ6yFQpWlKP7jKrL9pfWyY+lVN31X8RKpfiUO2Vm2i6bvqf4iVSvGs5eJmscEUrta1Z4tUcZjbaGpJLrbmTZl3g71XfiWLY5/iQ95n/kVv6waKjrKeSnk9TIMjzscDdjh1ggFVRsxon0+lnQyC0kcdQ1w5rjBmOkEWI6iFopXi0ZyjaafEu3EoFqY7030v3x/SVN8agWpp9N9L98f0lZxwfy+6Llivn9mWHiRiWCWSzXHqP0LzyzXessP7fJuH638U4QcsAnPV3Ho3Eq/qa7gtYWC+U1O2Lzu8fKwKtG66VhNhXyknmEu9Y49My8YiqZZHvkjdG7E43dZjr2v5+a1jRa3mUqya2I9H4l5z1/oeB0jVsAyMhkH+qBJ9LivQrZQQCNxsR1gqnNtFHhq4ZQP72It7zE76bPb8izpPaXWXdJxsko+C0bETvldLKe4uwt+awLpbQKLh9HVTALuEZe3vjIePq28Vt6ApeApaeH2uKJh6y1gBPiblb0gDgWnc4EEdIORUN7bmiWyx5o0TSmeSKIfrHxx5b+W4DLzXp5gAAA3CwHUBkFQ2znRRGlGxOzNMZnO6zFdgPxnNPkrl07X8BTTze1xyOHWQ04R4my1qu7SX5cypKybf5YherGhWV+kKyvmaHRRzOZC05te6Pk4yDvDQGkdZ6grIxKH7LyP+nQ9JdUFx6Twz9/hZdrWCjfUU00Mb8D5GFrXZ2BPTbOx3G3MVE/Fb6Fw8N/qdCGtjeS1skbnDeGuBI7wCmaToYqiJ8MzA+N4sWn5COgjeDzKiazVHSNI4SNgkDo+U2WC0mEjnGDlDxaLre0ptTrpLsjEUBGTi0YpARvvjybnzYclTp38LuSqlvErEZ1p0G6hqpadxJDSCxx/WMcLsd38x6wVyrLarq2Wd5fLI+R59c9xce7PcFr2WywMHa+wdZW7sYNqWo9/P2UaqWytbY+bUs/v5+yjU1fCXS8RYeNc2q0BRyvdJJS0z3uzc50TXOdlbMkZ5ALbxrmVWstJE90ck8bXtyLSTcZX6OgrnSe46G1vMWkdWaFsUpFHSghkhBELAQQ0kEZLf1bjEdJTMG5sUQ+aFya/WuidFK0VMRJZIALnMlpAG5ZNSa8TUUBvymNEbupzOT9Fj4qmnq7SU432cCRY1CtrpvQD36L6HqXY1DdrBvQj36L6HJQ8SHPwsiGyPLSH+jN9aNXRjVK7Kcq//AEZvrMVx41VXxEUvCbGNURrCXQaQndESHRzue0jeHYsW7nzO5Xc+UNBJNgAST0Ab1WepujOO1kta8fmmSOe0H10hN2Drwix78Kqk9W7Yqy1rJFnUUz3Rxukbhe5rS5t74HEAkX6is+Na+NGNYmxR+0OrmkrphMMJYcDW8wjGbCDzgg4u8lRqyt3afq9xiLjMbbzQDlWGckWZI6y0kuHViVS2XVCV0ck42kXhswd6WU3fU/xEq6mtGljS0z5wL8GYiR7JpkaHAdeElcfZqbaNp++o/iJU/aI70vqO6P7Riwfj+v3OheD6fYkdHWMljZIwgse1rmnpBFwubNoVpro61uTxHJC8ezac2HvBuO4joCg2yrWG16KQ77viv5vZ/MPhKysaUo6rsOL1lcz41BdTz6baW74/pKmeNQjVI+mulO9n0lEcH8vuhSxXz+zJ9jT+GPSfNacslmuI3gE/Iqch170gQDxjeB+qi+4nCm54BOooYlsa3Sk0NYLn+5m5+wVQdlIavW+ulY+N892Pa5rhwcYuHCxFw248FwrLqpQcFtOSrUU2rF56l1/DUVO++YZgPfGSw/Vv4rma/aI4yaE2vgqYwf2H5v8AqDyC5myqtvBNEf1bw4dzx/Vp81NyQd/euWXdm7HXB60Fcx6c0kKenmnNvzbHu7yBkPOy2o5g4Bw3EAjuIuFDNqVXhoHMvnK+JneA7GfqLqal1vC0NM4m5EbWHvZyD9VK3duPW71jV1f0PwWk9Iz2yeIcB98AfJ85g+RM2o12CiLAc5nsZ4Dlu+qB4qUB3/OlVntXrcUsEV8mMc8jrebD5GnzVU+9NfmBFXuwf5iN2ca1MpsVNM4Nie7Ex59TG4+qDjzA5Z8xv0q02yAgEEEHMEZg9xVIUOp9dLYincwHnlIi82uOIeS3quCv0SIiJwGyYuSwl8QLfWkPaBcg3yA3HoWk4RlLuvaZwnKEe8thcWNcvT+r9NWtwzxgutyZByZWfsv3+BuOpQrQm0WRz2RzxMs4tbjYSC0k2BLTe48VYWJYyg44m0Zxmth5/wBZtBvoqh8DziAs5j7WEjDuNuY7wesHqXLsrJ2xxjFSO9dadveAYyPIk+army6YO8U2c81aVhVamyfKmm65T9nGqusptqdrLHRRPjfHI4ufju3DYclozuRnknUi5RsiaclGW0tPEqb1z/Tqn9pv1GqX/lCg9qn+Z95QjTtaJ6iWZocGvIIDrXFmgZ27lNCEot3RdecZRVmcyy7+o2s/FJnNkP5iUjF/43bg/utkfDoXAmNgVq2W00mrMwg2ndHodkocAQQQRcEZgg84K0dOaLjq4XQy4sLrEFps5jhmHAnnVQ6A1pqKOzWOD4va35tHThO9vhl1KbUe0encPzkczD1WePAix+RcjpSWB2RqxeJ1dWNUYKFzntdJJI4Ycb7DC29yGtbuvYXvfdzKRYlEZNfqW12iZ3Vht9JUd0zrvPMC2IcCw84N5D8L1vh5pqlOT25idWnFbMjv656bMhFBTkOllIY8jcwHe0nuzPQAVJdD0DKaFkLNzBv53k5uceskkqsNU9LwUj3yyMlfIRhbhw2aDm48ojlHd3X6SpP+UKD2qf5n3k50peGK2f6yadSPik1f/ESbTmlm0sD5netGQ9k4+pHn/wDVxdRNZjWRuZIRw8Zz5sbSeS4Dq3HuHSoLrprLxxzGtDmxMF8LrXLjvJsbdQ8elcbQmk30szJmb2nMXye05OafD5bFNUu7txE63eusC+8SpXXfQHE6g4BaCW7o+hvsmeB3dRCmP5Sqf2if5n3lytZdcKWsgdEYZw71THEM5DwDY+q3ZkHqKmEZxeBdSUZLElOzo+l1P31H28qybQD/AGCo7o/tGKJasa7Q0tNFA6KZzmcJctw4Tike8Wu4Hc5O1k14hqaaWFsUzXPw2LsNhZwdnZ1+ZDhLXvbeHSR1LX3EEpp3RvbIwkPYQ5pHMRuV66vaYbVwMmbYEizm+wePVN/5zEKibKQ6naymhe/E1zonjNrbXDhucLkDdkfDoWtWGsrrEypT1XtwLmxKGaqn0z0n3s+krD+Uqn9on+Z95cHQ+tsUNXV1BjlLajDhaMOJtjflXNvJYxpys9n5c1lUjdbd/wBmWs43FjuOSjrdRdGjdTH94qP91cn8pVP7RP8AM+8j8pVP7RP8z7yShNYIpzg8Wdf0D6O9zu/eKj/dUB1y0bFT1JjhZhZgYbYnPzN75vJPyqVR7Rqc/qZ/mfeUR1n0o2qnMrGuaC1jbOtfk36CVtRjPWvLAxrShq7LXOns2q8FUWc0rHDxbZw+TF5q0cSpDRNYYJopbHkPa4gbyL8oDvFwp5+UKD2qb5n3kq1OTldIKFSKjZs5m1yruaaLo4SQ+Nmt/mXQ2UVd6aWM/q5SR1Ne0H6wd5qFa46UFXPwzWuDcDGAOtcWuTu63FZtS9Ym0L5S9r3Nka0WZa4c05HlEcxPyIcHqW3gqi6S+4ubEqU1vreFr6h17tDhGOoRtDfpDvNTE7SoOaCovzXwW+sq0e8lxcd5Jcesk3KKMHF3Y601JWRcupOmhUU7WkjhYg1jxz2GTXdxA87rsVtLHMwxysa9htdrhcZbiOg9YzVKaOrpIXtlicWuHOOcc4I5wpvo/aCLATQm/soyCD8F27zKVSi07xCnXi1aR3KLU+hheJGQnE03bjkke1pG4hrnEHxupBiUQfr7TAZNmJ6MIHy3UZ1j11nnYWRDgmHI2N3uHRiywju81HRVJPaadLTitmRp7RdMtqakNYbxwAsBG5ziQXkdVwB8FRVPsiy6Yqyscrd3cyMbchb1lq07c+5bdlrFbDKT2iWRZLZKmRc06k52WGye83JKSyh4mqwG2To2XNktlsU0eV+lCV2DdjJZLZLZFlZlcSyxyusFlstOZ9z1JPYUtpiKLJ1kWUGg2yWyWyLIASyLJbIsgBtkWTrIsgBtkWTrIsgBLJLJ1kWQAjDY3W83PNaVlmpn8ycSZcTYsiyWyLKzO5jey4stIhdKy1amOxv0pSRcWa9kWTrIsoLM9McrdCz2WrTmx71uWVrAzliNsmSNuCslkWTsK5zrIsnvbYkJLLM1NqkbvK2bLQbVvG4t8kcek6QuFe06a/a8uZ9C/wBLaQ/5Y58jfssVQbDvyWrx6TpCR1U87y1N+1KfleXMF+ltI+LHPkJZFknGXdlHGXdlR2lDyvLmX7sV/ixz5D2MubLeDVz21Lxuw+Sdx6TpCqPtOmv2vLmS/wBL6Q/5Y58jfsiy0OPSdIRx6TpCfalPyvLmT7raR8WOfIz1L+Za1kGqcfY+STjLuypftKD/AGvLmaL9L11/LHPkLZFknGXdlHGXdlLtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyFsiyTjLuyjjLuyjtKHleXMPdiv8AEjnyN2F1x1rLZc9tU8bsPkl49J0hX2pDyvLmQ/0tX+LHPkb9kySO4stPj0nSEcek6QjtSn5XlzD3W0j4sc+Q2yLINS7spOMO7KjtKHleXM092K/xI58hQt9uYBXP4w7sp7ax43Fqpe06a/a8uZL/AEvXf8sc+Rv2RZaHHpOkI49J0hPtSn5XlzI91tI+LHPkPqW8rvWKyV1U878Kbxl3ZUdpQ8ry5mi/TFdfyxz5GNInWRZeOfbWGpUtkWQFhEJbIsgLCJE6yLICw1KlsiyAsTPZvoSkrZHw1GMSYcTCxwaHYcpG2tvzB7r9C5GumgjRVUkOeDJ0ZPrmuzb4jMHrBWloPST6WeOZnqo3h1r2xdknoIuPFWztN0ayuoY62EXLGh9+cxPtiv1tNj1cpbxipU3bFf4eRVq1NH02OtJ6k9nopf8Adn9spdrbqytL6lUlHo1s8/C8Zc1gDA4BvCPzDbW9aLk5+tK42zDQHGqxrnC8UFpHdBLTyW+LhfuaVvbXdP8AD1PF2OvHT3abbjKb4/Kwb1EOShFKDm/kh6TVqVNKho9OTVu9Nrhw+v3Rx9negYq6qMUuPBglPJNjdpbbO3Wma/6Fioqt0MWLAAx3KNzdwuc12tjH6cfepP5Vr7YP8Qf73D9RGquivvuCqz7RdPWerq4br7Np09nGpNLXU8ks3CYmylgwOwiwa13R0uK7h2ZaOkuIqmTFuyfG8A9Ytf5Vn2MfoM3vzvs41TdWSJHEWuCbEDdyitG4QhFuN7nLGOlV9JrQhWcVF7N637MfT1JlrNsyqaZpkicJmNzOFpbI0dODO47iVBCrY2Sa0SySGkle57cLjGXnE9hZhu3Ecy22Y6LKJ7S9Espq6UMADHhsgaNzcW8DquCs6kI6qnDA6tD0qt08tG0i2sldNb1+fLfsJNqTqLRVNEyonMjSS/EWvDWNDCRc3GQsF0vQToL3Wz95i/otvUundJoJ8bBie+KsY1vsnOxgDPrKrs7PdJ3/AEY/HZ/VbNJRjaF9hwRlUq1qqlpWpqyaSbWF3hdrA29oGg6CmbCaOYSF3Ch9pWyYQA3D6ndvKiejdHyVErIYmkvcbNaOfnPcAASeoJ2k6CSCR0MrSJG2Dmkg2uARmMtxCs/YjoxobPUEAuu2JuXqRbE7Pru3y61il0lSyVj0p1Xoeh68p673N774b3sWOO4yaP2YUlPFwldON3K5YZEzqMj8zz55dy2GaiaGqw5tNOxzxzwzsmw/tNucvJV7r1p+SrqpHFxEbC5sbQeSxoJaLDdiO8nfnbcAuDTVL43ska94c0gtc11nNI5wRuVupSTso7DmhoWm1IKpLSGpPba2xf4v/Lt6nb1v1Sm0e8B9jG6+GRos19t4I9a7q+lR1XpNKNKaFdLI0cIIpH5DdLCHZjoxBvk+yowtWdaCi1bBnX7N0mdeEo1F34u0hqE6yLLI9GwiEtkWQFhEJbIsgLDUJ1kWQFhEJbIsgLCoSoUl2EQlQgLCISoQFhEJUICwiEqEBYRW5sh0u2WGWglsRZ7mNO4xusJW273X+GVUi6er2lX0lRHOy/IcDb2Y3FviLjxWtKepK5w+0dE6xQcFjivmsP7w+t9xcMdJHoShqJAWmRz34T7MklsAPTZuZ+EqOnlLnFziSS51yd5JNySpvtL1uZXOjZA8mFgvctc3G92/kuAOQyHwlBVdeSb1Y4I5/ZOjzjCVar45u7vjbdz+Vie7Gf04+9SfyrX2wf4g/wB7i+otXZ1puGiqeGnLsPBvbdrS43JFsh3FYtoOmYayrdNCXYC1jQXNLTdrbHI5o1l0NvUlU59pueq7amNtm7fgWLsY/QZvfn/Zxqm61p4R+R3n6xVi7N9caOipnxTueHPkc8BsbnjCWtbvaOlpXWdrjoRnKZStc4ZjDTMDr9RfaxVuMZ0495KxyQrVdG0us1RlJSatZP19HxOTse0BLwxqnsc2NrXBpItjc/Lk9IDb57s1wNqOkmVFdIWG7YwI7jcTH6q3wrjwXX1l2oSzMMVMzgWEWLr3kA6ARlHl0XPQQq8JUVJxUFCLv6nXoej1qmkS0qvHV2WjHFpev5fa8NhdupFQ6LQjpGEB7Iqt7SRcBzcRGXPmFBTtN0l7aP8A0s/opBqXrlQU9A2mqMZP50OYInPa5riciQLEEFbXoi1e9zt/d3/0W+1xjqzS2HmKMIV6zraNKd5ys0nhdlWaW0hJUyPnlIL3kFxIDQbAWyG7IBWjsT0g3BPAfV3bIB7IYQ11u6zfjBR3XjSmi5oWNo4gyQPu48C6O7bEWuRnnhUT0PpOWlmbNE7DIw36R0HEOdpGRXPGXR1Lt3+R6tWh13QnCMHC3hT2eHD6NbM9xv656FfSVcsbmkMJc5h5ntJJYR9HeCuJHEXEAAkkgADMkncAFcFPr/o6siayuhDSOmN0rAelrmAuZ4gd6fFrBoGj5cLWOkFy3g4nucP2XygNafEb1boRbvGasYU/adWnBU6lCeutmGx23/8AVdepuQ040doR7JbNkMUwPVJMHBo6yMQv+yVRx3nvKlOumuMmkHAEYIWkljAbi9rYnu9c7f3Xt0kxZRWmpNKOCOr2XotSlCVSt4pu7XD8u36YCISoWB6dhEJUICwiEqEBYRCVCAsIhKhAWM3BHs+YTTEex5hCF19XjxZ5nX6nBZ8xMPaZ5hO4PrZ5hIhLoI8WW9NnwWfMdwR7PmEcEez5hCFXV4+pHX6nBZ8xpiPY8wkw9pnmEIS6CPFlLTpvcs+YYe0zzCMPaZ5hCEugiV12fBZ8ww9pnmEYe0zzCEI6CIuuz4LPmGHtM8wjD2meYQhHQRDrs+Cz5hh7TPMIw9pnmEIR0ER9dnwWfMMPaZ5hGHtM8wkQjoIi67Pgs+YuHtM8wjD2meYQhHQRDrs+Cz5hh7TPMIw9pnmEIR0ER9dnwWfMMPaZ5hGHtM8whCOgiLrs+Cz5hh7TPMJS3tM8whCOgiPrs+Cz5iYe0zzCMPaZ5hCEdBEXXZ8FnzDD2meYRh7TPMIQjoIj67Pgs+Y4Rns+YS8Eez5hCFXV4+pn1+pwWfMOCPZ8wmYe0zzCEJOhH1Kjp03uWfMMPaZ5hOEZ7PmEIQqEfUJadNblnzF4I9nzCOCPZ8whCfV4+pPX6nBZ8z//2Q=='
        },
        {
            'title': 'Weather Channel',
            'url': 'http://weather-lh.akamaihd.net/i/twc_1@92006/index_2400_av-p.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbl_H5-1r-MHfEuy_K7R96SUidciP1ZLvD2zzM0Ph_QCD0w1TwbsfJI2KLSd1Pj-RSwVU&usqp=CAU'
        },

    ],
    'sports': [
        {
            'title': 'CBS Sports Network',
            'url': 'https://h4.ustvgo.la/CBSSN/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://mpng.subpng.com/20180404/dbq/kisspng-cbs-sports-radio-radio-personality-cbs-sports-netw-sports-5ac512f26702d7.737935281522864882422.jpg'
        },
        {
            'title': 'ESPN2',
            'url': 'https://h4.ustvgo.la/ESPN2/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://mpng.subpng.com/20181116/bea/kisspng-logo-brand-high-definition-television-product-vacalocatv-5bee65b62610b2.3527521815423502621559.jpg'
        },
        {
            'title': 'Fox Sports 2',
            'url': 'https://h4.ustvgo.la/FS2/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://e7.pngegg.com/pngimages/275/7/png-clipart-fox-sports-2-television-channel-fox-sports-networks-streaming-media-fox-sport-television-blue.png'
        },
    ],
    'reality': [
        {
            'title': 'Discovery',
            'url': 'https://bozztv.com/teleyupp/teleup-discovery/index.m3u8',
            'img': 'https://discovery-assets-production.s3.eu-west-1.amazonaws.com/app/uploads/2019/03/31153448/facebook.jpg'
        },
        {
            'title': 'Red Bull',
            'url': 'https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master_3360.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ00Quepr9MHVnBYoWUdGjYfKejQIx84KV3LpOqw8Zf92cWdDKrDf7Zl7aWGTk5nB6EiVg&usqp=CAU'
        },
        {
            'title': 'A&E',
            'url': 'https://bk7l2w4nlx53-hls-live.5centscdn.com/AETV/514c04b31b5f01cf00dd4965e197fdda.sdp/AETV/OBS11/chunks.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/ae-269x151.png'
        },
        {
            'title': 'AMC',
            'url': 'https://h1.ustvgo.la/AMC/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/amc-269x151.png'
        },
        {
            'title': 'HGTV',
            'url': 'http://50.7.161.82:8278/streams/d/HGTV/playlist.m3u8',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/HGTV-269x151.png'
        },
        {
            'title': 'Lively Place',
            'url': 'https://aenetworks-ae-1.roku.wurl.com/manifest/playlist.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxcv6hioK7x0ybzCO5qoFfz_07WgjHOVwr-Qpe8dAWDDwfX8Ad9kV9yIB4rBVoI2MPDe8&usqp=CAU'
        },
        {
            'title': 'This Old House',
            'url': 'https://thisoldhouse-2.roku.wurl.com/manifest/playlist.m3u8',
            'img': 'data:image/png;base64,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'
        },
        {
            'title': 'Architect Digest',
            'url': 'https://dai2.xumo.com/amagi_hls_data_xumo1212A-rokutraveler/CDN/playlist.m3u8',
            'img': 'data:image/png;base64,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'
        },
        {
            'title': 'The Design Network',
            'url': 'https://thedesignnetwork-tdn-2.roku.wurl.com/manifest/playlist.m3u8',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAT3CjUKmO_x2_IXz7opUmMNzwQweb1JEs9bROfHBIbMOoYNjw3YC81E47XT9VfEgXl_s&usqp=CAU'
        },
        {
            'title': 'RT Documentary',
            'url': 'https://rt-doc.secure.footprint.net/1101_2500Kb.m3u8',
            'img': 'https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/RTD-TV-logo.png/220px-RTD-TV-logo.png'
        },
        {
            'title': 'TLC',
            'url': 'http://xxxxlocal.com:8080/xiptv0985/ptXv7hZ0xy/11561',
            # 'url': 'https://h1.ustvgo.la/TLC/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/tlc-269x151.png'
        },
        {
            'title': 'DIY',
            'url': 'https://h1.ustvgo.la/DIY/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2019/01/diy.png'
        },
        {
            'title': 'Travel',
            'url': 'https://h1.ustvgo.la/Travel/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/Travel-269x151.png'
        },
        {
            'title': 'TruTV',
            'url': 'https://h1.ustvgo.la/TruTV/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/TruTV-269x151.png'
        },
        {
            'title': 'FX',
            'url': 'https://h1.ustvgo.la/FX/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/fx-269x151.png'
        },
        {
            'title': 'FXX',
            'url': 'https://h1.ustvgo.la/FXX/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSESZlb1AgkJX9Qg-4_65SstD_aCdp6vRt4tQ&usqp=CAU'
        },
        {
            'title': 'FXMovie',
            'url': 'https://h1.ustvgo.la/FXMovie/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'data:image/png;base64,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'
        },
        {
            'title': 'SYFY',
            'url': 'https://h1.ustvgo.la/SYFY/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'data:image/jpeg;base64,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'
        },
        {
            'title': 'E!',
            'url': 'https://h1.ustvgo.la/E/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLyHBsg8PKiP79KNaKEXLtsM4bSTuExNKiCUpoF48gHqeFjGmgA4oYlcKAuTWwvbhLD0Q&usqp=CAU'
        },
        {
            'title': 'We TV',
            'url': 'https://h1.ustvgo.la/WETV/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://www.logolynx.com/images/logolynx/s_9f/9f2b497b54649a9931790745f4c92f20.png'
        },
        {
            'title': 'VH1',
            'url': 'https://h1.ustvgo.la/VH1/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/vh1-269x151.png'
        },
        {
            'title': 'MTV',
            'url': 'https://h1.ustvgo.la/MTV/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA2qKhWBf2FD58XuKkmjZuk6EE5ZQAqXb_ZiNgDpnTT-M5jGx_0z5PuAICWQ5sMfsaD5A&usqp=CAU'
        },
        {
            'title': 'Comedy Central',
            'url': 'https://h2.ustvgo.la/Comedy/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'data:image/png;base64,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'
        }
    ],
    'kids': [
        {
            'title': 'Cartoon Network',
            'url': 'https://h3.ustvgo.la/CN/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/cartoon-network-269x151.png'
        }
    ],
    'CR': [
        {
            'title': 'Ticavision',
            'url': 'http://k3.usastreams.com:1935/HBTV/HBTV/playlist.m3u8',
            'img': 'https://i.ytimg.com/vi/HhiqLv4tZWs/mqdefault.jpg'
        },
        {
            'title': 'Repretel 6',
            'url': 'https://cr-repretel-canal6-live.ned.media/repretel/canal6/smil:live.smil/playlist.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjIxNDQwMDc0LCJzZXNzaW9uIjoiMTg2LjI2LjExOC4xOTEiLCJ3aGl0ZWxpc3QiOlsiMTg2LjI2LjExOC4xOTEiXX0sInNpZ25hdHVyZSI6ImY0YjMxYzA2ZjkwNjNlMzFjNDg5Njk0NzI1NmQwNzYwNzlmNjZhNWYifQ==',
            'img': 'https://www.repretel.com/wp-content/themes/albavision-theme/img/logo_grupo.png'
        },
    ],
    'documentary': [
        {
            'title': 'Animal Planet',
            'url': 'https://h1.ustvgo.la/Animal/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/animal-planet-269x151.png'
        },
        {
            'title': 'NatGEOWild',
            'url': 'https://h1.ustvgo.la/NatGEOWild/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/National-Geographic-269x151.png'
        },
        {
            'title': 'GEM Nature',
            'url': 'https://d2e40kvaojifd6.cloudfront.net/stream/gem_nature/playlist.m3u8',
            'img': 'https://live-tv-channels.org/pt-data/uploads/logo/ae-gem-nature-1212.jpg'
        },
        {
            'title': 'Science',
            'url': 'https://h1.ustvgo.la/Science/myStream/playlist.m3u8?wmsAuthSign=${ustvgotoken}',
            'img': 'http://123tv.live/wp-content/uploads/2018/08/sci-269x151.png'
        },
        {
            'title': 'Docurama',
            'url': 'https://cinedigm.vo.llnwd.net/conssui/amagi_hls_data_xumo1234A-docuramaA/CDN/master.m3u8',
            'img': 'https://camo.githubusercontent.com/fcb4817f613b346faf9e4b84379264af8dbc9511cb1ffa53ce76930fc08c7185/68747470733a2f2f692e696d6775722e636f6d2f624e67386d7a652e706e67'
        },
        {
            'title': 'NASA TV',
            'url': 'http://iphone-streaming.ustream.tv/uhls/6540154/streams/live/iphone/playlist.m3u8',
            'img': 'https://camo.githubusercontent.com/bd692a1770908ca326047f694b41c7abee5c6a1fd62de83215c279a37e635c6e/68747470733a2f2f692e696d6775722e636f6d2f726d79666f4f492e706e67'
        },
        {
            'title': 'Unsolved Mysteries',
            'url': 'https://dai.google.com/linear/hls/event/iLjE1UKtRCiSNkFatA65bg/master.m3u8',
            'img': 'https://komonews.com/resources/media2/3x1/full/119/center/90/5cf60259-ce44-452f-a8a1-cb33585ea701-small3x1_stirr_1219_epg_unsolvedmysteries_1920x1080.png?cb=c81e728d9d4c2f636f067f89cc14862c'
        },
    ],
}
