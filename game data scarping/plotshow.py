import matplotlib.pyplot as plt

def plot_data(game_genre):
    genres = list(game_genre.keys())
    counts = list(game_genre.values())

    plt.figure(figsize=(10, 6))
    plt.bar(genres, counts, color='blue')
    plt.xlabel('Game Genres')
    plt.ylabel('Number of Games')
    plt.title('Distribution of Game Genres')
    plt.xticks(rotation=45, ha='right')

    plt.show()
def highest_ten_show(game_genre):
    sorted_genres = sorted(game_genre.items(), key=lambda x: x[1], reverse=True)

    # Select the top 10 genres
    top_10_genres = dict(sorted_genres[0:10])

    # Plot the data for the top 10 genres
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_genres.keys(), top_10_genres.values(), color='blue')
    plt.xlabel('Game Genres')
    plt.ylabel('Number of Games')
    plt.title('Top 10 Game Genres')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()