# 🎬 Movie Recommendation System

A content-based movie recommendation engine built with Python. It uses **TF-IDF vectorization** and **cosine similarity** to suggest movies similar to one you already like — based on genres, plot, cast, and other metadata.

---

## 📌 Features

- Content-based filtering using movie metadata
- Flexible title matching — exact, substring, and fuzzy search
- Works with any CSV dataset that has a `title` and `genres` column
- Displays top 5 similar movie recommendations
- Supports both CLI argument and interactive input modes

---

## 🗂️ Project Structure

```
movie-recommendation-system/
│
├── main.py          # Core recommendation logic and CLI interface
├── movies.csv       # Movie dataset (you provide this)
└── README.md
```

---

## ⚙️ Requirements

- Python 3.7+
- pandas
- scikit-learn

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

## 📊 Dataset Format

Your `movies.csv` must include at minimum:

| Column   | Required | Description                        |
|----------|----------|------------------------------------|
| `title`  | ✅ Yes   | Movie name (also accepts `name`, `film`, `movie_title`, etc.) |
| `genres` | ✅ Yes   | Genre(s) of the movie              |

The following columns are **optional but improve recommendations**:

| Column       | Description                  |
|--------------|------------------------------|
| `plot`       | Movie plot / description     |
| `overview`   | Short summary                |
| `tagline`    | Movie tagline                |
| `keywords`   | Associated keywords          |
| `actors`     | Actor names                  |
| `stars`      | Lead stars                   |
| `writer`     | Screenwriter(s)              |
| `director`   | Director name (shown in output) |
| `cast`       | Full cast (shown in output)  |

---

## 🚀 Usage

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

or for multi-word titles:

```bash
python main.py The Dark Knight
```

---

## 📤 Sample Output

```
Since you liked 'Sholay', you might enjoy these:

Title   : Deewar
Genres  : Action, Drama
Director: Yash Chopra
----------------------------------------
Title   : Don
Genres  : Action, Crime, Thriller
Director: Chandra Barot
----------------------------------------
...
========================================
```

---

## 🔍 How It Works

1. **Metadata Aggregation** — Combines available text fields (`genres`, `plot`, `actors`, etc.) into a single metadata string per movie.
2. **TF-IDF Vectorization** — Converts metadata into numerical feature vectors, down-weighting common words.
3. **Cosine Similarity** — Measures how similar each movie is to the queried one based on their vectors.
4. **Title Matching** — Tries exact → substring → fuzzy matching to handle typos and partial titles.
5. **Top-5 Results** — Returns the 5 most similar movies, excluding the queried movie itself.

---

## 🛠️ Customization

- **Change number of recommendations** — Edit `sim_scores[1:6]` in `get_recommendations()` (e.g., `[1:11]` for top 10).
- **Adjust fuzzy match sensitivity** — Modify the `cutoff` parameter in `difflib.get_close_matches()` (default: `0.6`).
- **Add more metadata fields** — Extend the `metadata_fields` list with any additional columns in your CSV.

---

## 📝 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [scikit-learn](https://scikit-learn.org/) for TF-IDF and cosine similarity
- [pandas](https://pandas.pydata.org/) for data handling
- Inspired by classic collaborative and content-based filtering techniques
