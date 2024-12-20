from doublex import Spy
from doublex_expects import have_been_called
from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestButton:
    def test_click_button(self) -> None:
        label = "Click me!"
        callback = Spy()

        def create_app(label, callback) -> None:  # type: ignore
            from src.button.main import Button

            internal_app = Button(label, callback.call)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(label, callback))

        at = app.run()

        expect(at.button[0].label).to(equal(label))

        at.button[0].click()

        app.run()

        expect(callback.call).to(have_been_called)
