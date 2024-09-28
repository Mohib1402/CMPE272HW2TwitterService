from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon

app = Flask(__name__)

mastodon = Mastodon(
    access_token='dxPPlDEl1QAs5n91tC0wr7jqFadJFxLyS_soVUwiNRg',
    api_base_url='https://mastodon.social'
)
posts = []
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=['POST'])
def create_post():
    global posts
    content = request.form['status']
    created_post = mastodon.status_post(content)
    posts.append(created_post)
    return render_template('index.html', posts=[created_post])

@app.route('/retrieve_post', methods=['POST'])
def retrieve_post():
    global posts
    posts = mastodon.timeline_home()
    return render_template('index.html', posts = posts)

@app.route('/delete_post', methods=['POST'])
def delete_post():
    global posts
    post_id = request.form['post_id']
    mastodon.status_delete(post_id)
    posts = [post for post in posts if post.id != int(post_id)]
    return render_template('index.html', posts = posts)

if __name__ == '__main__':
    app.run(debug=True)
