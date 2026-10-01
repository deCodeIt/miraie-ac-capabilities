"""Tests for the miraie_ac_capabilities package."""

import pytest
from miraie_ac_capabilities import (
    ACCapabilities,
    OperationMode,
    SwingMode,
    ConvertibleMode,
    FanSpeed,
    SpecialMode,
)
from miraie_ac_capabilities.capabilities import TemperatureRange

def test_temperature_range():
    """Test temperature range validation."""
    temp_range = TemperatureRange(16.0, 30.0, 0.5)
    
    # Test valid temperatures
    assert temp_range.is_valid_temperature(16.0)
    assert temp_range.is_valid_temperature(16.5)
    assert temp_range.is_valid_temperature(30.0)
    
    # Test invalid temperatures
    assert not temp_range.is_valid_temperature(15.9)
    assert not temp_range.is_valid_temperature(30.1)
    assert not temp_range.is_valid_temperature(16.3)  # Not following step

def test_ac_capabilities():
    """Test AC capabilities functionality."""
    capabilities = ACCapabilities(
        model_name="Test Model",
        supported_modes=[OperationMode.COOL, OperationMode.HEAT],
        temperature_ranges={
            OperationMode.COOL: TemperatureRange(16.0, 30.0),
            OperationMode.HEAT: TemperatureRange(16.0, 30.0),
        },
        supported_swing_modes=[SwingMode.VERTICAL],
        supported_fan_speeds=[FanSpeed.AUTO, FanSpeed.HIGH],
        supported_special_modes=[SpecialMode.CLEAN],
        supported_convertible_modes=[ConvertibleMode.FULL_CAPACITY]
    )
    
    # Test mode support
    assert capabilities.supports_mode(OperationMode.COOL)
    assert not capabilities.supports_mode(OperationMode.DRY)
    
    # Test temperature ranges
    cool_range = capabilities.get_temperature_range(OperationMode.COOL)
    assert cool_range.min_temp == 16.0
    assert cool_range.max_temp == 30.0
    
    # Test swing support
    assert capabilities.supports_swing(SwingMode.VERTICAL)
    assert not capabilities.supports_swing(SwingMode.HORIZONTAL)
    
    # Test fan speeds
    assert capabilities.supports_fan_speed(FanSpeed.AUTO)
    assert not capabilities.supports_fan_speed(FanSpeed.MEDIUM)
    
    # Test special modes
    assert capabilities.supports_special_mode(SpecialMode.CLEAN)
    assert not capabilities.supports_special_mode(SpecialMode.ECO)
    
    # Test convertible modes
    assert capabilities.supports_convertible_mode(ConvertibleMode.FULL_CAPACITY)
    assert not capabilities.supports_convertible_mode(ConvertibleMode.MEDIUM_CAPACITY)
