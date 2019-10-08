import React from 'react'
import PropTypes from 'prop-types'

import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import Divider from '@material-ui/core/Divider'


const ProductItem = props => (
  <>
    <ListItem>
      <ListItemText
        primary={props.name}
        secondary={`$ ${props.price} - sku: ${props.sku}`}
      />
    </ListItem>
    <Divider variant="middle" component="li" />
  </>
)

ProductItem.propTypes = {
  name: PropTypes.string,
  price: PropTypes.number,
  sku: PropTypes.string,
}

export default ProductItem
