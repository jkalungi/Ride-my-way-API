import uuid
import json


class Request:
    def __init__(self, id, title, description, date):
        self.id = id
        self.title= title
        self.description = description
        self.date = date

    def json(self):
        """
        json representation of the Request model
        """
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date':self.date
        })