import time
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils

Modbus_TCP_Address1 = "192.168.1.200" #Modbus TCP converter
Powermeter_Address1 = 1 #Power meter Socomec Diris A-30
Modbus_TCP_Port = 502
Modbus_TCP_Delay = 0.05
Modbus_TCP_Debug = True #False

#################################
#New communication table from 01/2009
SOCOMEC_U12 = 50514 #PhaseToPhaseVoltageU12 [V/100]
SOCOMEC_U23 = 50516 #PhaseToPhaseVoltageU23 [V/100]
SOCOMEC_U31 = 50518 #PhaseToPhaseVoltageU31 [V/100]
SOCOMEC_V1 = 50520 #PhaseToNeutralVoltagePhase1 [V/100]
SOCOMEC_V2 = 50522 #PhaseToNeutralVoltagePhase2 [V/100]
SOCOMEC_V3 = 50524 #PhaseToNeutralVoltagePhase3 [V/100]
SOCOMEC_F = 50526 #Frequency [Hz/100]
SOCOMEC_I1 = 50528 #CurrentPhase1 [mA]
SOCOMEC_I2 = 50530 #CurrentPhase2 [mA]
SOCOMEC_I3 = 50532 #CurrentPhase3 [mA]
SOCOMEC_In = 50534 #NeutralCurrent [mA]
SOCOMEC_P = 50536 #ActivePower [+/-kW/100]
SOCOMEC_Q = 50538 #ReactivePower [+/-kvar/100]
SOCOMEC_S = 50540 #ApparentPower [kVA/100]
SOCOMEC_PF = 50542 #PowerFactor [+/-0.001]
SOCOMEC_P1 = 50544 #ActivePowerPhase1 [+/-kW/100]
SOCOMEC_P2 = 50546 #ActivePowerPhase2 [+/-kW/100]
SOCOMEC_P3 = 50548 #ActivePowerPhase3 [+/-kW/100]
SOCOMEC_Q1 = 50550 #ReactivePowerPhase1 [+/-kvar/100]
SOCOMEC_Q2 = 50552 #ReactivePowerPhase2 [+/-kvar/100]
SOCOMEC_Q3 = 50554 #ReactivePowerPhase3 [+/-kvar/100]
SOCOMEC_S1 = 50556 #ApparentPowerPhase1 [kVA/100]
SOCOMEC_S2 = 50558 #ApparentPowerPhase2 [kVA/100]
SOCOMEC_S3 = 50560 #ApparentPowerPhase2 [kVA/100]
SOCOMEC_PF1 = 50562 #PowerFactorPhase1 [+/-0.001]
SOCOMEC_PF2 = 50564 #PowerFactorPhase1 [+/-0.001]
SOCOMEC_PF3 = 50566 #PowerFactorPhase1 [+/-0.001]

SOCOMEC_LABEL = []
SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU12", "V"])
SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU23", "V"])
SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU31", "V"])
SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase1", "V"])
SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase2", "V"])
SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase3", "V"])
SOCOMEC_LABEL.append(["Frequency", "Hz"])
SOCOMEC_LABEL.append(["CurrentPhase1", "A"])
SOCOMEC_LABEL.append(["CurrentPhase2", "A"])
SOCOMEC_LABEL.append(["CurrentPhase3", "A"])
SOCOMEC_LABEL.append(["NeutralCurrent", "A"])
SOCOMEC_LABEL.append(["ActivePower", "kW"])
SOCOMEC_LABEL.append(["ReactivePower", "kvar"])
SOCOMEC_LABEL.append(["ApparentPower", "kVA"])
SOCOMEC_LABEL.append(["PowerFactor", " "])
SOCOMEC_LABEL.append(["ActivePowerPhase1", "kW"])
SOCOMEC_LABEL.append(["ActivePowerPhase2", "kW"])
SOCOMEC_LABEL.append(["ActivePowerPhase3", "kW"])
SOCOMEC_LABEL.append(["ReactivePowerPhase1", "kvar"])
SOCOMEC_LABEL.append(["ReactivePowerPhase2", "kvar"])
SOCOMEC_LABEL.append(["ReactivePowerPhase3", "kvar"])
SOCOMEC_LABEL.append(["ApparentPowerPhase1", "kVA"])
SOCOMEC_LABEL.append(["ApparentPowerPhase2", "kVA"])
SOCOMEC_LABEL.append(["ApparentPowerPhase3", "kVA"])
SOCOMEC_LABEL.append(["PowerFactorPhase1", " "])
SOCOMEC_LABEL.append(["PowerFactorPhase2", " "])
SOCOMEC_LABEL.append(["PowerFactorPhase3", " "])
SOCOMEC_UNIT = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.001, 0.001, 0.001, 0.001, 0.01, 0.01, 0.01, 0.001,
                0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
########################################

