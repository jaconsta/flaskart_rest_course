import axios from 'axios'

const SERVER_URL = `http://${window.location.hostname}:8000/api/`

export const fetchProducts = () => {
  return axios.get(`${SERVER_URL}products/`)
  .then(({data}) => data)
}

export const createProduct = body => {
  return axios.post(`${SERVER_URL}products/`, body)
  .then(({data}) => data)
}
