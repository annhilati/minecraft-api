from .api import Endpoints

class JavaAccount():
    """
    Class-Object for fecthing information about an Minecraft Java Edition account

    #### Arguments:
        identifier (str): The accounts UUID or current playername

    #### Attributes:
        uuid (str): The accounts Unique Universal Identifier
        playername(str): The accounts current playername
    
    #### Methods:
        update: Updates all attributes of the JavaAccount object that may change over time
    """

    def __init__(self, identifier: str):
        if len(identifier) in [32, 36]:
            uuid = identifier.replace("-", "")
            playername = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=uuid)["name"]
        else:
            playername = identifier
            uuid = Endpoints.MOJANG_PROFILE.fetch(playername=playername)["id"]

        self.uuid = uuid
        self.playername = playername

    def update(self) -> None:
        "Updates all attributes of the JavaAccount object that may change over time"
        self.playername = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=self.uuid)["id"]