from flask import Flask,request
from operations import add, sub, mult, div

app = Flask(__name__)

functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operation>")
def calculator(operation):
    """call on operations from operations file"""
    a = request.args.get("a",default=0,type=int)
    b = request.args.get("b",default=0,type=int)
    return str(functions[operation](a,b))
