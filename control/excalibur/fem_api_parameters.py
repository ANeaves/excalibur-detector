"""fem_api_parameters.py - EXCALIBUR FEM API parameter definitions

Automatically generated on: Thu Apr  6 16:58:11 2017 by generate_fem_api_parameters.py - do not edit manually!

"""

FEM_PIXELS_PER_CHIP_X = 256
FEM_PIXELS_PER_CHIP_Y = 256
FEM_CHIPS_PER_BLOCK_X = 4
FEM_BLOCKS_PER_STRIPE_X = 2
FEM_CHIPS_PER_STRIPE_X = 8
FEM_CHIPS_PER_STRIPE_Y = 1
FEM_STRIPES_PER_MODULE = 2
FEM_STRIPES_PER_IMAGE = 6
FEM_CHIP_GAP_PIXELS_X = 3
FEM_CHIP_GAP_PIXELS_Y_LARGE = 125
FEM_CHIP_GAP_PIXELS_Y_SMALL = 3
FEM_PIXELS_PER_STRIPE_X = ((FEM_PIXELS_PER_CHIP_X+FEM_CHIP_GAP_PIXELS_X)*FEM_CHIPS_PER_STRIPE_X-FEM_CHIP_GAP_PIXELS_X)
FEM_TOTAL_PIXELS_Y = (FEM_PIXELS_PER_CHIP_Y*FEM_CHIPS_PER_STRIPE_Y*FEM_STRIPES_PER_IMAGE + (FEM_STRIPES_PER_IMAGE/2-1)*FEM_CHIP_GAP_PIXELS_Y_LARGE + (FEM_STRIPES_PER_IMAGE/2)*FEM_CHIP_GAP_PIXELS_Y_SMALL)
FEM_TOTAL_PIXELS_X = FEM_PIXELS_PER_STRIPE_X
FEM_EDGE_PIXEL_RATIO_NUM = 2
FEM_EDGE_PIXEL_RATIO_DEN = 5
FEM_EDGE_PIXEL_RATIO = 2/5
FEM_BITS_PER_PIXEL_1 = 0
FEM_BITS_PER_PIXEL_4 = 1
FEM_BITS_PER_PIXEL_12 = 2
FEM_BITS_PER_PIXEL_24 = 3
FEM_CHIP_ALL = 0
FEM_RTN_OK = 0
FEM_RTN_UNKNOWNOPID = 1
FEM_RTN_ILLEGALCHIP = 2
FEM_RTN_BADSIZE = 3
FEM_RTN_INITFAILED = 4
FEM_OPMODE_NORMAL = 0
FEM_OPMODE_BURST = 1
FEM_OPMODE_HISTOGRAM = 2
FEM_OPMODE_DACSCAN = 3
FEM_OPMODE_MATRIXREAD = 4
FEM_TRIGMODE_INTERNAL = 0
FEM_TRIGMODE_EXTERNAL = 1
FEM_TRIGMODE_SYNC = 2
FEM_CTRSELECT_A = 0
FEM_CTRSELECT_B = 1
FEM_CTRSELECT_AB = 2
FEM_OP_STARTACQUISITION = 1
FEM_OP_STOPACQUISITION = 2
FEM_OP_LOADPIXELCONFIG = 3
FEM_OP_FREEALLFRAMES = 4
FEM_OP_LOADDACCONFIG = 5
FEM_OP_FEINIT = 6
FEM_OP_REBOOT = 7
FEM_OP_MPXIII_COLOURMODE = 1000
FEM_OP_MPXIII_COUNTERDEPTH = 1001
FEM_OP_MPXIII_EXTERNALTRIGGER = 1002
FEM_OP_MPXIII_OPERATIONMODE = 1003
FEM_OP_MPXIII_COUNTERSELECT = 1004
FEM_OP_MPXIII_NUMTESTPULSES = 1005
FEM_OP_MPXIII_READWRITEMODE = 1006
FEM_OP_MPXIII_DISCCSMSPM = 1007
FEM_OP_MPXIII_EQUALIZATIONMODE = 1008
FEM_OP_MPXIII_CSMSPMMODE = 1009
FEM_OP_MPXIII_GAINMODE = 1010
FEM_OP_MPXIII_TRIGGERPOLARITY = 1011
FEM_OP_MPXIII_LFSRBYPASS = 1012
FEM_OP_MPXIII_DACSENSE = 2000
FEM_OP_MPXIII_DACEXTERNAL = 2001
FEM_OP_MPXIII_THRESHOLD0DAC = 2002
FEM_OP_MPXIII_THRESHOLD1DAC = 2003
FEM_OP_MPXIII_THRESHOLD2DAC = 2004
FEM_OP_MPXIII_THRESHOLD3DAC = 2005
FEM_OP_MPXIII_THRESHOLD4DAC = 2006
FEM_OP_MPXIII_THRESHOLD5DAC = 2007
FEM_OP_MPXIII_THRESHOLD6DAC = 2008
FEM_OP_MPXIII_THRESHOLD7DAC = 2009
FEM_OP_MPXIII_PREAMPDAC = 2010
FEM_OP_MPXIII_IKRUMDAC = 2011
FEM_OP_MPXIII_SHAPERDAC = 2012
FEM_OP_MPXIII_DISCDAC = 2013
FEM_OP_MPXIII_DISCLSDAC = 2014
FEM_OP_MPXIII_SHAPERTESTDAC = 2015
FEM_OP_MPXIII_DISCLDAC = 2016
FEM_OP_MPXIII_DELAYDAC = 2017
FEM_OP_MPXIII_TPBUFFERINDAC = 2018
FEM_OP_MPXIII_TPBUFFEROUTDAC = 2019
FEM_OP_MPXIII_RPZDAC = 2020
FEM_OP_MPXIII_GNDDAC = 2021
FEM_OP_MPXIII_TPREFDAC = 2022
FEM_OP_MPXIII_FBKDAC = 2023
FEM_OP_MPXIII_CASDAC = 2024
FEM_OP_MPXIII_TPREFADAC = 2025
FEM_OP_MPXIII_TPREFBDAC = 2026
FEM_OP_MPXIII_TESTDAC = 2027
FEM_OP_MPXIII_DISCHDAC = 2028
FEM_OP_MPXIII_EFUSEID = 2029
FEM_OP_MPXIII_TESTPULSE_ENABLE = 2030
FEM_OP_MPXIII_PIXELMASK = 3000
FEM_OP_MPXIII_PIXELDISCL = 3001
FEM_OP_MPXIII_PIXELDISCH = 3002
FEM_OP_MPXIII_PIXELTEST = 3004
FEM_OP_NUMFRAMESTOACQUIRE = 4000
FEM_OP_ACQUISITIONTIME = 4001
FEM_OP_ACQUISITIONPERIOD = 4002
FEM_OP_P5V_A_VMON = 4003
FEM_OP_P5V_B_VMON = 4004
FEM_OP_P5V_FEMO0_IMON = 4005
FEM_OP_P5V_FEMO1_IMON = 4006
FEM_OP_P5V_FEMO2_IMON = 4007
FEM_OP_P5V_FEMO3_IMON = 4008
FEM_OP_P5V_FEMO4_IMON = 4009
FEM_OP_P5V_FEMO5_IMON = 4010
FEM_OP_P48V_VMON = 4011
FEM_OP_P48V_IMON = 4012
FEM_OP_P5VSUP_VMON = 4013
FEM_OP_P5VSUP_IMON = 4014
FEM_OP_HUMIDITY_MON = 4015
FEM_OP_AIR_TEMP_MON = 4016
FEM_OP_COOLANT_TEMP_MON = 4017
FEM_OP_COOLANT_FLOW_MON = 4018
FEM_OP_P3V3_IMON = 4019
FEM_OP_P1V8_IMON_A = 4020
FEM_OP_BIAS_IMON = 4021
FEM_OP_P3V3_VMON = 4022
FEM_OP_P1V8_VMON_A = 4023
FEM_OP_BIAS_VMON = 4024
FEM_OP_P1V8_IMON_B = 4025
FEM_OP_P1V8_VMON_B = 4026
FEM_OP_COOLANT_TEMP_STATUS = 4027
FEM_OP_HUMIDITY_STATUS = 4028
FEM_OP_COOLANT_FLOW_STATUS = 4029
FEM_OP_AIR_TEMP_STATUS = 4030
FEM_OP_BIAS_ON_OFF = 4031
FEM_OP_LV_ON_OFF = 4032
FEM_OP_FAN_FAULT = 4033
FEM_OP_BIAS_LEVEL = 4034
FEM_OP_VDD_ON_OFF = 4035
FEM_OP_P1V5_AVDD_1_POK = 4036
FEM_OP_P1V5_AVDD_2_POK = 4037
FEM_OP_P1V5_AVDD_3_POK = 4038
FEM_OP_P1V5_AVDD_4_POK = 4039
FEM_OP_P1V5_VDD_1_POK = 4040
FEM_OP_P2V5_DVDD_1_POK = 4041
FEM_OP_DAC_IN_TO_MEDIPIX = 4042
FEM_OP_DAC_OUT_FROM_MEDIPIX = 4043
FEM_OP_MOLY_TEMPERATURE = 4044
FEM_OP_LOCAL_TEMP = 4045
FEM_OP_REMOTE_DIODE_TEMP = 4046
FEM_OP_MOLY_HUMIDITY = 4047
FEM_OP_MEDIPIX_CHIP_DISABLE = 4048
FEM_OP_SCAN_DAC = 4049
FEM_OP_SCAN_START = 4050
FEM_OP_SCAN_STOP = 4051
FEM_OP_SCAN_STEP = 4052
FEM_OP_BURST_SUBMIT_PERIOD = 4053
FEM_OP_DATA_RECEIVER_ENABLE = 4054
FEM_OP_FRAMES_ACQUIRED = 4055
FEM_OP_CONTROL_STATE = 4056
FEM_OP_DAC_SCAN_STATE = 4057
FEM_OP_DAC_SCAN_STEPS_COMPLETE = 4058
FEM_OP_SOURCE_DATA_ADDR = 4059
FEM_OP_SOURCE_DATA_MAC = 4060
FEM_OP_SOURCE_DATA_PORT = 4061
FEM_OP_DEST_DATA_ADDR = 4062
FEM_OP_DEST_DATA_MAC = 4063
FEM_OP_DEST_DATA_PORT = 4064
FEM_OP_ACQUISITIONCOMPLETE = 5000
FEM_OP_CORRUPTIMAGE = 5001
