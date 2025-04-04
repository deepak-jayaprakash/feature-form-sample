from flask import Flask, jsonify, request
from featureform import Client

app = Flask(__name__)
serving = Client(insecure=True)

transformation_name = "avg_transactions"
transformation_variant = "quickstart"

@app.route('/feature/<user_id>', methods=['GET'])
def get_user_feature(user_id):
    try:
        user_feat = serving.features(
            [(transformation_name, transformation_variant)], 
            {"user": user_id}
        )
        return jsonify({
            "user_id": user_id,
            "feature_value": user_feat
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) 