# ########################################
# #Old communication table before 01/2009
# SOCOMEC_I1 = 768 #CurrentPhase1 [mA]
# SOCOMEC_I2 = 770 #CurrentPhase2 [mA]
# SOCOMEC_I3 = 772 #CurrentPhase3 [mA]
# SOCOMEC_In = 774 #NeutralCurrent [mA]
# SOCOMEC_U12 = 776 #PhaseToPhaseVoltageU12 [V/100]
# SOCOMEC_U23 = 778 #PhaseToPhaseVoltageU23 [V/100]
# SOCOMEC_U31 = 780 #PhaseToPhaseVoltageU31 [V/100]
# SOCOMEC_V1 = 782 #PhaseToNeutralVoltagePhase1 [V/100]
# SOCOMEC_V2 = 784 #PhaseToNeutralVoltagePhase2 [V/100]
# SOCOMEC_V3 = 786 #PhaseToNeutralVoltagePhase3 [V/100]
# SOCOMEC_F = 788 #Frequency [Hz/100]
# SOCOMEC_P = 790 #ActivePower [+/-kW/100]
# SOCOMEC_Q = 792 #ReactivePower [+/-kvar/100]
# SOCOMEC_S = 794 #ApparentPower [kVA/100]
# SOCOMEC_PF = 796 #PowerFactor [+/-0.001]
# SOCOMEC_P1 = 798 #ActivePowerPhase1 [+/-kW/100]
# SOCOMEC_P2 = 800 #ActivePowerPhase2 [+/-kW/100]
# SOCOMEC_P3 = 802 #ActivePowerPhase3 [+/-kW/100]
# SOCOMEC_Q1 = 804 #ReactivePowerPhase1 [+/-kvar/100]
# SOCOMEC_Q2 = 806 #ReactivePowerPhase2 [+/-kvar/100]
# SOCOMEC_Q3 = 808 #ReactivePowerPhase3 [+/-kvar/100]
# SOCOMEC_S1 = 810 #ApparentPowerPhase1 [kVA/100]
# SOCOMEC_S2 = 812 #ApparentPowerPhase2 [kVA/100]
# SOCOMEC_S3 = 814 #ApparentPowerPhase3 [kVA/100]
# SOCOMEC_PF1 = 816 #PowerFactorPhase1 [+/-0.001]
# SOCOMEC_PF2 = 818 #PowerFactorPhase2 [+/-0.001]
# SOCOMEC_PF3 = 820 #PowerFactorPhase3 [+/-0.001]

# SOCOMEC_LABEL = []
# SOCOMEC_LABEL.append(["CurrentPhase1", "A"])
# SOCOMEC_LABEL.append(["CurrentPhase2", "A"])
# SOCOMEC_LABEL.append(["CurrentPhase3", "A"])
# SOCOMEC_LABEL.append(["NeutralCurrent", "A"])
# SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU12", "V"])
# SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU23", "V"])
# SOCOMEC_LABEL.append(["PhaseToPhaseVoltageU31", "V"])
# SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase1", "V"])
# SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase2", "V"])
# SOCOMEC_LABEL.append(["PhaseToNeutralVoltagePhase3", "V"])
# SOCOMEC_LABEL.append(["Frequency", "Hz"])
# SOCOMEC_LABEL.append(["ActivePower", "kW"])
# SOCOMEC_LABEL.append(["ReactivePower", "kvar"])
# SOCOMEC_LABEL.append(["ApparentPower", "kVA"])
# SOCOMEC_LABEL.append(["PowerFactor", " "])
# SOCOMEC_LABEL.append(["ActivePowerPhase1", "kW"])
# SOCOMEC_LABEL.append(["ActivePowerPhase2", "kW"])
# SOCOMEC_LABEL.append(["ActivePowerPhase3", "kW"])
# SOCOMEC_LABEL.append(["ReactivePowerPhase1", "kvar"])
# SOCOMEC_LABEL.append(["ReactivePowerPhase2", "kvar"])
# SOCOMEC_LABEL.append(["ReactivePowerPhase3", "kvar"])
# SOCOMEC_LABEL.append(["ApparentPowerPhase1", "kVA"])
# SOCOMEC_LABEL.append(["ApparentPowerPhase2", "kVA"])
# SOCOMEC_LABEL.append(["ApparentPowerPhase3", "kVA"])
# SOCOMEC_LABEL.append(["PowerFactorPhase1", " "])
# SOCOMEC_LABEL.append(["PowerFactorPhase2", " "])
# SOCOMEC_LABEL.append(["PowerFactorPhase3", " "])
# SOCOMEC_UNIT = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.001, 0.001, 0.001, 0.001, 0.01, 0.01, 0.01, 0.001,
#                 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
# ####################################

def Modbus_Socomec(Modbus_IP, Modbus_ID):
    valid = True
    reading = []
    try:
        size = len(SOCOMEC_UNIT) * 2 #30
        PM_X = ModbusClient(host=Modbus_IP, port=Modbus_TCP_Port, unit_id=Modbus_ID, timeout=30.0, debug=Modbus_TCP_Debug, auto_open=True, auto_close=True)
        regs_list = PM_X.read_holding_registers(SOCOMEC_U12, size)
        if str(type(regs_list)) == "<class 'NoneType'>":
            valid = False
            print("Error read from modbus Socomec")
        elif len(regs_list) == size:
            print("Received")
            count_register, count_unit = 0, 0
            for count, regs in enumerate(regs_list):
                count_register += 1
                if count_register == 2:
                    value = utils.get_2comp((regs_list[count-1] << 16) + regs_list[count], val_size=32)
                    if SOCOMEC_UNIT[count_unit] == 0.1: decimal_point = 1
                    elif SOCOMEC_UNIT[count_unit] == 0.01: decimal_point = 2
                    elif SOCOMEC_UNIT[count_unit] == 0.001: decimal_point = 3
                    reading.append(round(value * SOCOMEC_UNIT[count_unit], decimal_point))
                    count_register = 0
                    count_unit += 1
        else:
            valid = False
            print("Invalid")
    except:
        valid = False
        print("Error")
    return valid, reading

while (True):
    check, read_signal = Modbus_Socomec(Modbus_TCP_Address1, Powermeter_Address1)
    if check is True:
        print(Modbus_TCP_Address1, Powermeter_Address1)
        for label, read in zip(SOCOMEC_LABEL, read_signal):
            print(label[0], read, label[1])
        print("===================================")
    time.sleep(2)