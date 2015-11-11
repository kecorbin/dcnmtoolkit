
class CablePlan(object):

    @classmethod
    def get(cls, session):
        url = '/cable-plans/discovery'
        resp =session.get(url)
        return resp.text
