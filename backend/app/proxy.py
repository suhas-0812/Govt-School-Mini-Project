from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL parameter'}), 400

    response = requests.get(url)
    return response.content, response.status_code

if __name__ == '__main__':
    app.run(port=8000)  # Run the proxy server on port 8000
