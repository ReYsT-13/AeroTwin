import math


def calculate_physics(P2, P3, T3, T4):
    """
    Simple Brayton-cycle based calculations.

    Inputs:
        P2 : Compressor inlet pressure (Pa)
        P3 : Compressor outlet pressure (Pa)
        T3 : Turbine inlet temperature (K)
        T4 : Turbine outlet temperature (K)

    Returns:
        Dictionary containing physics-based engine metrics.
    """

    gamma = 1.4

    # -----------------------------
    # Compressor Pressure Ratio
    # -----------------------------
    pressure_ratio = P3 / P2 if P2 != 0 else 0

    # -----------------------------
    # Turbine Temperature Drop
    # -----------------------------
    temperature_drop = T3 - T4

    # -----------------------------
    # Ideal Brayton Cycle Efficiency
    # -----------------------------
    if pressure_ratio > 0:
        ideal_efficiency = (
            1
            - 1 / (pressure_ratio ** ((gamma - 1) / gamma))
        )
    else:
        ideal_efficiency = 0

    # Convert to %
    ideal_efficiency *= 100

    # -----------------------------
    # Physics Status
    # -----------------------------
    if pressure_ratio > 8 and temperature_drop > 450:
        physics_status = "Excellent"

    elif pressure_ratio > 5 and temperature_drop > 300:
        physics_status = "Normal"

    else:
        physics_status = "Needs Inspection"

    return {

        "pressure_ratio": round(pressure_ratio, 2),

        "temperature_drop": round(temperature_drop, 1),

        "ideal_efficiency": round(ideal_efficiency, 2),

        "physics_status": physics_status

    }