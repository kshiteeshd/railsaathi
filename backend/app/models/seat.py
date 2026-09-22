from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Seat(Base):
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(primary_key=True)

    coach_id: Mapped[int] = mapped_column(
        ForeignKey("coaches.id"),
        nullable=False,
        index=True,
    )

    seat_number: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    seat_type: Mapped[str | None] = mapped_column(
        String(30)
    )

    row_number: Mapped[int | None] = mapped_column(
        Integer
    )

    column_number: Mapped[int | None] = mapped_column(
        Integer
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    coach: Mapped["Coach"] = relationship(
        "Coach",
        back_populates="seats",
    )