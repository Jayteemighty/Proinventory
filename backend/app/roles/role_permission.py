from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class RolePermission(Base):
    __tablename__ = "role_permission"

    role_id: Mapped[str] = mapped_column(
        ForeignKey("role.id", ondelete="CASCADE"),
        primary_key=True,
    )

    permission_id: Mapped[str] = mapped_column(
        ForeignKey("permission.id", ondelete="CASCADE"),
        primary_key=True,
    )