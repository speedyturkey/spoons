from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
requests = Table('requests', post_meta,
    Column('created_at', DateTime, default=ColumnDefault(<function datetime.now at 0x104599bf8>)),
    Column('updated_at', DateTime, onupdate=ColumnDefault(<function datetime.now at 0x104599c80>)),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('product_id', Integer),
    Column('requested_by_id', Integer),
    Column('requested_at', DateTime, default=ColumnDefault(<function datetime.now at 0x1046586a8>)),
    Column('status', String(length=128)),
    Column('requestor_note', String(length=255)),
    Column('reviewed_by_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['requests'].columns['reviewed_by_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['requests'].columns['reviewed_by_id'].drop()
