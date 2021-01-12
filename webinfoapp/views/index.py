from flask import Blueprint, render_template
import glob

bp = Blueprint(__name__, __name__,template_folder='templates')

def fetch_notes():
    final_note = []
    notes = glob.glob('webinfoapp/notes/*.note')

    for note in notes:
        with open(note) as _file:
            final_note.append(_file.read())
        
        _file.close
    return final_note

@bp.route('/')
def show():
    return render_template('index.html', notes =fetch_notes())