from datetime import datetime
import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime
from app.db.connectivity import db_base

schema = 'general_schema'  # Use respective schema


class ProductTransaction(db_base):
    __tablename__ = 'product_transactions'

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(String, unique=True, index=True)
    farmer_id = Column(String, index=True)
    transaction_hash = Column(String, unique=True, index=True)
    block_number = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(dt.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(dt.timezone.utc))


class SampleTable(db_base):
    __tablename__ = 'sample_table'
    __table_args__ = {'schema': schema}
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True, nullable=False, unique=True)
    unique_id = Column(String, index=True, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(dt.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(dt.timezone.utc),
                        onupdate=datetime.now(dt.timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'unique_id': self.unique_id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
