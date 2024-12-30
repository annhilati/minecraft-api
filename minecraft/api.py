import requests
from .exceptions import MojangAPIError

class Endpoint():
    def __init__(self, url: str):
        self.url = url

    def fetch(self, **kwargs) -> requests.Response.json:
        """
        Fetches an API endpoint.

        #### Attributes:
            (Please take a look at the endpoint's docstring)

        #### Returns:
            (Please take a look at the endpoint's docstring)
        """

        response = requests.get(self.url.format(**kwargs))
        if response.status_code == 200:
            return response.json()
        else:
            raise MojangAPIError(msg=response.text, response=response)

class Endpoints():
    """
    Collection of API endpoints where to get data from. Each Endpoint object has an url attribute or can be fetched by using their fetch method.
    """
    MOJANG_PROFILE = Endpoint("https://api.mojang.com/users/profiles/minecraft/{playername}")
    """
        #### Requires:
            playername (str): The accounts current playername
        #### Contains:
            "id" (str): The accounts uuid without dashes
            "name" (str): The accounts current playername
    """

    SESSIONSERVER_PROFILE = Endpoint("https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
    """
        #### Requires:
            uuid (str): The accounts uuid without dashes
        #### Contains:
            "id" (str): The accounts uuid without dashes
            "name" (str): The accounts current playername
            "properties" (list): ...
                [0] (dict): ...
                    "name" (str): ...
                    "value" (str): base64
            "profileActions" (list): ...
    """
