#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from os import environ
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:

    """ Engine """
    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        user = environ["HBNB_MYSQL_USER"]
        passw = environ["HBNB_MYSQL_PWD"]
        lc = environ["HBNB_MYSQL_HOST"]
        db = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}',
                                      pool_pre_ping=True
                                      .format(user, passw, lc, nm_dt))
        if environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        objs = {}
        if not cls:
            consulta = self.__session.query(User, State, City, Amenity,
                                            Placey, Review).all()
            for obj in consulta:
                name_cl = type(obj).__name__ + "." + str(obj.id)
                objs[name_cl] = obj
            return objs

        else:
            consulta1 = self.__session.query(cls).all()
        for obj in consulta1:
            name_cl = type(obj).__name__ + "." + str(obj.id)
            objs[name_cl] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit changes in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and
        create the current database session"""
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(s_factory)
        self.__session = Session()
