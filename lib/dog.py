from models import Base, Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///dogs.db')

Session = sessionmaker(bind=engine)

session = Session()


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    
def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()
    

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.like(id)).first()
    

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name).filter(Dog.breed == breed).first()
    pass

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({"breed": breed})
    pass