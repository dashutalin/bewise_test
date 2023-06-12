from flask import Flask, request, redirect, render_template, url_for
from sqlalchemy import exc
import uuid

from DataBase import create_song, create_user, get_user

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def reg():
    id = 0
    if request.method == 'POST':
        id = create_user(
            request.form['name'],
            str(uuid.uuid4())
        )
        return redirect(url_for('main', user_id=id))
    return render_template('auth.html', id=id)


@app.route('/<int:user_id>', methods=['GET', 'POST'])
def main(user_id):
    uuid_user = get_user(user_id)
    if request.method == 'POST':
        song = request.form['song'].split('.')[0]
        song = '.'.join([song, 'mp3'])
        song_id = create_song(
            user_id,
            song,
            str(uuid.uuid4())
        )
        return song
        # return f'http://localhost:5000/record?id={song_id}&user={user_id}.'
    return render_template('song.html', id=user_id, token=uuid_user)


# @app.route('/record/<int:id><int:user_id>')
# def get_song():
#     return ''


if __name__ == '__main__':
    app.run()
