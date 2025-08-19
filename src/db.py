from datetime import datetime
from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

engine = create_engine("sqlite:///splitbuddy.db", echo=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(128))

class Chat(Base):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_chat_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255))

class Bill(Base):
    __tablename__ = "bills"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    payer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Numeric(10,2))
    currency: Mapped[str] = mapped_column(String(8), default="RUB")
    description: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class BillParticipant(Base):
    __tablename__ = "bill_participants"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bill_id: Mapped[int] = mapped_column(ForeignKey("bills.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    share_amount: Mapped[float] = mapped_column(Numeric(10,2))

class Settlement(Base):
    __tablename__ = "settlements"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    from_user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    to_user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Numeric(10,2))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(engine)


def get_session():
    return Session(bind=engine)
