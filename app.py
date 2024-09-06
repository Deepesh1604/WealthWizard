from flask import Flask, render_template

app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    return render_template('home.html')  # Ensure this matches the HTML file name.

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
