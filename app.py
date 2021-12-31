from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/isEven", methods=["POST"])
def isEven():
	return jsonify(bool(request.json[0] % 2 == 0))


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
	
