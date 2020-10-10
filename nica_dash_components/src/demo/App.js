/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { RunSelector, TangoParameterSelector } from '../lib';
const availableParams = require('./attrs.json')

class App extends Component {

    constructor(props) {
        super(props);
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
                availableParams,
                dictionary: [{
                    name: "test_dict_param",
                    param: {
                        domain: "mpd",
                        family: "sts",
                        member: "hv",
                        name: "i"
                    }
                }]
            },
            style: {minWidth: "250px", margin: "10px", borderRadius: "0.6em"}
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
                    style={this.state.style}
                    {...this.state.runSelector}
                />
                <TangoParameterSelector
                    setProps={this.setProps}
                    style={this.state.style}
                    {...this.state.tangoParamSelector}/>
            </div>
        )
    }
}

export default App;
