import json
import requests


class Util:

    API_KEY='7521C64AE5AE8287D7028ED792721C1B'

    @classmethod
    def get_data(cls, param_string):
        url = 'http://api.eia.gov/series/?api_key=' + cls.API_KEY + '&' + param_string
        data = json.loads(requests.get(url).content)
        return data
