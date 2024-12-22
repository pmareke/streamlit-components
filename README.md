# Streamlit Components

The app is deployed at [my-components.streamlit.app](https://clean-components.streamlit.app).

Current examples:

- [Header page](./pages/header.py)
  - [Header Component](./src/header/main.py)
- [Divider page](./pages/divider.py)
  - [Divider Component](./src/divider/main.py)
- [Title page](./pages/title.py)
  - [Title Component](./src/title/main.py)
- [Link page](./pages/link.py)
  - [Link Component](./src/link/main.py)
- [Button page](./pages/button.py)
  - [Button Component](./src/button/main.py)
- [Form page](./pages/form.py)
    - [Form Component](./src/form/main.py)
    - The component relies on the [streamlit-pydantic](https://github.com/lukasmasuch/streamlit-pydantic) library.
- [Tab page](./pages/tab.py)
  - [Tab Component](./src/tab/main.py) 
- [Table page](./pages/table.py)
  - [Table Component](./src/table/main.py) 
- [Code page](./pages/code.py)
  - [Code Component](./src/code/main.py) 

Work in progress:

- [ ] Error Alerts
- [ ] Success Alerts
- [ ] Columns
- [ ] Grid

Everything is in the `examples` folder and all the example rely on the `Component` class.

## `Component` class

In order to have the ability to test our components and use the best coding practices we need to
define a common behaviour.

In this case all the components will have a `render` method, which will call streamlit in order to 
build the component.

We will use the constructor to set the component properties.

