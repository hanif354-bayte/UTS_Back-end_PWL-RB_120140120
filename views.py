# Import modul-modul yang diperlukan dari Pyramid
from pyramid.response import Response
from pyramid.view import view_config

# Import model produk dari file models.py
from .models import Product

# Definisikan view untuk halaman utama
@view_config(route_name='home', renderer='json')
def home(request):
    # Query semua produk dari database
    products = request.dbsession.query(Product).all()
    # Kembalikan produk dalam format JSON
    return {'products': [product.serialize() for product in products]}

# Definisikan view untuk menambahkan produk
@view_config(route_name='add_product', request_method='POST', renderer='json')
def add_product(request):
    # Ambil data JSON dari permintaan
    data = request.json_body
    # Lakukan validasi data di sini
    # Buat objek Produk baru dan tambahkan ke database
    new_product = Product(**data)
    request.dbsession.add(new_product)
    # Kembalikan respons JSON
    return {'status': 'success', 'message': 'Product added successfully'}

# Definisikan view untuk menghapus produk
@view_config(route_name='delete_product', request_method='DELETE', renderer='json')
def delete_product(request):
    # Ambil id produk dari path parameter
    product_id = int(request.matchdict['id'])
    # Query produk berdasarkan id
    product = request.dbsession.query(Product).get(product_id)
    # Hapus produk jika ditemukan
    if product:
        request.dbsession.delete(product)
        return {'status': 'success', 'message': 'Product deleted successfully'}
    else:
        return {'status': 'error', 'message': 'Product not found'}

# Definisikan view untuk memperbarui produk
@view_config(route_name='update_product', request_method='PUT', renderer='json')
def update_product(request):
    # Ambil id produk dari path parameter
    product_id = int(request.matchdict['id'])
    # Query produk berdasarkan id
    product = request.dbsession.query(Product).get(product_id)
    # Perbarui atribut produk jika ditemukan
    if product:
        # Ambil data JSON dari permintaan
        data = request.json_body
        # Lakukan validasi data di sini jika diperlukan
        # Perbarui atribut produk
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        # Kembalikan respons JSON
        return {'status': 'success', 'message': 'Product updated successfully'}
    else:
        return {'status': 'error', 'message': 'Product not found'}

# Definisikan view untuk pembelian produk
@view_config(route_name='purchase_product', request_method='POST', renderer='json')
def purchase_product(request):
    # Ambil id produk dari path parameter
    product_id = int(request.matchdict['id'])
    # Query produk berdasarkan id
    product = request.dbsession.query(Product).get(product_id)
    # Lakukan validasi stok produk dan proses pembelian jika ditemukan
    if product and product.stock > 0:
        # Kurangi stok produk
        product.stock -= 1
        # Kembalikan respons JSON
        return {'status': 'success', 'message': 'Product purchased successfully'}
    else:
        return {'status': 'error', 'message': 'Product not available for purchase'}
