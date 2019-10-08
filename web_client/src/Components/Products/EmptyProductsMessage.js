import React from 'react'

import Typography from '@material-ui/core/Typography';

import { EmptyListPaper } from './styled'

const EmptyProductMessage = () => (
  <EmptyListPaper>
    <Typography variant="h5" component="h3">
      There are no products to display
    </Typography>
  </EmptyListPaper>
)

export default EmptyProductMessage
