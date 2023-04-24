from flask import Flask,jsonify, request, make_response
# from flask_restful import Resource, Api, marshal_with, fields
import fuzzylab as fl

app = Flask(__name__)
# api = Api(app)

# reqFields = {
#     'input_one': fields.Float,
#     'input_two': fields.Float,
#     'input_three': fields.Float,
#     'input_four': fields.Float,
#     'input_five': fields.Float,
# }

# result = {
#     'name': fields.String,
#     'result': fields.Float,
# }

# class Predict(Resource):
#     # @marshal_with(reqFields)
#     def post(self, num):
#         model = ['Social-dimension', 'Economic-dimension', 'Environmental-dimension']
#         data = request.json
#         fis = fl.readfis('./models/'+model[num])
#         output = fl.evalfis(fis, [data['input_one'], data['input_two'], data['input_three'], data['input_four'], data['input_five']])
#         print(output)
#         return {'name': model[num], 'result': output}
    
# api.add_resource(Predict, '/predict/<int:num>')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method=='POST':
        data = request.get_json()
        num = data['id']
        model = ['Social-dimension', 'Economic-dimension', 'Environmental-dimension']
        fis = fl.readfis('./models/'+model[num])
        output = fl.evalfis(fis, [data['input_one'], data['input_two'], data['input_three'], data['input_four'], data['input_five']])
        print(output)
        return make_response(jsonify({'name': model[num], 'result': output}), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

