"""app_yourname.py - Project script.

Author: Your Name or Alias
Date: 2026-01

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.

TODO: Change the Author line of the docstring above to your name or alias.

TODO: RENAME this file from app_yourname.py to something
      that includes your name or alias, e.g., app_stellar_analytics.py.

TODO: Update the opening line of the docstring above to match the new file name.

TODO: Update the associated `uv run python` command in the README.md file.

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")


# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.
# Examples:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150

# See the other file for examples.
# TODO: Declare and initialize a string (str) variable of your choice below:


# TODO: Declare and initialize an integer (int) variable of your choice below:


# TODO: Declare and initialize a float (float) variable of your choice below:


# TODO: Declare and initialize a boolean (bool) variable of your choice (True or False) below:


# TODO: Declare and initialize a list of strings (list[str]) variable of your choice below:
# REQ: Strings must be in quotes and items are separated by commas,
# REQ: The list is wrapped in square brackets. (See the other file for examples.)


# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    # TODO: Create and return a multi-line f-string (triple-quoted) that includes
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    # See the other file for an example. Remember to start the string with an f!
    summary: str = f"""
    Custom Information:
        Company name: {MY_ANALYTICS_COMPANY}
        Employee count: {MY_EMPLOYEE_COUNT}
        TODO: Add your other global variables below:





    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    # REQ: Vary ONE of the sample data values.
    # See how the statistics change when you do.
    # TODO: Change one of the values in the list below.
    snowfall_inches: list[float] = [2.5, 3.5, 4.5, 5.5, 6.5]

    # Calculate descriptive statistics below - see other file for examples.

    # Example: Calculate total snowfall.
    total: float = sum(snowfall_inches)

    # Example : Calculate count of measurements.
    count: int = len(snowfall_inches)

    # TODO: Calculate minimum and maximum snowfall (see other file for examples).

    # Use the statistics module to calculate average.
    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0

    # TODO: Use the statistics module to calculate standard deviation below:

    # Build a formatted multi-line string using f and triple quotes.
    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        TODO: Add your count of measurements below:

        TODO: Add your minimum and maximum snowfall below:

        Average snowfall: {average:.2f} inches
        TODO: Add your standard deviation below:

    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    # Log a header for the application.
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    # Log start of main processing.
    LOG.info("START main()..................")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    # Log end of main processing.
    LOG.info("END main()..................")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.

if __name__ == "__main__":
    main()
