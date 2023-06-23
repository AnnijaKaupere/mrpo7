from app.db import db


class BaseMixin(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Employee(BaseMixin):
    __tablename__ = "VAD_employees"

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    patronymic = db.Column(db.String(30), nullable =False)
    address = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)


class Position(BaseMixin):
    __tablename__ = "VAD_positions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)


class Division(BaseMixin):
    __tablename__ = "VAD_divisions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)


class Job(BaseMixin):
    __tablename__ = "VAD_jobs"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('VAD_employees.id'))
    position_id = db.Column(db.Integer, db.ForeignKey('VAD_positions.id'))
    division_id = db.Column(db.Integer, db.ForeignKey('VAD_divisions.id'))
    date_of_employment = db.Column(db.Date, nullable=False)
    date_of_dismissal = db.Column(db.Date)
