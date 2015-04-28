subsystem-xxx-public.csv
==========================
|Short Name|Long Name|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |
|AcceActPos |Accelerator Actual  Position |WIKI |T |T |T |T |
|AcceActPosV |Accelerator Actual  Position Validity |BBC |T |T |T |T |
|AutocTrCmdGear |Automatic Transimission Commanded Gear |ECM |T |T |T | |
|BBB |Brake Bread Beer |TOP\|ECM | | | |T |

subsystem-x-secret.csv
==========================
|Short Name|Long Name|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |
|AcceActPos |Accelerator Actual  Position |SCS |T |T |T |T |
|AcceActPosV |Accelerator Actual  Position Validity |SCS |T |T |T |T |
|AutocTrCmdGear |Automatic Transimission Commanded Gear |ECM |T |T |T | |
|BrkPdlPos |Brake Pedal Position |GW\|ECM | | | |T |


Generated Data
==========================

```yaml
Accelerator Actual  Position:
  subsystem-x-secret:
    Short Name: AcceActPos
    Subscriber:
    - SCS
  subsystem-xxx-public:
    Short Name: AcceActPos
    Subscriber:
    - WIKI
Accelerator Actual  Position Validity:
  subsystem-x-secret:
    Short Name: AcceActPosV
    Subscriber:
    - SCS
  subsystem-xxx-public:
    Short Name: AcceActPosV
    Subscriber:
    - BBC
Automatic Transimission Commanded Gear:
  subsystem-x-secret:
    Short Name: AutocTrCmdGear
    Subscriber:
    - ECM
  subsystem-xxx-public:
    Short Name: AutocTrCmdGear
    Subscriber:
    - ECM
Brake Bread Beer:
  subsystem-xxx-public:
    Short Name: BBB
    Subscriber:
    - TOP
    - ECM
Brake Pedal Position:
  subsystem-x-secret:
    Short Name: BrkPdlPos
    Subscriber:
    - GW
    - ECM
```