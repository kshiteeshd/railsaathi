from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)

    booking_reference: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    journey_run_id: Mapped[int] = mapped_column(
        ForeignKey("journey_runs.id"),
        nullable=False,
        index=True,
    )

    source_stop_id: Mapped[int] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=False,
    )

    destination_stop_id: Mapped[int] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=False,
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="CONFIRMED",
    )

    booked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    user: Mapped["User"] = relationship(
        "User",
    )

    journey_run: Mapped["JourneyRun"] = relationship(
        "JourneyRun",
    )

    source_stop: Mapped["TrainStop"] = relationship(
        "TrainStop",
        foreign_keys=[source_stop_id],
    )

    destination_stop: Mapped["TrainStop"] = relationship(
        "TrainStop",
        foreign_keys=[destination_stop_id],
    )

    passengers: Mapped[list["BookingPassenger"]] = relationship(
        "BookingPassenger",
        back_populates="booking",
        cascade="all, delete-orphan",
    )