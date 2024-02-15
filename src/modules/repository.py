import requests
import os
import json
import pathlib

from modules.directories import ProjectDirs

class Repository:
    def __init__(self):
        dirs = ProjectDirs("com.github.XtremeTHN.XtremePKG")
        self.config: pathlib.Path = pathlib.Path(dirs.config_dir) / "repository.json"
        
        if self.config.exists() is False:
            self.generate_repo()
        
        self.config_content: list[dict] = json.loads(self.config.read_text())

    def generate_repo(self):
        repo_url = "https://api.github.com/users/XtremeTHN/repos"

        content: list[dict] = json.loads(requests.get(repo_url).content)

        repository_content: list[dict] = []
        for x in content:
            repository_content.append({
                "name": x.get("name"),
                "description": x.get("description"),
                "url": x.get("html_url"),
            })

        with self.config.open("w") as f:
            json.dump(repository_content, f, indent=4)

    def get_pkg(self, name):
        return list(filter(lambda x: x.get("name") == name, self.config_content))[0]
        
    def install_pkg(self, repo_name: str):
        ...
