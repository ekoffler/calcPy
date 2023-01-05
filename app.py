from flask import Flask, jsonify, json, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/calculator', methods=['POST'])
def calculator():
    def use_calculator(operation, number1, number2):
        n1 = int(number1)
        n2 = int(number2)
        if operation == 'add':
            result = n1 + n2
        elif operation == 'subtract':
            result = n1 - n2
        elif operation == 'divide':
            result = n1 / n2
        elif operation == 'multiply':
            result = n1 * n2
        else: 
            result = 'Invalid operation'
        return str(result)

    operation = request.json['operation']
    n1 = request.json['n1']
    n2 = request.json['n2']
    result = use_calculator(operation, n1, n2)
    return jsonify({"El resultado de la operacion es": result})

if __name__ == '__main__':
    app.run(debug=True, port=4000)




