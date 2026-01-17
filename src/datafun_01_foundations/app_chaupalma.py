"""app_chaupalma.py - Project script.

Author: Chau Palma
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

: Change the Author line of the docstring above to your name or alias.

: RENAME this file from app_yourname.py to something
      that includes your name or alias, e.g., app_stellar_analytics.py.

: Update the opening line of the docstring above to match the new file name.

: Update the associated `uv run python` command in the README.md file.

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
# : Declare and initialize a string (str) variable of your choice below:

Confidence: Final[str] = "My confidence level is low but improving learning python."

# : Declare and initialize an integer (int) variable of your choice below:

MY_ANXIETY_LEVEL: Final[int] = 8

# : Declare and initialize a float (float) variable of your choice below:

PERCENTAGE_I_PASS_MY_MASTERS: Final[float] = 99.9

# : Declare and initialize a boolean (bool) variable of your choice (True or False) below:

WILL_I_PASS_MY_MASTERS: Final[bool] = True

# : Declare and initialize a list of strings (list[str]) variable of your choice below:
# REQ: Strings must be in quotes and items are separated by commas,
# REQ: The list is wrapped in square brackets. (See the other file for examples.)

MY_FAVORITE_THINGS_TO_DO: Final[list[str]] = [
    "Eating",
    "Traveling",
    "Shopping",
    "Sleeping",
]
# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    # : Create and return a multi-line f-string (triple-quoted) that includes
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    # See the other file for an example. Remember to start the string with an f!
    summary: str = f"""
    Custom Information:
        Company name: {MY_ANALYTICS_COMPANY}
        Employee count: {MY_EMPLOYEE_COUNT}
        Confidence: {Confidence}
        Anxiety level: {MY_ANXIETY_LEVEL}
        Percentage I pass my masters: {PERCENTAGE_I_PASS_MY_MASTERS}%
        Will I pass my masters: {WILL_I_PASS_MY_MASTERS}
        My favorite things to do: {', '.join(MY_FAVORITE_THINGS_TO_DO)}


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
    # : Change one of the values in the list below.
    snowfall_inches: list[float] = [2.2, 3.5, 4.5, 5.5, 6.5]

    # Calculate descriptive statistics below - see other file for examples.

    # Example: Calculate total snowfall.
    total: float = sum(snowfall_inches)

    # Example : Calculate count of measurements.
    count: int = len(snowfall_inches)

    # : Calculate minimum and maximum snowfall (see other file for examples).

    min_snowfall: float = min(snowfall_inches) if count > 0 else 0.0
    max_snowfall: float = max(snowfall_inches) if count > 0 else 0.0

    # Use the statistics module to calculate average.
    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0

    # : Use the statistics module to calculate standard deviation below:

    stdev: float = statistics.stdev(snowfall_inches) if count > 1 else 0.0

    # Build a formatted multi-line string using f and triple quotes.
    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches

        Count of measurements: {count}

        minimum snowfall: {min_snowfall:.2f} inches
        maximum snowfall: {max_snowfall:.2f} inches

        Average snowfall: {average:.2f} inches

        Standard deviation: {stdev:.2f} inches

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
