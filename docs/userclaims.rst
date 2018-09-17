Insert User Claims
=====================

.. literalinclude:: ../examples/user_claims.py

.. important:: To make protected query or mutation with auth decorators, we have to make union with
               flask_graphql_auth.AuthInfoField to allow auth decorators return AuthInfoField when a problem occurs.
