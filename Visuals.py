# This creates the page for displaying data visualizations.

import streamlit as st
import json
import altair
import pandas

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("My Ideal Weekend with a Friend")
st.write("How I would spend an ideal weekend with a friend broken down into your prefences and the time we'd spend doing each one!")

# PART 1: GRAPHS FROM data.json
with open("data.json","r") as file:
    data = json.load(file)
    st.write(data)

st.subheader(data["chart_title"])
st.bar_chart(data["data_points"],x="label",y="value")

activities = []
for point in data[data.points]:
    activities.append(point["Label"])

if chosenActivity not in st.sessionState:
    st.sessionState[chosenActivity] = activities

st.multiselect("What activities are you down to join me?",options = activities,key = "chosenActivity")
selectedData = []

for point in data[data.points]:
    if point["Label"] in  st.sessionState[chosenActivity]:
        selectedData.append(point)

if selectedData:
    chartData = pd.DataFrame(selectedData)

    pie = altair.Chart(chartData).markArc().encode(
        theta=alt.Theta("value:Q", title="Hours"),
        color=alt.Color("label:N", title="Activity")).properties(title="Our Weekend Adventures")

    st.altair_chart(pie)
else:
    st.write("Please choose at least one") 
        
    

# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
