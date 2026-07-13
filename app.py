import streamlit as st
from backend import predict_engine
from charts import (
    component_health_chart,
    health_gauge,
    health_trend
)

# ----------------------------
# PAGE SETTINGS
# ----------------------------
st.set_page_config(
    page_title="AeroTwin Digital Twin",
    layout="wide"
)

st.title("✈️ AeroTwin - Digital Twin Dashboard")
st.caption("HAL x IIT Indore | AI-based Turbojet Health Monitoring")



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

# ----------------------------
# PREDICT BUTTON
# ----------------------------

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
    st.success(f"Prediction Complete!  {result['status']}")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Compressor Health",
        f"{result["compressor"]:.2f}"
    )

    c2.metric(
        "Combustor Health",
        f"{result["combustor"]:.2f}"
    )

    c3.metric(
        "Turbine Health",
        f"{result["turbine"]:.2f}"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Overall Health",
        f"{result["overall"]:.2f}"
    )

    c5.metric(
        "Predicted Thrust",
        f"{result["thrust"]:.2f}"
    )

    c6.metric(
        "TSFC",
        f"{result["tsfc"]:.4f}"
    )

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
    st.info(f"🤖 AI Confidence: {result['confidence']}%")