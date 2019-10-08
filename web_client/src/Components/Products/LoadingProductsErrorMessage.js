import React from 'react'
import PropTypes from 'prop-types'

import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';

const LoadingProductsErrorMessage = props => (
  <Snackbar
    open={props.open}
    autoHideDuration={6000}
    onClose={props.onClose}
    message={<span id="message-id">{props.message}</span>}
    action={[
      <IconButton
        key="close"
        aria-label="Close"
        color="inherit"
        onClick={props.onClose}
      >
        <CloseIcon />
      </IconButton>,
    ]}
  />
)

LoadingProductsErrorMessage.propTypes = {
  open: PropTypes.bool,
  onClose: PropTypes.func,
  message: PropTypes.string,
}

export default LoadingProductsErrorMessage
