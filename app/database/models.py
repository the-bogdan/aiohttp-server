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


order_product = Table(
    'orders_products',
    Base.metadata,
    Column('order_id', Integer, ForeignKey("orders.id")),
    Column('product_id', Integer, ForeignKey("products.id"))
)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', foreign_keys=[user_id], back_populates="orders")
    products = relationship(
        'Product',
        secondary=order_product,
        back_populates='orders'
    )


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    left_in_stock = Column(Integer)

    orders = relationship(
        "Order",
        secondary=order_product,
        back_populates='products'
    )
