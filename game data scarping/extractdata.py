from bs4 import BeautifulSoup
import requests

class Type:
    def __init__(self, name):
        self.name = name
        self.counter = 0
    def increment_counter(self):
        self.counter += 1

def extract_data(url):
    url1 = requests.get(url)
    soup = BeautifulSoup(url1.content, 'html.parser')
    game_data = []
    types = set()
    for game in soup.find_all('div', class_='tab_item_content'):
        name = game.find('div', class_='tab_item_name').text.strip()

        tags = [tag.text.strip().lstrip(',') for tag in game.find_all('span', class_='top_tag')]
        types.update(tags)
        game_data.append({
            'name': name,
            'tags': [tag.replace(" ", "") for tag in tags]
        })
    types = [type.replace(" ", "") for type in types]
    game_genre = types_dict = {type: 0 for type in types}
    for game in game_data:
        for tag in game['tags']:
            game_genre[tag] += 1

    return game_data, game_genre


list1, types = extract_data('https://store.steampowered.com/explore/upcoming/')
# Convert the generator expression to a list before printing