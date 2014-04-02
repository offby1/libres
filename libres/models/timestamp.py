import arrow

from sqlalchemy import types
from sqlalchemy.orm import deferred
from sqlalchemy.schema import Column
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin(object):
    """ Mixin providing created/modified timestamps for all records. Pretty
    much relies on the database being Postgresql but could be made to work
    with others.

    The columns are deferred loaded as this is primarily for logging and future
    forensics.

    """

    @declared_attr
    def created(cls):
        return deferred(
            Column(
                types.DateTime(timezone=True),
                default=arrow.utcnow().datetime
            )
        )

    @declared_attr
    def modified(cls):
        return deferred(
            Column(
                types.DateTime(timezone=True),
                onupdate=arrow.utcnow().datetime
            )
        )
