import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import r2_score
import joblib

print("Loading dataset...")

df = pd.read_csv("data/turbojet_complete_dataset.csv")

print("\nColumns in dataset:")
print(df.columns.tolist())

# -----------------------------
# INPUT FEATURES
# -----------------------------
feature_columns = [
   "Altitude_m", "Mach",
    "Tamb_K", "Pamb_Pa",
    "RPM_rev_min", "FuelFlow_kg_s",
    "P2_Pa", "T2_K",
    "P3_Pa", "T3_K", "P4_Pa", "T4_K"
]

# -----------------------------
# OUTPUT TARGETS
# -----------------------------
target_columns = [
    "CompressorHealth",
    "CombustorHealth",
    "TurbineHealth",
    "OverallHealth",
    "Thrust_N",
    "TSFC_g_N_s"
]

X = df[feature_columns]
y = df[target_columns]

print(f"\nTraining on {len(df)} samples...")

model = MultiOutputRegressor(
    RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
)

model.fit(X, y)

predictions = model.predict(X)

score = r2_score(y, predictions)

print(f"\nTraining R² Score: {score:.4f}")

joblib.dump(model, "models/model.pkl")

print("\nModel saved successfully!")