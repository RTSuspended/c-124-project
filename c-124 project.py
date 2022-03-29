from flask import Flask,jsonify,request

app=Flask(__name__)
tasks=[
    {
        'id':1,
        'Name':u'Vikas',
        'Contact':u'9818999300',
        'done':False
    },
    {
        'id':2,
        'Name':u'Geetu',
        'Contact':u'9818999498',
        'done':False
    }
]
@app.route('/add-data',methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)

    t={
        "id":tasks[-1]["id"]+1,
        "title":request.json['title'],
        "description":request.json.get('description'," "),
        "done":False
    }
    tasks.append(t)

    return jsonify({
            "status":"success",
            "message":"task added successfully"
        })

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)