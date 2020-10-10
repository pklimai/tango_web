# AUTO GENERATED FILE - DO NOT EDIT

tangoParameterSelector <- function(id=NULL, availableParams=NULL, dictionary=NULL, selectedParam=NULL, style=NULL) {
    
    props <- list(id=id, availableParams=availableParams, dictionary=dictionary, selectedParam=selectedParam, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TangoParameterSelector',
        namespace = 'nica_dash_components',
        propNames = c('id', 'availableParams', 'dictionary', 'selectedParam', 'style'),
        package = 'nicaDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
