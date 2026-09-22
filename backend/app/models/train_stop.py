from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, UniqueConstraint

from app.core.database import Base
from app.utils.time import utc_now


class TrainStop(Base):
    __tablename__ = "train_stops"

    __table_args__ = (
        UniqueConstraint(
            "route_id",
            "stop_sequence",
            name="uq_train_stops_route_sequence",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id"),
        nullable=False,
        index=True,
    )

    station_id: Mapped[int] = mapped_column(
        ForeignKey("stations.id"),
        nullable=False,
        index=True,
    )

    stop_sequence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    arrival_offset_minutes: Mapped[int | None] = mapped_column(
        Integer
    )

    departure_offset_minutes: Mapped[int | None] = mapped_column(
        Integer
    )

    distance_from_origin_km: Mapped[Decimal | None] = mapped_column(
        Numeric(8, 2)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    route: Mapped["Route"] = relationship(
        "Route",
        back_populates="stops",
    )

    station: Mapped["Station"] = relationship(
        "Station",
    )