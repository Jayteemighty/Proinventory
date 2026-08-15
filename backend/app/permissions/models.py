from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import AppBaseModel

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.roles.models import Role


class Permission(AppBaseModel):
    __tablename__ = "permission"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    module: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    roles: Mapped[list["Role"]] = relationship(
        "Role",
        secondary="role_permission",
        back_populates="permissions",
    )