import streamlit as st

def metric_card(title, value, color="#1f77b4"):
    st.markdown(
        f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:18px;
            border-left:6px solid {color};
            box-shadow:0px 6px 15px rgba(0,0,0,0.3);
            text-align:center;
        ">
            <h4 style="color:white;margin-bottom:8px;">{title}</h4>
            <h1 style="color:{color};margin:0;">{value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


def status_card(status, color):
    st.markdown(
        f"""
        <div style="
            background-color:#111827;
            padding:20px;
            border-radius:18px;
            text-align:center;
            border:2px solid {color};
        ">
            <h2 style="color:{color};">{status}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )