from dcnmtoolkit import Session, Org, Partition, Network, VTEP, VNI, Profile, CablePlan, AutoConfigSettings
import unittest
import json

try:
    from credentials import URL, LOGIN, PASSWORD
except ImportError:
    print
    print 'To run live tests, please create a credentials.py file with the following variables filled in:'
    print """
    URL = ''
    LOGIN = ''
    PASSWORD = ''
    """
TEST_VNI = '11001100'
TEST_MCAST = '225.4.0.2'

MAX_RANDOM_STRING_SIZE = 20


class OfflineTests(unittest.TestCase):

    def test_create_valid_org(self):
        """
        Test basic Org creation
        """
        org = Org(name='testorg')
        data = '{"organizationName": "testorg"}'

        self.assertIsInstance(org, Org)
        self.assertEqual(org.get_json(), data)

    def test_create_org_from_json(self):
        """
        Test basic Org creation
        """
        data = '{"organizationName": "testorg-json"}'
        org = Org._from_json(json.loads(data))


        self.assertIsInstance(org, Org)
        self.assertEqual(org.get_json(), data)

    def test_create_valid_partition(self):
        org = Org(name='testorg')
        part = Partition('test-partition', org)
        self.assertIsInstance(part, Partition)

class LiveTestReadOnly(unittest.TestCase):
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_login(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_orgs(self):
        orgs = Org.get(self.session())
        self.assertIsInstance(orgs, list)

    def test_get_profiles(self):
        profiles = Profile.get(self.session())
        self.assertIsInstance(profiles, list)

    def test_get_vteps(self):
        vteps = VTEP.get(self.session())
        self.assertIsInstance(vteps, list)
        self.assertIsInstance(vteps[0], VTEP)


    def test_get_vnis_for_switch(self):
        vteps = VTEP.get(self.session())
        for vtep in vteps:
            vnis = vtep.get_vnis(self.session())
            self.assertIsInstance(vnis, list)
            has_vni = hasattr(vnis[0], 'vni')
            self.assertTrue(has_vni)

    def test_get_vnis_by_vni(self):
        vnis = VTEP.get(self.session(), vni=TEST_VNI)
        has_vni = hasattr(vnis[0], 'vni')
        self.assertTrue(has_vni)

    def test_get_vnis_by_mcast(self):
        vnis = VTEP.get(self.session(), mcast=TEST_MCAST)
        has_vni = hasattr(vnis[0], 'vni')
        self.assertTrue(has_vni)
        self.assertIsInstance(vnis, list)

class ProfileReadOnlyTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_profiles(self):
        profiles = Profile.get(self.session)
        print profiles
        self.assertIsInstance(profiles, list)

    def test_get_profile_attributes(self):
        profiles = Profile.get(self.session)
        print profiles
        testprofile = profiles[0]

        for method in dir(profiles[0]):
            if method.startswith('get_'):
                a = getattr(testprofile, method)
                a()

    def test_set_profile_attributes(self):
        profiles = Profile.get(self.session)
        print profiles
        testprofile = profiles[0]

        for method in dir(profiles[0]):
            if method.startswith('set_'):
                a = getattr(testprofile, method)
                a('foo')

class AutoConfigReadWriteTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_create_org(self):
        testorg = Org('unittesting')
        resp = self.session.push_to_dcnm(testorg.get_url(), testorg.get_json())
        print resp.status_code
        print resp.ok
        self.assertTrue(resp.ok)

    def test_create_partition(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        resp = self.session.push_to_dcnm(testpartition.get_url(), testpartition.get_json())
        self.assertTrue(resp.ok)

    def test_create_network(self):
        testorg = Org('unittesting')
        testpartition = Partition('p1', testorg)
        n1 = Network('net1', testpartition)
        n1.segmentId = 333
        n1.vlanId = n1.segmentId
        resp = self.session.push_to_dcnm(n1.get_url(), n1.get_json())
        print resp.text
    #
    # def test_delete_network(self):
    #     testorg = Org('unittesting')
    #     testpartition = Partition('p1', testorg)
    #     n1 = Network('net1', testpartition)
    #     n1.mark_as_deleted()
    #     resp = self.session.delete_from_dcnm(n1.get_url())

    # orgs
    ##############

    # orgs = Org.get(dcnm)
    # print orgs
    # parts = Partition.get(dcnm, orgs[0])
    # print parts[0]

    ################
    # network tests
    #################
    # raw = dcnm.get('/rest/auto-config/organizations/test-org/partitions?detail=true')
    # print raw
    # print raw.text
    # nets = Network.get(dcnm, parts[0])
    # print nets
    # test = Org('test-org')
    # p1 = Partition('DMZ', test)
    # n1 = Network('net1', p1)
    # n1.segmentId = 2345
    # n1.vlanId = 2345
    # print dcnm.push_to_dcnm(n1).text




class CablePlanTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_cableplans(self):
        cps = CablePlan.get(self.session)
        print cps
        self.assertIsInstance(cps, list)


class SessionTests(unittest.TestCase):

    @property
    def session(self):
        session = Session(URL, LOGIN, PASSWORD)
        res = session.login()
        return session

    def test_get_auto_config_settings(self):
        settings = AutoConfigSettings.get(self.session)
        print settings

if __name__ == '__main__':
    readonly = unittest.TestSuite()
    readonly.addTest(LiveTestReadOnly)
    readonly.addTest(ProfileReadOnlyTests)
    readonly.addTest(CablePlanTests)
    readonly.addTest(SessionTests)

    readwrite = unittest.TestSuite()
    readwrite.addTest(AutoConfigReadWriteTests)

    offline = unittest.TestSuite()
    offline.addTest(unittest.makeSuite(OfflineTests))

    full = unittest.TestSuite([readonly, readwrite, offline])

    # Add tests to this suite while developing the tests
    # This allows only these tests to be run
    develop = unittest.TestSuite()

    unittest.main(defaultTest='full')