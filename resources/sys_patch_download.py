# Download PatcherSupportPkg for usage with Root Patching
# Copyright (C) 2020-2022, Dhinak G, Mykola Grymalyuk

from data import os_data
from resources import utilities
from pathlib import Path
import shutil

class grab_patcher_support_pkg:

    def __init__(self, constants):
        self.constants = constants
    
    def generate_pkg_link(self):
        link = f"{self.constants.url_patcher_support_pkg}{self.constants.patcher_support_pkg_version}/Universal-Binaries.zip"
        return link

    def download_files(self):
        link = self.generate_pkg_link()
        if Path(self.constants.payload_local_binaries_root_path).exists():
            print("- Removing old Apple Binaries folder")
            # Delete folder
            shutil.rmtree(self.constants.payload_local_binaries_root_path)

        download_result = None
        local_zip = Path(self.constants.payload_path) / f"Universal-Binaries.zip"
        if Path(local_zip).exists():
            print(f"- Found local {local_zip} zip, skipping download")
            download_result = True
        else:
            print(f"- No local version found, downloading...")
            download_result = utilities.download_file(link, self.constants.payload_local_binaries_root_path_zip)

        return download_result, link