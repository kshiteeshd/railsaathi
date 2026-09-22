from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class Train(Base):
    __tablename__ = "trains"

    id: Mapped[int] = mapped_column(primary_key=True)

    train_number: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    train_type: Mapped[str | None] = mapped_column(
        String(50)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )

    routes: Mapped[list["Route"]] = relationship(
        "Route",
        back_populates="train",
        cascade="all, delete-orphan",
    )

    coaches: Mapped[list["Coach"]] = relationship(
        "Coach",
        back_populates="train",
        cascade="all, delete-orphan",
    )

    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule",
        back_populates="train",
    )