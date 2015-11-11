__author__ = 'kecorbin'

class VXLANBaseObject(object):
    pass


class VTEP(VXLANBaseObject):

    def __init__(self, ip=None):
        self.ip = None
        self.switchid = None
        self.nve = None

    @classmethod
    def _get(cls, session, url):
        ret = session.get(url)
        resp = []
        for i in ret.json():
            obj = cls._from_json(i)
            resp.append(obj)
        return resp

    @classmethod
    def get(cls, session, vni=None, mcast=None):
        if vni:
            url = '/topology/switches/vxlan?vni=%s' % str(vni)
        elif mcast:
            url = '/toplogy/switches/vxlan?multicast-address=%s' % mcast
        else:
            url = '/topology/switches/vxlan/vteps?detail=true'
        resp = cls._get(session, url)
        return resp

    def vni(self):
        url =



    @classmethod
    def _from_json(cls, item):
        obj = cls()
        obj.ip = item['Vtep Ip']
        obj.nve = item['Nve Interface']
        obj.switchid = item['Switch Id']
        return obj

