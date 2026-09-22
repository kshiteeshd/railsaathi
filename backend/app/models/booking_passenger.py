from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class BookingPassenger(Base):
    __tablename__ = "booking_passengers"

    id: Mapped[int] = mapped_column(primary_key=True)

    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.id"),
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
    )

    seat_preference: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="NO_PREFERENCE",
    )

    seat_id: Mapped[int | None] = mapped_column(
        ForeignKey("seats.id"),
        nullable=True,
    )

    fare: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="CONFIRMED",
    )

    booking: Mapped["Booking"] = relationship(
        "Booking",
        back_populates="passengers",
    )

    seat: Mapped["Seat | None"] = relationship(
        "Seat",
    )

    segments: Mapped[list["BookingSegment"]] = relationship(
        "BookingSegment",
        back_populates="booking_passenger",
        cascade="all, delete-orphan",
    )