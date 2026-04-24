"""
===========================================================
COMPLETE REQUESTS + OS MASTER IMPLEMENTATION
Production-Style Data Engineering Code

Covers:
- API Client (GET, POST, headers, params)
- Retry mechanism
- Session handling (connection pooling)
- Pagination handling
- Rate limiting handling
- Streaming large files
- File uploads
- Error handling & logging
- Directory & file management (os)
- Environment variables
- File metadata
- Directory traversal
- Temporary files
===========================================================
"""

import os
import time
import json
import logging
import tempfile
import requests
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# =========================================================
# LOGGER SETUP
# =========================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# =========================================================
# FILE MANAGER (OS MODULE)
# =========================================================
class FileManager:
    def __init__(self, base_dir="data"):
        self.base_dir = base_dir
        self._ensure_dir(base_dir)

    def _ensure_dir(self, path):
        """Create directory if not exists"""
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Created directory: {path}")

    def get_partitioned_path(self):
        """Create partitioned path like data/year/month/day"""
        now = datetime.now()
        path = os.path.join(
            self.base_dir,
            str(now.year),
            str(now.month),
            str(now.day)
        )
        self._ensure_dir(path)
        return path

    def save_json(self, filename, data):
        """Save JSON data"""
        file_path = os.path.join(self.base_dir, filename)

        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

        logging.info(f"Saved JSON: {file_path}")

    def save_stream(self, filename, response):
        """Save large streaming response"""
        file_path = os.path.join(self.base_dir, filename)

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        logging.info(f"Saved stream file: {file_path}")

    def list_files(self):
        """List files"""
        return os.listdir(self.base_dir)

    def read_all_files(self):
        """Read all files recursively"""
        contents = []

        for root, _, files in os.walk(self.base_dir):
            for file in files:
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    contents.append(f.read())

        return contents

    def get_file_metadata(self, file_path):
        """Get file stats"""
        stat = os.stat(file_path)
        return {
            "size": stat.st_size,
            "modified": stat.st_mtime
        }


# =========================================================
# API CLIENT (REQUESTS MODULE)
# =========================================================
class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = self._create_session()

    def _create_session(self):
        """Create session with retry logic"""
        session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504]
        )

        adapter = HTTPAdapter(max_retries=retry)

        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _get_headers(self):
        """Prepare headers"""
        headers = {"Content-Type": "application/json"}

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        return headers

    def get(self, endpoint, params=None):
        """GET request with retry + timeout + error handling"""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.get(
                url,
                headers=self._get_headers(),
                params=params,
                timeout=5
            )

            if response.status_code == 429:
                logging.warning("Rate limited. Retrying...")
                time.sleep(2)
                return self.get(endpoint, params)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"GET Error: {e}")
            return None

    def post(self, endpoint, data):
        """POST request"""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.post(
                url,
                headers=self._get_headers(),
                json=data,
                timeout=5
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"POST Error: {e}")
            return None

    def fetch_all_pages(self, endpoint):
        """Pagination handling"""
        results = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            response = self.session.get(url, timeout=5)
            data = response.json()

            results.extend(data.get("data", []))
            url = data.get("next_page")

        return results

    def download_stream(self, endpoint, file_manager, filename):
        """Download large file"""
        url = f"{self.base_url}/{endpoint}"

        with self.session.get(url, stream=True) as response:
            response.raise_for_status()
            file_manager.save_stream(filename, response)

    def upload_file(self, endpoint, file_path):
        """Upload file"""
        url = f"{self.base_url}/{endpoint}"

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = self.session.post(url, files=files)

        return response.json()


# =========================================================
# TEMP FILE HANDLING
# =========================================================
def process_with_temp_file(data):
    """Example of temp file usage"""
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp:
        tmp.write(json.dumps(data))
        temp_path = tmp.name

    logging.info(f"Temp file created: {temp_path}")
    return temp_path


# =========================================================
# ENVIRONMENT VARIABLES
# =========================================================
def load_env():
    """Load environment configs"""
    return {
        "API_URL": os.environ.get("API_URL", "https://jsonplaceholder.typicode.com"),
        "API_KEY": os.environ.get("API_KEY", None)
    }


# =========================================================
# MAIN PIPELINE (REAL-WORLD FLOW)
# =========================================================
def run_pipeline():
    """
    FULL DATA PIPELINE:
    API → Fetch → Process → Store → Metadata
    """

    # Load configs
    config = load_env()

    # Initialize components
    client = APIClient(config["API_URL"], config["API_KEY"])
    file_manager = FileManager()

    # Step 1: Fetch data
    data = client.get("posts")

    if not data:
        logging.error("No data fetched")
        return

    # Step 2: Process data
    processed_data = [
        {
            "id": item["id"],
            "title": item["title"].upper(),
            "timestamp": datetime.now().isoformat()
        }
        for item in data
    ]

    # Step 3: Save data
    partition_path = file_manager.get_partitioned_path()
    file_path = os.path.join(partition_path, "data.json")

    with open(file_path, "w") as f:
        json.dump(processed_data, f, indent=2)

    logging.info(f"Data saved to: {file_path}")

    # Step 4: Metadata
    metadata = file_manager.get_file_metadata(file_path)
    logging.info(f"File metadata: {metadata}")

    # Step 5: Temp processing
    temp_file = process_with_temp_file(processed_data)

    # Step 6: List files
    files = file_manager.list_files()
    logging.info(f"Files in base dir: {files}")


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    run_pipeline()