import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';


/**
 * @param  {TangoParameterSelector.propTypes} props
 * @returns {JSX.Element}
 * @constructor
 */
export default function TangoParameterSelector(props) {
    const {id, setProps, availableParams, selectedParam} = props;

    const [domain, setDomain] = React.useState("")
    const [family, setFamily] = React.useState("")
    const [member, setMember] = React.useState("")

    const availableDomains = Object.keys(availableParams)
    const availableFamilies = domain? Object.keys(availableParams[domain]) : []
    const availableMembers = family? availableParams[domain][family] : []

    useEffect(() => {

        if(!selectedParam) {
            setDomain("")
            setFamily("")
            setMember("")
        } else {
            setDomain(selectedParam.domain)
            setFamily(selectedParam.family)
            setMember(selectedParam.member)
        }

    }, [selectedParam,])

    return (
        <Card style={{minWidth: "200px", margin: "10px", borderRadius: "0.6em"}} id={id}>
            <CardHeader
                title={"Tango Parameter"}
                style={{ justifyContent: 'center', textAlign: 'center'}}>
            </CardHeader>
            <CardContent style={
                { justifyContent: 'center', display: "grid", gridRowGap: "10px"}}>
                <FormControl variant="outlined" style={{minWidth: 120}}>
                    <InputLabel id="domain-label">Domain</InputLabel>
                    <Select
                        labelId="domain-label"
                        id="domain"
                        value={domain}
                        onChange={e => {
                            setDomain(e.target.value)
                            setFamily("")
                            setMember("")
                        }}
                        label="Domain"
                    >
                        <MenuItem value="">
                            <em>None</em>
                        </MenuItem>
                        {availableDomains.map(domain =>
                            <MenuItem key={domain} value={domain}>{domain}</MenuItem>)
                        }
                    </Select>
                </FormControl>
                <FormControl variant="outlined" style={{minWidth: 120}}>
                    <InputLabel id="family-label">Family</InputLabel>
                    <Select
                        labelId="family-label"
                        id="family"
                        value={family}
                        onChange={e => {
                            setFamily(e.target.value)
                            setMember("")
                        }}
                        label="Family"
                    >
                        <MenuItem value="">
                            <em>None</em>
                        </MenuItem>
                        {availableFamilies.map(family =>
                            <MenuItem key={family} value={family}>{family}</MenuItem>)
                        }
                    </Select>
                </FormControl>
                <FormControl variant="outlined" style={{minWidth: 120}}>
                    <InputLabel id="member-label">Member</InputLabel>
                    <Select
                        labelId="member-label"
                        id="member"
                        value={member}
                        onChange={e => {
                            setMember(e.target.value)
                        }}
                        label="Member"
                    >
                        <MenuItem value="">
                            <em>None</em>
                        </MenuItem>
                        {availableMembers.map(member =>
                            <MenuItem key={member} value={member}>{member}</MenuItem>)
                        }
                    </Select>
                </FormControl>
            </CardContent>
            <CardActions style={
                { justifyContent: 'center', display: "grid", gridRowGap: "10px"}}>
                <Button
                    variant={'outlined'} style={{minWidth: 120}}
                    onClick={e => {
                        setProps({selectedParam: {domain, family, member}})
                    }}
                >
                    Load
                </Button>
            </CardActions>
        </Card>
    );
}

TangoParameterSelector.defaultProps = {
};

TangoParameterSelector.propTypes = {

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    availableParams: PropTypes.objectOf(
        PropTypes.objectOf(
            PropTypes.arrayOf(PropTypes.string)
        )
    ).isRequired,

    selectedParam: PropTypes.shape({
        domain: PropTypes.string,
        family: PropTypes.string,
        member: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
