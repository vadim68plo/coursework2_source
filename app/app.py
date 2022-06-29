import logging
from flask import Flask, render_template, request, jsonify
from utils import utils

logging.basicConfig(
    level=logging.INFO,
    filename = "../logs/api.log",
    format = "%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%H:%M:%S',
    )


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def page_index():
    post = utils.get_posts_all()
    return render_template("bookmarks.html", posts=post)


@app.route('/posts/<int:post_id>')
def search_post_page(post_id):
  post_user = utils.get_post_by_pk(post_id)
  comment_user = utils.get_comments_by_post_id(post_id)
  _len_comment_user = len(comment_user)
  return render_template("post.html", posts=post_user, comments=comment_user, len=_len_comment_user)


@app.route('/search/')
def search_page():
  s = request.args['s']
  post = utils.search_post(s)
  _len_s = len(post)
  return render_template("search.html", len=_len_s, posts=post)


@app.route('/users/<username>')
def user_page(username):
  user = utils.get_posts_by_user(username)
  return render_template("user-feed.html", posts=user)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route("/api/posts/")
def api_page():
    posts = utils.get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def api_post_page(post_id):
    _posts_id = utils.get_post_by_pk(post_id)
    return jsonify(_posts_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=800)




