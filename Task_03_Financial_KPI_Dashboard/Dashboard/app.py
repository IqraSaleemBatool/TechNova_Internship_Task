
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output



#  Loading and Preparing Data

df = pd.read_excel("Financial_Sample.xlsx")

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month-Year"] = df["Date"].dt.strftime("%Y-%m")



# 2. Creating Dash App


app = Dash(__name__)

app.title = "Financial KPI Dashboard"


# 3. Filter Options

countries = sorted(df["Country"].dropna().unique())
segments = sorted(df["Segment"].dropna().unique())
products = sorted(df["Product"].dropna().unique())
years = sorted(df["Year"].dropna().unique())


# 4. Dashboard Layout

app.layout = html.Div([

    html.H1(
        "Financial KPI Dashboard",
        style={
            "textAlign": "center",
            "marginBottom": "25px"
        }
    ),

    # Filters

    html.Div([

        html.Div([
            html.Label("Country"),
            dcc.Dropdown(
                id="country-filter",
                options=[{"label": c, "value": c} for c in countries],
                placeholder="All Countries",
                multi=True
            )
        ], style={"width": "24%"}),

        html.Div([
            html.Label("Segment"),
            dcc.Dropdown(
                id="segment-filter",
                options=[{"label": s, "value": s} for s in segments],
                placeholder="All Segments",
                multi=True
            )
        ], style={"width": "24%"}),

        html.Div([
            html.Label("Product"),
            dcc.Dropdown(
                id="product-filter",
                options=[{"label": p, "value": p} for p in products],
                placeholder="All Products",
                multi=True
            )
        ], style={"width": "24%"}),

        html.Div([
            html.Label("Year"),
            dcc.Dropdown(
                id="year-filter",
                options=[{"label": str(y), "value": y} for y in years],
                placeholder="All Years",
                multi=True
            )
        ], style={"width": "24%"})

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "marginBottom": "30px"
    }),


    
    # KPI Cards

    html.Div([

        html.Div([
            html.H4("Total Sales"),
            html.H2(id="total-sales")
        ], className="kpi-card"),

        html.Div([
            html.H4("Total Profit"),
            html.H2(id="total-profit")
        ], className="kpi-card"),

        html.Div([
            html.H4("Total COGS"),
            html.H2(id="total-cogs")
        ], className="kpi-card"),

        html.Div([
            html.H4("Profit Margin"),
            html.H2(id="profit-margin")
        ], className="kpi-card"),

        html.Div([
            html.H4("Units Sold"),
            html.H2(id="total-units")
        ], className="kpi-card")

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "marginBottom": "30px"
    }),


    # Charts

    dcc.Graph(id="monthly-financial-chart"),

    html.Div([

        html.Div([
            dcc.Graph(id="sales-segment-chart")
        ], style={"width": "50%"}),

        html.Div([
            dcc.Graph(id="profit-country-chart")
        ], style={"width": "50%"})

    ], style={"display": "flex"}),


    html.Div([

        html.Div([
            dcc.Graph(id="profit-product-chart")
        ], style={"width": "100%"})

    ])

], style={
    "padding": "30px",
    "fontFamily": "Arial"
})


#  Callback

@app.callback(

    Output("total-sales", "children"),
    Output("total-profit", "children"),
    Output("total-cogs", "children"),
    Output("profit-margin", "children"),
    Output("total-units", "children"),

    Output("monthly-financial-chart", "figure"),
    Output("sales-segment-chart", "figure"),
    Output("profit-country-chart", "figure"),
    Output("profit-product-chart", "figure"),

    Input("country-filter", "value"),
    Input("segment-filter", "value"),
    Input("product-filter", "value"),
    Input("year-filter", "value")
)

def update_dashboard(
    selected_countries,
    selected_segments,
    selected_products,
    selected_years
):

    filtered_df = df.copy()


    # Country filter
    if selected_countries:
        filtered_df = filtered_df[
            filtered_df["Country"].isin(selected_countries)
        ]


    # Segment filter
    if selected_segments:
        filtered_df = filtered_df[
            filtered_df["Segment"].isin(selected_segments)
        ]


    # Product filter
    if selected_products:
        filtered_df = filtered_df[
            filtered_df["Product"].isin(selected_products)
        ]


    # Year filter
    if selected_years:
        filtered_df = filtered_df[
            filtered_df["Year"].isin(selected_years)
        ]


    # KPI Calculations

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_cogs = filtered_df["COGS"].sum()
    total_units = filtered_df["Units Sold"].sum()

    profit_margin = (
        total_profit / total_sales * 100
        if total_sales != 0
        else 0
    )


    
    # Monthly Financial Performance

    monthly = (
        filtered_df
        .groupby("Date", as_index=False)
        .agg({
            "Sales": "sum",
            "COGS": "sum",
            "Profit": "sum"
        })
        .sort_values("Date")
    )

    monthly_fig = px.line(
        monthly,
        x="Date",
        y=["Sales", "COGS", "Profit"],
        markers=True,
        title="Monthly Financial Performance"
    )

    monthly_fig.update_layout(
        template="plotly_white"
    )


    # Ssles by Segement
    

    segment_data = (
        filtered_df
        .groupby("Segment", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    segment_fig = px.bar(
        segment_data,
        x="Segment",
        y="Sales",
        title="Sales by Customer Segment",
        text_auto=".2s"
    )

    segment_fig.update_layout(
        template="plotly_white"
    )


    # Profit By Country

    country_data = (
        filtered_df
        .groupby("Country", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    country_fig = px.bar(
        country_data,
        x="Country",
        y="Profit",
        title="Profit by Country",
        text_auto=".2s"
    )

    country_fig.update_layout(
        template="plotly_white"
    )


    # Profit by Product

    product_data = (
        filtered_df
        .groupby("Product", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    product_fig = px.bar(
        product_data,
        x="Product",
        y="Profit",
        title="Profit by Product",
        text_auto=".2s"
    )

    product_fig.update_layout(
        template="plotly_white"
    )


    
    # Returning Results

    return (
        f"${total_sales:,.2f}",
        f"${total_profit:,.2f}",
        f"${total_cogs:,.2f}",
        f"{profit_margin:.2f}%",
        f"{total_units:,.0f}",

        monthly_fig,
        segment_fig,
        country_fig,
        product_fig
    )


#  Runnig App


if __name__ == "__main__":
    app.run(debug=True)
