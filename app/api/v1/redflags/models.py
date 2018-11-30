from flask import jsonify, make_response, request
incidents = []

class RedFlagModel():

    def __init__(self):
        self.db = incidents
        if len(incidents) == 0:
            self.id = 1
        else:
            self.id = incidents[-1]['id'] + 1  
        self.id = len(incidents) + 1

    def save(self, data):
        data['id'] = self.id

        self.db.append(data)
    
    def find(self, redflag_id):
        for incident in self.db:
            if incident['id'] == redflag_id:
                return incident

        return None

    def delete(self, incident):
        self.db.remove(incident)


    def get_all(self):
        return self.db


    
          