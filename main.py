# Creation of front-end mechanics by using Python's Flask extension.
import blockchain as bc
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

# Link to file template to enable Flask to comprehend paths.
app = Flask(__name__, template_folder='template')

# Routing to index.html page, which is the home page of our application.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Routing to addgraduate.html, where function add_graduate() enables user to fill form to add a new block to blockchain.
@app.route('/addgraduate', methods=['POST', 'GET'])
def add_graduate():
    if request.method == 'POST':
        key = request.form['key']
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']
        # Check if user input is correctedly filled in and if the key is correct. Otherwise, produce negative feedback.
        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "" or key != "12345":
            feedback = "The input is invalid. Please try again."
            return render_template('addgraduate.html', feedback=feedback, subject=subject, color="red", name=name,
                                   birthday=birthday, graduation=graduation, key=key)

        # If all input fields are valid, we return a success message and call the create_block() function from
        # blockchain.py to add a new block to blockchain with the data provided by the user. After successfully
        # creating a block, we reset all input fields.
        feedback = "Diploma successfully added to the blockchain!"
        bc.create_block(name=name, birthday=birthday, subject=subject, graduation=graduation, key=key)
        return render_template('addgraduate.html', feedback=feedback, subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")

    return render_template('addgraduate.html', subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")

# Routing to checkgraduate.html, where the user can fill out a form to check whether a block with entered data exists in
# the chain and whether this block is genuine or corrupted.
@app.route('/checkgraduate', methods=['POST', 'GET'])
def check_graduate():
    subject = "Choose..."
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']
        # Checks if all input-fiels are filled in correctly and returns feedback message if not.
        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "":
            feedback = "The input is invalid. Please try again."
            return render_template('checkgraduate.html', feedback=feedback, subject=subject)
        # If the form is successfully filled in, the verify_diploma() function from blockchain.py will search through
        # each block in the chain for entered data and if its real.
        result = bc.verify_diploma(name=name, birthday=birthday, subject=subject, graduation=graduation)
        # User will be routed to diploma.html, where result of verify_diploma() method will be shown.
        return diploma(result)

    return render_template('checkgraduate.html', subject=subject)

# Routing to verification.html, where without any input from user the method verify_chain() from blockchain.py will be
# executed before entering the page and the output will be shown.
@app.route('/verification', methods=['GET'])
def verification():
    results = bc.verify_chain()
    return render_template('verification.html', results=results)


# Simple method that loads the result-page of the method verify_diploma().
@app.route('/diploma', methods=['GET'])
def diploma(result):
    return render_template('diploma.html', results=result)


# Standard statement that checks if the script is launched from the console and that runs our application if not.
# Debug is added to allow flask to reload every time if code is changed.
if __name__ == '__main__':
    app.run(debug=True)
