import requests
import os
import json
import pathlib

from modules.directories import ProjectDirs

class Repository:
    def __init__(self):
        dirs = ProjectDirs()
        self.config: pathlib.Path = dirs.config_dir / "repository.json"
        
        if self.config.exists() is False:
            content = requests.get("https://github.com/XtrrmeTHN/XtremePKG/src/repository.json").content

            self.config.write_bytes(content)
        
        self.config_content = json.loads(self.config.read_text())

    def generate_repo(self):
        repo_url = "https://api.github.com/users/XtremeTHN/repos"


    def get_pkg(self, name):
        ...
        
    def install_pkg(self, repo_name: str):
        ...
