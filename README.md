# Flask Blog Application

This Flask application serves as a simple blog where users can view, add, update, delete, and like blog posts.

## Features

- **View Posts:** See a list of all blog posts on the home page.
- **Add Post:** Add a new blog post with fields for author, title, and content.
- **Update Post:** Edit existing blog posts to update author, title, or content.
- **Delete Post:** Remove blog posts from the list.
- **Like Post:** Increment the likes on a post with a dedicated "Like" button.

## Files

- **app.py:** Contains the Flask application setup and routes for handling blog functionality.
- **templates/:** Directory containing HTML templates for different pages (index.html, add.html, update.html).
- **static/:** Directory for static assets such as CSS stylesheets (style.css) and images (like.svg).

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/OkanShr/MasterBlog.git
   cd MasterBlog

2. **Install Dependencies**
    ```bash  
    pip install flask

3. **Run The Application**
    ```bash
    python app.py


## Usage

- **View Posts:** Navigate to the home page (`http://localhost:5000`) to see existing blog posts.
- **Add Post:** Click on "Add New Post" to fill out a form and submit a new blog post.
- **Update Post:** Click "Update" next to a post to edit its details.
- **Delete Post:** Click "Delete" to remove a post from the list.
- **Like Post:** Click "Like" to increment the likes for a post.
