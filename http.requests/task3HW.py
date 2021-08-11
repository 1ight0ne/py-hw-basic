import requests
from datetime import datetime, timedelta, timezone


def get_stackexchange(tag='python', days=3):
    today = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0)
    date_ago = datetime.now().replace(hour=00,minute=0,second=0,microsecond=0) - timedelta(days=days)
    fromdate = int(date_ago.replace(tzinfo=timezone.utc).timestamp())
    todate = int(today.replace(tzinfo=timezone.utc).timestamp())
    url = 'https://api.stackexchange.com/2.3/questions?site=stackoverflow&order=desc&sort=activity'
    url += f'&tagged={tag}&fromdate={str(fromdate)}&todate={str(todate)}'
    r = requests.get(url)
    for item in r.json()['items']:
        print(item['title'])

if __name__ == "__main__":
    get_stackexchange()