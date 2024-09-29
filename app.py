from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon, MastodonRatelimitError

app = Flask(__name__)

mastodon = Mastodon(
    access_token='dxPPlDEl1QAs5n91tC0wr7jqFadJFxLyS_soVUwiNRg',
    api_base_url='https://mastodon.social'
)
posts = []
#written by Mohibkhan Pathan
@app.route('/')
def index():
    return render_template('index.html', posts=posts)
#written by Mohibkhan Pathan
@app.route('/create_post', methods=['POST'])
def create_post():
    global posts
    content = request.form['status']
    try :                                           #edited by Praful John to handle the exception also added the validations
        created_post = mastodon.status_post(content)
        posts.append(created_post)
        return redirect(url_for('index'))   #redirecting to index page to fix the testing error edited by Praful John
    except MastodonRatelimitError:
        return render_template('index.html', posts=posts, error_message="Rate limit exceeded. Please try again later.")
    except Exception as e:
        return render_template('index.html', posts=posts, error_message=f"An error occurred: {str(e)}")
#written by Mohibkhan Pathan
@app.route('/retrieve_post', methods=['POST'])
def retrieve_post():
    global posts
    posts = mastodon.timeline_home()
    return render_template('index.html', posts = posts)
# New route for retrieving post by ID 
#written by Praful John
@app.route('/retrieve_post_by_id', methods=['POST'])
def retrieve_post_by_id():
    post_id = request.form['post_id']

    try:
        post = mastodon.status(post_id)
        return render_template('index.html', posts=[post], error_message=None)
    
    except Exception as e:
        return render_template('index.html', posts=[], error_message=f"Post with ID {post_id} not found.")
#written by Mohibkhan Pathan
@app.route('/delete_post', methods=['POST'])
def delete_post():
    global posts
    post_id = request.form['post_id']
    try:                                #edited by Praful John to handle the exception also added the validations
        mastodon.status_delete(post_id)
        posts = [post for post in posts if post['id'] != int(post_id)]  # Using 'post['id']' instead of 'post.id' edited by Praful John
        return redirect(url_for('index'))   #redirecting to index page to fix the testing error edited by Praful John
    except MastodonRatelimitError:
        return render_template('index.html', posts=posts, error_message="Rate limit exceeded. Please try again later.")
    except Exception as e:
        return render_template('index.html', posts=posts, error_message=f"An error occurred: {str(e)}")
    

if __name__ == '__main__':
    app.run(debug=True)
