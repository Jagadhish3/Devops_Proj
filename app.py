from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found."]
    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommended = []
    for i in distances[1:6]:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_route():
    movie_name = request.form['movie']
    recs = recommend(movie_name)
    return jsonify(recs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
