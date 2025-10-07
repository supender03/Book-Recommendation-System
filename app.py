from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample dataframe (replace this with your actual dataframe)
data = pd.read_csv('books.csv')

df2 = pd.DataFrame(data)

app = Flask(__name__)

def BookRecommender(book_name, num_recommendations=5):
    # Vectorizing the book titles using TF-IDF
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df2['title'])
    
    # Transform the input book_name into the same vector space
    book_vector = tfidf_vectorizer.transform([book_name])
    
    # Calculate cosine similarity between the input book and all other books
    cosine_similarities = cosine_similarity(book_vector, tfidf_matrix).flatten()
    
    # Get indices of the top similar books (excluding the input book itself)
    similar_indices = cosine_similarities.argsort()[-(num_recommendations + 1):-1][::-1]
    
    # Get the titles of the most similar books
    recommended_books = df2.iloc[similar_indices]['title'].tolist()
    
    return recommended_books

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        book_name = request.form["book_name"]
        recommendations = BookRecommender(book_name)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(port=8000,debug=True)
