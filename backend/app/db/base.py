from sqlalchemy.orm import DeclarativeBase

from app.db.mixins import (
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
)


class Base(DeclarativeBase):
    pass


class AppBaseModel(
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    __abstract__ = True