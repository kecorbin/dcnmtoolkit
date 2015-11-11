import requests
import json
import logging

logging.getLogger(__name__)
class Session(object):

    def __init__(self, url, user, passwd):
        self.base_url = url + '/rest'
        self.user = user
        self.passwd = passwd
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.token = None
        self.expiration_time = 1000000

    def login(self):
        url = self.base_url + '/logon'
        payload = {'expirationTime': self.expiration_time}
        resp = requests.post(url, auth=(self.user, self.passwd), data=json.dumps(payload))
        self.headers.update(json.loads(resp.text))
        return resp

    def push_to_dcnm(self, object):
        url = self.base_url + object.get_parent_url()
        resp = requests.post(url, headers=self.headers, data=object.get_json())

        if not resp.ok:
            logging.info('Posting %s to %s' % (object.get_json(), url))
        return resp

    def get(self, url):
        url = self.base_url + url
        resp = requests.get(url, headers=self.headers)
        if resp.ok:
            logging.info('Got %s. Received response: %s' % (url, resp.text))
        else:
            logging.error('Cloud not get %s. Received response: %s', url, resp.text)
        return resp


