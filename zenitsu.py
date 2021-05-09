from flask import Flask,jsonify,request

app = Flask(__name__)

contact = {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact',""),
    'done':False
}
@app.route("/add-data",methods=["POST"])
def hello_world():
    if not request.json
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

if (__name__ == "__main__"):
    app.run(debug=True)