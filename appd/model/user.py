"""
Model classes for AppDynamics REST API

moduleauthor:: Srikar Achanta <srikar.achanta@appdynamics.com>

"""

from . import JsonObject, JsonList


class User(JsonObject):

    FIELDS = {'id': '', 'name': '', 'displayName': '', 'email': '', 'security_provider_type': '', 'roles': None,
              'groups': None}

    def __init__(self, id='0', name=None, displayName=None, email=None, security_provider_type=None, roles=None,
                 groups=None):
        self.id, self.name, self.displayName, self.email, self.security_provider_type, self.roles, self.groups = \
            id, name, displayName, email, security_provider_type, roles, groups


class Users(JsonList):
    """
        Represents a collection of :class:User objects. Extends :class:UserList, so it supports the
        standard array index and :keyword:`for` semantics.
        """

    def __init__(self, initial_list=None):
        super(Users, self).__init__(User, initial_list)

    def __getitem__(self, i):
        """
        :rtype: User
        """
        return self.data[i]

    def by_name(self, name):
        """
        Finds a user by name.

        :returns: First user with the correct name
        :rtype: User
        """
        found = [x for x in self.data if x.name == name]
        try:
            return found[0]
        except IndexError:
            raise KeyError(name)

    def by_id(self, id):
        """
        Finds a user by id.

        :returns: First user with the correct id
        :rtype: User
        """
        found = [x for x in self.data if x.id == id]
        try:
            return found[0]
        except IndexError:
            raise KeyError(id)
