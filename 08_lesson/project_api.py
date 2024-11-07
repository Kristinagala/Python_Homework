import requests


class Project:

    def __init__(self, url):
        self.url = url

    def get_token(self, login, password, companyId):
        creds = {
            'login': login,
            'password': password,
            'companyId': companyId
            }
        resp = requests.post(self.url+'/api-v2/auth/keys', json=creds)
        token = resp.json()["key"]
        return token

    def get_project_list(self):
        token = self.get_token()
        my_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url+'/api-v2/projects', headers=my_headers)
        return resp.json()
    
    def get_project_list_negative(self):
        token = self.get_token()
        my_headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url+'/api-v2/projects', headers=my_headers)
        return resp.status_code

    def create_project(self, name):
        project = {
            'title': name
        }
        token = self.get_token()
        my_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        resp = requests.post(self.url+'/api-v2/projects', headers=my_headers, json=project)
        return resp.json()
    
    def create_project_negative(self, name):
        project = {
            'title': name
        }
        token = self.get_token()
        my_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        resp = requests.post(self.url+'/api-v2/projects', headers=my_headers, json=project)
        return resp.status_code
    
    def get_project(self, id):
        token = self.get_token()
        my_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url+'/api-v2/projects/' + str(id), headers=my_headers)
        return resp.json()
    
    def edit(self, new_id, new_name):
        token = self.get_token()
        my_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        project = {
            'title': new_name
        }
        resp = requests.put(self.url+'/api-v2/projects/' + str(new_id), json=project, headers=my_headers)
        return resp.json()