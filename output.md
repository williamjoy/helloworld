subsystem-x-secret.csv
==========================
|Short Name|Long Name|Publisher|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |--- |
|AcceActPos |Accelerator Actual  Position |ECM |SCS |T |T |T |T |
|AcceActPosV |Accelerator Actual  Position Validity |ECM |SCS |T |T |T |T |
|AutocTrCmdGear |Automatic Transimission Commanded Gear |GEAR |ECM |T |T |T | |
|BrkPdlPos |Brake Pedal Position |BRKR |GW\|ECM | | | |T |

subsystem-xxx-public.csv
==========================
|Short Name|Long Name|Publisher|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |--- |
|AcceActPos |Accelerator Actual  Position |ECM |WIKI |T |T |T |T |
|AcceActPosV |Accelerator Actual  Position Validity |ECM |BBC |T |T |T |T |
|AutocTrCmdGear |Automatic Transimission Commanded Gear |GEAR |ECM |T |T |T | |
|BBB |Brake Bread Beer |BRKR |TOP\|ECM | | | |T |


Generated Data
==========================

```yaml
Accelerator Actual  Position:
  subsystem-x-secret:
    Publisher: ECM
    Short Name: AcceActPos
    Subscriber:
    - SCS
  subsystem-xxx-public:
    Publisher: ECM
    Short Name: AcceActPos
    Subscriber:
    - WIKI
Accelerator Actual  Position Validity:
  subsystem-x-secret:
    Publisher: ECM
    Short Name: AcceActPosV
    Subscriber:
    - SCS
  subsystem-xxx-public:
    Publisher: ECM
    Short Name: AcceActPosV
    Subscriber:
    - BBC
Automatic Transimission Commanded Gear:
  subsystem-x-secret:
    Publisher: GEAR
    Short Name: AutocTrCmdGear
    Subscriber:
    - ECM
  subsystem-xxx-public:
    Publisher: GEAR
    Short Name: AutocTrCmdGear
    Subscriber:
    - ECM
Brake Bread Beer:
  subsystem-xxx-public:
    Publisher: BRKR
    Short Name: BBB
    Subscriber:
    - TOP
    - ECM
Brake Pedal Position:
  subsystem-x-secret:
    Publisher: BRKR
    Short Name: BrkPdlPos
    Subscriber:
    - GW
    - ECM
```