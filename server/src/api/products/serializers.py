from marshmallow import fields, Schema, post_dump
from marshmallow_sqlalchemy import ModelSchema

from connections.db import db  # session
from .models import Products


class ProductSchema(ModelSchema):
    class Meta:
        model = Products
        sqla_session = db.session


class ProductFieldsSchema(Schema):
    name = fields.String(required=True)
    sku = fields.String(required=True)
    price = fields.Integer(required=True)


class ProductPicturesSchema(Schema):
    id = fields.Integer()
    path = fields.String()
    name = fields.String()

    @post_dump(pass_many=False)
    def add_pre_to_path(self, data, **kwargs):
        path = data.get("path")
        if path:
            data["path"] = f'/static/{data["path"]}'
        return data


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
product_picture_schema = ProductPicturesSchema()
product_pictures_schema = ProductPicturesSchema(many=True)
