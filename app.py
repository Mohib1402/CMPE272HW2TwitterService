from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon

app = Flask(__name__)

mastodon = Mastodon(
    access_token='dxPPlDEl1QAs5n91tC0wr7jqFadJFxLyS_soVUwiNRg',
    api_base_url='https://mastodon.social'
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
