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
    return {'products': products}

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

# Buat view dan route untuk update dan pembelian produk
