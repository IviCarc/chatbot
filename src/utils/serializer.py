from sqlalchemy.inspection import inspect

class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        # attributes = {}
        # for attribute_name in inspect(self).attrs.keys():
        #     attribute_value = getattr(self, attribute_name)
        #     attributes[attribute_name] = attribute_value
        # return attributes

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
