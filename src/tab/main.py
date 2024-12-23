import streamlit as st

from src.component import Component


class Tab(Component):
    def __init__(self) -> None:
        self.items: dict[str, Component] = {}

    def add(self, name: str, component: Component) -> None:
        self.items[name] = component

    def render(self) -> None:
        tabs = st.tabs(list(self.items.keys()))

        for index, _tab in enumerate(tabs):
            with _tab:
                components = list(self.items.values())
                components[index].render()


if __name__ == "__main__":

    class DummyComponent(Component):
        def render(self) -> None:
            st.text("any-text")

    tab = Tab()
    dummy_component = DummyComponent()
    tab.add("Dummy tab", dummy_component)
    tab.render()
