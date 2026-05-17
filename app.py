from flask import Flask, jsonify, render_template
import praw
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Reddit API setup
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# SQLite setup
def init_db():
    conn = sqlite3.connect('top_posts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (subreddit TEXT, title TEXT, url TEXT, score INTEGER, created_utc INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_posts')
# Mock data for testing (replace with real API calls later)
def fetch_posts():
    conn = sqlite3.connect('top_posts.db')
    c = conn.cursor()
    init_db()
    
    # Fetch cached posts
    c.execute('SELECT * FROM posts')
    cached_posts = c.fetchall()
    
    if cached_posts:
        posts = [{'subreddit': p[0], 'title': p[1], 'url': p[2], 'score': p[3]} for p in cached_posts]
        return jsonify(posts)
    
    # Mock data (replace with real API calls)
    posts = [
        {'subreddit': 'AskReddit', 'title': 'What’s the most useless fact you know?', 'url': 'https://reddit.com/r/AskReddit/comments/1awvfn', 'score': 12345},
        {'subreddit': 'todayilearned', 'title': 'TIL octopuses have three hearts.', 'url': 'https://reddit.com/r/todayilearned/comments/1awvfo', 'score': 9876},
        {'subreddit': 'worldnews', 'title': 'Breaking: Major scientific breakthrough announced.', 'url': 'https://reddit.com/r/worldnews/comments/1awvfp', 'score': 5432}
    ]
    
    for post in posts:
        c.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?)',
                  (post['subreddit'], post['title'], post['url'], post['score'], 1715927700))
    
    conn.commit()
    conn.close()
    return jsonify(posts)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)