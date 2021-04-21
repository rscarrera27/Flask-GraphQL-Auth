.. _Configuration Options:

Configuration Options
=====================

You can change many options for how this extension works via

.. code-block:: python

  app.config[OPTION_NAME] = new_option_value

Options:
~~~~~~~~~~~~~~~~

================================= =================================================
``JWT_TOKEN_ARGUMENT_NAME``        Where to look for a JWT in resolver argument
``JWT_ACCESS_TOKEN_EXPIRES``       How long an access token should live before
                                   it expires. This takes a ``datetime.timedelta``
                                   or an ``int``, and defaults to 15 minutes. Can
                                   be set to ``False`` to disable expiration.
                                   If this value is an ``int`` it will be parsed
                                   as minutes.
``JWT_REFRESH_TOKEN_EXPIRES``      How long a refresh token should live before
                                   it expires. This takes a ``datetime.timedelta``
                                   or an ``int``, and defaults to 30 days. Can
                                   be set to ``False`` to disable expiration.
                                   If this value is an ``int`` it will be parsed
                                   as days.
``JWT_SECRET_KEY``                 The secret key needed for symmetric based signing
                                   algorithms, such as ``HS*``. If this is not set,
                                   we use the flask ``SECRET_KEY`` value instead.
``JWT_IDENTITY_CLAIM``             Claim in the tokens that is used as source of identity.
                                   For interoperability, the JWT RFC recommends using
                                   ``'sub'``. Defaults to ``'identity'`` for legacy reasons.
``JWT_USER_CLAIMS``                Claim in the tokens that is used to store user claims.
                                   Defaults to ``'user_claims'``.
================================= =================================================
