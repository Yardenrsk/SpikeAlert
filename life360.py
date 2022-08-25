import requests
import json


class life360:
    base_url = "https://api.life360.com/v3/"
    circles_url = "circles.json"
    circle_url = "circles/"

    def __init__(self, authorization_token=None):
        self.authorization_token = authorization_token

    def make_request(self, url, params=None, method='GET', authheader=None):
        headers = {'Accept': 'application/json'}
        if authheader:
            headers.update({'Authorization': authheader, 'cache-control': "no-cache", })

        if method == 'GET':
            r = requests.get(url, headers=headers)
        elif method == 'POST':
            r = requests.post(url, data=params, headers=headers)

        return r.json()

    def get_circles(self):
        url = self.base_url + self.circles_url
        authheader = "bearer " + self.authorization_token
        r = self.make_request(url=url, method='GET', authheader=authheader)
        return r['circles']

    def get_circle(self, circle_id):
        url = self.base_url + self.circle_url + circle_id
        authheader = "bearer " + self.authorization_token
        r = self.make_request(url=url, method='GET', authheader=authheader)
        return r