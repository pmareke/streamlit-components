from collections.abc import Callable

import streamlit as st

from examples.component import Component


class Button(Component):
    def __init__(self, label: str, callback: Callable) -> None:
        self.label = label
        self.callback = callback

    def render(self) -> None:
        button = st.button(self.label)
        if button:
            self.callback()


if __name__ == "__main__":
    button = Button("Send", callback=lambda: st.write("Button clicked!!!"))
    button.render()
