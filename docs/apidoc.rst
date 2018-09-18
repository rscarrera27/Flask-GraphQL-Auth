API Documentation
=================
In here you will find the API for everything exposed in this extension.

Configuring Flask-GraphQL-Auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. currentmodule:: flask_graphql_auth

.. module:: flask_graphql_auth

.. autoclass:: GraphQLAuth

   .. automethod:: __init__
   .. automethod:: init_app

Protected query decorators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: query_jwt_required
.. autofunction:: query_jwt_refresh_token_required

Protected mutation decorators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: mutation_jwt_required
.. autofunction:: mutation_jwt_refresh_token_required


Utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: create_access_token
.. autofunction:: create_refresh_token
.. autofunction:: get_raw_jwt
.. autofunction:: get_jwt_identity
.. autofunction:: get_jwt_claims
.. autofunction:: decode_jwt
.. autofunction:: get_jwt_data

Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: AuthInfoField