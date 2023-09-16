'''
This file contains the JiraAPI class which securely accesses the Jira API.
'''
import requests
class JiraAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.jira.com"
    def get_issue_details(self, issue_id):
        '''
        Retrieve issue details from Jira API
        '''
        url = f"{self.base_url}/issues/{issue_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve issue details: {response.text}")
    def update_issue(self, issue_id, data):
        '''
        Update issue in Jira API
        '''
        url = f"{self.base_url}/issues/{issue_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update issue: {response.text}")