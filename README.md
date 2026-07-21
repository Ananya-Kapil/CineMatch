# 🎬 CineMatch

> *"Finding your next favorite movie, one recommendation at a time."*

CineMatch is a **content-based movie recommendation system** built using **Python**, **Pandas**, and **Scikit-learn**. It recommends movies with similar genres by applying **TF-IDF vectorization** and **Cosine Similarity** on the MovieLens dataset.

---

## ✨ Features

- 🎥 Search movies by title
- 🤖 Content-based recommendation engine
- 📊 Uses TF-IDF for genre vectorization
- 📐 Computes similarity using Cosine Similarity
- ⚡ Fast command-line interface
- 🗂️ Built on the MovieLens dataset

---

## 🧠 How It Works

```text
User enters a movie
        │
        ▼
Search movie in dataset
        │
        ▼
Convert genres into vectors (TF-IDF)
        │
        ▼
Calculate similarity scores
        │
        ▼
Sort movies by similarity
        │
        ▼
Display Top 5 Recommendations
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- MovieLens Dataset

---

## 📂 Project Structure

```
CineMatch/
│
├── data/
│   └── movies.csv
│
├── main.py
├── recommender.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Ananya-Kapil/CineMatch.git
```

Move into the project directory:

```bash
cd CineMatch
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 💻 Sample Output

```text
========================================
🎬 Movie Recommendation System
========================================

Enter a movie name: Toy Story

Top 5 Recommendations

1. Toy Story 2 (1999)
2. A Bug's Life (1998)
3. Monsters, Inc. (2001)
4. Antz (1998)
5. Finding Nemo (2003)
```

---

## 📚 Dataset

This project uses the **MovieLens Latest Small Dataset**, which contains thousands of movies and their genres for building recommendation systems.

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Content-Based Recommendation Systems
- Text Vectorization using TF-IDF
- Cosine Similarity
- Data Manipulation with Pandas
- Building a Python CLI application

---

## 🔮 Future Improvements

- 🎨 Streamlit Web Interface
- ⭐ Recommendations based on user ratings
- 🎭 Multi-feature recommendations (genres + tags + cast)
- 🔍 Smarter movie search with suggestions
- ❤️ Save favorite movies

---

## 👩‍💻 Author

**Ananya Kapil**

If you like this project, consider ⭐ starring the repository!

---
