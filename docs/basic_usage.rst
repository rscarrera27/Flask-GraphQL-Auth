Basic Usage
===============

.. literalinclude:: ../examples/basic.py

.. important:: To make protected query or mutation with auth decorators, we have to make union with
               flask_graphql_auth.AuthInfoField to allow auth decorators return AuthInfoField when a problem occurs.
               Also, If you want to assign union to mutation, you have to override resolve_type

To get token with auth mutation try this query::

   mutation {
      auth(password:<any word>, username: <any word>){
      accessToken
      refreshToken
      }
   }


To access a jwt_required protected query or mutation , all we have to do is send in the JWT in the query.
By default, this is done with an mutation or query argument that looks like::

   {
     protected(message:"hello", token:<access token>)
   }
