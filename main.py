from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define the endpoint of the API
api_endpoint = "https://hp-api.onrender.com/api/characters"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters', methods=['GET', 'POST'])
def characters():
    # Get the selected category from the dropdown menu
    category = request.form['category']

    # Fetch the characters from the API
    response = requests.get(api_endpoint)
    characters = response.json()

    # Filter the characters based on the selected category
    filtered_characters = []
    for character in characters:
        if category in character['house']:
            filtered_characters.append(character)

    # Render the characters template with the filtered characters
    return render_template('characters.html', characters=filtered_characters)

if __name__ == '__main__':
    app.run(debug=True)