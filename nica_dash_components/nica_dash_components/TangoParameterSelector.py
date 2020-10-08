# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TangoParameterSelector(Component):
    """A TangoParameterSelector component.
@param  {TangoParameterSelector.propTypes} props
@returns {JSX.Element}
@constructor

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- availableParams (dict with strings as keys and values of type dict with strings as keys and values of type list of strings; required)
- selectedParam (dict; optional): selectedParam has the following type: dict containing keys 'domain', 'family', 'member'.
Those keys have the following types:
  - domain (string; optional)
  - family (string; optional)
  - member (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, availableParams=Component.REQUIRED, selectedParam=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'availableParams', 'selectedParam']
        self._type = 'TangoParameterSelector'
        self._namespace = 'nica_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'availableParams', 'selectedParam']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['availableParams']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TangoParameterSelector, self).__init__(**args)
