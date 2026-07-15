import streamlit as st
from PIL import Image
from backend import predict_engine
from physics import calculate_physics

from charts import (
    component_health_chart,
    health_gauge,
    health_trend
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AeroTwin Digital Twin",
    page_icon="✈️",
    layout="wide"
)
banner = Image.open("assets/banner.png")

st.image(
    banner,
    use_container_width=True
)

st.markdown(
    """
    <div style="text-align:center;
                color:#9CA3AF;
                font-size:18px;
                margin-top:-10px;
                margin-bottom:20px;">
    AI + Physics Powered Turbojet Digital Twin
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.write("")
st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Engine Inputs")

Altitude = st.sidebar.slider(
    "Altitude (m)",
    0,
    12000,
    8000
)

Mach = st.sidebar.slider(
    "Mach Number",
    0.0,
    1.5,
    0.75
)

Tamb = st.sidebar.slider(
    "Ambient Temperature (K)",
    200,
    330,
    288
)

Pamb = st.sidebar.slider(
    "Ambient Pressure (Pa)",
    10000,
    101325,
    40000
)

RPM = st.sidebar.slider(
    "RPM",
    1000,
    15000,
    9000
)

FuelFlow = st.sidebar.slider(
    "Fuel Flow (kg/s)",
    0.05,
    1.00,
    0.35
)

P2 = st.sidebar.slider(
    "P2 (Pa)",
    10000,
    300000,
    80000
)

T2 = st.sidebar.slider(
    "T2 (K)",
    200,
    700,
    350
)

P3 = st.sidebar.slider(
    "P3 (Pa)",
    10000,
    500000,
    200000
)

T3 = st.sidebar.slider(
    "T3 (K)",
    600,
    1800,
    1200
)

P4 = st.sidebar.slider(
    "P4 (Pa)",
    1000,
    300000,
    60000
)

T4 = st.sidebar.slider(
    "T4 (K)",
    400,
    1500,
    700
)

# -------------------------------------------------
# RUN MODEL
# -------------------------------------------------

if st.button("🚀 Predict Engine Health"):

    result = predict_engine([
        Altitude,
        Mach,
        Tamb,
        Pamb,
        RPM,
        FuelFlow,
        P2,
        T2,
        P3,
        T3,
        P4,
        T4
    ])

    physics = calculate_physics(
        P2,
        P3,
        T3,
        T4, 
         result["overall"]
    )

    st.success(
        f"Prediction Complete • {result['status']}"
    )
    # -------------------------------------------------
    # AI PREDICTIONS
    # -------------------------------------------------

    st.divider()

    st.subheader("🤖 AI Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Compressor Health",
            f"{result['compressor']:.1f} %"
        )

    with c2:
        st.metric(
            "Combustor Health",
            f"{result['combustor']:.1f} %"
        )

    with c3:
        st.metric(
            "Turbine Health",
            f"{result['turbine']:.1f} %"
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "Overall Health",
            f"{result['overall']:.1f} %"
        )

    with c5:
        st.metric(
            "Predicted Thrust",
            f"{result['thrust']:.2f} kN"
        )

    with c6:
        st.metric(
            "TSFC",
            f"{result['tsfc']:.4f}"
        )

    st.info(
        f"🤖 Model Confidence : {result['confidence']}%"
    )

    st.markdown(f"""
<div style="
background:#0B1220;
padding:18px;
border-radius:15px;
border-left:8px solid #10B981;
margin-bottom:25px;
">

<h2 style="color:white;">
🟢 Engine Status : {result["status"]}
</h2>

<p style="font-size:18px;color:#D1D5DB;">

Overall Health :
<b>{result["overall"]:.1f}%</b>

<br>

Hybrid Agreement :
<b>{physics["hybrid_score"]}%</b>

<br>

Model Confidence :
<b>{result["confidence"]}%</b>

</p>

</div>
""", unsafe_allow_html=True)

    # -------------------------------------------------
    # VISUAL DASHBOARD
    # -------------------------------------------------

    st.divider()

    st.subheader("📊 Engine Health Dashboard")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            health_gauge(result["overall"]),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            component_health_chart(result),
            use_container_width=True
        )

    st.plotly_chart(
        health_trend(result),
        use_container_width=True
    )

    # -------------------------------------------------
    # PHYSICS LAYER
    # -------------------------------------------------

    st.divider()

    st.subheader("⚙️ Physics Validation")
    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Pressure Ratio",
            physics["pressure_ratio"]
        )

        st.metric(
            "Temperature Drop",
            f"{physics['temperature_drop']} K"
        )

    with col2:

        st.metric(
            "Ideal Brayton Efficiency",
            f"{physics['ideal_efficiency']} %"
        )

        st.metric(
            "Hybrid Confidence",
            f"{physics['hybrid_score']} %"
        )

    st.success(
        physics["assessment"]
    )

    # -------------------------------------------------
    # HYBRID DIGITAL TWIN
    # -------------------------------------------------

    st.divider()

    st.subheader("🛰 Hybrid Digital Twin Assessment")

    st.metric(
        "Hybrid Confidence",
        f"{physics['hybrid_score']} %"
    )

    if physics["hybrid_score"] >= 90:
        st.success(physics["assessment"])

    elif physics["hybrid_score"] >= 70:
        st.warning(physics["assessment"])

    else:
        st.error(physics["assessment"])

    st.divider()

    st.caption(
        "AeroTwin • Hybrid Digital Twin using Machine Learning + Brayton Cycle Physics"
    )
