# Example usage of miraie-ac-capabilities
from miraie_ac_capabilities import (
    ACCapabilities,
    OperationMode,
    SwingMode,
    ConvertibleMode,
    FanSpeed,
    SpecialMode,
)
from miraie_ac_capabilities.capabilities import TemperatureRange

# Define capabilities for a high-end Panasonic AC model
ac_capabilities = ACCapabilities(
    model_name="Panasonic CS-XU18XKY-8",
    supports_wifi=True,
    supported_modes=[
        OperationMode.AUTO,
        OperationMode.COOL,
        OperationMode.DRY,
        OperationMode.HEAT,
        OperationMode.FAN,
    ],
    temperature_ranges={
        OperationMode.COOL: TemperatureRange(16.0, 30.0, 0.5),
        OperationMode.HEAT: TemperatureRange(16.0, 30.0, 0.5),
        OperationMode.AUTO: TemperatureRange(16.0, 30.0, 0.5),
        OperationMode.DRY: TemperatureRange(16.0, 30.0, 0.5),
    },
    supported_swing_modes=[
        SwingMode.OFF,
        SwingMode.VERTICAL,
        SwingMode.HORIZONTAL,
        SwingMode.BOTH,
    ],
    supported_fan_speeds=[
        FanSpeed.AUTO,
        FanSpeed.LOW,
        FanSpeed.MEDIUM,
        FanSpeed.HIGH,
        FanSpeed.POWERFUL,
    ],
    supports_display_control=True,
    supported_special_modes=[
        SpecialMode.NORMAL,
        SpecialMode.CLEAN,
        SpecialMode.QUIET,
        SpecialMode.ECO,
        SpecialMode.NANOE,
    ],
    supported_convertible_modes=[
        ConvertibleMode.FULL_CAPACITY,
        ConvertibleMode.HIGH_CAPACITY,
        ConvertibleMode.MEDIUM_CAPACITY,
        ConvertibleMode.LOW_CAPACITY,
    ],
)

# Example usage
print(f"Model: {ac_capabilities.model_name}")
print(f"Supports cooling: {ac_capabilities.supports_mode(OperationMode.COOL)}")
print(f"Cooling temperature range: {ac_capabilities.get_temperature_range(OperationMode.COOL)}")
print(f"Supports vertical swing: {ac_capabilities.supports_swing(SwingMode.VERTICAL)}")
print(f"Supports nanoe: {ac_capabilities.supports_special_mode(SpecialMode.NANOE)}")
