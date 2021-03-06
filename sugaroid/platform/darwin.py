import logging
import os


class Darwin:
    def __init__(self):
        logging.error(
            "MacOS is untested. sugaroid is trying to use Linux config on Mac"
        )

    def cfgpath(self):
        return self.make_config()

    @staticmethod
    def make_config():
        if os.getenv("XDG_CONFIG_HOME") is None:
            path = os.path.expanduser("~/.config/sugaroid/")
        else:
            path = os.getenv("XDG_CONFIG_HOME").split(":")[0] + "/sugaroid"
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                logging.error(
                    "Error creating configuration file in dir {path}. Error code:{e}".format(
                        path=path, e=e
                    )
                )
        return path

    def system(self):
        return "Darwin"

    def increment(self):
        pass

    def paths(self):
        return ["bin", "/usr/bin", "~/.local/bin", "~/bin", "/usr/local/bin"]
