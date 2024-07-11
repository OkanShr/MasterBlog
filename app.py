from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


def load_posts():
    with open('db/posts.json', 'r') as f:
        return json.load(f)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
