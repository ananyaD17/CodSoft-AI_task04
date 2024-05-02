import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User ratings matrix (rows = users, columns = movies)
ratings = np.array([
    [3, 4, 0, 5, 0],
    [5, 0, 4, 0, 2],
    [0, 2, 3, 4, 0],
    [4, 0, 0, 3, 5]
])

# Calculate similarity matrix using cosine similarity
similarities = cosine_similarity(ratings)

def recommend_movies(user_id, ratings, similarities, num_recommendations=3):
    # Find similar users
    similar_users = np.argsort(similarities[user_id])[::-1]  # Sort in descending order
    recommended_movies = []

    # Gather top-rated movies from similar users
    for user in similar_users:
        if user != user_id:
            for movie in range(ratings.shape[1]):
                if ratings[user_id, movie] == 0 and ratings[user, movie] > 0:
                    recommended_movies.append(movie)
                if len(recommended_movies) >= num_recommendations:
                    return recommended_movies

    return recommended_movies

# Example: Recommend movies for User1 (index 0)
user_id = 0
recommended_movies = recommend_movies(user_id, ratings, similarities)
print("Recommended movies for User1:")
for movie_id in recommended_movies:
    print(f"Movie{movie_id + 1}")
