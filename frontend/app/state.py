import requests
from reflex import State


class AppState(State):
    message_input: str = ""
    messages_list: list = []


    def set_message_input(self, value: str):
        self.message_input = value
        
    def add_button_click(self):
        if self.message_input:
            # Send a POST request to the backend
            requests.post("http://localhost:8001/api/messages", json={"text": self.message_input})
            self.message_input = ""
            self.load_messages()

    def load_messages(self):
        try:
            # Send a GET request to the backend
            response = requests.get("http://localhost:8001/api/messages", timeout=5)
            if response.status_code == 200:
                messages = response.json()
                self.messages_list = [f"{msg[0]}: {msg[1]}" for msg in messages]
            else:
                self.messages_list = ["Failed to load messages"]
        except requests.exceptions.RequestException as e:
            self.messages_list = [f"Error: {str(e)}"]

    def on_startup(self):
        # Load messages when the app starts
        self.load_messages()
