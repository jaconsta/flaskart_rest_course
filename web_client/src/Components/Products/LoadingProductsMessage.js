import React from 'react'
import PropTypes from 'prop-types'

import CircularProgress from '@material-ui/core/CircularProgress'
import Typography from '@material-ui/core/Typography';

const LoadingProductsMessage = ({ show }) => {
  if (!show) return null
  return (
    <div>
      <CircularProgress />
      <Typography variant="h5" component="h3">
        Loading your products
      </Typography>
    </div>
  )
}

LoadingProductsMessage.propTypes = {
  show: PropTypes.bool,
}

LoadingProductsMessage.defaultProps = {
  show: false,
}

export default LoadingProductsMessage
