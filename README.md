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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to propose changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.











































# Data Pipeline for Google Chat Spaces

**Project Duration:** July 2022 to Present (Full Time)

## Description

Developed a Python-based data pipeline to extract data from chat spaces, including messages, attachments, member details, etc., The data pipeline aims to streamline the process of collecting and analyzing data from Google Chat spaces to derive insights and patterns for informed decision-making.

## Key Features

- Developed a Python tool to extract data from chat spaces and store it in Google Sheets and Snowflake DB for future analysis.
- Analyzed the collected data using Python and relevant libraries to derive insights and patterns.
- Created a dynamic dashboard to visualize key metrics and insights for informed decision-making.
- Integrated the data pipeline with a scheduling system to run it on a regular basis, ensuring up-to-date data analysis.
- Worked collaboratively with the team to ensure efficient data management and analysis processes.
- Utilized Python, Pygsheets, Sheets API, Chat API, People API, and SQL for seamless data management and analysis.

## Technologies Used

- Python
- Pygsheets
- Google Sheets API
- Google Chat API
- Google People API
- Snowflake DB
- SQL

## How It Works

1. The Python tool extracts data from chat spaces, including messages, attachments, and member details, using the Google Chat API and People API.
2. The extracted data is stored in Google Sheets and Snowflake DB for future analysis.
3. Python scripts analyze the collected data to derive insights and patterns using relevant libraries.
4. A dynamic dashboard is created using Python visualization libraries to visualize key metrics and insights for informed decision-making.
5. The data pipeline is integrated with a scheduling system to run it on a regular basis, ensuring up-to-date data analysis.

## Benefits

- Streamlines the process of collecting and analyzing data from Google Chat spaces.
- Provides insights and patterns for informed decision-making.
- Facilitates collaboration and efficiency in data management and analysis processes.
- Ensures up-to-date data analysis through integration with a scheduling system.

## Usage

The data pipeline is used to extract data from Google Chat spaces, store it in Google Sheets and Snowflake DB, analyze the collected data, and visualize key metrics and insights using the dynamic dashboard.

## Contributions

Contributions to the data pipeline project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support related to the data pipeline project, please contact [Sudhanshu Kumar](mailto:Sudhansu65r@gmail.com).
