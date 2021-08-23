from graphene import ObjectType, String

class SubProductPayee(ObjectType):
    human_name = String(description="The human readable name of the payee, for example 'Super Project'")
    machine_name = String(description="The machine readable name of the payee, for example 'superproject'")
