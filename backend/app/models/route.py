from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(primary_key=True)

    train_id: Mapped[int] = mapped_column(
        ForeignKey("trains.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str | None] = mapped_column(
        String(150)
    )

    direction: Mapped[str | None] = mapped_column(
        String(20)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    train: Mapped["Train"] = relationship(
        "Train",
        back_populates="routes",
    )

    stops: Mapped[list["TrainStop"]] = relationship(
        "TrainStop",
        back_populates="route",
        cascade="all, delete-orphan",
        order_by="TrainStop.stop_sequence",
    )

    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule",
        back_populates="route",
    )