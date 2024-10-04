import streamlit as st

# Define emission factors for different industries
INDUSTRY_EMISSION_FACTORS = {
    "Manufacturing": {
        "Electricity": 0.14,  # kgCO2/kWh
        "Natural Gas": 0.185,  # kgCO2/m3
        "Fuel Oil": 0.33,  # kgCO2/litre
        "Waste": 0.05  # kgCO2/kg (landfill emission)
    },
    "Agriculture": {
        "Diesel": 2.68,  # kgCO2/litre
        "Electricity": 0.14,  # kgCO2/kWh
        "Waste": 0.05  # kgCO2/kg (landfill emission)
    },
    "Transportation": {
        "Diesel": 2.68,  # kgCO2/litre
        "Gasoline": 2.31,  # kgCO2/litre
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Industrial Carbon Calculator for Kenya")

# Streamlit app code
st.title("Industrial Carbon Calculator App - Kenya")

# User inputs
st.subheader("🏭 Select Your Industry")
industry = st.selectbox("Select", list(INDUSTRY_EMISSION_FACTORS.keys()))

col1, col2 = st.columns(2)

if industry == "Manufacturing":
    with col1:
        st.subheader("💡 Monthly electricity consumption (in kWh)")
        electricity = st.slider("Electricity", 0.0, 10000.0, key="electricity_input")

        st.subheader("🔥 Natural Gas consumption (in m³)")
        gas = st.slider("Natural Gas", 0.0, 5000.0, key="gas_input")

    with col2:
        st.subheader("🚚 Fuel Oil consumption (in litres)")
        fuel_oil = st.slider("Fuel Oil", 0.0, 5000.0, key="fuel_input")

        st.subheader("🗑️ Waste generated per month (in kg)")
        waste = st.slider("Waste", 0.0, 2000.0, key="waste_input")

elif industry == "Agriculture":
    with col1:
        st.subheader("💡 Monthly electricity consumption (in kWh)")
        electricity = st.slider("Electricity", 0.0, 10000.0, key="electricity_input")

        st.subheader("🚜 Diesel consumption (in litres)")
        diesel = st.slider("Diesel", 0.0, 10000.0, key="diesel_input")

    with col2:
        st.subheader("🗑️ Waste generated per month (in kg)")
        waste = st.slider("Waste", 0.0, 2000.0, key="waste_input")

elif industry == "Transportation":
    with col1:
        st.subheader("🚛 Diesel consumption (in litres)")
        diesel = st.slider("Diesel", 0.0, 10000.0, key="diesel_input")

    with col2:
        st.subheader("🚗 Gasoline consumption (in litres)")
        gasoline = st.slider("Gasoline", 0.0, 10000.0, key="gasoline_input")

# Normalize inputs to yearly values
if 'electricity' in locals():
    electricity = electricity * 12  # Convert monthly to yearly
if 'gas' in locals():
    gas = gas * 12  # Convert monthly to yearly
if 'fuel_oil' in locals():
    fuel_oil = fuel_oil * 12  # Convert monthly to yearly
if 'waste' in locals():
    waste = waste * 12  # Convert monthly to yearly
if 'diesel' in locals():
    diesel = diesel * 12  # Convert monthly to yearly
if 'gasoline' in locals():
    gasoline = gasoline * 12  # Convert monthly to yearly

# Calculate carbon emissions for each input
electricity_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Electricity", 0) * electricity if 'electricity' in locals() else 0
gas_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Natural Gas", 0) * gas if 'gas' in locals() else 0
fuel_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Fuel Oil", 0) * fuel_oil if 'fuel_oil' in locals() else 0
waste_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Waste", 0) * waste if 'waste' in locals() else 0
diesel_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Diesel", 0) * diesel if 'diesel' in locals() else 0
gasoline_emissions = INDUSTRY_EMISSION_FACTORS[industry].get("Gasoline", 0) * gasoline if 'gasoline' in locals() else 0

# Convert emissions to tonnes and round off to 2 decimal points
electricity_emissions = round(electricity_emissions / 1000, 2)
gas_emissions = round(gas_emissions / 1000, 2)
fuel_emissions = round(fuel_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)
diesel_emissions = round(diesel_emissions / 1000, 2)
gasoline_emissions = round(gasoline_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    electricity_emissions + gas_emissions + fuel_emissions +
    waste_emissions + diesel_emissions + gasoline_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        if electricity_emissions > 0:
            st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        if gas_emissions > 0:
            st.info(f"🔥 Natural Gas: {gas_emissions} tonnes CO2 per year")
        if fuel_emissions > 0:
            st.info(f"🛢️ Fuel Oil: {fuel_emissions} tonnes CO2 per year")
        if waste_emissions > 0:
            st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        if diesel_emissions > 0:
            st.info(f"🚛 Diesel: {diesel_emissions} tonnes CO2 per year")
        if gasoline_emissions > 0:
            st.info(f"🚗 Gasoline: {gasoline_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
