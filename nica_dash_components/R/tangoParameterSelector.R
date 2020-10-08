# AUTO GENERATED FILE - DO NOT EDIT

tangoParameterSelector <- function(id=NULL, availableParams=NULL, selectedParam=NULL) {
    
    props <- list(id=id, availableParams=availableParams, selectedParam=selectedParam)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TangoParameterSelector',
        namespace = 'nica_dash_components',
        propNames = c('id', 'availableParams', 'selectedParam'),
        package = 'nicaDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
