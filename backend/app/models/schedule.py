from datetime import datetime, time

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)

    train_id: Mapped[int] = mapped_column(
        ForeignKey("trains.id"),
        nullable=False,
        index=True,
    )

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id"),
        nullable=False,
        index=True,
    )

    departure_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    arrival_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    operating_days: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
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

    train: Mapped["Train"] = relationship(
        "Train",
        back_populates="schedules",
    )

    route: Mapped["Route"] = relationship(
        "Route",
        back_populates="schedules",
    )

    journey_runs: Mapped[list["JourneyRun"]] = relationship(
        "JourneyRun",
        back_populates="schedule",
        cascade="all, delete-orphan",
    )