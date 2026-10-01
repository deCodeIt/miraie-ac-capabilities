"""Enums for Panasonic MirAIe AC capabilities."""

from enum import Enum, auto

class OperationMode(Enum):
    """Available operation modes for the AC."""
    AUTO = auto()
    COOL = auto()
    DRY = auto()
    HEAT = auto()
    FAN = auto()

class SwingMode(Enum):
    """Available swing modes for the AC."""
    OFF = auto()
    VERTICAL = auto()
    HORIZONTAL = auto()
    BOTH = auto()

class ConvertibleMode(Enum):
    """Available convertible modes for power consumption."""
    FULL_CAPACITY = auto()
    HIGH_CAPACITY = auto()
    MEDIUM_CAPACITY = auto()
    LOW_CAPACITY = auto()

class FanSpeed(Enum):
    """Available fan speed settings."""
    AUTO = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    POWERFUL = auto()

class SpecialMode(Enum):
    """Special operation modes."""
    NORMAL = auto()
    CLEAN = auto()
    QUIET = auto()
    ECO = auto()
    NANOE = auto()  # Panasonic's air purification technology
