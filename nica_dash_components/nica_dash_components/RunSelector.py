# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RunSelector(Component):
    """A RunSelector component.
@param  {RunSelector.propTypes} props
@returns {JSX.Element}
@constructor

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- availableRuns (dict; required): availableRuns has the following type: list of dicts containing keys 'period', 'numbers'.
Those keys have the following types:
  - period (number; optional)
  - numbers (list of numbers; optional)
- selectedRun (dict; optional): selectedRun has the following type: dict containing keys 'number', 'period'.
Those keys have the following types:
  - number (number; optional)
  - period (number; optional)
- selectedTimeInterval (dict; optional): selectedTimeInterval has the following type: dict containing keys 'start', 'end'.
Those keys have the following types:
  - start (string; optional)
  - end (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, availableRuns=Component.REQUIRED, selectedRun=Component.UNDEFINED, selectedTimeInterval=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'availableRuns', 'selectedRun', 'selectedTimeInterval']
        self._type = 'RunSelector'
        self._namespace = 'nica_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'availableRuns', 'selectedRun', 'selectedTimeInterval']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['availableRuns']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(RunSelector, self).__init__(**args)
