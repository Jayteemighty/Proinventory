from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AppBaseModel

if TYPE_CHECKING:
    from app.organization.models import Organization
    from app.department.models import Department
    from app.roles.models import Role
    from app.permissions.models import Permission


class User(AppBaseModel):
    __tablename__ = "users"

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organization.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    department_id: Mapped[str | None] = mapped_column(
        ForeignKey("department.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    role_id: Mapped[str | None] = mapped_column(
        ForeignKey("role.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    position: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    organization: Mapped["Organization"] = relationship(
        "Organization",
    )

    department: Mapped["Department | None"] = relationship(
        "Department",
    )

    role: Mapped["Role | None"] = relationship(
        "Role",
    )

    permissions: Mapped[list["Permission"]] = relationship(
        "Permission",
        secondary="user_permission",
    )