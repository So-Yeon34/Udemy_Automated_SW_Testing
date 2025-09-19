from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/') # http://www.mysite.com/blog

def home():
    return jsonify({'message' : 'Hello, world!'}) # Dictionary message return

# The condition `if __name__ == "__main__":` ensures that
# the code inside this block only runs when this file is executed directly,
# e.g., with `python app.py`.
# If this file is imported as a module in another file,
# the code inside will NOT run automatically.
#
# This prevents the Flask server from starting unintentionally
# when the file is imported elsewhere.
if __name__ == '__main__':
    app.run()