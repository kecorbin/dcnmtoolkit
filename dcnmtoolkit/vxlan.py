__author__ = 'kecorbin'

class VXLANBaseObject(object):
    pass


class VNI(VXLANBaseObject):
    def __init__(self):
        self.status = None
        self.nve = None
        self.switchname = None
        self.mcast = None
        self.switchid = None
        self.Vlan = None
        self.vni = None


    @classmethod
    def from_json(cls, item):
        obj = cls()
        obj.status = item['Vni Status']
        obj.nve = item['Nve Interface']
        obj.switchname = item['Switch Name']
        obj.mcast = item['Multicast Address']
        obj.switchid = item['Switch id']
        obj.Vlan = item['Vlan']
        obj.vni = item['Vni']
        return obj

    def peers(self, session):
        url = '/topology/switches/vxlan/peers?switch-id=%s&vni=%s' % (self.switchid, self.vni)
        resp = session.get(url)
        return resp.json()


class VTEP(VXLANBaseObject):

    def __init__(self, ip=None):
        self.ip = None
        self.switchid = None
        self.nve = None

    @classmethod
    def _get(cls, session, url):
        ret = session.get(url)
        resp = []
        if ('vni' in url) or ('multicast' in url):
            for i in ret.json():
                obj = VNI.from_json(i)
                resp.append(obj)
        else:
            for i in ret.json():
                obj = cls._from_json(i)
                resp.append(obj)
        return resp

    @classmethod
    def get(cls, session, vni=None, mcast=None):
        if vni:
            url = '/topology/switches/vxlan?vni=%s' % str(vni)

        elif mcast:
            url = '/topology/switches/vxlan?multicast-address=%s' % mcast

        else:
            url = '/topology/switches/vxlan/vteps?detail=true'
        resp = cls._get(session, url)
        return resp


    def get_vnis(self, session):
        url = '/topology/switches/vxlan?switch-id=%s' % self.switchid
        resp = []
        ret = session.get(url)
        for i in ret.json():
            obj = VNI.from_json(i)
            resp.append(obj)
        return resp

    @classmethod
    def _from_json(cls, item):
        obj = cls()
        obj.ip = item['Vtep Ip']
        obj.nve = item['Nve Interface']
        obj.switchid = item['Switch Id']
        return obj
