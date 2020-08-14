"""
Model classes for AppDynamics REST API

moduleauthor:: Srikar Achanta <srikar.achanta@appdynamics.com>

"""

from . import JsonObject, JsonList


class Role(JsonObject):

    FIELDS = {'id': '', 'name': '', 'description': ''}
    # FIELDS = {'id': '', 'name': ''}

    def __init__(self, id='0', name=None, description=None):
        self.id, self.name, self.description = id, name, description


class Roles(JsonList):
    """
    Represents a collection of :class:Role objects. Extends :class:UserList, so it supports the
    standard array index and :keyword:`for` semantics.
    """

    def __init__(self, initial_list=None):
        super(Roles, self).__init__(Role, initial_list)

    def __getitem__(self, i):
        """
        :rtype: Role
        """
        return self.data[i]

    def by_name(self, name):
        """
        Finds a role by name.

        :returns: First role with the correct name
        :rtype: Role
        """
        found = [x for x in self.data if x.name == name]
        try:
            return found[0]
        except IndexError:
            raise KeyError(name)

    def by_id(self, id):
        """
        Finds a role by id.

        :returns: First role with the correct id
        :rtype: Role
        """
        found = [x for x in self.data if x.id == id]
        try:
            return found[0]
        except IndexError:
            raise KeyError(id)
