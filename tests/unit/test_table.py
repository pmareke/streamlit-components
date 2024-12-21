import pandas as pd
from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTabComponent:
    def test_table(self) -> None:
        dataframe = pd.DataFrame({"foo": ["bar"]})
        app = AppTest.from_file("src/table/main.py")

        at = app.run()

        expect(at.table[0].value.to_string()).to(equal(dataframe.to_string()))
