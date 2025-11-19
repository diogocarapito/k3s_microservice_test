import os
import requests
from reflex.state import State


# Fetch the backend URL from the environment variable, with a default fallback
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-svc:8001")
#BACKEND_URL = os.getenv("BACKEND_URL", "http://0.0.0.0:8001")


class MessageState(State):
    message_input: str = ""
    messages_list: list = []
    response_code = "hello"

    def add_message(self):
        """Send a POST request to the backend to add a message."""
        message = self.message_input

        def _do_post():
            try:
                requests.post(
                    f"{BACKEND_URL}/api/messages",
                    json={"text": message},
                    timeout=5,
                )
            except requests.exceptions.RequestException as e:
                print(f"Error adding message: {e}")

    def load_messages(self):
        """Send a GET request to the backend to load messages."""
        try:
            response = requests.get(f"{BACKEND_URL}/api/messages", timeout=5)
            if response.status_code == 200:
                messages = response.json()
                self.messages_list = [f"{msg[0]}: {msg[1]}" for msg in messages]
                print("Messages loaded successfully")
            else:
                self.messages_list = ["Failed to load messages"]
                print(f"Error: Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.messages_list = [f"Error: {str(e)}"]
            print(f"Error loading messages: {e}")
            print(f"{BACKEND_URL}/api/messages")

    def set_message_input(self, value: str):
        """Set the message input value."""
        self.message_input = value

    def on_startup(self):
        """Load messages when the app starts."""
        self.load_messages()
        
    def test_backend_api(self):
        try:
            response = requests.get(f"{BACKEND_URL}/api/messages", timeout=5)
            if response.status_code == 200:
                messages = response.json()
                for msg in messages:
                    print(f"{msg[0]}: {msg[1]}")
                self.response_code = "success"
            else:
                self.response_code = "error"

        except requests.exceptions.RequestException as e:
            self.response_code = "error_exception"
            
