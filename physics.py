def calculate_physics(P2, P3, T3, T4, ai_health):
    """
    Hybrid physics layer.

    Calculates:
    - Compressor Pressure Ratio
    - Turbine Temperature Drop
    - Ideal Brayton Efficiency

    Then compares them with the AI prediction.
    """

    gamma = 1.4

    # -------------------------
    # Physics calculations
    # -------------------------

    pressure_ratio = P3 / P2 if P2 else 0

    temperature_drop = T3 - T4

    if pressure_ratio > 0:
        ideal_efficiency = (
            1
            - 1 / (pressure_ratio ** ((gamma - 1) / gamma))
        ) * 100
    else:
        ideal_efficiency = 0

    # -------------------------
    # Consistency score
    # -------------------------

    score = 100

    # Low pressure ratio generally indicates reduced compressor performance
    if pressure_ratio < 2:
        score -= 25

    # Small turbine temperature drop means poor energy extraction
    if temperature_drop < 300:
        score -= 25

    # Very low ideal efficiency suggests poor thermodynamic performance
    if ideal_efficiency < 35:
        score -= 20

    # Compare with AI prediction
    if ai_health < 70:
        score -= 20
    elif ai_health > 90:
        score += 5

    score = max(0, min(score, 100))

    # -------------------------
    # Hybrid Assessment
    # -------------------------

    if score >= 90:
        assessment = "Excellent Agreement"

    elif score >= 75:
        assessment = "Good Agreement"

    elif score >= 60:
        assessment = "Moderate Agreement"

    else:
        assessment = "Physics and AI disagree"

    return {

        "pressure_ratio": round(pressure_ratio, 2),

        "temperature_drop": round(temperature_drop, 1),

        "ideal_efficiency": round(ideal_efficiency, 2),

        "hybrid_score": score,

        "assessment": assessment

    }