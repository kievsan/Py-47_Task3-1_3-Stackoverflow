

import requests

class StackOverflowApi():

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip'
        }

    def get_questions(self):
        api_address = 'https://api.stackexchange.com'
        api_service = '/2.3/questions/'
        api_tags = 'Python'
        url = api_address + api_service + api_tags
        headers = self.get_headers()
        params = {'fromdate': '1646179200', 'order': 'desc', 'sort': 'creation', 'site': 'stackoverflow'}
        response = requests.get(url=url, headers=headers, params=params)
        print(f'\n\t\t{response.status_code}')
        return response.json()

