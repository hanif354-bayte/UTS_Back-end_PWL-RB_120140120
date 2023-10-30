# Import modul-modul yang diperlukan dari SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Deklarasikan Base sebagai kelas dasar untuk model SQLAlchemy
Base = declarative_base()

# Definisikan kelas Product yang akan merepresentasikan tabel 'products' dalam database
class Product(Base):
    # Tentukan nama tabel dalam database
    __tablename__ = 'products'
    
    # Kolom id sebagai primary key dengan tipe data Integer
    id = Column(Integer, primary_key=True)
    
    # Kolom name sebagai nama produk dengan tipe data String
    name = Column(String)
    
    # Kolom price sebagai harga produk dengan tipe data Integer
    price = Column(Integer)
    
    # Kolom stock sebagai stok produk dengan tipe data Integer
    stock = Column(Integer)
