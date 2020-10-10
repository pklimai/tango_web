# AUTO GENERATED FILE - DO NOT EDIT

runSelector <- function(id=NULL, availableRuns=NULL, selectedRun=NULL, selectedTimeInterval=NULL, style=NULL) {
    
    props <- list(id=id, availableRuns=availableRuns, selectedRun=selectedRun, selectedTimeInterval=selectedTimeInterval, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'RunSelector',
        namespace = 'nica_dash_components',
        propNames = c('id', 'availableRuns', 'selectedRun', 'selectedTimeInterval', 'style'),
        package = 'nicaDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
