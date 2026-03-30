import difflib
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

def run_recommendation_system():
    # Load the Dataset
    csv_path = os.path.join(os.path.dirname(__file__), 'movies.csv')
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("Error: 'movies.csv' not found. Please ensure the file is in the same directory as main.py.")
        return

    title_aliases = ['title', 'name', 'movie', 'movie title', 'movie_title', 'original_title', 'film']
    current_title_col = None
    for alias in title_aliases:
        for col in df.columns:
            if col.strip().lower() == alias:
                current_title_col = col
                break
        if current_title_col:
            break

    if current_title_col is None:
        print("Error: no title column found in movies.csv. Expected a column named 'title' or similar.")
        return

    if current_title_col != 'title':
        df = df.rename(columns={current_title_col: 'title'})

    if 'genres' not in df.columns:
        print("Error: no genres column found in movies.csv. Expected a column named 'genres'.")
        return

    # Preprocessing: build a metadata text field from available movie columns
    metadata_fields = [
        'genres', 'writer', 'plot', 'description',
        'overview', 'tagline', 'keywords', 'actors', 'stars'
    ]

    for field in metadata_fields:
        if field not in df.columns:
            df[field] = ''

    df[metadata_fields] = df[metadata_fields].fillna('')
    df['metadata'] = df[metadata_fields].agg(' '.join, axis=1)

    # Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['metadata'])

    # Compute Similarity Scores
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Recommendation Logic
    def get_recommendations(title):
        title_lower = title.strip().lower()

        # Exact title match first
        title_match = df[df['title'].str.lower() == title_lower]

        # If exact match fails, try substring match
        if title_match.empty:
            title_match = df[df['title'].str.lower().apply(lambda x: title_lower in x)]

        # If substring match fails, try a close fuzzy match
        if title_match.empty:
            close_titles = difflib.get_close_matches(title_lower, df['title'].str.lower().tolist(), n=1, cutoff=0.6)
            if close_titles:
                title_match = df[df['title'].str.lower() == close_titles[0]]

        if title_match.empty:
            return None

        idx = title_match.index[0]

        # Get pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort movies based on similarity scores 
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get top 5 similar movies (skipping the first one as it is the movie itself)
        sim_scores = sim_scores[1:6]

        movie_indices = [i[0] for i in sim_scores]
        display_cols = ['title', 'genres']
        if 'director' in df.columns:
            display_cols.append('director')
        if 'cast' in df.columns:
            display_cols.append('cast')
        return df[display_cols].iloc[movie_indices]

    # CLI Interaction
    print("\n" + "="*40)
    print("   MOVIE RECOMMENDATION SYSTEM   ")
    print("="*40)

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("\nEnter a movie you liked (e.g., Sholay, RRR, Drishyam): ")

    results = get_recommendations(query)

    if results is not None:
        print(f"\nSince you liked '{query}', you might enjoy these:\n")
        for idx, row in results.reset_index(drop=True).iterrows():
            print(f"Title   : {row['title']}")
            print(f"Genres  : {row['genres']}")
            if 'director' in results.columns and row.get('director'):
                print(f"Director: {row['director']}")
            if 'cast' in results.columns and row.get('cast'):
                print(f"Cast    : {row['cast']}")
            if idx < len(results) - 1:
                print("-" * 40)
        print("\n" + "="*40)
    else:
        print(f"\nSorry, '{query}' was not found in our database.")
        print("Check for spelling or try another popular title.")

if __name__ == "__main__":
    run_recommendation_system()
