import React from 'react'
import PropTypes from 'prop-types'

import Button from '@material-ui/core/Button'
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogTitle from '@material-ui/core/DialogTitle'
import DialogContent from '@material-ui/core/DialogContent'
import TextField from '@material-ui/core/TextField'

const AddProductDialog = props => (
  <Dialog
    open={props.open}
    onClose={props.handleClose}
  >
    <DialogTitle>
      Add a new product
    </DialogTitle>
    <DialogContent>
      <form onSubmit={props.onSubmit}>
        <TextField autoFocus id="create-product-name" label="name" type="text" fullWidth value={props.product.name} onChange={props.onChange('name')} />
        <TextField id="create-product-price" label="price" type="number" fullWidth value={props.product.price} onChange={props.onChangeNumber('price')} />
        <TextField id="create-product-sku" label="SKU" type="text" fullWidth value={props.product.sku} onChange={props.onChange('sku')} />
      </form>
    </DialogContent>
    <DialogActions>
      <Button onClick={props.handleClose} color="primary">
        Cancel
      </Button>
      <Button onClick={props.onSubmit} color="secondary">
        Create
      </Button>
    </DialogActions>
  </Dialog>
)

AddProductDialog.propTypes = {
  open: PropTypes.bool,
  onChange: PropTypes.func,
  onChangeNumber: PropTypes.func,
  handleClose: PropTypes.func,
  product: PropTypes.shape({
    name: PropTypes.string,
    price: PropTypes.number,
    sku: PropTypes.string,
  }),
  onSubmit: PropTypes.func,
}

export default AddProductDialog
