import streamlit as st

# Add custom CSS for styling without changing functionality
st.markdown("""
<style>
    .title {
        color: #2E86C1;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        padding: 10px;
        border-bottom: 2px solid #2E86C1;
    }
    .result {
        background-color: #eef9ff;
        padding: 20px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: 500;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stSelectbox label {
        font-weight: 500;
        color: #333;
    }
    .stNumberInput label {
        font-weight: 500;
        color: #333;
    }
    .unit-type {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# distance converter function 
def distance_converter(from_unit,to_unit,value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Temperature Converter Function
def temperature_converter(from_unit, to_unit,value):
    if from_unit =="Celsius" and to_unit =="Fahrenheit":
        result = (value * 9/5) + 32
    elif  from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

# Weight Converter Function
def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Pressure Converter Function
def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# streamlit UI
st.markdown("<h1 class='title'>Unit Converter</h1>", unsafe_allow_html=True)

# Create container for unit type selection
st.markdown("<div class='unit-type'>", unsafe_allow_html=True)
unit_type = st.selectbox("Select Unit Type", ["Distance", "Temperature", "Weight", "Pressure"])
st.markdown("</div>", unsafe_allow_html=True)

# Use columns for input fields to improve layout
col1, col2 = st.columns(2)

if unit_type == "Distance":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    
    value = st.number_input("Enter Value")
    result = distance_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    
    value = st.number_input("Enter Value")
    result = temperature_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    
    value = st.number_input("Enter Value")
    result = weight_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Pressure":
    with col1:
        from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    with col2:
        to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

else:
    st.error("Invalid Unit Type")