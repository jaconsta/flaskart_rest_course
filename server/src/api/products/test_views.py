import pytest
# from server import create_app
# from connections.db import db, init_db, drop_db


# @pytest.fixture(scope='module')
# def test_create_client():
#     app = create_app('sqlite:///test_flaskart.sqlite')
#     client = app.test_client()
#
#     context = app.app_context()
#     context.push()
#
#     yield client
#
#     context.pop()
#
#
# @pytest.fixture(scope='module')
# def test_create_tables():
#     db.init_db()
#     yield
#     db.drop_db()


def test_list_products(test_create_client, test_create_tables):
    """
    GIVEN no products exists
    WHEN I get 'products/'
    THEN I should receive an empty product list.

    :param test_create_client:
    :param test_create_tables:
    :return:
    """
    """
    client = app.test_client()
    context = app.app_context()
    context.push()

    # Run test
    init_db()
    x = client.get('/api/products/')

    assert x.status_code == 200, f'Response {x.status_code}'
    assert x.data.decode('utf-8')[:-1] == '{"products":[]}'

    context.pop()
    """
    x = test_create_client.get('/api/products/')

    assert x.status_code == 200, f'Response {x.status_code}'
    assert x.data.decode('utf-8') == '{"products":[]}\n'


def test_add_product(test_create_client, test_create_tables):
    """
    GIVEN no products on list
    WHEN I add a product
    AND I get 'products/'
    THEN I receive the product created

    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
    https://www.guru99.com/pytest-tutorial.html
    """
    product_data = {
        "name": "product6", "price": 1000, "sku": "abc"
    }
    test_create_client.post('/api/products/', json=product_data)

    products_response = test_create_client.get('/api/products/')

    assert products_response.status_code == 200, f'Response {products_response.status_code}'
    product_response = products_response.get_json().get('products')
    assert len(product_response) == 1
    assert product_response[0]['name'] == 'product6'
    assert product_response[0]['price'] == 1000

    product_res = test_create_client.get(f'/api/products/{product_response[0]["id"]}/')
    assert product_res.status_code == 200, f'Response {product_response.status_code}'
    prod_res = product_res.get_json().get('product')
    assert prod_res['name'] == 'product6'
    assert prod_res['price'] == 1000
