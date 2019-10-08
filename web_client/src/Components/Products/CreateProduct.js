import React, { useState } from 'react'

import AddProductDialog from './AddProductDialog'
import { ButtomButton } from './styled'

import { createProduct } from 'services/api/products'

const emptyProduct = {
  name: '',
  price: 0,
  sku: ''
}

const CreateProduct = props => {
  const [isDialogOpen, setDialogOpen] = useState(false)
  const [product, setProduct] = useState(emptyProduct)

  const openAddProductDialog = () => setDialogOpen(true)
  const closeAddProductDialog = () => {
    setProduct(emptyProduct)
    setDialogOpen(false)
  }

  const textChange = name => e => {
    setProduct({ ...product, [name]: e.target.value })
  }
  const numberChange = name => e => {
    setProduct({ ...product, [name]: parseInt(e.target.value) })
  }
  const submitForm = async e => {
    if(e) e.preventDefault()
    await createProduct(product)
    closeAddProductDialog()
    props.refreshProducts()
  }

  return (
    <>
      <AddProductDialog open={isDialogOpen} handleClose={closeAddProductDialog} product={product} onChange={textChange} onChangeNumber={numberChange} onSubmit={submitForm} />
      <ButtomButton onClick={openAddProductDialog} variant="contained" color="primary" size="medium">Add a product</ButtomButton>
    </>
  )
}

export default CreateProduct
