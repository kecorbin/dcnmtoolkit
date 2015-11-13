import json

class AutoConfigSettings(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['vrfName'] = None
            self.attributes['isSelectiveHA'] = None
            self.attributes['useLocalDhcp'] = None
            self.attributes['ldapPassWord'] = None
            self.attributes['xmppGroup'] = None
            self.attributes['xmppResponseTimeout'] = None
            self.attributes['xmppSearch'] = None
            self.attributes['xmppUserName'] = None
            self.attributes['amqpExchangeName'] = None
            self.attributes['isTopDown'] = None
            self.attributes['globalAnycastGatewayMAC'] = None
            self.attributes['isHA'] = None
            self.attributes['coreDynamicVlans'] = None
            self.attributes['translateVlans'] = None
            self.attributes['enableAmqpNotification'] = None
            self.attributes['ldapUserName'] = None
            self.attributes['xmppPassWord'] = None
            self.attributes['globalMobilityDomain'] = None
            self.attributes['dhcpPrimarySubnet'] = None
            self.attributes['amqpPort'] = None
            self.attributes['xmppServer'] = None
            self.attributes['amqpServer'] = None
            self.attributes['enableSecureLDAP'] = None
            self.attributes['systemDynamicVlans'] = None
            self.attributes['partitionIdRange'] = None
            self.attributes['selectiveHAFeature'] = None
            self.attributes['segmentIdRange'] = None
            self.attributes['ldapServer'] = None
            self.attributes['amqpPassWord'] = None
            self.attributes['amqpUserName'] = None
            self.attributes['amqpVirtualHost'] = None

    def set_vrfName(self, val):
        self.attributes['vrfName'] = val

    def get_vrfName(self):
        return self.attributes['vrfName']

    def set_isSelectiveHA(self, val):
        self.attributes['isSelectiveHA'] = val

    def get_isSelectiveHA(self):
        return self.attributes['isSelectiveHA']

    def set_useLocalDhcp(self, val):
        self.attributes['useLocalDhcp'] = val

    def get_useLocalDhcp(self):
        return self.attributes['useLocalDhcp']

    def set_ldapPassWord(self, val):
        self.attributes['ldapPassWord'] = val

    def get_ldapPassWord(self):
        return self.attributes['ldapPassWord']

    def set_xmppGroup(self, val):
        self.attributes['xmppGroup'] = val

    def get_xmppGroup(self):
        return self.attributes['xmppGroup']

    def set_xmppResponseTimeout(self, val):
        self.attributes['xmppResponseTimeout'] = val

    def get_xmppResponseTimeout(self):
        return self.attributes['xmppResponseTimeout']

    def set_xmppSearch(self, val):
        self.attributes['xmppSearch'] = val

    def get_xmppSearch(self):
        return self.attributes['xmppSearch']

    def set_xmppUserName(self, val):
        self.attributes['xmppUserName'] = val

    def get_xmppUserName(self):
        return self.attributes['xmppUserName']

    def set_amqpExchangeName(self, val):
        self.attributes['amqpExchangeName'] = val

    def get_amqpExchangeName(self):
        return self.attributes['amqpExchangeName']

    def set_isTopDown(self, val):
        self.attributes['isTopDown'] = val

    def get_isTopDown(self):
        return self.attributes['isTopDown']

    def set_globalAnycastGatewayMAC(self, val):
        self.attributes['globalAnycastGatewayMAC'] = val

    def get_globalAnycastGatewayMAC(self):
        return self.attributes['globalAnycastGatewayMAC']

    def set_isHA(self, val):
        self.attributes['isHA'] = val

    def get_isHA(self):
        return self.attributes['isHA']

    def set_coreDynamicVlans(self, val):
        self.attributes['coreDynamicVlans'] = val

    def get_coreDynamicVlans(self):
        return self.attributes['coreDynamicVlans']

    def set_translateVlans(self, val):
        self.attributes['translateVlans'] = val

    def get_translateVlans(self):
        return self.attributes['translateVlans']

    def set_enableAmqpNotification(self, val):
        self.attributes['enableAmqpNotification'] = val

    def get_enableAmqpNotification(self):
        return self.attributes['enableAmqpNotification']

    def set_ldapUserName(self, val):
        self.attributes['ldapUserName'] = val

    def get_ldapUserName(self):
        return self.attributes['ldapUserName']

    def set_xmppPassWord(self, val):
        self.attributes['xmppPassWord'] = val

    def get_xmppPassWord(self):
        return self.attributes['xmppPassWord']

    def set_globalMobilityDomain(self, val):
        self.attributes['globalMobilityDomain'] = val

    def get_globalMobilityDomain(self):
        return self.attributes['globalMobilityDomain']

    def set_dhcpPrimarySubnet(self, val):
        self.attributes['dhcpPrimarySubnet'] = val

    def get_dhcpPrimarySubnet(self):
        return self.attributes['dhcpPrimarySubnet']

    def set_amqpPort(self, val):
        self.attributes['amqpPort'] = val

    def get_amqpPort(self):
        return self.attributes['amqpPort']

    def set_xmppServer(self, val):
        self.attributes['xmppServer'] = val

    def get_xmppServer(self):
        return self.attributes['xmppServer']

    def set_amqpServer(self, val):
        self.attributes['amqpServer'] = val

    def get_amqpServer(self):
        return self.attributes['amqpServer']

    def set_enableSecureLDAP(self, val):
        self.attributes['enableSecureLDAP'] = val

    def get_enableSecureLDAP(self):
        return self.attributes['enableSecureLDAP']

    def set_systemDynamicVlans(self, val):
        self.attributes['systemDynamicVlans'] = val

    def get_systemDynamicVlans(self):
        return self.attributes['systemDynamicVlans']

    def set_partitionIdRange(self, val):
        self.attributes['partitionIdRange'] = val

    def get_partitionIdRange(self):
        return self.attributes['partitionIdRange']

    def set_selectiveHAFeature(self, val):
        self.attributes['selectiveHAFeature'] = val

    def get_selectiveHAFeature(self):
        return self.attributes['selectiveHAFeature']

    def set_segmentIdRange(self, val):
        self.attributes['segmentIdRange'] = val

    def get_segmentIdRange(self):
        return self.attributes['segmentIdRange']

    def set_ldapServer(self, val):
        self.attributes['ldapServer'] = val

    def get_ldapServer(self):
        return self.attributes['ldapServer']

    def set_amqpPassWord(self, val):
        self.attributes['amqpPassWord'] = val

    def get_amqpPassWord(self):
        return self.attributes['amqpPassWord']

    def set_amqpUserName(self, val):
        self.attributes['amqpUserName'] = val

    def get_amqpUserName(self):
        return self.attributes['amqpUserName']

    def set_amqpVirtualHost(self, val):
        self.attributes['amqpVirtualHost'] = val

    def get_amqpVirtualHost(self):
        return self.attributes['amqpVirtualHost']

    def get_json(self):
        return json.dumps(self.attributes)


    @classmethod
    def get(cls, session):
        url = '/rest/auto-config/settings'
        ret = session.get(url)
        obj = cls(attributes=ret.json())
        return obj
