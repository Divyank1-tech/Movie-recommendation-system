#  Movie Recommendation System

A content-based movie recommendation engine built with Python, focused on 'Indian cinema' . It uses 'TF-IDF vectorization and  'cosine similarity' on genre metadata to suggest movies similar to one you already like.

---

##  Features

- Content-based filtering using genre metadata
- Flexible title matching — exact, substring, and fuzzy search
- Dataset of '100 popular Indian movies' across genres
- Displays top 5 similar movie recommendations
- Supports both CLI argument and interactive input modes

---

##  Project Structure

```
movie-recommendation-system/
│
├── main.py          # Core recommendation logic and CLI interface
├── movies.csv       # 100 Indian movies with genre metadata
└── README.md
```

---

##  Requirements

- Python 3.7+
- pandas
- scikit-learn

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

##  Dataset

The included `movies.csv` contains '100 popular Indian movies' with the following columns:

| Column     | Description                                      |
|------------|--------------------------------------------------|
| `movie_id` | Unique identifier for each movie                 |
| `title`    | Movie name                                       |
| `genres`   | Space-separated genre tags (e.g. `Action Drama`) |

### Sample Data

| movie_id | title                          | genres                        |
|----------|--------------------------------|-------------------------------|
| 1        | Sholay                         | Action Adventure Comedy Drama |
| 2        | Dilwale Dulhania Le Jayenge    | Romance Drama Musical         |
| 3        | Baahubali: The Beginning       | Action Adventure Fantasy      |
| 4        | 3 Idiots                       | Comedy Drama                  |
| 5        | Dangal                         | Action Biography Drama Sport  |

> Note: Recommendations are based purely on genre similarity. Movies sharing more genre tags will rank higher as similar matches.

---

##  Usage

### Interactive Mode

```bash
python main.py
```

You'll be prompted to enter a movie name:

```
========================================
   MOVIE RECOMMENDATION SYSTEM   
========================================

Enter a movie you liked (e.g., Sholay, RRR, Drishyam): Sholay
```

### Command-Line Argument Mode

```bash
python main.py Sholay
```

For multi-word titles:

```bash
python main.py Dilwale Dulhania Le Jayenge
```

---

##  Sample Output

```
Since you liked 'Sholay', you might enjoy these:

Title   : RRR
Genres  : Action Adventure Drama
----------------------------------------
Title   : Baahubali: The Beginning
Genres  : Action Adventure Fantasy
----------------------------------------
Title   : Dangal
Genres  : Action Biography Drama Sport
----------------------------------------
...
========================================
```

---

##  How It Works

1. Metadata Aggregation — Uses the `genres` column as the primary text signal for each movie.
2. TF-IDF Vectorization — Converts genre tags into numerical feature vectors, down-weighting very common genre words.
3. Cosine Similarity — Measures how similar each movie is to the queried one based on their genre vectors.
4. Title Matching — Tries exact → substring → fuzzy matching to handle typos and partial titles.
5. Top-5 Results — Returns the 5 most genre-similar movies, excluding the queried movie itself.

---

##  Customization

- Change number of recommendations — Edit `sim_scores[1:6]` in `get_recommendations()` (e.g., `[1:11]` for top 10).
- Adjust fuzzy match sensitivity — Modify the `cutoff` parameter in `difflib.get_close_matches()` (default: `0.6`).
- Improve recommendation quality — Add more columns to `movies.csv` such as `plot`, `director`, `cast`, or `keywords`. The system will automatically pick them up and use them for richer matching.

---

##  Possible Improvements

- Add `plot`, `cast`, and `director` columns to `movies.csv` for deeper content-based filtering
- Expand the dataset beyond 100 movies
- Build a web UI using Flask or Streamlit
- Add collaborative filtering based on user ratings

---

##  Acknowledgements

- [scikit-learn](https://scikit-learn.org/) for TF-IDF and cosine similarity
- [pandas](https://pandas.pydata.org/) for data handling
- Dataset: 100 popular Indian movies
