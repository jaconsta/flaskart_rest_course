import os
import time

from flask import jsonify, request
from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename

from .models import Products, ProductPictures
from .serializers import products_schema, product_schema, product_pictures_schema, product_picture_schema


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Set literal
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, '../static/uploads/')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


product_bp = Blueprint('product', __name__)


@product_bp.route('/', methods=['get'])
def get_all_products():
    time.sleep(2)
    products = Products.get_all()
    data = products_schema.dump(products)
    return jsonify({'products': data.data})


@product_bp.route('/', methods=['post'])
def create_product():
    product = product_schema.load(request.json)
    Products.save_new(product.data)
    created = product_schema.dump(product.data)
    return jsonify([{'product': created.data}])


@product_bp.route('/<int:product_id>/', methods=['get'])
def get_product(product_id):
    product = product_schema.dump(Products.get_by_id(product_id))
    if not product.data:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return jsonify(product=product.data)


@product_bp.route('/<int:product_id>/', methods=['put'])
def update_product(product_id):
    product = product_schema.load(request.json, instance=Products.get_by_id(product_id))
    Products.update_one(product.data)
    created = product_schema.dump(product.data)
    return jsonify({'product': created.data})


@product_bp.route('/<int:product_id>/', methods=['delete'])
def delete_product(product_id):
    Products.delete_one(product_id)
    return jsonify({'product': 'deleted'})


@product_bp.route('files/', methods=['post'])
def add_product_picture():
    'https://flask.palletsprojects.com/en/1.0.x/patterns/fileuploads/'
    'https://blog.miguelgrinberg.com/post/video-streaming-with-flask'
    if 'file' not in request.files:
        # Form field not present
        response = jsonify({'error': 'missing file'})
        response.status_code = 400
        return response
    file = request.files['file']
    if file.filename == '':
        # Form field is empty
        response = jsonify({'error': 'missing file'})
        response.status_code = 400
        return response
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_name = abs(hash(f'{secure_filename(file.filename)}{time.time()}'))
        file_extension = filename.rsplit('.', 1)[1].lower()
        save_filename = f'prod-{unique_name}.{file_extension}'

        product_name = request.form.get('name', f'prod-{unique_name}.{file_extension}')
        product_picture = ProductPictures.create_new(path=save_filename, name=product_name)
        path = os.path.join(UPLOAD_FOLDER, save_filename)
        file.save(path)

        product_data = product_picture_schema.dump(product_picture).data
        return jsonify({'message': 'file saved', 'product_picture': product_data})

    response = jsonify({'error': f'Invalid images. Allowed file type: {", ".join(ALLOWED_EXTENSIONS)}'})
    response.status_code = 400
    return response


@product_bp.route('files/', methods=['get'])
def get_product_pictures():
    pictures = ProductPictures.get_all()
    data = product_pictures_schema.dump(pictures)
    return jsonify({'products': data.data})


@product_bp.route('files/<int:picture_id>', methods=['get'])
def get_product_picture(picture_id):
    pictures = ProductPictures.get_by_id(picture_id)
    data = product_picture_schema.dump(pictures)
    return jsonify({'product': data.data})
