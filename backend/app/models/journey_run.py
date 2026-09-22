from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class JourneyRun(Base):
    __tablename__ = "journey_runs"

    __table_args__ = (
        UniqueConstraint(
            "schedule_id",
            "journey_date",
            name="uq_journey_runs_schedule_date",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    schedule_id: Mapped[int] = mapped_column(
        ForeignKey("schedules.id"),
        nullable=False,
        index=True,
    )

    journey_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="SCHEDULED",
    )

    current_stop_id: Mapped[int | None] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=True,
    )

    next_stop_id: Mapped[int | None] = mapped_column(
        ForeignKey("train_stops.id"),
        nullable=True,
    )

    delay_minutes: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    actual_departure: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    actual_arrival: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
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

    schedule: Mapped["Schedule"] = relationship(
        "Schedule",
        back_populates="journey_runs",
    )

    current_stop: Mapped["TrainStop | None"] = relationship(
        "TrainStop",
        foreign_keys=[current_stop_id],
    )

    next_stop: Mapped["TrainStop | None"] = relationship(
        "TrainStop",
        foreign_keys=[next_stop_id],
    )