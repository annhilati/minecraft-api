from .api import Endpoints

class JavaAccount():

    def __init__(self, identifier: str):
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
            
        if len(identifier) not in [32, 36]:
            playername = identifier
            uuid = Endpoints.MOJANG_PROFILE.fetch(playername=playername)["id"]
        else:
            uuid = identifier.replace("-", "")

        self.update() # Lädt somit alle anderen Eigenschaften initial

        self.uuid = uuid
        self.playername = playername

    def update(self) -> None:
        "Updates all attributes of the JavaAccount object that may change over time"
        self.playername = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=self.uuid)["id"]