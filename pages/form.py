import streamlit as st
from pydantic import BaseModel

from examples.component import Component
from examples.form.main import Form
from examples.header.main import Header
from examples.link.main import Link


class ExampleModel(BaseModel):  # type: ignore
    some_text: str
    some_number: int
    some_boolean: bool


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Form example")

    def render(self) -> None:
        header = Header()
        header.render("Form Example")

        form = Form(self._callback, ExampleModel)
        form.render()

        Link.go_home()

    def _callback(self) -> None:
        st.write("Form submitted")


if __name__ == "__main__":
    page = Page()
    page.render()
