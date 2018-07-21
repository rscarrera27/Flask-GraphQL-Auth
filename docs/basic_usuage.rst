Basic Usuage
===============

.. literalinclude:: ../examples/basic.py

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
