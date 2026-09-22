from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class FareRule(Base):
    __tablename__ = "fare_rules"

    id: Mapped[int] = mapped_column(primary_key=True)

    coach_class_id: Mapped[int] = mapped_column(
        ForeignKey("coach_classes.id"),
        nullable=False,
        index=True,
    )

    rate_per_km: Mapped[Decimal] = mapped_column(
        Numeric(8, 2),
        nullable=False,
    )

    minimum_fare: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    effective_from: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    effective_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
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

    coach_class: Mapped["CoachClass"] = relationship(
        "CoachClass",
    )