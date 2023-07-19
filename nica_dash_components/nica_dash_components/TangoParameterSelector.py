# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TangoParameterSelector(Component):
    """A TangoParameterSelector component.
@param  {TangoParameterSelector.propTypes} props
@returns {JSX.Element}
@constructor

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- availableParams (dict with strings as keys and values of type dict with strings as keys and values of type dict with strings as keys and values of type list of strings; required)

- dictionary (list of dicts; optional)

    `dictionary` is a list of dicts with keys:

    - name (string; optional)

    - param (optional)

- isCustomProperty (boolean; default False)

- selectedParam (optional)

- style (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'nica_dash_components'
    _type = 'TangoParameterSelector'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, availableParams=Component.REQUIRED, dictionary=Component.UNDEFINED, selectedParam=Component.UNDEFINED, style=Component.UNDEFINED, isCustomProperty=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'availableParams', 'dictionary', 'isCustomProperty', 'selectedParam', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'availableParams', 'dictionary', 'isCustomProperty', 'selectedParam', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['availableParams']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(TangoParameterSelector, self).__init__(**args)
