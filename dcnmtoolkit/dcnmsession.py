import requests
import json
import logging

logging.getLogger(__name__)


class AutoConfigSettings(object):

    def __init__(self):
        self.vrfName = None
        self.isSelectiveHA = None
        self.useLocalDhcp = None
        self.ldapPassWord = None
        self.xmppResponseTimeout = None
        self.xmppSearch = None
        self.xmppUserName = None
        self.dhcpPrimarySubnet = None
        self.amqpExchangeName = None
        self.isTopDown = None
        self.globalAnycastGatewayMAC = None
        self.isHA = None
        self.coreDynamicVlans = None
        self.translateVlans = None
        self.enableAmqpNotification = None
        self.xmppGroup = None
        self.xmppPassWord = None
        self.globalMobilityDomain = None
        self.ldapUserName = None
        self.amqpPort = None
        self.xmppServer = None
        self.amqpServer = None
        self.enableSecureLDAP = None
        self.systemDynamicVlans = None
        self.partitionIdRange = None
        self.selectiveHAFeature = None
        self.amqpUserName = None
        self.ldapServer = None
        self.amqpPassWord = None
        self.segmentIdRange = None
        self.amqpVirtualHost = None

    @classmethod
    def get(cls, session):
        ret = session.get('/rest/auto-config/settings')
        obj = cls()
        for k in ret.json().keys():
            setattr(obj, k, ret.json()[k])
        return obj

    def _generate_attributes(self):
        attributes = {}
        for i in dir(self):
            if i.startswith('_') or i.startswith('get'):
                pass
            else:

                attributes[i] = getattr(self, i)
        return attributes

    def get_json(self):
        return json.dumps(self._generate_attributes())


class Session(object):

    def __init__(self, url, user, passwd):
        self.base_url = url
        self.user = user
        self.passwd = passwd
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.token = None
        self.expiration_time = 1000000
        self.settings = None

    def login(self, load_settings=False):
        url = self.base_url + '/rest/logon'
        payload = {'expirationTime': self.expiration_time}
        try:
            resp = requests.post(url, auth=(self.user, self.passwd), data=json.dumps(payload))
            if resp.ok:
                logging.info('Successfully logged into %s' % url)
            else:
                logging.error('Could not login to %s: Response: %s' % (url, resp.text))
            self.headers.update(json.loads(resp.text))
            return resp

        except requests.exceptions.ConnectionError:
            logging.error('Connection Timed out to %s' % url)

    @property
    def version(self):
        url = '/rest/dcnm-version'
        resp = self.get(url)
        return resp.json()['Dcnm-Version']

    def push_to_dcnm(self, url, data):
        url = self.base_url + url
        resp = requests.post(url, headers=self.headers, data=data)
        print resp.text

        if not resp.ok:
            logging.info('Posting %s to %s' % (data, url))
        return resp

    def delete_from_dcnm(self,url):
        resp = requests.delete(url, headers=self.headers)
        if not resp.ok:
            logging.error('Could not delete: Response was %s ' % resp.text)
        return resp


    def get(self, url):
        url = self.base_url + url
        resp = requests.get(url, headers=self.headers)
        if resp.ok:
            logging.info('Got %s. Received response: %s' % (url, resp.text))
        else:
            logging.error('Cloud not get %s. Received response: %s', url, resp.text)
        return resp

    def fm_get(self, url):
        """
        used for API endpoints under /fmrest
        """
        url = self.url + '/fmrest%s' % url
        resp = requests.get(url, headers=self.headers)
        if resp.ok:
            logging.info('Got %s. Received response: %s' % (url, resp.text))
        else:
            logging.error('Cloud not get %s. Received response: %s', url, resp.text)
        return resp

    def get_settings(self):
        obj = AutoConfigSettings.get(self)
        return obj

    def save_settings(self, obj):
        if isinstance(obj, AutoConfigSettings):
            resp = requests.put(self.base_url + '/auto-config/settings', headers=self.headers, data=obj.get_json())
            return resp
        else:
            raise TypeError()