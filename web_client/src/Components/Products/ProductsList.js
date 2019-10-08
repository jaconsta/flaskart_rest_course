import React, {useEffect, useState} from 'react';
import map from 'lodash/map'

import List from '@material-ui/core/List'

import CreateProduct from './CreateProduct'
import EmptyProductsMessage from './EmptyProductsMessage'
import LoadingProductsMessage from './LoadingProductsMessage'
import LoadingProductsErrorMessage from './LoadingProductsErrorMessage'
import ProductItem from './ProductItem'
import { fetchProducts } from 'services/api/products'

const initialProducts = []

const ProductsList = () => {
  const [products, setProducts] = useState(initialProducts)
  const [isLoadingProducts, setIsLoadingProducts] = useState(false)
  const [productsDidLoad, setProductsDidLoad ] = useState(false)
  const [showError, setShowError] = useState(false)

  const handleErrorClose = () => setShowError(false)
  const getAllProducts = () => {
    setIsLoadingProducts(true)
    fetchProducts()
    .then(({products}) => {
      setProducts(products)
    })
    .catch(err => {
      setShowError(true)
    })
    .finally(() => {
      setIsLoadingProducts(false)
      setProductsDidLoad(true)
    })
  }
  const refreshProducts = () => setProductsDidLoad(false)

  useEffect(getAllProducts, [productsDidLoad])

  return (
    <>
      { products.length < 1 && !isLoadingProducts && <EmptyProductsMessage />}
      <LoadingProductsMessage show={isLoadingProducts} />
      { !isLoadingProducts && (
        <List>
          { map(products, product => <ProductItem key={product.id} { ...product }/>) }
        </List>
      )}
      <LoadingProductsErrorMessage open={showError} onClose={handleErrorClose} />
      <CreateProduct refreshProducts={refreshProducts}/>
    </>
  )
}

export default ProductsList
