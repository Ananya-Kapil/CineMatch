import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data/movies.csv")

# Replace missing genres
movies["genres"] = movies["genres"].fillna("")

# Convert genres into vectors
tfidf = TfidfVectorizer()
genre_matrix = tfidf.fit_transform(movies["genres"])

# Calculate similarity matrix
similarity = cosine_similarity(genre_matrix)


def recommend(movie_name):
    # Find the movie
    movie = movies[movies["title"].str.contains(movie_name, case=False, na=False)]

    if movie.empty:
        print("\n❌ Movie not found!")
        return

    index = movie.index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Movies similar to '{movie.iloc[0]['title']}':\n")

    for i in scores[1:6]:
        print("-", movies.iloc[i[0]]["title"])