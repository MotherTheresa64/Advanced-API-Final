# app/service_ticket/schemas.py

from app import ma
from app.models import ServiceTicket
from app.mechanic.schemas import MechanicSchema


class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        include_fk = True
        include_relationships = True   # enable relationship fields
        load_instance = True

    # explicitly nest mechanics so they appear in the output
    mechanics = ma.Nested(MechanicSchema, many=True, dump_only=True)


service_ticket_schema = ServiceTicketSchema()
service_tickets_schema = ServiceTicketSchema(many=True)
