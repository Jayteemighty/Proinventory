from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import AppBaseModel


class RolePermission(AppBaseModel):
    __tablename__ = "role_permission"

    role_id: Mapped[str] = mapped_column(
        ForeignKey("role.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    permission_id: Mapped[str] = mapped_column(
        ForeignKey("permission.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )