import blockchain as bc
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        sender = request.form['sender']
        amount = request.form['amount']
        receiver = request.form['receiver']

        if len(sender) > 0 or len(amount) > 0 or len(receiver) > 0:
            if not bc.verify_input(sender, amount, receiver):
                feedback = ["The input is invalid. Please try again."]
                return render_template('index.html', feedback=feedback)

        bc.create_block(payer=sender, amount=amount, receiver=receiver)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/verification', methods=['GET'])
def verification():
    results = bc.verify_chain()
    return render_template('verification.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
