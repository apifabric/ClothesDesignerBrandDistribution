# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 16, 2024 19:32:05
# Database: sqlite:////tmp/tmp.CkpILSE81U-01JCV7AVM9T6SE7KK2XEAKGQYH/ClothesDesignerBrandDistribution/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Brand(SAFRSBaseX, Base):
    """
    description: Represents a designer brand providing clothing lines.
    """
    __tablename__ = 'brands'
    _s_collection_name = 'Brand'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    BrandDesignerList : Mapped[List["BrandDesigner"]] = relationship(back_populates="brand")
    CollectionList : Mapped[List["Collection"]] = relationship(back_populates="brand")
    SupplyOrderList : Mapped[List["SupplyOrder"]] = relationship(back_populates="brand")



class Designer(SAFRSBaseX, Base):
    """
    description: Represents individual designers who create styles.
    """
    __tablename__ = 'designers'
    _s_collection_name = 'Designer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    speciality = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    BrandDesignerList : Mapped[List["BrandDesigner"]] = relationship(back_populates="designer")



class Gallery(SAFRSBaseX, Base):
    """
    description: Location where collections are showcased.
    """
    __tablename__ = 'galleries'
    _s_collection_name = 'Gallery'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    capacity = Column(Integer)
    established_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    EventList : Mapped[List["Event"]] = relationship(back_populates="gallery")



class Store(SAFRSBaseX, Base):
    """
    description: Retail stores selling collections.
    """
    __tablename__ = 'stores'
    _s_collection_name = 'Store'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    PurchaseOrderList : Mapped[List["PurchaseOrder"]] = relationship(back_populates="store")



class Supplier(SAFRSBaseX, Base):
    """
    description: Supply chain partners providing materials.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    material_type = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyOrderList : Mapped[List["SupplyOrder"]] = relationship(back_populates="supplier")



class Warehouse(SAFRSBaseX, Base):
    """
    description: Warehouse for storing collections and items.
    """
    __tablename__ = 'warehouses'
    _s_collection_name = 'Warehouse'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    max_capacity = Column(Integer)
    temperature_control = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)



class BrandDesigner(SAFRSBaseX, Base):
    """
    description: Association between brands and designers.
    """
    __tablename__ = 'brand_designers'
    _s_collection_name = 'BrandDesigner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    brand_id = Column(ForeignKey('brands.id'), nullable=False)
    designer_id = Column(ForeignKey('designers.id'), nullable=False)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("BrandDesignerList"))
    designer : Mapped["Designer"] = relationship(back_populates=("BrandDesignerList"))

    # child relationships (access children)



class Collection(SAFRSBaseX, Base):
    """
    description: Represents a collection of clothing items under a brand.
    """
    __tablename__ = 'collections'
    _s_collection_name = 'Collection'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    brand_id = Column(ForeignKey('brands.id'), nullable=False)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("CollectionList"))

    # child relationships (access children)
    ItemList : Mapped[List["Item"]] = relationship(back_populates="collection")
    PurchaseOrderList : Mapped[List["PurchaseOrder"]] = relationship(back_populates="collection")



class Event(SAFRSBaseX, Base):
    """
    description: Brand events showcasing collections.
    """
    __tablename__ = 'events'
    _s_collection_name = 'Event'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    event_date = Column(DateTime, nullable=False)
    gallery_id = Column(ForeignKey('galleries.id'), nullable=False)

    # parent relationships (access parent)
    gallery : Mapped["Gallery"] = relationship(back_populates=("EventList"))

    # child relationships (access children)



class SupplyOrder(SAFRSBaseX, Base):
    """
    description: Orders placed by brands to suppliers.
    """
    __tablename__ = 'supply_orders'
    _s_collection_name = 'SupplyOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    brand_id = Column(ForeignKey('brands.id'), nullable=False)
    total_cost = Column(Integer)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("SupplyOrderList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplyOrderList"))

    # child relationships (access children)



class Item(SAFRSBaseX, Base):
    """
    description: Represents individual clothing items within a collection.
    """
    __tablename__ = 'items'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    item_type = Column(String, nullable=False)
    price = Column(Integer)
    release_date = Column(DateTime, nullable=False)
    collection_id = Column(ForeignKey('collections.id'), nullable=False)

    # parent relationships (access parent)
    collection : Mapped["Collection"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)



class PurchaseOrder(SAFRSBaseX, Base):
    """
    description: Orders placed by stores for collection items.
    """
    __tablename__ = 'purchase_orders'
    _s_collection_name = 'PurchaseOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    store_id = Column(ForeignKey('stores.id'), nullable=False)
    collection_id = Column(ForeignKey('collections.id'), nullable=False)
    total_amount = Column(Integer)

    # parent relationships (access parent)
    collection : Mapped["Collection"] = relationship(back_populates=("PurchaseOrderList"))
    store : Mapped["Store"] = relationship(back_populates=("PurchaseOrderList"))

    # child relationships (access children)
