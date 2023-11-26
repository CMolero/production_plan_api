from flask import Flask, request, jsonify
from production_plan import calculate_production_plan

app = Flask(__name__)

@app.route("/productionplan", methods=["POST"])
def production_plan_endpoint():
    try:
        payload = request.get_json()
        result = calculate_production_plan(payload)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8888)
