import re
import logging
import requests
import os
from django.core.files.storage import Storage
from myapp.onedrive_auth import get_access_token  # Import the get_access_token function

logger = logging.getLogger(__name__)


class OneDriveStorage(Storage):
    # Use the shared folder ID in the BASE_URL
    BASE_URL = "https://graph.microsoft.com/v1.0/sites/negativezero-my.sharepoint.com:/personal/sohit_negativezero_onmicrosoft_com:/drives/{drive_id}/root:/"

    def sanitize_file_path(self, file_path):
        return re.sub(r'[<>:"/\\|?*]', "_", file_path)

    def generate_filename(self, name):
        return os.path.basename(name)

    def save(self, name, content, max_length=None):
        access_token = get_access_token()
        name = self.sanitize_file_path(name)
        headers = {"Authorization": f"Bearer {access_token}"}

        # Construct the URL for uploading to the specific folder
        upload_url = f"{self.BASE_URL}{name}:/content"

        response = requests.put(upload_url, headers=headers, data=content)

        if response.status_code == 201:
            return response.json()  # File uploaded successfully
        elif response.status_code == 401:
            raise Exception(
                "Unauthorized: Check if the access token is valid or expired."
            )
        elif response.status_code == 403:
            raise Exception("Forbidden: Ensure your app has the right permissions.")
        else:
            logger.error(
                f"Failed to upload file: {response.status_code} - {response.json()}"
            )
            raise Exception(f"Failed to upload file: {response.json()}")

    def url(self, name):
        access_token = get_access_token()
        name = self.sanitize_file_path(name)
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{self.BASE_URL}{name}", headers=headers)

        if response.status_code == 200:
            return response.json().get("@microsoft.graph.downloadUrl")
        elif response.status_code == 401:
            raise Exception(
                "Unauthorized: Check if the access token is valid or expired."
            )
        elif response.status_code == 403:
            raise Exception("Forbidden: Ensure your app has the right permissions.")
        else:
            logger.error(
                f"Failed to get file URL: {response.status_code} - {response.json()}"
            )
            raise Exception(f"Failed to get file URL: {response.json()}")
