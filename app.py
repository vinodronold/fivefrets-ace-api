from chalice import Chalice
from chalicelib import SONGS, CHORDS

app = Chalice(app_name='fivefrets-ace-api')


@app.route('/')
def index():
    return {
        'app': 'fivefrets',
        'version': '0.0.0'
    }


@app.route('/songs')
def get_songs():
    return SONGS


@app.route('/song/{id}')
def get_one_song(id):
    try:
        return SONGS[id]
    except KeyError:
        from chalice import BadRequestError
        raise BadRequestError('Song Not Available')


@app.route('/chords/{id}')
def get_chords(id):
    try:
        return CHORDS[id]
    except KeyError:
        from chalice import BadRequestError
        raise BadRequestError('Chords Not Available')


@app.route('/song/chords/{id}')
def get_one_song_chords(id):
    try:
        song_chords = SONGS[id]
        song_chords["chords"] = CHORDS[id]
        return song_chords
    except KeyError:
        from chalice import BadRequestError
        raise BadRequestError('Chords Not Available')
