from collections.abc import Callable
from typing import Any

import streamlit as st
import streamlit_pydantic as sp

from examples.component import Component


class Form(Component):
    def __init__(self, callback: Callable, model: Any) -> None:
        self.callback = callback
        self.model = model

    def render(self) -> None:
        data = sp.pydantic_form(key=__name__, model=self.model)
        if data:
            self.callback()


if __name__ == "__main__":
    form = Form(callback=lambda: st.write("Form submitted"))
    form.render()
