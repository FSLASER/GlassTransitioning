from enum import Enum, auto

class AutoName(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

#============= API Endpoints and Headers =============
class XY2(AutoName): 
    XY2_ENDPOINT = auto()
    XY2_SET_LASER_PWM = auto()
    XY2_SET_POSITION_RAW = auto()
    XY2_SET_POSITION_MM = auto()
    XY2_SAS_LAP_JOB = auto()
    XY2_LAP_JOB = auto()
    XY2_LAP_JOB_PERIMETER = auto()
    XY2_LAST_LAP_JOB = auto()
    XY2_LAST_LAP_JOB_PERIMETER = auto()
    XY2_STOP_JOB = auto()
    XY2_PAUSE_JOB = auto()
    XY2_RESUME_JOB = auto()
    XY2_GET_STATUS = auto()
    XY2_SET_LASER_ON = auto()
    XY2_SET_LASER_OFF = auto()
    XY2_TOGGLE_VISUAL_ALIGNMENT_LASER = auto()
    XY2_TOGGLE_CAMERA_ALIGNMENT_LASER = auto()
    XY2_TOGGLE_RED_LASER = auto()
    XY2_ADJUST_CAMERA_ALIGNMENT_LASER_BRIGHTNESS = auto()
    XY2_GET_LASER_SOURCE_STATUS = auto()
    XY2_SET_TRANS_MM = auto()
    XY2_SET_TRANS_DAC = auto()
    XY2_RESET_TRANS_MM = auto()
    XY2_RESET_TRANS_DAC = auto()

class VISION(AutoName):
    VISION_ENDPOINT = auto()
    VISION_SET_LENS_FOCUS = auto()
    VISION_AUTOFOCUS_LENS = auto()
    VISION_SET_ET = auto()
    VISION_LASER_AUTOFOCUS_GALVO_Z = auto()
    VISION_GET_CAPTURE = auto()
    VISION_TOGGLE_VIDEO_STREAMS = auto()
    VISION_UPLOAD_OVERVIEW = auto()
    VISION_UPLOAD_ORI_OVERVIEW = auto()
    VISION_UPLOAD_COAXIS = auto()
    VISION_SAVE_OVERVIEW = auto()
    VISION_SAVE_ORI_OVERVIEW = auto()
    VISION_SAVE_COAXIS = auto()

class CNC(AutoName):
    CNC_ENDPOINT = auto()
    CNC_JOG_START = auto()
    CNC_JOG_STOP = auto()
    CNC_SEND_CMD = auto()
    CNC_SEND_CMD_AWAIT = auto()
    CNC_GET_STATUS = auto()
    CNC_FEED_HOLD = auto()
    CNC_RESET_ALARM = auto()
    CNC_CYCLE_START = auto()
    CNC_SOFT_RESET = auto()
    CNC_HOME = auto()
    CNC_SET_OVERHEAD_LIGHT = auto()
    CNC_TOGGLE_DOOR = auto()
    CNC_STOP = auto()
    CNC_OVERWRITE_SETTING = auto()
    

#=============== SALSA Micro Servers =================
class TO_SALSA_SIO_EVENTS(AutoName):
    TO_SALSA_CONTROL = auto()
    TO_SALSA_GET_STATUS_UPDATE = auto()
    TO_SALSA_ECHO = auto()
    TO_SALSA_ESTOP = auto()

class FROM_SALSA_SIO_EVENTS(AutoName):
    FROM_SALSA_TOAST = auto()
    FROM_SALSA_STATUS_UPDATE = auto()
    FROM_SALSA_IMAGE = auto()
    FROM_SALSA_ECHO = auto()
    FROM_SALSA_JOB_END = auto()
