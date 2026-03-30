# Movie Recommendation System

A robust AI-based recommendation engine developed for the Build Your Own Project (BYOP) submission. This system uses Natural Language Processing (NLP) to suggest movies based on a "Metadata Soup" of genres, cast, and directors.

## 🌟 Features
- **Fuzzy Matching:** Uses `difflib` to handle user typos and partial title matches.
- **Metadata Fusion:** Combines Genres, Cast, and Director into a single vector for higher accuracy.
- **CLI-First:** Built strictly for Command Line Interface execution as per project guidelines.
- **Robust Error Handling:** Automatically detects title/genre columns and manages missing data.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, Scikit-learn
- **Algorithm:** TF-IDF Vectorization + Cosine Similarity

## 📥 Installation

1. **Clone the repository:**
   ```bash
   gh repo clone Divyank1-tech/Movie-recommendation-system
