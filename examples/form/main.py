from collections.abc import Callable

import streamlit as st
import streamlit_pydantic as sp

from examples.component import Component


class Form(Component):
    def __init__(self, callback: Callable) -> None:
        self.callback = callback

    def render(self) -> None:
        data = sp.pydantic_form(key=__name__, model=self.model)
        if data:
            self.callback()


if __name__ == "__main__":
    form = Form(callback=lambda: st.write("Form submitted"))
    form.render()
