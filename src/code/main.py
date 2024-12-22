import streamlit as st

from src.component import Component


class Code(Component):
    def __init__(self, language: str, content: str) -> None:
        self.language = language
        self.content = content

    def render(self) -> None:
        st.code(body=self.content, language=self.language)


if __name__ == "__main__":
    code = Code(
        language="python",
        content='Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))',
    )
    code.render()
