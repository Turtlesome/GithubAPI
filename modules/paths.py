import json
from pathlib import Path
from datetime import datetime


def open_config():
    """
    Reads a YAML configuration file and returns its contents.

    Returns:
        - dict: The contents of the YAML configuration file.
    """

    app_dir = Path(__file__).parent.parent
    json_file = app_dir / "config.json"

    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def create_logger():
    """
    Creates a logger with the specified path and name and returns it.
    
    Returns:
    - str: The path for newly created logger.
    """
    
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    filename = Path(__file__).parent.parent / "logs" / f"logger_{timestamp}.log"

    return str(filename)