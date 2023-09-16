from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=25))

    books = relationship('Book', secondary='Book_author')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publication_year = Column(Integer)


book_author = Table('book_author', Base.metadata,
                    Column('book_id', Integer, ForeignKey('books.id')),
                    Column('author_id', Integer, ForeignKey('authors.id'))
                    )
