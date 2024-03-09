from extractdata import extract_data
from tagpercent import cal_percent_tag
from plotshow import plot_data, highest_ten_show

def main():
    game_data, game_genre = extract_data('https://store.steampowered.com/explore/upcoming/')
    highest_ten_show(game_genre)
    type = input(f"Select a tag of those tags{game_genre.keys()}: \n")
    print(f'The percent of the chosen type from the games list :  {cal_percent_tag(game_data, game_genre, type)}%')

if __name__ == "__main__":
    main()