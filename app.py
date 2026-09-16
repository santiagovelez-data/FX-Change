import streamlit as st
import datetime
import pandas as pd
import altair as alt

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate, get_rate_trend, get_daily_rates
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("Currency Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()
if currencies is None:
    st.error("Currency not available")    

# Add input fields for capturing amount, from and to currencies
amount = st.number_input("Amount", value = 1)

# creates the currency selectors for from and to currencies
from_currency = st.selectbox("From currency", currencies, index=currencies.index("USD"))
to_currency = st.selectbox("To currency", currencies, index=currencies.index("AUD"))

# display the latest rate for selected currencies and amount
if st.button("Get latest rate"):
    result = get_latest_rates(from_currency, to_currency, amount)
    rate_date = result[0]
    rate = result[1]
    if rate is None:
        st.error("Could not get the exchange rate.")
    else:
        output = format_output(rate_date, from_currency, to_currency, rate, amount)
        st.text(output)

# Add a date selector (calendar)
date_selector = st.date_input("Need a different date?")

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button("Historical Rate"):
    date_text = str(date_selector)
    result = get_historical_rate(from_currency, to_currency, date_text, amount)
    rate = result
    if rate is None:
        st.error("Could not get the exchange rate.")
    else:
        output = format_output(date_text, from_currency, to_currency, rate, amount)
        st.text(output)        

#display currency exchange rate trends
st.write("Trend over time")
years = st.slider("Years to display", min_value=1, max_value=10, value=1)

if from_currency == to_currency:
    st.info("Choose two different currencies.")
else:
    trend = get_daily_rates(from_currency, to_currency, years)

    if trend is None:
        st.error("Could not load exchange rates.")
    else:
        chart_data = pd.DataFrame(
            list(trend.items()),
            columns=["Date", "Rate"]
        )
        chart = alt.Chart(chart_data).mark_line().encode(
    x=alt.X("Date:T", axis=None),
    y="Rate:Q"
)

st.altair_chart(chart, use_container_width=True)

st.divider()
st.caption('Created by Santiago Velez Cardenas for Data Science Practice')
st.caption('Professor: Mir Kabir')
st.caption('University of Technology Sydney')
st.caption('Student ID: 14751465')