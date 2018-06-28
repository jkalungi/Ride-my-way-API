import unittest
import json
from app import app
from app.config import app_config


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        # app.run(port = 5000)
        # self.client = app.test_client(self)
        # self.app_context.push()

        return app

        def setUp(self):
             #pass
            self.client = app.test_client(self)
            app.config.from_object(app_config["testing"])

            def tearDown(self):
                """
                Drop the data structure data
                """

                def check_manyoffers(self):
                    send = self.client.get('/api/v1/rides',content_type='application/json')
                    return send
                    def check_singleoffers(self,id):
                        send = self.client.get('/api/v1/rides/{}'.format(id),content_type='application/json')
                        return send