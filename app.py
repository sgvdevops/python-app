from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the form
        user_name = request.form['username']
        user_email = request.form['email']
        
        # Here, you can do something with the data (like save it to a database)
        # For now, we'll just return a simple confirmation message
        return render_template('submit.html', name=user_name, email=user_email)

if __name__ == '__main__':
    app.run(debug=True)
