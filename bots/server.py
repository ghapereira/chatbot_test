from flask import Flask, request, jsonify

server = Flask(__name__)

@server.route('/')
def index():
    return 'Hello, world!'

# Example request:
# curl -H "Content-Type: application/json" -H "Authorization Key XXXX"
# -X POST -d '{"id": "0001", "to": "???@???.??", "type": "text/plain",
# "content": "Hello, how can I help you?"}' https://msging.net/messages

@server.route('/jsonresponses', methods=['POST'])
def get_response():
    if not request.json:
        abort(400)

    print(request.json)

    return jsonify(request.json), 201

if __name__ == '__main__':
    server.run(debug=True)
