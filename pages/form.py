import streamlit as st
from pydantic import BaseModel

from src.code.main import Code
from src.component import Component
from src.form.main import Form
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class ExampleModel(BaseModel):  # type: ignore
    some_text: str
    some_number: int
    some_boolean: bool


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Form example")

    def render(self) -> None:
        header = Header("Form Example")
        header.render()

        form = Form(self._callback, ExampleModel)
        tab = Tab()
        tab.add("Form", form)
        lines = [
            "class ExampleModel(BaseModel):",
            "  some_text: str",
            "  some_number: int",
            "  some_boolean: bool",
            "",
            "Form(lamda: st.write('Form submitted'), ExampleModel)",
        ]
        content = "\n".join(lines)
        code = Code(language="python", content=content)

        tab.add("Source code", code)
        tab.render()

        Link.go_home()

    def _callback(self) -> None:
        st.write("Form submitted")


if __name__ == "__main__":
    page = Page()
    page.render()
