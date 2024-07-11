from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_posts():
    with open("db/posts.json", 'r') as f:
        return json.load(f)


def save_posts(posts):
    with open("db/posts.json", 'w') as f:
        json.dump(posts, f, indent=4)


def fetch_post_by_id(post_id):
    blog_posts = load_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    blog_posts = load_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break

    save_posts(blog_posts)
    return redirect(url_for('index'))


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = load_posts()
        new_id = max(
            post['id'] for post in blog_posts) + 1 if blog_posts else 1
        new_post = {
            'id': new_id,
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }
        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    blog_posts = load_posts()
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    save_posts(blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog_posts = load_posts()
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        print("Form Data Received:", request.form)

        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')

        print("Updated Post:", post)

        for i, p in enumerate(blog_posts):
            if p['id'] == post_id:
                blog_posts[i] = post
                break

        save_posts(blog_posts)

        updated_posts = load_posts()
        print("Posts after saving:", updated_posts)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
