"""
Model classes for AppDynamics REST API

.. moduleauthor:: Srikar Achanta <srikar.achanta@appdynamics.com>
"""

from . import JsonObject, JsonList


class User(JsonObject):

    # FIELDS = {'id': '', 'name': '', 'displayName': '', 'security_provider_type': '', 'email': ''}
    #
    # def __init__(self, id='0', name=None, displayName=None, security_provider_type=None, email=None):
    #     self.id, self.name, self.displayName, self.security_provider_type, self.email \
    #         = id, name, displayName, security_provider_type, email

    FIELDS = {'id': '', 'name': ''}

    def __init__(self, id='0', name=None):
        self.id, self.name = id, name


class Users(JsonList):

    def __init__(self, initial_list=None):
        super(Users, self).__init__(User, initial_list)

    def __getitem__(self, i):
        """
        :rtype: User
        """
        return self.data[i]
