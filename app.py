from flask import Flask, jsonify, request # type: ignore
import os
import random
import json

app = Flask(__name__)

# Function to load all articles from a directory
def load_articles():
    articles = []
    articles_dir = './articles'  # Directory where your JSON files are stored
    for filename in os.listdir(articles_dir):
        if filename.endswith(".json"):
            with open(os.path.join(articles_dir, filename), 'r', encoding='utf-8') as file:
                articles.append(json.load(file))
    return articles

# Route to get a random article
@app.route('/get-random-article', methods=['GET'])
def get_random_article():
    articles = load_articles()
    random_article = random.choice(articles)
    return jsonify(random_article)

# Route to handle classification
@app.route('/classify-article', methods=['POST'])
def classify_article():
    data = request.get_json()
    article_id = data.get('articleId')
    classification = data.get('classification')
    
    # You can store classification data or process it as needed
    # For simplicity, we're just sending a success message
    return jsonify({'message': f'Artículo clasificado como {classification}'})


if __name__ == '__main__':
    app.run(debug=True)

