from doublex import Spy
from doublex_expects import have_been_called
from expects import expect
from streamlit.testing.v1 import AppTest


class TestForm:
    def test_submit_form(self) -> None:
        callback = Spy()

        def create_app(callback) -> None:  # type: ignore
            from dataclasses import dataclass

            from examples.form.main import Form

            @dataclass
            class MyModel:
                name: str
                age: int

            model = MyModel(name="John Doe", age=30)
            internal_app = Form(callback.call, model)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(callback,))

        at = app.run()

        at.button[0].click()

        app.run()

        expect(callback.call).to(have_been_called)
