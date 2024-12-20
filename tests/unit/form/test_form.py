from doublex import Spy
from doublex_expects import have_been_called
from expects import equal, expect
from pydantic import BaseModel
from streamlit.testing.v1 import AppTest


class MyModel(BaseModel):  # type: ignore
    name: str
    age: int


class TestForm:
    def test_submit_form(self) -> None:
        callback = Spy()

        def create_app(callback, model) -> None:  # type: ignore
            from examples.form.main import Form

            internal_app = Form(callback.call, model)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(callback, MyModel))

        at = app.run()

        expect(at.text_input[0].label).to(equal("Name"))
        expect(at.number_input[0].label).to(equal("Age"))

        at.button[0].click()

        app.run()

        expect(callback.call).to(have_been_called)
