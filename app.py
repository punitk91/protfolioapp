
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    updates = [
        {"date": "2024-09-29", "content": "Started learning Flask for web development."},
        {"date": "2024-09-28", "content": "Updated my resume with new backend project details."}
    ]
    return render_template('index.html', updates=updates)

# Route for About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Logic to handle form submission, e.g., send email or save to a database
        return 'Message sent!'
    return render_template('contact.html')

# Route to download resume
@app.route('/resume')
def download_resume():
    return send_file('static/resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
