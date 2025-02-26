import streamlit as st

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

# Length converter function 
def Length_converter(from_unit, to_unit, value):
    units = {
         "Meter": 1,
         "Kilometer": 1000,
         "Centimeter": 0.01,
         "Millimeter": 0.001,
         "Inch": 0.0254,
         "Foot": 0.3048,
         "Yard": 0.9144,
         "Mile": 1609.34,
         "Nautical Mile": 1852,
         "Light Year": 9.4607e15
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Temperature Converter Function
def temperature_converter(from_unit, to_unit, value):
    # Convert from the input unit to Kelvin
    if from_unit == "Celsius":
        k = value + 273.15
    elif from_unit == "Fahrenheit":
        k = (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        k = value
    elif from_unit == "Rankine":
        k = value * 5/9
    else:
        k = value

    # Convert from Kelvin to the target unit
    if to_unit == "Celsius":
        result = k - 273.15
    elif to_unit == "Fahrenheit":
        result = k * 9/5 - 459.67
    elif to_unit == "Kelvin":
        result = k
    elif to_unit == "Rankine":
        result = k * 9/5
    else:
        result = k
    return result

# Weight Converter Function
def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Metric Ton": 1000,
        "Stone": 6.35029,
        "Imperial Ton": 1016.05
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
        "Atmospheres": 101325,
        "mmHg": 133.322,
        "psi": 6894.76
    }
    result = value * units[from_unit] / units[to_unit]
    return result
def energy_converter(from_unit, to_unit, value):
    units = {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,    
        "Kilocalorie": 4184,   
        "Electronvolt": 1.60218e-19,
        "Kilowatt-hour": 3600000,
        "BTU": 1055.06
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Power Converter Function

def power_converter(from_unit, to_unit, value):
    power_units = {
        "Watts": 1,
        "Kilowatts": 1000,
        "Horsepower": 745.699,
        "BTU/hour": 3412.14,
        "Megawatts": 1000000
    }
    result = value * power_units[from_unit] / power_units[to_unit]
    return result

# Volume Converter Function

def volume_converter(from_unit, to_unit, value):
    volume_units = {
        "Cubic Meter": 1,
        "Liter": 0.001,
        "Milliliter": 1e-6,
        "US Gallon": 0.00378541,
        "US Quart": 0.000946353,
        "US Pint": 0.000473176,
        "US Cup": 0.000236588,
        "US Fluid Ounce": 2.9574e-5,
        "US Tablespoon": 1.47868e-5,
        "US Teaspoon": 4.92892e-6
    }
    result = value * volume_units[from_unit] / volume_units[to_unit]
    return result



# streamlit UI
st.markdown("<h1 class='title'>Unit Converter</h1>", unsafe_allow_html=True)

# Create container for unit type selection
st.markdown("<div class='unit-type'>", unsafe_allow_html=True)
unit_type = st.selectbox("Select Unit Type", ["Length", "Temperature", "Weight", "Pressure", "Energy", "Power", "Volume"])

# Use columns for input fields to improve layout
col1, col2 = st.columns(2)

if unit_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot", "Yard", "Mile", "Nautical Mile", "Light Year"])
    with col2:
        to_unit = st.selectbox("To", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot", "Yard", "Mile", "Nautical Mile", "Light Year"])
    
    value = st.number_input("Enter Value")
    result = Length_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin", "Rankine"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin", "Rankine"])
    
    value = st.number_input("Enter Value")
    result = temperature_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Ton", "Stone", "Imperial Ton"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces", "Metric Ton", "Stone", "Imperial Ton"])
    
    value = st.number_input("Enter Value")
    result = weight_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Pressure":
    with col1:
        from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar", "Atmospheres", "mmHg", "psi"])
    with col2:
        to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar", "Atmospheres", "mmHg", "psi"])
    
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Energy":
    with col1:
        from_unit = st.selectbox("From", ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Electronvolt", "Kilowatt-hour", "BTU"])
    with col2:
        to_unit = st.selectbox("To", ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Electronvolt", "Kilowatt-hour", "BTU"])
    
    value = st.number_input("Enter Value")
    result = energy_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Power":
    with col1:
        from_unit = st.selectbox("From", ["Watts", "Kilowatts", "Horsepower", "BTU/hour", "Megawatts"])
    with col2:
        to_unit = st.selectbox("To", ["Watts", "Kilowatts", "Horsepower", "BTU/hour", "Megawatts"])
    
    value = st.number_input("Enter Value")
    result = power_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

elif unit_type == "Volume":
    with col1:
        from_unit = st.selectbox("From", ["Cubic Meter", "Liter", "Milliliter", "US Gallon", "US Quart", "US Pint", "US Cup", "US Fluid Ounce", "US Tablespoon", "US Teaspoon"])
    with col2:
        to_unit = st.selectbox("To", ["Cubic Meter", "Liter", "Milliliter", "US Gallon", "US Quart", "US Pint", "US Cup", "US Fluid Ounce", "US Tablespoon", "US Teaspoon"])
    
    value = st.number_input("Enter Value")
    result = volume_converter(from_unit, to_unit, value)
    st.markdown(f"<div class='result'>{value} {from_unit} is equal to {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
else:
    st.error("Invalid Unit Type")
# Close container for unit type selection
st.markdown("</div>", unsafe_allow_html=True)



