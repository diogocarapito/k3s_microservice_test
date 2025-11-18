# pylint: disable=E1102

import reflex as rx
from .state import AppState
from rxconfig import config


# Define the app layout
def main() -> rx.Component:

    message = AppState.messages_list

    return rx.container(
        rx.heading("k3s microservice test", size="9"),
        rx.foreach(
            message,
            lambda msg: rx.box(rx.text(msg)),
        ),
        rx.button(
            "fetch messages",
            color_scheme="teal",
            on_click=AppState.load_messages,
        ),
        rx.input(
            placeholder="Enter your message",
            value=AppState.message_input,
            on_change=AppState.set_message_input,
        ),
        rx.button(
            "Add Message",
            color_scheme="blue",
            on_click=AppState.add_button_click,
        ),
    )


app = rx.App()

# App config
app.config = config

app.add_page(main, route="/", title="Home")
