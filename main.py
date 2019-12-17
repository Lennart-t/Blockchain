import blockchain as bc
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/addgraduate', methods=['POST', 'GET'])
def add_graduate():
    if request.method == 'POST':
        key = request.form['key']
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']

        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "" or key != "12345":
            feedback = "The input is invalid. Please try again."
            return render_template('addgraduate.html', feedback=feedback, subject=subject, color="red", name=name,
                                   birthday=birthday, graduation=graduation, key=key)

        feedback = "Diploma successfully added to the blockchain!"
        bc.create_block(name=name, birthday=birthday, subject=subject, graduation=graduation, key=key)
        return render_template('addgraduate.html', feedback=feedback, subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")

    return render_template('addgraduate.html', subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")


@app.route('/checkgraduate', methods=['POST', 'GET'])
def check_graduate():
    subject = "Choose..."
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']

        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "":
            feedback = "The input is invalid. Please try again."
            return render_template('checkgraduate.html', feedback=feedback, subject=subject)

        result = bc.verify_diploma(name=name, birthday=birthday, subject=subject, graduation=graduation)
        return diploma(result)

    return render_template('checkgraduate.html', subject=subject)


@app.route('/verification', methods=['GET'])
def verification():
    results = bc.verify_chain()
    return render_template('verification.html', results=results)


@app.route('/diploma', methods=['GET'])
def diploma(result):
    return render_template('diploma.html', results=result)


if __name__ == '__main__':
    app.run(debug=True)
