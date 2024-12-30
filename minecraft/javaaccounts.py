from .api import Endpoints
import base64
import json

class JavaAccount():

    def __init__(self, identifier: str):
        """
        Class-Object for fetching information about an Minecraft Java Edition account

        #### Arguments:
            identifier (str): The accounts UUID or current playername

        #### Attributes:
            uuid (str): The accounts Unique Universal Identifier
            _uuid (str): The accounts Unique Universal Identifier without dashes
        
        #### Methods:
            skinmodel: Returns whether the model of the accounts current skin is normal or slim
            skinurl: Returns the URL to the accounts current skin
            playername: Returns the accounts current playername
        """
            
        if len(identifier) not in [32, 36]:
            playername = identifier
            self._uuid = Endpoints.MOJANG_PROFILE.fetch(playername=playername)["id"]
        else:
            self._uuid = identifier.replace("-", "")

        self.uuid = f"{self._uuid[:8]}-{self._uuid[8:12]}-{self._uuid[12:16]}-{self._uuid[16:20]}-{self._uuid[20:]}"

    def skinmodel(self) -> str:
        "Returns whether the model of the accounts current skin is `\"normal\"` or `\"slim`\""
        texturesBase64 = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=self._uuid)["properties"][0]["value"]

        texturesStr = base64.b64decode(texturesBase64.strip()).decode("utf-8")

        textures = json.loads(texturesStr)

        try:
            return textures["textures"]["SKIN"]["metadata"]["model"]
        except KeyError:
            return "normal"

    def skinurl(self) -> str:
        "Returns the URL to the accounts current skin"
        texturesBase64 = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=self._uuid)["properties"][0]["value"]

        texturesStr = base64.b64decode(texturesBase64.strip()).decode("utf-8")

        textures = json.loads(texturesStr)

        return textures["textures"]["SKIN"]["url"]
    
    def playername(self):
        "Returns the accounts current playername"
        playername = Endpoints.SESSIONSERVER_PROFILE.fetch(uuid=self._uuid)["name"]
        return playername

    