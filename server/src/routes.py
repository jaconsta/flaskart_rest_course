from flask import send_from_directory

def register_routes(app):
    from api.products.views import product_bp

    app.register_blueprint(product_bp, url_prefix='/api/products')

    @app.route('/static/<path:path>')
    def static_serving(path):
        """
        Remember not to use it on production, Use a proxy like Nginx instead.
        """
        return send_from_directory('static/uploads', path)
