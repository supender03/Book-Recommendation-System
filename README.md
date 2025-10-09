# Book Recommendation System

An intelligent **Book Recommendation System** that suggests books to users based on their preferences using **Natural Language Processing (NLP)** and **Cosine Similarity**. The system is built with **Flask** for the web interface and **Elasticsearch** for fast and relevant search results.

---

## Features

- **Personalized Book Recommendations:** Uses NLP and cosine similarity to recommend books similar to user input.  
- **Search Integration:** Powered by Elasticsearch to quickly fetch books based on keywords or queries.  
- **User-Friendly Interface:** Simple and responsive web interface built with Flask.  
- **CSV-Based Book Dataset:** Easily adaptable to new datasets.

---

## Getting Started

Follow these steps to set up and run the Book Recommendation System locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/supender03/Book-Recommendation-System.git
cd Book-Recommendation-System
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Run the Application
```bash
python app.py
```
### Step 4: Open in Browser
Open your web browser and go to:
```bash
http://127.0.0.1:5000/
```

### How It Works

The system reads the books.csv dataset containing book details.
Uses NLP to process book metadata and compute cosine similarity between books.
Takes user input (book name or keyword) via the web interface.
Returns a list of recommended books based on similarity scores.
Elasticsearch integration enhances the search functionality for fast results.

### Dependencies

Flask 

pandas

scikit-learn

Elasticsearch

numpy

Full list of packages available in requirements.txt.


### License

This project is licensed under the MIT License.

Feel free to use and modify it for your own projects.
