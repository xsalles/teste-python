import logging
import json
import requests
import os
import time
from dotenv import load_dotenv
from helpers.get_device_info import get_device_info

# Load environment variables from .env file
load_dotenv()

# Setup logging to work with Android
try:
    # For Android
    from android.storage import app_storage_path
    log_dir = app_storage_path()
    log_file = os.path.join(log_dir, "device_collector.log")
except ImportError:
    # Fallback for non-Android
    log_file = "device_collector.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file
)

logger = logging.getLogger(__name__)

def collect_and_send_data(server_url=None, max_retries=3):
    if not server_url:
        # Try to get URL from environment variable
        server_url = os.environ.get("SERVER_URL")
        
        # Fallback to hardcoded URL if environment variable not set
        if not server_url:
            logger.info("Using default server URL (no SERVER_URL in .env)")
    
    logger.info(f"Using server URL: {server_url}")
    
    # Collect the device information
    data = get_device_info()
    logger.info(f"Collected data for device: {data.get('model', 'unknown')}")
    
    # Send to server with retries
    for attempt in range(max_retries):
        try:
            logger.info(f"Sending data to {server_url} (attempt {attempt+1}/{max_retries})")
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                server_url,
                data=json.dumps(data),
                headers=headers,
                timeout=30  # 30 second timeout
            )
            
            if response.status_code == 201:
                logger.info("Data sent successfully")
                return True
            else:
                logger.warning(f"Server returned status code: {response.status_code}")
                logger.warning(f"Response: {response.text}")
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
        
        # Wait before retry (exponential backoff)
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt
            logger.info(f"Waiting {wait_time} seconds before retry")
            time.sleep(wait_time)
    
    logger.error("Failed to send data after all retry attempts")
    return False