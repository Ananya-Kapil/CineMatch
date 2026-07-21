from recommender import recommend

print("=" * 40)
print("🎬 Movie Recommendation System")
print("=" * 40)

while True:
    movie = input("\nEnter a movie name (or type 'exit'): ")

    if movie.lower() == "exit":
        print("Goodbye!")
        break

    recommend(movie)