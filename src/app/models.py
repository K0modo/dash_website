from .server import db
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class Claims(db.Model):
    __tablename__ = 't_claims'

    claim_trans: db.Mapped[int] = db.mapped_column(primary_key=True)
    claim_id: db.Mapped[int]
    claim_item: db.Mapped[int]
    mem_acct_id: db.Mapped[int]
    injury_disease_id: db.Mapped [int] = db.mapped_column(ForeignKey("t_injury_disease.id"), nullable=False)
    specialty_id: db.Mapped[int] = db.mapped_column(ForeignKey("t_specialty.id"), nullable=False)
    facility_id: db.Mapped[int] = db.mapped_column(ForeignKey("t_facility.id"), nullable=False)

    # payment: db.Mapped[int] = db.relationship('ClaimsPaid', backref= backref('t_claims'))

    payments = db.relationship("ClaimsPaid", backref=db.backref("t_claims"), cascade="all, delete-orphan")

    # Declare relationship between the 2 classes involved
    # Relationship() is a function that allows ORM mapped classes to refer to each other
    # Relationship() defines an abstraction on top of database foreign keys which indicate how table rows can refer
    # to each other


    def __repr__(self):
        return (
            f"Claims (claim_trans={self.claim_trans!r}, "
            f"claim_id={self.claim_id!r}, claim_item={self.claim_item!r}, mem_acct_id={self.mem_acct_id!r}, "
            f"injury_disease={self.injury_disease_id!r},"
            f" specialty_id={self.specialty_id!r}, facility_id={self.facility_id!r}"
        )


class ClaimsPaid(db.Model):
    __tablename__ = "t_claims_paid"

    pay_trans: db.Mapped[str] =db.mapped_column(primary_key=True)
    claim_trans_id: db.Mapped[int] = db.mapped_column(ForeignKey("t_claims.claim_trans"), nullable=False)
    charge_allowed: db.Mapped[float]
    deduct_copay: db.Mapped[float]
    charge_paid_ins: db.Mapped[float]
    charge_trans_date: db.Mapped[datetime]
    period: db.Mapped[int]
    quarter: db.Mapped[str]


    def __repr__(self):
        return (
            f"ClaimsPaid (pay_trans={self.pay_trans!r}, claim_trans={self.claim_trans_id!r}, charge_allowed={self.charge_allowed!r}, "
            f"deduct_copay={self.deduct_copay!r}, charge_paid_ins= {self.charge_paid_ins!r}, charge_trans_date={self.charge_trans_date!r}, "
            f"period={self.period!r}, quarter={self.quarter!r}"
        )


class InjuryDisease(db.Model):
    __tablename__ = 't_injury_disease'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    category: db.Mapped[str]
    color_code: db.Mapped[str]

    claims = db.relationship('Claims', backref=db.backref('t_injury_disease'),
                          cascade="all, delete-orphan")

    def __repr__(self):
        return  (
            f"InjuryDisease (Id = {self.id!r}, Name = {self.name!r}, Category = {self.category!r}, Color Code = "
            f"{self.color_code!r}"
        )


"""
Mapping Foreign Key & Relationship

Claims:
injury_disease_id: db.Mapped[int] = db.mapped_column(ForeignKey("t_injury_disease.id"), nullable=False)

Injury_Disease:
claims = relationship('Claims', backref=backref('t_injury_disease'), cascade="all, delete-orphan")
"""


class Specialty(db.Model):
    __tablename__ = 't_specialty'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    category: db.Mapped[str]
    color_code: db.Mapped[str]

    claims = db.relationship('Claims', backref=db.backref('t_specialty'),
                             cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"Specialty (Id = {self.id!r}, Name = {self.name!r}, Category = {self.category!r}, Color Code = "
            f"{self.color_code!r}"
        )


class Facility(db.Model):
    __tablename__ = 't_facility'

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    category: db.Mapped[str]
    color_code: db.Mapped[str]

    claims = db.relationship('Claims', backref=db.backref('t_facility'),
                             cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"Facility (Id = {self.id!r}, Name = {self.name!r}, Category = {self.category!r}, Color Code = "
            f"{self.color_code!r}"
        )


