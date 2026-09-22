from datetime import date
from decimal import Decimal

from sqlalchemy import select

from app.core.database import SessionLocal
from app.models import CoachClass, FareRule, Role


def seed_roles(db):
    roles = [
        {
            "name": "USER",
            "description": "Regular Rail Saathi user",
        },
        {
            "name": "ADMIN",
            "description": "Rail Saathi administrator",
        },
    ]

    for role_data in roles:
        existing = db.scalar(
            select(Role).where(Role.name == role_data["name"])
        )

        if not existing:
            db.add(Role(**role_data))


def seed_coach_classes(db):
    classes = [
        {
            "code": "1A",
            "name": "AC First Class",
            "description": "Air-conditioned first class",
            "seat_layout_type": "CABIN",
            "default_fare_multiplier": Decimal("1.00"),
        },
        {
            "code": "2A",
            "name": "AC 2 Tier",
            "description": "Air-conditioned 2-tier sleeper",
            "seat_layout_type": "BERTH",
            "default_fare_multiplier": Decimal("1.00"),
        },
        {
            "code": "3A",
            "name": "AC 3 Tier",
            "description": "Air-conditioned 3-tier sleeper",
            "seat_layout_type": "BERTH",
            "default_fare_multiplier": Decimal("1.00"),
        },
        {
            "code": "SL",
            "name": "Sleeper",
            "description": "Non-air-conditioned sleeper",
            "seat_layout_type": "BERTH",
            "default_fare_multiplier": Decimal("1.00"),
        },
        {
            "code": "CC",
            "name": "Chair Car",
            "description": "Air-conditioned chair car",
            "seat_layout_type": "CHAIR",
            "default_fare_multiplier": Decimal("1.00"),
        },
    ]

    for class_data in classes:
        existing = db.scalar(
            select(CoachClass).where(
                CoachClass.code == class_data["code"]
            )
        )

        if not existing:
            db.add(CoachClass(**class_data))


def seed_fare_rules(db):
    fare_rules = [
        {
            "code": "1A",
            "rate_per_km": Decimal("3.50"),
            "minimum_fare": Decimal("500.00"),
        },
        {
            "code": "2A",
            "rate_per_km": Decimal("2.50"),
            "minimum_fare": Decimal("350.00"),
        },
        {
            "code": "3A",
            "rate_per_km": Decimal("1.80"),
            "minimum_fare": Decimal("250.00"),
        },
        {
            "code": "SL",
            "rate_per_km": Decimal("1.00"),
            "minimum_fare": Decimal("150.00"),
        },
        {
            "code": "CC",
            "rate_per_km": Decimal("1.40"),
            "minimum_fare": Decimal("200.00"),
        },
    ]

    for fare_data in fare_rules:
        coach_class = db.scalar(
            select(CoachClass).where(
                CoachClass.code == fare_data["code"]
            )
        )

        if not coach_class:
            continue

        existing = db.scalar(
            select(FareRule).where(
                FareRule.coach_class_id == coach_class.id,
                FareRule.effective_from == date.today(),
            )
        )

        if not existing:
            db.add(
                FareRule(
                    coach_class_id=coach_class.id,
                    rate_per_km=fare_data["rate_per_km"],
                    minimum_fare=fare_data["minimum_fare"],
                    effective_from=date.today(),
                )
            )


def seed_database():
    db = SessionLocal()

    try:
        seed_roles(db)
        seed_coach_classes(db)

        db.flush()

        seed_fare_rules(db)

        db.commit()

        print("Database seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()