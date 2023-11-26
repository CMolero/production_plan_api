# Power Plant Production Planning

This project calculates the production plan for a set of power plants based on the given load and fuel costs.

## Requirements

- Python 3.8 or higher
- Flask

## Installation

1. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   `bash
 .\venv\Scripts\activate
 `
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app/main.py
   ```

2. Access the production plan endpoint:
   - [http://localhost:8080/productionplan](http://localhost:8080/productionplan)

## API Endpoint

- **Endpoint:** `/productionplan`
- **Method:** POST
- **Request Payload:** JSON with the structure specified in example_payloads directory.
- **Response:** JSON with the structure specified in example_payloads directory.

## Additional Notes

- The power produced by each power plant is a multiple of 0.1 MW.
