/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { RunSelector } from '../lib';

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
            </div>
        )
    }
}

export default App;
