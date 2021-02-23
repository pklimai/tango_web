import React, {useEffect} from 'react';
import DateFnsUtils from '@date-io/date-fns';
import PropTypes from 'prop-types';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Switch from '@material-ui/core/Switch';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import Input from '@material-ui/core/Input';
import { DateTimePicker, MuiPickersUtilsProvider } from "@material-ui/pickers";
import _ from 'lodash'


class DateFnsUtilsCustom extends DateFnsUtils {
    constructor() {
        super();
        this.dateTime24hFormat = "dd.MM.yyyy HH:mm:ss"
    }
}


/**
 * @param  {RunSelector.propTypes} props
 * @returns {JSX.Element}
 * @constructor
 */
export default function RunSelector(props) {
    const {id, setProps, availableRuns, selectedTimeInterval, selectedRun, style} = props;

    const [timeChecked, setTimeChecked] = React.useState(false)
    const [runNumber, setRunNumber] = React.useState("")
    const [runNumberErr, setRunNumberErr] = React.useState(false)
    const [runPeriod, setRunPeriod] = React.useState("")

    const [startDT, setStartDT] = React.useState(new Date());
    const [endDT, setEndDT] = React.useState(new Date())

    const availableNumbers = (availableRuns.find(run => run.period === runPeriod) || {numbers: []}).numbers

    useEffect(() => {
        if(selectedRun) {
            setRunNumber(selectedRun.number)
            setRunPeriod(selectedRun.period)
        }

        if(selectedTimeInterval) {
            setStartDT(new Date(selectedTimeInterval.start))
            setEndDT(new Date(selectedTimeInterval.end))
        }
    }, [selectedTimeInterval, selectedRun])


    useEffect(() => {
        if (timeChecked) {
            // console.log({selectedTimeInterval: {start: startDT.toISOString(), end: endDT.toISOString()}});
            setProps({selectedTimeInterval: {start: startDT.toISOString(), end: endDT.toISOString()}})
        } else {
            if(runNumber && runPeriod) {
                // console.log({selectedRun: {number: Number(runNumber), period: Number(runPeriod)}});
                setProps({selectedRun: {number: Number(runNumber), period: Number(runPeriod)}})
            }
        }
    }, [runNumber, runPeriod, startDT, endDT])

    return (
        <Card style={style} id={id}>
            <CardHeader
                title={"Run Selector"}
                style={{
                    justifyContent: 'center',
                    textAlign: 'center',
                }}>
            </CardHeader>
            <Typography component="div" style={
                { justifyContent: 'center', display: "grid"}}>
                <Grid component="label" container alignItems="center" spacing={1} alignContent={'center'}>
                    <Grid item>Run</Grid>
                    <Grid item>
                        <Switch checked={timeChecked} onChange={e => setTimeChecked(e.target.checked)}/>
                    </Grid>
                    <Grid item>Time</Grid>
                </Grid>
            </Typography>
            <CardContent style={
                { justifyContent: 'center', display: "grid", gridRowGap: "10px"}}>
                {timeChecked?
                    <>
                        <MuiPickersUtilsProvider utils={DateFnsUtilsCustom}>
                            <DateTimePicker
                                label="Start Date"
                                ampm={false}
                                inputVariant="outlined"
                                value={startDT}
                                onChange={setStartDT}
                            />
                            <DateTimePicker
                                label="End Date"
                                ampm={false}
                                inputVariant="outlined"
                                value={endDT}
                                onChange={setEndDT}
                            />
                        </MuiPickersUtilsProvider>
                    </>
                    :
                    <>
                        <FormControl variant="outlined" style={{minWidth: 230}}>
                            <InputLabel id="run-period-label">BM@N Period</InputLabel>
                            <Select
                                labelId="run-period-label"
                                id="run-period"
                                value={runPeriod}
                                onChange={e => {
                                    setRunPeriod(e.target.value)
                                    setRunNumber("")
                                }}
                                label="BM@N Period"
                            >
                                <MenuItem value="">
                                    <em>None</em>
                                </MenuItem>
                                {availableRuns.sort().map(run =>
                                    <MenuItem key={run.period} value={run.period}>{run.period}</MenuItem>)}
                            </Select>
                        </FormControl>
                        <FormControl variant="outlined" style={{minWidth: 230, marginTop: 10}}>
                            <InputLabel id="run-number-label">Run Number {runNumberErr? "(not found)": ""}</InputLabel>
                            <Input type="number"  placeholder={availableNumbers.length?
                                `${_.min(availableNumbers)}...${_.max(availableNumbers)}` : ''}
                                   value={runNumber} onChange={
                                       e => {
                                           let val = e.target.value
                                           setRunNumber(val)
                                           setRunNumberErr(
                                               val !== "" &&  !(availableNumbers.includes(Number(val))))
                                       }
                                   }
                                   error={runNumberErr}
                            />
                        </FormControl>
                    </>
                }
            </CardContent>
        </Card>
    );
}

RunSelector.defaultProps = {

    selectedTimeInterval: null
};

RunSelector.propTypes = {

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    availableRuns: PropTypes.arrayOf(
        PropTypes.shape({
            period: PropTypes.number,
            numbers: PropTypes.arrayOf(PropTypes.number)})
    ).isRequired,

    selectedRun: PropTypes.shape({
        number: PropTypes.number,
        period: PropTypes.number}
    ),

    selectedTimeInterval: PropTypes.shape({
        start: PropTypes.string,
        end: PropTypes.string
    }),

    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
