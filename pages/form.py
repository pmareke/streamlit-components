import streamlit as st
from pydantic import BaseModel

from src.code.main import Code
from src.component import Component
from src.divider.main import Divider
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
        code = Code(language="python", content=self._content)

        tab.add("Source code", code)
        tab.render()

        Divider.render()

        Link.go_home()

    def _callback(self, data: dict) -> None:
        st.json(data)

    @property
    def _content(self) -> str:
        lines = [
            "class ExampleModel(BaseModel):",
            "  some_text: str",
            "  some_number: int",
            "  some_boolean: bool",
            "",
            "Form(lambda data: st.json(data), ExampleModel)",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    page = Page()
    page.render()
