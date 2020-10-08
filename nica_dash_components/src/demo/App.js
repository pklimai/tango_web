/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { RunSelector, TangoParameterSelector } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            /**
             * @type RunSelector.propTypes
             */
            runSelector: {
                availableRuns: [{
                    period: 1,
                    numbers: [1,2,3]
                }, {
                    period: 2,
                    numbers: [1,2,3]
                }]
            },
            tangoParamSelector: {
                availableParams: {
                    'mpd': {
                        'tof': ['hv', 'adc_202', 'mpd_beam_lv', 'hv_st', 'adc_mpd_gas', 'adc_mpd_house', 'gas_202',
                            'dustmon_42', 'pir230e_cleanroom', 'avg_adc_202'],
                        't0t': ['status', 'jpts'],
                        'ecal': ['hv', 'hv_st', 'hv_new'],
                        'gem': ['wiener_hv', 'wiener_lv', 'adc_gas_sensors'],
                        'dch': ['wiener_hv', 'wiener_lv', 'mpod_lv'],
                        'zdc': ['hv', 'hv_st', 'position_sys'],
                        'tof700': ['hv', 'hv_st', 'temp', 'hv_5000', 'hv_5001', 'hv_5002', 'hv_5003'],
                        'bmn': ['adc_bman_beam', 'sensors', 'statusserver'],
                        'daq': ['crates', 'run_status', 'switches_201', 'bmn_switch', 'elma_crates', 'runcontrol'],
                        'switch': ['bmn11'],
                        'tof400': ['gas_bmn', 'preamp', 'wiener_hv', 'hv', 'preamp_bmn1', 'preamp_bmn2', 'preamp_bmn3',
                            'preamp_bmn4', 'preamp_bmn5', 'preamp_bmn6', 'wiener_hv_imes', 'gas_scales', 'gas_sensors',
                            'wiener_lv', 'sensor_202'],
                        'scales': ['caspb60'],
                        'gas_202': ['mks_pac100'],
                        'test_beam': ['switch'],
                        'crate': ['new'],
                        'sts': ['adc1', 'hv', 'adc2', 'lv', 'adc1_proxy', 'adc2_proxy'],
                        'mwpc': ['wiener_hv']
                    }, 'bmn': {'daq': ['ups']}
                }
            }
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div style={{width: "min-content"}}>
                <RunSelector
                    setProps={this.setProps}
                    {...this.state.runSelector}
                />
                <TangoParameterSelector
                    setProps={this.setProps}
                    {...this.state.tangoParamSelector}/>
            </div>
        )
    }
}

export default App;