class DailyClaims(db.Model):
    __tablename__ = 'v_daily_claims'

    charge_trans_date: db.Mapped[datetime] = db.mapped_column(primary_key=True)
    period: db.Mapped[int]
    claims_count: db.Mapped[int]
    charges_paid: db.Mapped[float]

    # def __repr__(self):
    #     return (
    #         f"ClaimsPaid  Date: {self.charge_trans_date!r}  Period: {self.period!r},   "
    #         f"Claims_Count: {self.claims_count!r}  Claims_Paid: {self.charges_paid!r}"
    #     )

class DailyMember(db.Model):
    __tablename__ = 'v_daily_member'

    charge_trans_date: db.Mapped[datetime] = db.mapped_column(primary_key=True)
    period: db.Mapped[int]
    member_count: db.Mapped[int]

    # def __repr__(self):
    #     return (
    #         f"ClaimsPaid  Date: {self.charge_trans_date!r}  Period: {self.period!r},   "
    #         f"Claims_Count: {self.member_count!r} "
    #     )


class PeriodSummary(db.Model):
    __tablename__ = 'v_period_summary'

    period: db.Mapped[int] = db.mapped_column(primary_key=True)
    day_count: db.Mapped[int]
    claims_period_count: db.Mapped[float]
    claims_daily_avg: db.Mapped[float]
    claims_period_paid: db.Mapped[float]
    claims_paid_daily_avg: db.Mapped[float]
    claims_period_count_cum: db.Mapped[float]
    claims_period_average_cum: db.Mapped[float]
    claims_period_paid_cum: db.Mapped[float]
    claims_period_paid_average_cum: db.Mapped[float]


    # def __repr__(self):
    #     return (
    #         f"Period Summary  Period: {self.period!r}  Day Count: {self.day_count!r}   "
    #         f"Sum Claim Count: {self.claims_period_count!r}  Daily Average: {self.claims_daily_avg!r}  "
    #         f"Cum Claims: {self.claims_period_count_cum!r}  Cum Claims Average: {self.claims_period_average_cum!r} "
    #         f"Cum Paid : {self.claims_period_paid_cum!r}  Cum Paid Average : {self.claims_period_paid_average_cum!r}"
    #     )


class PeriodMember(db.Model):
    __tablename__ = 'v_member_period_stats'

    period: db.Mapped[int] = db.mapped_column(primary_key=True)
    mem_acct_id: db.Mapped[int]
    claims_member: db.Mapped[int]
    charges_member: db.Mapped[float]


class MemberSummary(db.Model):
    __tablename__ = 'v_member_summary'

    period: db.Mapped[int] = db.mapped_column(primary_key=True)
    daily_member_avg: db.Mapped[float]
    daily_member_sum: db.Mapped[int]
    annual_ytd_avg: db.Mapped[float]


class InjuryDiseaseSummary(db.Model):
    __tablename__ = 'v_injury_disease_summary'

    injury_disease_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_paid: db.Mapped[float]
    color_code: db.Mapped[str]


class InjuryDiseaseRacing(db.Model):
    __tablename__ = 'v_icd_racing'

    injury_disease_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    period: db.Mapped[int]
    color_code: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_count_ytd: db.Mapped[float]


class SpecialtySummary(db.Model):
    __tablename__ = 'v_specialty_summary'

    specialty_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_paid: db.Mapped[float]
    color_code: db.Mapped[str]


class SpecialtyRacing(db.Model):
    __tablename__ = 'v_specialty_racing'

    specialty_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    period: db.Mapped[int]
    color_code: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_count_ytd: db.Mapped[float]


class FacilitySummary(db.Model):
    __tablename__ = 'v_facility_summary'

    facility_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_paid: db.Mapped[float]
    color_code: db.Mapped[str]


class FacilityRacing(db.Model):
    __tablename__ = 'v_facility_racing'

    facility_id: db.Mapped[int] = db.mapped_column(primary_key=True)
    name: db.Mapped[str]
    period: db.Mapped[int]
    color_code: db.Mapped[str]
    claim_count: db.Mapped[int]
    claim_count_ytd: db.Mapped[float]

class ConsolidatedCodes(db.Model):
    __tablename__ = 'v_consolidated_codes'

    claim_trans: db.Mapped[int] = db.mapped_column(primary_key=True)
    charge_trans_date: db.Mapped[str]
    period: db.Mapped[int]
    mem_acct_id: db.Mapped[int]
    injury_disease_id: db.Mapped[int]
    specialty_id: db.Mapped[int]
    facility_id: db.Mapped[int]
    charge_allowed: db.Mapped[int]
    charge_paid_ins: db.Mapped[int]
    deduct_copay: db.Mapped[int]


