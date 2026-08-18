from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserPermission(Base):
    __tablename__ = "user_permission"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    permission_id: Mapped[str] = mapped_column(
        ForeignKey("permission.id", ondelete="CASCADE"),
        primary_key=True,
    )