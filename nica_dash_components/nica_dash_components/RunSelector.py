# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RunSelector(Component):
    """A RunSelector component.
@param  {RunSelector.propTypes} props
@returns {JSX.Element}
@constructor

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- availableRuns (list of dicts; required)

    `availableRuns` is a list of dicts with keys:

    - numbers (list of numbers; optional)

    - period (number; optional)

- selectedRun (dict; optional)

    `selectedRun` is a dict with keys:

    - number (number; optional)

    - period (number; optional)

- selectedTimeInterval (dict; optional)

    `selectedTimeInterval` is a dict with keys:

    - end (string; optional)

    - start (string; optional)

- style (dict; optional)

- timeCheckedProperty (boolean; default False)

- wrongRunProperty (boolean; default False)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'nica_dash_components'
    _type = 'RunSelector'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, availableRuns=Component.REQUIRED, selectedRun=Component.UNDEFINED, selectedTimeInterval=Component.UNDEFINED, style=Component.UNDEFINED, timeCheckedProperty=Component.UNDEFINED, wrongRunProperty=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'availableRuns', 'selectedRun', 'selectedTimeInterval', 'style', 'timeCheckedProperty', 'wrongRunProperty']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'availableRuns', 'selectedRun', 'selectedTimeInterval', 'style', 'timeCheckedProperty', 'wrongRunProperty']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['availableRuns']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(RunSelector, self).__init__(**args)
