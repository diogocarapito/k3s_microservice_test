# pylint: disable=E1102

import reflex as rx
from .state import MessageState
from rxconfig import config


# Define the app layout
def main() -> rx.Component:

    message = MessageState.messages_list

    return rx.container(
        rx.heading("k3s microservice test", size="9"),
        rx.foreach(
            message,
            lambda msg: rx.box(rx.text(msg)),
        ),
        rx.button(
            "fetch messages",
            color_scheme="teal",
            on_click=MessageState.load_messages,
        ),
        rx.input(
            placeholder="Enter your message",
            value=MessageState.message_input,
            on_change=MessageState.set_message_input,
        ),
        rx.button(
            "Add Message",
            color_scheme="blue",
            on_click=MessageState.add_message,
        ),
        rx.text("Powered by Reflex"),
        # test button that calls backend API
        rx.button(
            "Test Backend API",
            color_scheme="green",
            # custom on_click that calls the backend /api/messages endpoint and prints the result
            on_click=MessageState.test_backend_api,
        ),
        rx.text(MessageState.response_code),
        # basic button that show a message when clicked
        rx.button(
            "Click Me",
            color_scheme="purple",
            on_click=MessageState.show_message,
        ),
        rx.text(MessageState.display_message),
    )


app = rx.App()

# App config
app.config = config

# Disable the Reflex footer
app.config.disable_footer = True

app.add_page(main, route="/", title="Home")
