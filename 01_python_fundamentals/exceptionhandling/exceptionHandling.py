"""
COMPLETE EXCEPTION HANDLING MASTER FILE
Production-style implementation for Data Engineering

Covers:
- try/except/else/finally
- custom exceptions
- exception chaining
- logging
- file handling
- API handling
- retry mechanisms
- generators
- async handling
- threading
- context managers
- suppression
"""

import logging
import json
import time
import requests
import threading
import asyncio
from contextlib import suppress

# ==========================================
# LOGGING CONFIG (PRODUCTION STYLE)
# ==========================================

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==========================================
# CUSTOM EXCEPTION HIERARCHY
# ==========================================

class PipelineError(Exception):
    """Base class for pipeline errors"""
    pass

class DataValidationError(PipelineError):
    pass

class APIError(PipelineError):
    pass

class FileProcessingError(PipelineError):
    pass

# ==========================================
# BASIC EXCEPTION HANDLING
# ==========================================

def basic_example():
    try:
        x = int("abc")
    except ValueError as e:
        logging.error("Conversion failed", exc_info=True)
    else:
        logging.info(f"Conversion success: {x}")
    finally:
        logging.info("Basic example executed")

# ==========================================
# EXCEPTION CHAINING
# ==========================================

def exception_chaining():
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Higher-level failure") from e

# ==========================================
# DATA VALIDATION FUNCTION
# ==========================================

def validate_record(record):
    if "id" not in record:
        raise DataValidationError("Missing ID")
    if not isinstance(record.get("value"), int):
        raise DataValidationError("Value must be integer")

# ==========================================
# RETRY MECHANISM (EXPONENTIAL BACKOFF)
# ==========================================

def retry(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logging.warning(f"Retry {i+1} failed: {e}")
            time.sleep(2 ** i)
    raise APIError("Max retries exceeded")

# ==========================================
# API HANDLING
# ==========================================

def fetch_api():
    def call():
        response = requests.get("https://api.example.com/data", timeout=5)
        response.raise_for_status()
        return response.json()
    
    try:
        return retry(call)
    except Exception as e:
        logging.error("API failed", exc_info=True)
        return None

# ==========================================
# FILE PROCESSING
# ==========================================

def process_file(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error("File not found")
        return []
    except json.JSONDecodeError:
        logging.error("Invalid JSON")
        return []

    valid_data = []

    for record in data:
        try:
            validate_record(record)
            valid_data.append(record)
        except DataValidationError as e:
            logging.warning(f"Skipping bad record: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    return valid_data

# ==========================================
# GENERATOR WITH EXCEPTION HANDLING
# ==========================================

def data_generator(data):
    for item in data:
        try:
            if item < 0:
                raise ValueError("Negative value")
            yield item
        except Exception as e:
            logging.warning(f"Generator skipped: {e}")

# ==========================================
# CUSTOM CONTEXT MANAGER
# ==========================================

class ResourceManager:
    def __enter__(self):
        logging.info("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            logging.error(f"Exception in context: {exc_value}")
        logging.info("Resource closed")

# ==========================================
# SUPPRESSING EXCEPTIONS
# ==========================================

def suppress_example():
    with suppress(FileNotFoundError):
        open("missing.txt")

# ==========================================
# THREADING EXCEPTION HANDLING
# ==========================================

def thread_task():
    try:
        raise Exception("Thread error")
    except Exception as e:
        logging.error(f"Thread failed: {e}")

def run_thread():
    t = threading.Thread(target=thread_task)
    t.start()
    t.join()

# ==========================================
# ASYNC EXCEPTION HANDLING
# ==========================================

async def async_task():
    raise Exception("Async error")

async def async_main():
    try:
        await async_task()
    except Exception as e:
        logging.error(f"Async error: {e}")

# ==========================================
# MAIN PIPELINE
# ==========================================

def main_pipeline():
    logging.info("Pipeline started")

    # Basic example
    basic_example()

    # API call
    api_data = fetch_api()

    # File processing
    processed_data = process_file("data.json")

    # Generator processing
    for val in data_generator([1, 2, -1, 3]):
        logging.info(f"Processed value: {val}")

    # Context manager usage
    try:
        with ResourceManager():
            logging.info("Inside resource block")
    except Exception:
        pass

    # Suppress example
    suppress_example()

    # Thread execution
    run_thread()

    # Async execution
    asyncio.run(async_main())

    logging.info("Pipeline completed")

# ==========================================
# ENTRY POINT WITH FAIL-SAFE
# ==========================================

if __name__ == "__main__":
    try:
        main_pipeline()
    except PipelineError as e:
        logging.critical(f"Pipeline error: {e}", exc_info=True)
    except Exception as e:
        logging.critical(f"Unexpected crash: {e}", exc_info=True)