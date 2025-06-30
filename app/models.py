from . import db

mechanic_service = db.Table(
    'mechanic_service',
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id')),
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id'))
)

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    service_tickets = db.relationship(
        'ServiceTicket',
        secondary=mechanic_service,
        back_populates='mechanics'
    )

class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    is_open = db.Column(db.Boolean, default=True)
    mechanics = db.relationship(
        'Mechanic',
        secondary=mechanic_service,
        back_populates='service_tickets'
    )
