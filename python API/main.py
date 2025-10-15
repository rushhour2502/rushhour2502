from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "hey brother how are you doing"

    """
    GET:REQUEST DATA FROM A SPECIFIED RESOURCE
    POST:CREATE A RESOURCE
    PUT:UPDATE A RESOURCE
    DELETE:DELETE A RESOURCE
    """
     
if __name__=="__main__":
    app.run(debug=True)
