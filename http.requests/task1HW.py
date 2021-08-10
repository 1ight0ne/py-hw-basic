import requests

def get_hero_intel(*names):
    site = 'https://superheroapi.com/api/2619421814940190/'
    intel_dict = {}
    for name in names:
        try:
            hero_search = requests.get(site + '/search/' + name).json()
        except requests.exceptions.RequestException as e:
            return e
        if hero_search['response'] == 'error':
            return hero_search['error']
        for hero in hero_search['results']:
            if hero['name'] == name:
                intel_dict[name] = int(hero['powerstats']['intelligence'])
    return max(intel_dict, key=intel_dict.get)

if __name__ == "__main__":
    print(get_hero_intel('Hulk', 'Captain America', 'Thanos'))
