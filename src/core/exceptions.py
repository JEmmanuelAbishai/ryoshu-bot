class BotError(Exception):
    """Base class for all bot-related exceptions."""
    pass

class InvalidDurationError(BotError):
    """Raised when an invalid duration is provided."""
    pass

class MemberNotFoundError(BotError):
    """Raised when a member is not found in the guild."""
    pass