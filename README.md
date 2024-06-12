# Automation-Test-Framework-UI

## Overview
This repository contains a Python-based automation testing framework designed to simplify the execution of test scripts for non-technical users. Utilizing `pytest` for testing, `Selenium` for browser automation, and `Flask` for the backend, this framework provides an intuitive HTML/CSS user interface to run tests and view results through Allure reports.

## Features
- **User-Friendly Interface**: Execute test scripts via a simple HTML/CSS UI.
- **Automation with Selenium**: Browser automation for comprehensive end-to-end testing.
- **Pytest Integration**: Robust testing framework with extensive plugin support.
- **Flask Backend**: Lightweight and flexible backend server.
- **Shell Scripting**: Automate test runs and specific commands.
- **Allure Reporting**: Visualize test results with interactive Allure reports.

## Prerequisites
- Python 3.x
- `pip` (Python package installer)
- `virtualenv` (Recommended for creating an isolated Python environment)
- Node.js and npm (for serving static files, if needed)

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Prasad9246/Automation-Test-Framework-UI.git
    cd Automation-Test-Framework-UI
    ```

2. **Create a Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Install Allure Commandline**:
    Follow the installation guide from [Allure Documentation](https://docs.qameta.io/allure/).

## Usage

1. **Start the Flask Server**:
    ```sh
    python app.py
    ```

2. **Open the UI**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

3. **Run Tests**:
    Use the UI to select and run test scripts.

4. **View Allure Reports**:
    After the tests complete, access the Allure report link provided in the UI.

## Directory Structure
