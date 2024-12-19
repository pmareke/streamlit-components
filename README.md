# Streamlit Components

Current examples:

- [X] [Header](./examples/header/main.py)
- [X] [Link](./examples/link/main.py)
- [X] [Button](./examples/button/main.py)
- [X] [Form](./examples/form/main.py)
    - The component relies on the [streamlit-pydantic](https://github.com/lukasmasuch/streamlit-pydantic) library.
- [X] [Tab](./examples/tab/main.py)

Everything is in the `examples` folder and all the example rely on the `Component` class.

## `Component` class

In order to have the ability to test our components and use the best coding practices we need to
define a common behaviour.

In this case all the components will have a `render` method, which will call streamlit in order to 
build the component.

We will use the constructor to set the component properties.

