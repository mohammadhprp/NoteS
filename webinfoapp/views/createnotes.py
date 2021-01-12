from flask import Blueprint, render_template, request, redirect 
import random
bp = Blueprint(__name__, __name__,template_folder='templates')

def random_string(length= 10):
    fianal_string = ''
    chars = 'abcdefghijlmnopqrstuxz0123456789'

    for i in range(0 , length):
        fianal_string += chars[random.randint(0, len(chars)-1)]
    
    return  fianal_string


@bp.route('/createnotes', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
            text = request.form.get('notetext')

            with open('webinfoapp/notes/{}.note'.format(random_string()), 'w+') as _file:
                _file.write(text)

            _file.close()

            return redirect('/')
    return render_template('createnote.html')