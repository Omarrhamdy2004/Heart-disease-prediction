import sys
import json
import joblib

# Load the model
try:
    model = joblib.load("project.pkl")
except Exception as e:
    print(json.dumps({"error": f"Failed to load model: {str(e)}"}))
    sys.exit(1)

# Get input from Node.js
try:
    data = json.loads(sys.argv[1])
    input_data = data["input"]
except Exception as e:
    print(json.dumps({"error": f"Invalid input: {str(e)}"}))
    sys.exit(1)

# Validate input_data
if not isinstance(input_data, list):
    print(json.dumps({"error": "Input data must be a list."}))
    sys.exit(1)
# Check for correct number of features
expected_input_length = model.n_features_in_  # Get expected number of features
if len(input_data) != expected_input_length:
    print(json.dumps({"error": f"Input data must have {expected_input_length} features."}))
    sys.exit(1)
# Predict
try:
    prediction = model.predict([input_data])
    print(json.dumps({"prediction": prediction.tolist()}))
except Exception as e:
    print(json.dumps({"error": f"Prediction failed: {str(e)}"}))
    sys.exit(1)