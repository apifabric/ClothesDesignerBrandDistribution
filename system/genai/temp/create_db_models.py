# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Brand(Base):
    """description: Represents a designer brand providing clothing lines."""

    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)


class Designer(Base):
    """description: Represents individual designers who create styles."""

    __tablename__ = 'designers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    speciality = Column(String)


class Collection(Base):
    """description: Represents a collection of clothing items under a brand."""

    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)


class Gallery(Base):
    """description: Location where collections are showcased."""

    __tablename__ = 'galleries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=False)
    capacity = Column(Integer)
    established_date = Column(DateTime, nullable=False)


class Item(Base):
    """description: Represents individual clothing items within a collection."""

    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    item_type = Column(String, nullable=False)
    price = Column(Integer)
    release_date = Column(DateTime, nullable=False)
    collection_id = Column(Integer, ForeignKey('collections.id'), nullable=False)


class Store(Base):
    """description: Retail stores selling collections."""

    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)


class Supplier(Base):
    """description: Supply chain partners providing materials."""

    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    material_type = Column(String, nullable=False)


class BrandDesigner(Base):
    """description: Association between brands and designers."""

    __tablename__ = 'brand_designers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    designer_id = Column(Integer, ForeignKey('designers.id'), nullable=False)


class Warehouse(Base):
    """description: Warehouse for storing collections and items."""

    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=False)
    max_capacity = Column(Integer)
    temperature_control = Column(Boolean)


class Event(Base):
    """description: Brand events showcasing collections."""

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    event_date = Column(DateTime, nullable=False)
    gallery_id = Column(Integer, ForeignKey('galleries.id'), nullable=False)


class PurchaseOrder(Base):
    """description: Orders placed by stores for collection items."""

    __tablename__ = 'purchase_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    collection_id = Column(Integer, ForeignKey('collections.id'), nullable=False)
    total_amount = Column(Integer)


class SupplyOrder(Base):
    """description: Orders placed by brands to suppliers."""

    __tablename__ = 'supply_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    total_cost = Column(Integer)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Test data for Brand
brand1 = Brand(name='Elegance', country='Italy')
brand2 = Brand(name='Urban Chic', country='USA')
brand3 = Brand(name='Vintage Virtue', country='France')
brand4 = Brand(name='Modern Minimal', country='Japan')

# Test data for Designer


designer1 = Designer(name='Alex Monroe', speciality='Evening wear')
designer2 = Designer(name='Linda Wells', speciality='Casual streetwear')
designer3 = Designer(name='Hiro Nakamura', speciality='Bohemian Chic')
designer4 = Designer(name='Veronica Chloe', speciality='Accessories')

# Test data for Collection
collection1 = Collection(name='Spring Fling', season='Spring', brand_id=1)
collection2 = Collection(name='Winter Wonder', season='Winter', brand_id=2)
collection3 = Collection(name='Autumn Aura', season='Autumn', brand_id=3)
collection4 = Collection(name='Summer Style', season='Summer', brand_id=4)

# Test data for Gallery
gallery1 = Gallery(location='Milan', capacity=300, established_date=date(2010, 5, 2))
gallery2 = Gallery(location='New York', capacity=500, established_date=date(2008, 8, 10))
gallery3 = Gallery(location='Paris', capacity=250, established_date=date(2015, 3, 16))
gallery4 = Gallery(location='Tokyo', capacity=400, established_date=date(2012, 7, 23))

# Test data for Item
item1 = Item(name='Silk Dress', item_type='Dress', price=300, release_date=date(2023, 3, 1), collection_id=1)
item2 = Item(name='Wool Coat', item_type='Outerwear', price=550, release_date=date(2022, 11, 20), collection_id=2)
item3 = Item(name='Leather Jacket', item_type='Jacket', price=450, release_date=date(2023, 9, 5), collection_id=3)
item4 = Item(name='Cotton Shirt', item_type='Shirt', price=100, release_date=date(2022, 7, 11), collection_id=4)

# Test data for Store
store1 = Store(name='Chic Essentials', location='Los Angeles')
store2 = Store(name='Fashion Hub', location='London')
store3 = Store(name='Trendsetters', location='Sydney')
store4 = Store(name='Style Corner', location='Berlin')

# Test data for Supplier
supplier1 = Supplier(name='Fabric Corp', material_type='Textiles')
supplier2 = Supplier(name='Leather Goods Ltd', material_type='Leather')
supplier3 = Supplier(name='Button World', material_type='Accessories')
supplier4 = Supplier(name='Threadline', material_type='Threads')

# Test data for BrandDesigner
brandDesigner1 = BrandDesigner(brand_id=1, designer_id=1)
brandDesigner2 = BrandDesigner(brand_id=2, designer_id=2)
brandDesigner3 = BrandDesigner(brand_id=3, designer_id=3)
brandDesigner4 = BrandDesigner(brand_id=4, designer_id=4)

# Test data for Warehouse
warehouse1 = Warehouse(location='Central City', max_capacity=1000, temperature_control=True)
warehouse2 = Warehouse(location='West End', max_capacity=1500, temperature_control=False)
warehouse3 = Warehouse(location='East Side', max_capacity=800, temperature_control=True)
warehouse4 = Warehouse(location='North Point', max_capacity=1200, temperature_control=False)

# Test data for Event
event1 = Event(name='Exclusive Spring Show', event_date=date(2023, 3, 15), gallery_id=1)
event2 = Event(name='Winter Fashion Week', event_date=date(2022, 12, 5), gallery_id=2)
event3 = Event(name='Autumn Exhibition', event_date=date(2023, 9, 20), gallery_id=3)
event4 = Event(name='Summer Style Gala', event_date=date(2023, 6, 30), gallery_id=4)

# Test data for PurchaseOrder
order1 = PurchaseOrder(order_date=date(2023, 4, 10), store_id=1, collection_id=1, total_amount=1000)
order2 = PurchaseOrder(order_date=date(2023, 1, 20), store_id=2, collection_id=2, total_amount=2000)
order3 = PurchaseOrder(order_date=date(2023, 7, 15), store_id=3, collection_id=3, total_amount=1500)
order4 = PurchaseOrder(order_date=date(2023, 8, 25), store_id=4, collection_id=4, total_amount=700)

# Test data for SupplyOrder
supply_order1 = SupplyOrder(order_date=date(2023, 1, 5), supplier_id=1, brand_id=1, total_cost=2500)
supply_order2 = SupplyOrder(order_date=date(2023, 9, 19), supplier_id=2, brand_id=2, total_cost=3500)
supply_order3 = SupplyOrder(order_date=date(2023, 5, 10), supplier_id=3, brand_id=3, total_cost=1500)
supply_order4 = SupplyOrder(order_date=date(2023, 11, 22), supplier_id=4, brand_id=4, total_cost=1200)


session.add_all([brand1, brand2, brand3, brand4, designer1, designer2, designer3, designer4, collection1, collection2, collection3, collection4, gallery1, gallery2, gallery3, gallery4, item1, item2, item3, item4, store1, store2, store3, store4, supplier1, supplier2, supplier3, supplier4, brandDesigner1, brandDesigner2, brandDesigner3, brandDesigner4, warehouse1, warehouse2, warehouse3, warehouse4, event1, event2, event3, event4, order1, order2, order3, order4, supply_order1, supply_order2, supply_order3, supply_order4])
session.commit()
