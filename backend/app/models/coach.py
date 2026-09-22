from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.utils.time import utc_now


class Coach(Base):
    __tablename__ = "coaches"

    __table_args__ = (
        UniqueConstraint(
            "train_id",
            "coach_number",
            name="uq_coaches_train_number",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    train_id: Mapped[int] = mapped_column(
        ForeignKey("trains.id"),
        nullable=False,
        index=True,
    )

    coach_class_id: Mapped[int] = mapped_column(
        ForeignKey("coach_classes.id"),
        nullable=False,
        index=True,
    )

    coach_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    position: Mapped[int | None] = mapped_column(
        Integer
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
        back_populates="coaches",
    )

    coach_class: Mapped["CoachClass"] = relationship(
        "CoachClass",
        back_populates="coaches",
    )

    seats: Mapped[list["Seat"]] = relationship(
        "Seat",
        back_populates="coach",
        cascade="all, delete-orphan",
    )
