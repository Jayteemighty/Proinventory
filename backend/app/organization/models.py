from sqlalchemy import Boolean, String

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import (
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
)


class Organization(
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    __tablename__ = "organization"

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(30),
    )

    address: Mapped[str] = mapped_column(
        String(255),
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="NGN",
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="Africa/Lagos",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )