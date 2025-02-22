"""
Mug class
"""
import re

from openrazer_daemon.hardware.device_base import RazerDeviceBrightnessSuspend as _RazerDeviceBrightnessSuspend


class RazerChromaMugHolder(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Chroma Mug Holder
    """
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Chroma_Mug_Holder-if0(1|2)-event-kbd')

    USB_VID = 0x1532
    USB_PID = 0x0F07
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]
    METHODS = ['get_device_type_accessory',
               'set_static_effect', 'set_spectrum_effect', 'set_wave_effect', 'set_none_effect', 'set_breath_single_effect', 'set_breath_dual_effect', 'set_breath_random_effect', 'set_blinking_effect',
               'is_mug_present',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets2.razerzone.com/images/mug-holder/e64e507b73e61c44789d996065fd9645-1500x1000mug_01.jpg"


class RazerChromaARGB(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Chroma Addressable RGB Controller
    """
    USB_VID = 0x1532
    USB_PID = 0x0F1F
    HAS_MATRIX = True
    MATRIX_DIMS = [6, 80]
    WAVE_DIRS = (1, 2)
    METHODS = ['get_device_type_accessory',
               'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row',
               'get_channel1_brightness', 'set_channel1_brightness',
               'get_channel2_brightness', 'set_channel2_brightness',
               'get_channel3_brightness', 'set_channel3_brightness',
               'get_channel4_brightness', 'set_channel4_brightness',
               'get_channel5_brightness', 'set_channel5_brightness',
               'get_channel6_brightness', 'set_channel6_brightness',
               'get_channel1_size', 'set_channel1_size',
               'get_channel2_size', 'set_channel2_size',
               'get_channel3_size', 'set_channel3_size',
               'get_channel4_size', 'set_channel4_size',
               'get_channel5_size', 'set_channel5_size',
               'get_channel6_size', 'set_channel6_size'
               ]

    DEVICE_IMAGE = "https://dl.razerzone.com/src/3903-1-EN-v1.png"


class RazerChromaHDK(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Chroma Hardware Development Kit (HDK)
    """
    USB_VID = 0x1532
    USB_PID = 0x0F09
    HAS_MATRIX = True
    MATRIX_DIMS = [4, 16]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets2.razerzone.com/images/chromahdk2017/788b689d471fedbc0c5a175592316657-gallery-08.jpg"


class RazerBaseStationChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Base Station Chroma (Headphone Stand)
    """
    USB_VID = 0x1532
    USB_PID = 0x0F08
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://rzrwarranty.s3.amazonaws.com/145dcc47f9f9d33b0bd07b066364704160f45e87b756d690b203decec7d1e87c.png"


class RazerMouseDock(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mouse Dock
    """
    USB_VID = 0x1532
    USB_PID = 0x007E
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 1]
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Mouse_Dock-if0(1|2)-event-kbd')
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_spectrum_effect', 'set_brightness',
               'get_brightness', 'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect',
               'set_breath_dual_effect', 'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets.razerzone.com/eeimages/support/products/1711/1711_-_mouse_dock_chroma.png"


class RazerNommoChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Nommo Chroma (Speakers)
    """
    USB_VID = 0x1532
    USB_PID = 0x0517
    HAS_MATRIX = True
    MATRIX_DIMS = [2, 24]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets.razerzone.com/eeimages/support/products/1275/1275_nommo_chroma.png"


class RazerNommoPro(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Nommo Pro (Speakers)
    """
    USB_VID = 0x1532
    USB_PID = 0x0518
    HAS_MATRIX = True
    MATRIX_DIMS = [2, 8]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets.razerzone.com/eeimages/support/products/1419/1419_nommo_pro.png"


class RazerMouseBungeeV3Chroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mouse Bungee V3 Chroma
    """
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Mouse_Bungee_V3_Chroma-if01-event-kbd')

    USB_VID = 0x1532
    USB_PID = 0x0F1D
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 8]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets2.razerzone.com/images/pnx.assets/03970e1bd220f3d2985c5e0060fb3bbf/razer-mouse-bungee-v3-chroma.png"


class RazerBaseStationV2Chroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Base Station V2 Chroma
    """
    EVENT_FILE_REGEX = re.compile(r'.*RAZER_Razer_Base_Station_V2_Chroma-if01-event-kbd')

    USB_VID = 0x1532
    USB_PID = 0x0F20
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 8]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://dl.razerzone.com/src/3897-1-EN-v2.png"


class RazerThunderbolt4DockChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Thunderbolt 4 Dock Chroma
    """
    USB_VID = 0x1532
    USB_PID = 0x0F21
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 12]
    METHODS = ['get_device_type_accessory', 'set_static_effect', 'set_wave_effect', 'set_spectrum_effect',
               'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               'set_starlight_random_effect', 'set_starlight_single_effect', 'set_starlight_dual_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://dl.razerzone.com/src/4030-1-EN-v1.png"


class RazerChargingPadChroma(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Charging Pad Chroma
    """
    EVENT_FILE_REGEX = re.compile(r'.*RAZER_Razer_Charging_Pad_Chroma-event-if01')

    USB_VID = 0x1532
    USB_PID = 0x0F26
    HAS_MATRIX = True
    WAVE_DIRS = (1, 2)
    MATRIX_DIMS = [1, 10]
    METHODS = ['get_device_type_accessory', 'set_custom_effect', 'set_key_row', 'get_charging_brightness', 'set_charging_brightness', 'get_fast_charging_brightness', 'set_fast_charging_brightness', 'get_fully_charged_brightness', 'set_fully_charged_brightness',
               # Idle
               'set_wave_effect', 'set_static_effect', 'set_spectrum_effect', 'set_none_effect', 'set_breath_random_effect', 'set_breath_single_effect', 'set_breath_dual_effect',
               # Charging
               'set_charging_wave', 'set_charging_static', 'set_charging_spectrum', 'set_charging_none', 'set_charging_breath_random', 'set_charging_breath_single', 'set_charging_breath_dual',
               # Fast Charging
               'set_fast_charging_wave', 'set_fast_charging_static', 'set_fast_charging_spectrum', 'set_fast_charging_none', 'set_fast_charging_breath_random', 'set_fast_charging_breath_single', 'set_fast_charging_breath_dual',
               # Fully Charged
               'set_fully_charged_wave', 'set_fully_charged_static', 'set_fully_charged_spectrum', 'set_fully_charged_none', 'set_fully_charged_breath_random', 'set_fully_charged_breath_single', 'set_fully_charged_breath_dual']

    DEVICE_IMAGE = "https://dl.razerzone.com/Images/ChargingPadChroma/CPC-ProductImage.png"
