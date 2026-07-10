from flask import Flask, jsonify, render_template
from services.simulator import generate_train_data
from services.predictor import predict_delay
from services.scheduler import detect_conflicts, resolve_conflicts

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/simulate", methods=["GET"])
def simulate():
    trains = generate_train_data()
    return jsonify({
        "success": True,
        "message": "Simulated train data generated successfully",
        "data": trains
    })


@app.route("/api/run-control", methods=["GET"])
def run_control():
    trains = generate_train_data()

    predictions = []
    for train in trains:
        predictions.append({
            "train_id": train["train_id"],
            "predicted_delay": predict_delay(train)
        })

    conflicts = detect_conflicts(trains)
    updated_trains, resolutions = resolve_conflicts(trains, conflicts)

    return jsonify({
        "success": True,
        "message": "Traffic control executed successfully",
        "data": {
            "trains": updated_trains,
            "predictions": predictions,
            "conflicts": conflicts,
            "resolutions": resolutions
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
