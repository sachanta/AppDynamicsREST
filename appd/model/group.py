"""
Model classes for AppDynamics REST API

moduleauthor:: Srikar Achanta <srikar.achanta@appdynamics.com>

"""

from . import JsonObject, JsonList


class Group(JsonObject):

    FIELDS = {'id': '', 'name': '', 'description': '', 'security_provider_type': '', 'roles': None}

    def __init__(self, id='0', name=None, description=None, security_provider_type=None, roles=None):
        self.id, self.name, self.description, self.security_provider_type, self.roles = id, name, description, \
                                                                                        security_provider_type, roles


class Groups(JsonList):
    """
    Represents a collection of :class:Group objects. Extends :class:UserList, so it supports the
    standard array index and :keyword:`for` semantics.
    """

    def __init__(self, initial_list=None):
        super(Groups, self).__init__(Group, initial_list)

    def __getitem__(self, i):
        """
        :rtype: Group
        """
        return self.data[i]

    def by_name(self, name):
        """
        Finds a group by name.

        :returns: First group with the correct name
        :rtype: Group
        """
        found = [x for x in self.data if x.name == name]
        try:
            return found[0]
        except IndexError:
            raise KeyError(name)

    def by_id(self, id):
        """
        Finds a group by id.

        :returns: First group with the correct id
        :rtype: Group
        """
        found = [x for x in self.data if x.id == id]
        try:
            return found[0]
        except IndexError:
            raise KeyError(id)
