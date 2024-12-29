class MinecraftAPIException(Exception):
    "Base class for exceptions in minecraft-api"

    def __init__(self, msg: str):
        "Base class for exceptions in minecraft-api"
        self.message = msg

    def __str__(self):
        return self.message

class MojangAPIError(MinecraftAPIException):
    def __init__(self, msg, response: None):
        super().__init__(msg)
        self.response = response