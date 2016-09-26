from flask import Flask, render_template
app2 = Flask(__name__)##creates an instance of a flask and instatiates its name

@app2.route("/")

def hello_world():
    return "No hablo queso-v2"

coll = [1, 3, 3, 7]

@app2.route("/my_first_template")
def tet_template():
    return render_template("foo.html", foo = "SILENCIO", fool=coll)

    
if __name__=="__main__":
        app2.debug = True
        app2.run()
        
