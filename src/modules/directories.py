import os, sys, logging

class ProjectDirs:
    def __mkdirs(self):
        os.makedirs(self.share_dir, exist_ok=True)
        os.makedirs(self.config_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
    def __init__(self, name):
        logger = logging.getLogger("ProjectDirs()")
        if sys.platform == "win32":
            self.home = os.getenv("USERPROFILE")
            self.appdata = os.getenv("APPDATA")
            self.local = os.getenv("LOCALAPPDATA")

            self.share_dir = os.path.join(self.local, name)
            self.log_dir = os.path.join(self.share_dir, "logs")
            self.config_dir = os.path.join(self.appdata, name, "config")

        elif sys.platform == "linux":
            self.home = os.getenv("HOME")
            self.share_dir = os.path.join(self.home, ".local", "share", name)
            self.log_dir = os.path.join(self.share_dir, "logs")
            self.config_dir = os.path.join(self.home, ".config", name)

        elif sys.platform == "darwin":
            logger.error("MacOS is not implemented yet")
        
        self.__mkdirs()
