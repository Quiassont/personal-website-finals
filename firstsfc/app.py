from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='firstsfc/dist', static_url_path='') # Adjust 'firstsfc/dist' to your actual dist folder path

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True) # Remove debug=True for production on PythonAnywhere