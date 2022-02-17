from flask import Flask,request,jsonify
import json

app = Flask(__name__)

todoapp=[{'id':'0','tittle':'todo name','description':'todo content'}]

@app.route('/',methods=['GET','POST'])
def addtask():
    if request.method == 'GET':
        return jsonify({
            'todoapp':todoapp
        })
    elif request.method == 'POST':
        data=json.loads(request.data)
        todoid = data['id']
        todotittle = data['tittle']
        tododescription = data['description']

        addnew = {
            'id':todoid,
            'tittle':todotittle,
            'description':tododescription
        }

        todoapp.append(addnew)
        return jsonify({
            'msg': 'add done'
        })


@app.route('/update/<int:id>',methods=['GET','PUT'])
def updatetask(id):
    if request.method == 'GET':
        return jsonify({
            'todoapp':todoapp[id]
        })
    elif request.method == 'PUT':
        data = json.loads(request.data)
        todoid = data['id']
        todotittle = data['tittle']
        tododescription = data['description']

        updatetodo = {
            'id': todoid,
            'tittle':todotittle,
            'description': tododescription
        }
        todoapp[id]=updatetodo
        return jsonify({
            'todoapp': todoapp[id]
        })
@app.route('/delete/<int:id>',methods=['GET','DELETE'])
def deletetask(id):
    if request.method == 'GET':
        return jsonify({
            'todoapp': todoapp[id]
        })
    elif request.method == 'DELETE':
        todoapp.pop(id)
        return jsonify({
            'msg':'deleted'
        })

app.run(host='127.0.0.1',port=5000,debug=True)