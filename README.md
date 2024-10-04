# Industrial Carbon Calculator for Kenya

## Overview

The Industrial Carbon Calculator is a Streamlit application designed to help industries in Kenya calculate their carbon emissions based on their energy consumption and waste generation. This tool is tailored for the manufacturing, agriculture, and transportation sectors, providing a straightforward way to understand their carbon footprint.

## Features

User-Friendly Interface: Simple and intuitive design that guides users through inputting their data.

Custom Emission Factors: Utilizes specific emission factors for various energy sources and waste types based on industry standards.

Annual Emission Calculation: Converts monthly consumption inputs into annual carbon emissions.

Detailed Results: Provides emissions breakdown by category and displays total carbon footprint in tonnes of CO2.

## Technologies Used

Streamlit: A fast way to build and share beautiful machine learning and data science web apps.

Python: The primary programming language for the application.

## Installation

Clone the repository or download the code files.

Install the required libraries:

bash

Copy code

pip install streamlit

## Run the application:

bash

Copy code

streamlit run your_script_name.py

## How to Use

Select Your Industry: Choose between Manufacturing, Agriculture, or Transportation.

Input Data: Use the sliders to enter your monthly energy consumption and waste generation for the selected industry.

For Manufacturing: Input values for electricity, natural gas, fuel oil, and waste.

For Agriculture: Input values for electricity, diesel, and waste.

For Transportation: Input values for diesel and gasoline.

Calculate Emissions: Click the "Calculate CO2 Emissions" button to see your carbon emissions by category and total footprint.
Emission Factors

## The application uses the following emission factors (in kgCO2) per unit:

### Manufacturing:

Electricity: 0.14 kgCO2/kWh

Natural Gas: 0.185 kgCO2/m³

Fuel Oil: 0.33 kgCO2/litre

Waste: 0.05 kgCO2/kg

### Agriculture:

Diesel: 2.68 kgCO2/litre

Electricity: 0.14 kgCO2/kWh

Waste: 0.05 kgCO2/kg

### Transportation:

Diesel: 2.68 kgCO2/litre

Gasoline: 2.31 kgCO2/litre
