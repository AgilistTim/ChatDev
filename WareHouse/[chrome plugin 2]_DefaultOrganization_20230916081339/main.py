'''
This is the main file of the chrome plugin. It initializes the GUI and handles user interactions.
'''
import tkinter as tk
from jira_api import JiraAPI
from chatgpt_api import ChatGPTAPI
class ChromePlugin:
    def __init__(self):
        self.jira_api = None
        self.chatgpt_api = ChatGPTAPI()
        self.root = tk.Tk()
        self.root.title("Jira Chat Plugin")
        # Create UI elements
        self.api_key_entry = tk.Entry(self.root)
        self.api_key_entry.pack()
        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_jira_api)
        self.connect_button.pack()
        self.root.mainloop()
    def connect_jira_api(self):
        api_key = self.api_key_entry.get()
        self.jira_api = JiraAPI(api_key)
if __name__ == "__main__":
    plugin = ChromePlugin()