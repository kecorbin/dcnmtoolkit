import json
import logging


class BaseObject(object):

    def get_json(self):
        return json.dumps(self._generate_attributes())


class Org(BaseObject):
    def __init__(self, name):
        self.organizationName = name

    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        return attributes

    def _get_url_extension(self):
        return '/%s' % self.organizationName

    def get_parent_url(self):
        return '/auto-config/organizations'

    def get_url(self):
        return self._get_parent_url() + self._get_url_extension()

    def get_json(self):
        return json.dumps(self._generate_attributes())

    @classmethod
    def _get_parent_url(cls):
        return '/auto-config/organizations'

    @classmethod
    def _from_json(cls, item):
        obj = cls(item['organizationName'])
        return obj

    @classmethod
    def get(cls, session):
        url = '/auto-config/organizations?detail=True'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i)
            resp.append(obj)
        return resp


class Partition(BaseObject):
    def __init__(self, name, parent, profile='vrf-common-evpn'):
        self.organizationName = parent.organizationName
        self.partitionName = name
        self.vrfName = self.organizationName + ":" + self.partitionName
        self.vrfProfileName = profile

    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        attributes['partitionName'] = self.partitionName
        attributes['vrfName'] = self.vrfName
        attributes['vrfProfileName'] = self.vrfProfileName
        return attributes

    def _get_url_extenstion(self):
        return 'partitions/%s' % self.partitionName

    def _get_parent_url(self):
        return '/auto-config/organizations/%s/partitions' % self.organizationName

    @classmethod
    def _from_json(cls, item, parent):
        print item
        obj = cls(item['partitionName'], parent)

        return obj

    def get_url(self):
        return '/auto-config/organizations/%s/partitions/%s' % (self.organizationName, self.partitionName)

    @classmethod
    def get(cls, session, parent):
        url = parent.get_url() + '/partitions?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i, parent)
            resp.append(obj)
        return resp

class Network(BaseObject):
    def __init__(self, name, parent, profile='defaultNetworkEvpnProfile', mobilityDomainId='md0'):
        self.networkName = name
        self.organizationName = parent.organizationName
        self.partitionName = parent.partitionName
        self.vrfName = parent.vrfName
        self.vlanId = None
        self.segmentId = None
        self.profileName = profile
        self.mobilityDomainId = mobilityDomainId

    def _generate_attributes(self):
        attributes = dict()
        attributes['organizationName'] = self.organizationName
        attributes['partitionName'] = self.partitionName
        attributes['vrfName'] = self.vrfName
        attributes['networkName'] = self.networkName
        attributes['vlanId'] = self.vlanId
        attributes['segmentId'] = self.segmentId
        attributes['profileName'] = self.profileName
        attributes['mobilityDomainId'] = self.mobilityDomainId

        return attributes

    def get_parent_url(self):
        return '/auto-config/organizations/%s/partitions/%s/networks' % (self.organizationName,
                                                                         self.partitionName)

    def get_url(self):
        return '/auto-config/organizations/%s/partitions/%s/networks' % (self.organizationName,
                                                                            self.partitionName)

    @classmethod
    def get(cls, session, parent):
        url = parent.get_url() + '/networks?detail=true'
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i, parent)
            resp.append(obj)
        return resp

    @classmethod
    def _from_json(cls, item, parent):
        obj = cls(item['networkName'], parent)
        return obj