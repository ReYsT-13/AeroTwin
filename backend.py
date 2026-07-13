import joblib
import pandas as pd
import numpy as np

# ---------------------------------------
# Load AI Model
# ---------------------------------------

model = joblib.load("models/model.pkl")


# ---------------------------------------
# Feature Names
# ---------------------------------------

FEATURE_COLUMNS = [
    "Altitude_m",
    "Mach",
    "Tamb_K",
    "Pamb_Pa",
    "RPM_rev_min",
    "FuelFlow_kg_s",
    "P2_Pa",
    "T2_K",
    "P3_Pa",
    "T3_K",
    "P4_Pa",
    "T4_K"
]


# ---------------------------------------
# Predict
# ---------------------------------------

def predict_engine(inputs):
    """
    inputs:
        list containing 12 input values

    returns:
        dictionary of predictions
    """

    df = pd.DataFrame([inputs], columns=FEATURE_COLUMNS)

    prediction = model.predict(df)[0]

    compressor = float(prediction[0])
    combustor = float(prediction[1])
    turbine = float(prediction[2])
    overall = float(prediction[3])

    thrust = float(prediction[4])
    tsfc = float(prediction[5])

    # -----------------------------------
    # AI Confidence
    # (simple heuristic)
    # -----------------------------------

    confidence = min(
        99,
        round(
            90
            + (
                compressor
                + combustor
                + turbine
            )
            * 3,
            1,
        ),
    )

    # -----------------------------------
    # Maintenance Recommendation
    # -----------------------------------

    if overall >= 0.90:
        status = "🟢 HEALTHY"

    elif overall >= 0.75:
        status = "🟡 INSPECTION RECOMMENDED"

    else:
        status = "🔴 MAINTENANCE REQUIRED"

    return {

        "compressor": round(compressor * 100, 1),

    "combustor": round(combustor * 100, 1),

    "turbine": round(turbine * 100, 1),

    "overall": round(overall * 100, 1),

    "thrust": round(thrust / 1000, 2),   # Convert N → kN

    "tsfc": round(tsfc, 4),

    "confidence": confidence,

    "status": status
    }


if __name__ == "__main__":

    sample = [
        8000,
        0.75,
        288,
        40000,
        9000,
        0.35,
        80000,
        350,
        200000,
        1200,
        60000,
        700
    ]

    result = predict_engine(sample)

    print(result)