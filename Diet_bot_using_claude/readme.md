# Glucose Control bot using Claude

**Glucose guide** is a personalized meal planning tool designed specifically for diabetic patients. By entering your sugar levels and dietary preferences, GlucoGuide generates meal plans that are tailored to help you manage your blood sugar levels effectively.

## Features

- **Personalized Meal Plans**: Generate meal plans based on your fasting, pre-meal, and post-meal sugar levels, as well as your dietary preferences.
- **Streamlit Interface**: User-friendly interface to input your details and get personalized meal plans.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/HaroonTaufiq/Streamlit-Projects
    cd Diet_bot_using_claude
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install streamlit anthropic
    ```

4. **Set up your Anthropic API key**:
    - Obtain your Anthropic API key.
    - Set the `ANTHROPIC_API_KEY` environment variable:
    ```sh
    export ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

## Usage

1. **Activate the virtual environment**:
    ```sh
    source venv/bin/activate
    ```

2. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

3. **Open your web browser** and navigate to `http://localhost:8501` to access the application.

## How to Use

1. **Enter your sugar levels** in the sidebar:
    - Fasting Sugar Levels (mg/dL)
    - Pre-Meal Sugar Levels (mg/dL)
    - Post-Meal Sugar Levels (mg/dL)

2. **Enter your dietary preferences** (e.g., vegetarian, low-carb) in the sidebar.

3. **Click the "Generate Meal Plan" button** to get a personalized meal plan.

4. **View the generated meal plan** displayed in the main area of the application.

## Dependencies

- `streamlit`
- `anthropic`
