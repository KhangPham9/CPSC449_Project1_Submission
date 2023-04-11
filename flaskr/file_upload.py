from flask import (
    Blueprint, flash, redirect, render_template, session, request, url_for, current_app, jsonify
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

import os

bp = Blueprint('file', __name__, url_prefix='/file')

upload_path = 'upload'
accepted_file_endings = ['.txt', '.png', '.pdf']

max_content_length = 1024 * 1024

@bp.route('upload')
def upload():
    if 'loggedin' in session:
        return render_template('file_upload.html')
    else:
        return redirect(url_for('auth.login'))


@bp.route('uploaded_file', methods=['GET', 'POST'])
def upload_file():

    uploaded_file = request.files['file']


    filename = secure_filename(uploaded_file.filename)
    if filename != '':

        file_size = request.content_length
        if file_size < max_content_length:
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in accepted_file_endings:
                abort(415)


            uploaded_file.save(os.path.join(upload_path, filename))
        else:
            abort(413)

    return render_template('file_upload.html')
