from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AppBaseModel


class Department(AppBaseModel):
    __tablename__ = "department"

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organization.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    organization = relationship(
        "Organization",
        back_populates="departments",
    )