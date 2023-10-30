Description

This script provides a simple graphical user interface (GUI) to view data from a CSV file. The data is displayed in a table format, similar to Excel, with alternating row colors for better readability. The script will automatically refresh and display the latest data from the CSV file every 1/10th of a second.
Requirements

    Python 3.x
    pandas (pip install pandas)
    tkinter (usually comes bundled with Python)

Usage

    Ensure you have Python installed and that the required packages (pandas and tkinter) are available.
    Place the script in the same directory as the CSV file named gh.csv.
    Run the script using Python: python path_to_script.py.

Alternatively, you can use the provided .bat file (if available) to execute the script. Simply double-click on the .bat file.
Features

    Auto-refreshes data every 1/10th of a second.
    Displays data in a table format with gridlines.
    Alternating row colors for better readability.
    Vertical scrollbar to navigate through the data.

Customization

To use a different CSV file or adjust other settings, modify the script directly. Look for the line app = CSVViewer("gh.csv") and change "gh.csv" to the desired filename or path.
