"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class FormState(rx.State):
    form_data: dict = {}
    form_submitted: bool = False

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.form_submitted = True


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Finance Manager!", font_size="2em"),
            rx.box("Track and manage all your income and expenses"),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
        rx.vstack(
            rx.link(
                "New Transaction",
                href="/new-transaction",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="5%",
        )
    )


def transactionList() -> rx.Component:
    return rx.vstack(
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )


def transactionForm() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    id="first_name",
                ),
                rx.input(
                    placeholder="Last Name", id="last_name"
                ),
                rx.hstack(
                    rx.checkbox("Checked", id="check"),
                    rx.switch("Switched", id="switch"),
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormState.handle_submit,
        ),
    )


@rx.page(route='/new-transaction')
def newTransaction():
    return rx.cond(FormState.form_submitted,
                   transactionList(),
                   transactionForm(),
                   )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
