import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ---------------------------------------
# Component Health Bar Chart
# ---------------------------------------

def component_health_chart(result):

    df = pd.DataFrame({
        "Component": [
            "Compressor",
            "Combustor",
            "Turbine",
            "Overall"
        ],

        "Health": [
            result["compressor"],
            result["combustor"],
            result["turbine"],
            result["overall"]
        ]
    })

    fig = px.bar(

        df,

        x="Component",

        y="Health",

        color="Health",

        text="Health",

        color_continuous_scale="Viridis"

    )

    fig.update_layout(

        title="Engine Component Health",

        template="plotly_dark",

        height=400,

        coloraxis_showscale=False

    )

    fig.update_traces(

        texttemplate='%{text:.1f}%',

        textposition='outside'

    )

    return fig


# ---------------------------------------
# Overall Health Gauge
# ---------------------------------------

def health_gauge(value):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            number={'suffix': "%"},

            title={'text': "Overall Health"},

            gauge={

                "axis": {"range": [0,100]},

                "bar": {"color":"limegreen"},

                "steps":[

                    {"range":[0,50],"color":"red"},

                    {"range":[50,75],"color":"orange"},

                    {"range":[75,100],"color":"green"}

                ]

            }

        )

    )

    fig.update_layout(

        template="plotly_dark",

        height=350

    )

    return fig


# ---------------------------------------
# Health Trend
# ---------------------------------------

def health_trend(result):

    health = result["overall"]

    values = [

        health+4,

        health+2,

        health+1,

        health,

        health-1,

        health-2,

        health-3

    ]

    cycles = [

        "Cycle 1",

        "Cycle 2",

        "Cycle 3",

        "Cycle 4",

        "Cycle 5",

        "Cycle 6",

        "Cycle 7"

    ]

    fig = px.line(

        x=cycles,

        y=values,

        markers=True

    )

    fig.update_layout(

        title="Health Trend",

        template="plotly_dark",

        yaxis_title="Health (%)",

        xaxis_title="Engine Cycle",

        height=350

    )

    return fig
