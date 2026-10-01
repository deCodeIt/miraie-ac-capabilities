"""Core capabilities class for Panasonic MirAIe AC."""

from dataclasses import dataclass
from typing import Optional, List, Dict
from .enums import (
    OperationMode,
    SwingMode,
    ConvertibleMode,
    FanSpeed,
    SpecialMode
)

@dataclass
class TemperatureRange:
    """Defines the valid temperature range and step."""
    min_temp: float
    max_temp: float
    step: float = 1.0

    def is_valid_temperature(self, temperature: float) -> bool:
        """Check if a temperature value is valid within the range and step."""
        if temperature < self.min_temp or temperature > self.max_temp:
            return False
        # Check if the temperature follows the step pattern
        steps_from_min = (temperature - self.min_temp) / self.step
        return abs(round(steps_from_min) - steps_from_min) < 0.001

@dataclass
class ACCapabilities:
    """Represents the capabilities of a Panasonic MirAIe AC unit."""
    
    # Basic capabilities
    model_name: str
    supports_wifi: bool = True
    
    # Operation modes
    supported_modes: List[OperationMode]
    
    # Temperature control
    temperature_ranges: Dict[OperationMode, TemperatureRange]
    
    # Swing capabilities
    supported_swing_modes: List[SwingMode]
    
    # Fan control
    supported_fan_speeds: List[FanSpeed]
    
    # Special features
    supports_display_control: bool = True
    supported_special_modes: List[SpecialMode]
    supported_convertible_modes: List[ConvertibleMode]
    
    def supports_mode(self, mode: OperationMode) -> bool:
        """Check if the AC supports a specific operation mode."""
        return mode in self.supported_modes
    
    def get_temperature_range(self, mode: OperationMode) -> Optional[TemperatureRange]:
        """Get the valid temperature range for a specific mode."""
        return self.temperature_ranges.get(mode)
    
    def supports_swing(self, mode: SwingMode) -> bool:
        """Check if the AC supports a specific swing mode."""
        return mode in self.supported_swing_modes
    
    def supports_fan_speed(self, speed: FanSpeed) -> bool:
        """Check if the AC supports a specific fan speed."""
        return speed in self.supported_fan_speeds
    
    def supports_special_mode(self, mode: SpecialMode) -> bool:
        """Check if the AC supports a specific special mode."""
        return mode in self.supported_special_modes
    
    def supports_convertible_mode(self, mode: ConvertibleMode) -> bool:
        """Check if the AC supports a specific convertible mode."""
        return mode in self.supported_convertible_modes
