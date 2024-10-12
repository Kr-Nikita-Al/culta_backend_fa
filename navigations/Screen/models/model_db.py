import uuid
import datetime

from sqlalchemy import Column, String, Boolean, Integer, DateTime, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.base_model import Base
from utils.constants import EMPTY_UUID


###########################
# БЛОК ОПИСАНИЯ МОДЕЛИ БД #
###########################


class ScreenDB(Base):
    __tablename__ = 'screen'

    screen_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Properties
    title = Column(String(20), default='')
    sub_title = Column(String(20), default='')
    count_number = Column(Integer, default=0)

    # Connection fields
    company_id = Column(UUID, ForeignKey('company.company_id'))
    company = relationship("Company", backref="companies")

    company_group_id = Column(Integer, default=-1)

    # Technical fields
    creator_id = Column(UUID(as_uuid=True), default=EMPTY_UUID)
    updater_id = Column(UUID(as_uuid=True), default=EMPTY_UUID)
    time_created = Column(DateTime(timezone=True), default=datetime.datetime.now())
    time_updated = Column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())


