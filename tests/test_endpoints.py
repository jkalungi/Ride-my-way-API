import json

from tests.base import BaseTestCase

class MyEndpointTest(BaseTestCase):


    def test_offers(self):

        val = self.check_offers()

        sift = val.get_json()

        semisift = sift[1]
        finalsift = semisiftt["status"]

self.assertequal(finalsift["code"], 600)


def test_singleoffer(self):

       val = self.check_singleoffer(1000)

       sift = val.get_json()

       semisift = sift[1]
       finalsift = semisift["status"]

self.assertequal(finalsift["code"], 600)    