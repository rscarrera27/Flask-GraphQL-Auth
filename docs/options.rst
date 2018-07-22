.. _Configuration Options:

Configuration Options
=====================

You can change many options for how this extension works via

.. code-block:: python

  app.config[OPTION_NAME] = new_options

Options:
~~~~~~~~~~~~~~~~

.. tabularcolumns:: |p{6cm}|p{7cm}|

================================= =========================================
``JWT_TOKEN_ARGUMENT_NAME``       Where to look for a JWT in resolver argument
``JWT_ACCESS_TOKEN_EXPIRES``      How long an access token should live before it expires. This
                                  takes a ``datetime.timedelta``, and defaults to 15 minutes.
                                  Can be set to ``False`` to disable expiration.
``JWT_REFRESH_TOKEN_EXPIRES``     How long a refresh token should live before it expires. This
                                  takes a ``datetime.timedelta``, and defaults to 30 days.
                                  Can be set to ``False`` to disable expiration.
``JWT_SECRET_KEY``                The secret key needed for symmetric based signing algorithms,
                                  such as ``HS*``. If this is not set, we use the
                                  flask ``SECRET_KEY`` value instead.
``JWT_IDENTITY_CLAIM``            Claim in the tokens that is used as source of identity.
                                  For interoperability, the JWT RFC recommends using ``'sub'``.
                                  Defaults to ``'identity'`` for legacy reasons.
``JWT_USER_CLAIMS``               Claim in the tokens that is used to store user claims.
                                  Defaults to ``'user_claims'``.
================================= =========================================
