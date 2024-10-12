# Industrial Carbon Calculator for Kenya

## Overview

The **Industrial Carbon Calculator** is a Streamlit application designed to help industries in Kenya calculate their carbon emissions based on energy consumption and waste generation. It serves industries in the **Manufacturing**, **Agriculture**, and **Transportation** sectors, providing a simple way to understand their carbon footprint.

## Features

- **User-Friendly Interface**: Intuitive design that guides users through inputting their data.
- **Custom Emission Factors**: Utilizes specific emission factors based on industry standards.
- **Annual Emission Calculation**: Converts monthly consumption inputs into annual carbon emissions.
- **Detailed Results**: Provides an emissions breakdown and displays the total carbon footprint in tonnes of CO₂.

## Technologies Used

- **Streamlit**: Web framework for creating interactive apps.
- **Python**: The main programming language for logic and calculations.

## Installation

### Setting Up a Virtual Environment

1. Navigate to your project directory:
   
```bash
cd your_project_directory
```

2. Create a virtual environment (using `venv`):
   
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows**:
   
   ```bash
   venv\Scripts\activate
   ```
   - **MacOS/Linux**:
   
   ```bash
   source venv/bin/activate
   ```

### Installing Dependencies

1. Install the required libraries via `requirements.txt`. Here's how to do that:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```plaintext
streamlit==1.25.0  # Replace with the latest version if necessary
numpy==1.21.2      # Required for numerical calculations (if applicable)
pandas==1.3.3      # Required for data handling (if applicable)
```

### Run the Application

To run the application, use the command below:

```bash
streamlit run your_script_name.py
```

## How to Use

1. **Select Your Industry**: Choose Manufacturing, Agriculture, or Transportation.
2. **Input Data**: Use the sliders to enter monthly energy consumption and waste generation data.
   - **Manufacturing**: Enter values for electricity, natural gas, fuel oil, and waste.
   - **Agriculture**: Enter values for electricity, diesel, and waste.
   - **Transportation**: Enter values for diesel and gasoline.
3. **Calculate Emissions**: Click "Calculate CO₂ Emissions" to see the emissions breakdown and total carbon footprint.
