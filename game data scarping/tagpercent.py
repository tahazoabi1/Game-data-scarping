
def cal_percent_tag(games_data, game_genre, type):
    games_len = len(games_data)
    return game_genre[type]/games_len * 100
