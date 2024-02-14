import requests
import os
import json
import pathlib

from modules.directories import ProjectDirs

class Repository:
    def __init__(self):
        dirs = ProjectDirs()
        self.config = dirs.config_dir / "repository.json"
        
        if self.config.exists() is False:
            
        
        self.config_content = json.loads(self.config.read_text())
        
