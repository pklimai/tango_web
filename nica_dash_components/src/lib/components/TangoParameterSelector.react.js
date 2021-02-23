import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import Grid from '@material-ui/core/Grid';
import Switch from '@material-ui/core/Switch';
import Typography from '@material-ui/core/Typography';


/**
 * @param  {TangoParameterSelector.propTypes} props
 * @returns {JSX.Element}
 * @constructor
 */
export default function TangoParameterSelector(props) {
    const {id, setProps, availableParams, selectedParam, style, dictionary} = props;

    const [domain, setDomain] = React.useState("")
    const [family, setFamily] = React.useState("")
    const [member, setMember] = React.useState("")
    const [name, setName] = React.useState("")

    const availableDomains = Object.keys(availableParams)
    const availableFamilies = domain? Object.keys(availableParams[domain]) : []
    const availableMembers = family? Object.keys(availableParams[domain][family]) : []
    const availableNames = member? availableParams[domain][family][member] : []

    const [option, setOption] = React.useState("")

    const availableOptions = dictionary? dictionary.map(item => item.name) : []

    const [isCustom, setIsCustom] = React.useState(true)

    useEffect(() => {

        if(!selectedParam) {
            setDomain("")
            setFamily("")
            setMember("")
            setName("")
        } else {
            setDomain(selectedParam.domain)
            setFamily(selectedParam.family)
            setMember(selectedParam.member)
            setName(selectedParam.name)
        }

    }, [selectedParam,])

    return (
        <Card style={style} id={id}>
            <CardHeader
                title={"Tango Parameter"}
                style={{ justifyContent: 'center', textAlign: 'center'}}>
            </CardHeader>
            <Typography component="div" style={
                { justifyContent: 'center', display: "grid"}}>
                <Grid component="label" container alignItems="center" spacing={1} alignContent={'center'}>
                    <Grid item>Dictionary</Grid>
                    <Grid item>
                        <Switch
                            checked={isCustom}
                            onChange={e => setIsCustom(e.target.checked)}
                        />
                    </Grid>
                    <Grid item>Custom</Grid>
                </Grid>
            </Typography>
            <CardContent style={
                { justifyContent: 'center', display: "grid", gridRowGap: "10px"}}>
                {
                    isCustom? <> <FormControl variant="outlined" style={{minWidth: 250}}>
                        <InputLabel id="domain-label">Domain</InputLabel>
                        <Select
                            labelId="domain-label"
                            id="domain"
                            value={domain}
                            onChange={e => {
                                setDomain(e.target.value)
                                setFamily("")
                                setMember("")
                                setName("")
                            }}
                            label="Domain"
                        >
                            <MenuItem value="">
                                <em>None</em>
                            </MenuItem>
                            {availableDomains.sort().map(domain =>
                                <MenuItem key={domain} value={domain}>{domain}</MenuItem>)
                            }
                        </Select>
                    </FormControl>
                        <FormControl variant="outlined" style={{minWidth: 250}}>
                            <InputLabel id="family-label">Family</InputLabel>
                            <Select
                                labelId="family-label"
                                id="family"
                                value={family}
                                onChange={e => {
                                    setFamily(e.target.value)
                                    setMember("")
                                    setName("")
                                }}
                                label="Family"
                            >
                                <MenuItem value="">
                                    <em>None</em>
                                </MenuItem>
                                {availableFamilies.sort().map(family =>
                                    <MenuItem key={family} value={family}>{family}</MenuItem>)
                                }
                            </Select>
                        </FormControl>
                        <FormControl variant="outlined" style={{minWidth: 250}}>
                            <InputLabel id="member-label">Member</InputLabel>
                            <Select
                                labelId="member-label"
                                id="member"
                                value={member}
                                onChange={e => {
                                    setMember(e.target.value)
                                    setName("")
                                }}
                                label="Member"
                            >
                                <MenuItem value="">
                                    <em>None</em>
                                </MenuItem>
                                {availableMembers.sort().map(member =>
                                    <MenuItem key={member} value={member}>{member}</MenuItem>)
                                }
                            </Select>
                        </FormControl>
                        <FormControl variant="outlined" style={{minWidth: 250}}>
                            <InputLabel id="name-label">Name</InputLabel>
                            <Select
                                labelId="name-label"
                                id="name"
                                value={name}
                                onChange={e => {
                                    setName(e.target.value)
                                    setProps({selectedParam: {domain, family, member, name: e.target.value}})
                                }}
                                label="Name"
                            >
                                <MenuItem value="">
                                    <em>None</em>
                                </MenuItem>
                                {availableNames.sort().map(name =>
                                    <MenuItem key={name} value={name}>{name}</MenuItem>)
                                }
                            </Select>
                        </FormControl>
                    </> : <>
                        <FormControl variant="outlined" style={{minWidth: 250}}>
                            <InputLabel id="option-label">Parameter (Alias)</InputLabel>
                            <Select
                                labelId="option-label"
                                id="option"
                                value={option}
                                onChange={e => {
                                    if(!e.target.value) {
                                        setDomain("")
                                        setFamily("")
                                        setMember("")
                                        setName("")
                                        setProps({selectedParam: undefined})

                                    } else {
                                        const {domain, family, member, name} = dictionary
                                            .find(option => option.name === e.target.value)
                                            .param
                                        setDomain(domain)
                                        setFamily(family)
                                        setMember(member)
                                        setName(name)

                                        setProps({selectedParam: {domain, family, member, name}})
                                    }


                                    setOption(e.target.value)
                                }}
                                label="Parameter (Alias)"
                            >
                                <MenuItem value="">
                                    <em>None</em>
                                </MenuItem>
                                {availableOptions.sort().map(option =>
                                    <MenuItem key={option} value={option}>{option}</MenuItem>)
                                }
                            </Select>
                        </FormControl>
                    </>

                }
            </CardContent>
        </Card>
    );
}

TangoParameterSelector.defaultProps = {
};

const TangoParam = PropTypes.shape({
    domain: PropTypes.string,
    family: PropTypes.string,
    member: PropTypes.string,
    name: PropTypes.string
})

TangoParameterSelector.propTypes = {

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    availableParams: PropTypes.objectOf(
        PropTypes.objectOf(
            PropTypes.objectOf(
                PropTypes.arrayOf(PropTypes.string)
            )
        )
    ).isRequired,

    dictionary: PropTypes.arrayOf(PropTypes.shape({
        name: PropTypes.string,
        param: TangoParam
    })),

    selectedParam: TangoParam,

    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
