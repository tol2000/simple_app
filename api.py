class Api:

    api_key = None

    def __init__(self, api_key):
        self.api_key = api_key

    def hello(self):
        print('Hello!')
        print(f'api key: {self.api_key}')
