import json
from tests.base import BaseTestCase

class MyEndpointTests(BaseTestCase):


    def test_manyoffers(self):

        val = self.check_manyoffers();

        sift = val.get_json()

        semisift = sift[1]
        finalsift = semisiftt["status"]

   self.assertequal(finalsift["code"], 600)


   def test-singleoffer(self):

       val = self.check_singleoffer(1000);

       sift = val.get_json()

       semisift = sift[1]
       finalsift = semisift["status"
       
       self.assertEqual(finalsift["code"], 600)     