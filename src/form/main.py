from collections.abc import Callable

import streamlit as st
import streamlit_pydantic as sp
from pydantic import BaseModel

from src.component import Component


class Form(Component):
    def __init__(self, callback: Callable, model: type[BaseModel]) -> None:
        self.callback = callback
        self.model = model

    def render(self) -> None:
        data = sp.pydantic_form(key=__name__, model=self.model)
        if data:
            self.callback(data.model_dump())


if __name__ == "__main__":

    class MyModel(BaseModel):  # type: ignore
        name: str
        age: int

    form = Form(callback=lambda _: st.write("Form submitted"), model=MyModel)
    form.render()
