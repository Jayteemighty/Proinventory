from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AppBaseModel


class Role(AppBaseModel):
    __tablename__ = "role"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_system: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )

    permissions = relationship(
        "Permission",
        secondary="role_permission",
        back_populates="roles",
    )