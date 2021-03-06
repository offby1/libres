from datetime import datetime
from libres.db.models.types import UTCDateTime
from pytz import timezone
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

    @staticmethod
    def timestamp():
        return datetime.utcnow().replace(tzinfo=timezone('UTC'))

    @declared_attr
    def created(cls):
        return deferred(
            Column(
                UTCDateTime(timezone=False),
                default=cls.timestamp
            )
        )

    @declared_attr
    def modified(cls):
        return deferred(
            Column(
                UTCDateTime(timezone=False),
                onupdate=cls.timestamp
            )
        )
