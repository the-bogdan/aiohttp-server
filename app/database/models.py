from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table


__all__ = [
    'Base',
    'User',
    'Order',
    'UserRelation'
]


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    family_name = Column(String)
    _nickname = Column(String)
    _password = Column(String)

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"Пользователь {self.last_name} {self.first_name}"


class UserRelation(Base):
    __tablename__ = 'users_relations'

    id = Column(Integer, primary_key=True)
    src_user_id = Column(Integer, ForeignKey("users.id"))
    dst_user_id = Column(Integer, ForeignKey("users.id"))

    src_user = relationship("User", foreign_keys=[src_user_id])
    dst_user = relationship("User", foreign_keys=[src_user_id])


class OrderProduct(Base):
    __tablename__ = 'orders_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    order = relationship("Order", foreign_keys=[order_id], back_populates='products')
    product = relationship("Product", foreign_keys=[product_id], back_populates='orders')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', foreign_keys=[user_id], back_populates="orders")
    products = relationship('OrderProduct', back_populates='order')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    left_in_stock = Column(Integer)

    orders = relationship("OrderProduct", back_populates='product')
