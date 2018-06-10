# Contact: https://github.com/Unna000

import requests
import json


class HasteBinApi:

    def __init__(self, content):
        self.content = content

    def get_key(self):
        req = requests.post('https://hastebin.com/documents',
                            # headers={},
                            data=self.content)

        key = json.loads(req.content)
        return key['key']


# The method will return a key to access, example:
example = HasteBinApi('example 01')
KEY = example.get_key()
# With the key we can access, https://hastebin.com/KEY
