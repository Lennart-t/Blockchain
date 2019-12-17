#Creation of front end by using Python's Flask structure
import blockchain as bc
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
#Link to file template to enable Flask to comprehend paths
app = Flask(__name__, template_folder='template')

#Routing to index.html page, which is the base page of our application
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#Routing to addgraduate.html, where function add_graduate enables user to fill form to add a new block to blockchain
@app.route('/addgraduate', methods=['POST', 'GET'])
def add_graduate():
    if request.method == 'POST':
        key = request.form['key']
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']
        #Checks for input
        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "" or key != "12345":
            feedback = "The input is invalid. Please try again."
            return render_template('addgraduate.html', feedback=feedback, subject=subject, color="red", name=name,
                                   birthday=birthday, graduation=graduation, key=key)
        #If all input valid, it returns success message and uses create_block() function from blockchain.py to add a new block to blockcahin
        feedback = "Diploma successfully added to the blockchain!"
        bc.create_block(name=name, birthday=birthday, subject=subject, graduation=graduation, key=key)
        return render_template('addgraduate.html', feedback=feedback, subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")

    return render_template('addgraduate.html', subject="Choose...", color="green", name="",
                                   birthday="", graduation="", key="")

#Routing to chechkgraduate.html, where user can fill a form to check whether block with entered data already exisits
@app.route('/checkgraduate', methods=['POST', 'GET'])
def check_graduate():
    subject = "Choose..."
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        subject = request.form['subject']
        graduation = request.form['graduation']
        #Checks if all input-fiels are filled and returns error message if not
        if len(name) == 0 or subject == "Choose..." or birthday == "" or graduation == "":
            feedback = "The input is invalid. Please try again."
            return render_template('checkgraduate.html', feedback=feedback, subject=subject)
        #If form succesfully filled verify_diploma() function from blockchain.py will search each block in chain for entered data and return false block or geniune block 
        result = bc.verify_diploma(name=name, birthday=birthday, subject=subject, graduation=graduation)
        #User will be routed to diploma.html (function is defined below), where result of verify_diploma will be shown. 
        return diploma(result)

    return render_template('checkgraduate.html', subject=subject)

#Routing to verification.html, where without any input from user function verify_chain from blockchain.py will be executed and check if blockchain is corrupted
@app.route('/verification', methods=['GET'])
def verification():
    results = bc.verify_chain()
    return render_template('verification.html', results=results)


@app.route('/diploma', methods=['GET'])
def diploma(result):
    return render_template('diploma.html', results=result)

#Standard statement that checks if the script is launched from the console and runs our application. Debug is added to allow flask to relaid everytime if code is changed
if __name__ == '__main__':
    app.run(debug=True)
