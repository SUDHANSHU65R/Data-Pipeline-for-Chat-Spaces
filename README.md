# Google Chat Exporter

A Python script to export chat messages from Google Chat and update a Google Sheet and Snowflake database.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to extract chat messages from Google Chat spaces, format the data, and update a Google Sheet with the extracted messages. Additionally, it creates a table in Snowflake database for further analysis.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/google-chat-exporter.git
    cd google-chat-exporter
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the necessary Google API credentials and Snowflake connection credentials set up.

## Usage

1. Update the `Google_auth.py` file with your Google API credentials.

2. Set up your Snowflake connection credentials in the `connection_fn.py` file.

3. Replace the placeholder sheet ID (`insert sheet ID`) in the `main.py` file with your actual Google Sheet ID.

4. Run the script:

    ```bash
    python main.py
    ```

5. Check the specified Google Sheet and Snowflake database for the exported chat messages.

## Dependencies

- `os`: For interacting with the operating system.
- `logging`: For logging messages during script execution.
- `pandas`: For data manipulation and DataFrame operations.
- `pygsheets`: For interacting with Google Sheets.
- `Google_auth`: Your Google API credentials.
- `googleapiclient`: For making requests to Google APIs.
- `datetime`, `timedelta`, `pytz`: For date and time operations.
- `connection_fn`: Contains functions for connecting to Snowflake.
- `snowflake.connector.pandas_tools`: For writing Pandas DataFrames to Snowflake.
- `numpy`: For numerical operations (required by pandas).
- `sys`: For system-specific parameters and functions.

## Benefits

- Streamlines the process of collecting and analyzing data from Google Chat spaces.
- Provides insights and patterns for informed decision-making.
- Facilitates collaboration and efficiency in data management and analysis processes.
- Ensures up-to-date data analysis through integration with a scheduling system.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to propose changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
