from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('postgresql:///catalog', echo=True)
Base = declarative_base()


class Category(Base):
    # Define table schema
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # Define relationship to Item class
    items = relationship('Item', back_populates='category')

    def __repr__(self):
        return 'id: {}, name: {}, items: {}'.format(
            self.id, self.name, self.items)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'items': ([i.serialize() for i in self.items]),
            }


class Item(Base):
    # Define table schema
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    cat_id = Column(Integer, ForeignKey('categories.id'))
    # Define relationship to Category class
    category = relationship('Category', back_populates='items')

    def __repr__(self):
        return 'id: {}, title: {}, description: {}, cat_id: {}'.format(
            self.id, self.title, self.description, self.cat_id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'cat_id': self.cat_id,
            }


Session = sessionmaker(bind=engine)
session = Session()
