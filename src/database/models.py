from datetime import datetime, timezone

from sqlalchemy import BigInteger, DateTime, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ConversationMessage(Base):
    __tablename__ = "conversation_messages"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, index=True)
    user_id: Mapped[int]  = mapped_column(BigInteger, index=True)
    role: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

class ChannelPersonality(Base):
    __tablename__ = "channel_personalities"
    channel_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    personality_name: Mapped[str] = mapped_column(String(64)
                                                  )