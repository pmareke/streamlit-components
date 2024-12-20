# Streamlit Components

Current examples:

- [X] [Header](./pages/header.py)
- [X] [Link](./pages/link.py)
- [X] [Button](./pages/button.py)
- [X] [Form](./pages/form.py)
    - The component relies on the [streamlit-pydantic](https://github.com/lukasmasuch/streamlit-pydantic) library.
- [X] [Tab](./pages/tab.py)

Everything is in the `examples` folder and all the example rely on the `Component` class.

## `Component` class

In order to have the ability to test our components and use the best coding practices we need to
define a common behaviour.

In this case all the components will have a `render` method, which will call streamlit in order to 
build the component.

We will use the constructor to set the component properties.

