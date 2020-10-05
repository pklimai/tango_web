% Auto-generated: do not edit by hand
\name{runSelector}

\alias{runSelector}

\title{RunSelector component}

\description{
@param  {RunSelector.propTypes} props @returns {JSX.Element} @constructor
}

\usage{
runSelector(id=NULL, availableRuns=NULL, selectedRun=NULL,
selectedTimeInterval=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{availableRuns}{List of lists containing elements 'period', 'numbers'.
those elements have the following types:
  - period (numeric; optional)
  - numbers (list of numerics; optional)s. }

\item{selectedRun}{Lists containing elements 'number', 'period'.
those elements have the following types:
  - number (numeric; optional)
  - period (numeric; optional). }

\item{selectedTimeInterval}{Lists containing elements 'start', 'end'.
those elements have the following types:
  - start (optional)
  - end (optional). }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

