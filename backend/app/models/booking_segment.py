from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class BookingSegment(Base):
    __tablename__ = "booking_segments"

    id: Mapped[int] = mapped_column(primary_key=True)

    booking_passenger_id: Mapped[int] = mapped_column(
        ForeignKey("booking_passengers.id"),
        nullable=False,
        index=True,
    )

    journey_run_id: Mapped[int] = mapped_column(
        ForeignKey("journey_runs.id"),
        nullable=False,
        index=True,
    )

    seat_id: Mapped[int] = mapped_column(
        ForeignKey("seats.id"),
        nullable=False,
        index=True,
    )

    from_stop_id: Mapped[int] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=False,
    )

    to_stop_id: Mapped[int] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=False,
    )

    booking_passenger: Mapped["BookingPassenger"] = relationship(
        "BookingPassenger",
        back_populates="segments",
    )

    journey_run: Mapped["JourneyRun"] = relationship(
        "JourneyRun",
    )

    seat: Mapped["Seat"] = relationship(
        "Seat",
    )

    from_stop: Mapped["TrainStop"] = relationship(
        "TrainStop",
        foreign_keys=[from_stop_id],
    )

    to_stop: Mapped["TrainStop"] = relationship(
        "TrainStop",
        foreign_keys=[to_stop_id],
    )