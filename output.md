subsystem-x-secret.csv
==========================
|Short Name|Long Name|Publisher|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |--- |
|`AcceActPos` |`Accelerator Actual  Position` |`ECM` |`SCS` |`T` |`T` |`T` |`T` |
|`AcceActPosV` |`Accelerator Actual  Position Validity` |`ECM` |`SCS` |`T` |`T` |`T` |`T` |
|`AutocTrCmdGear` |`Automatic Transimission Commanded Gear` |`GEAR` |`ECM` |`T` |`T` |`T` | |
|`BrkPdlPos` |`Brake Pedal Position` |`BRKR` |`GW`\|`ECM` | | | |`T` |

subsystem-xxx-public.csv
==========================
|Short Name|Long Name|Publisher|Subscriber|Feature02:EBD|Feature05:ABS|Feature06:TCS|Feature07:SCS  |
| --- |--- |--- |--- |--- |--- |--- |--- |
|`AcceActPos` |`Accelerator Actual  Position` |`ECM` |`WIKI` |`T` |`T` |`T` |`T` |
|`AcceActPosV` |`Accelerator Actual  Position Validity` |`ECM` |`BBC` |`T` |`T` |`T` |`T` |
|`AutocTrCmdGear` |`Automatic Transimission Commanded Gear` |`GEAR` |`ECM` |`T` |`T` |`T` | |
|`BBB` |`Brake Bread Beer` |`BRKR` |`TOP`\|`ECM` | | | |`T` |


Generated Data
==========================

```yaml
BBC:
  Receiving:
    Accelerator Actual  Position Validity:
      subsystem-xxx-public:
      - ECM
BRKR:
  Sending:
    Brake Bread Beer:
      subsystem-xxx-public:
      - TOP
      - ECM
    Brake Pedal Position:
      subsystem-x-secret:
      - GW
      - ECM
ECM:
  Receiving:
    Automatic Transimission Commanded Gear:
      subsystem-x-secret:
      - GEAR
      subsystem-xxx-public:
      - GEAR
    Brake Bread Beer:
      subsystem-xxx-public:
      - BRKR
    Brake Pedal Position:
      subsystem-x-secret:
      - BRKR
  Sending:
    Accelerator Actual  Position:
      subsystem-x-secret:
      - SCS
      subsystem-xxx-public:
      - WIKI
    Accelerator Actual  Position Validity:
      subsystem-x-secret:
      - SCS
      subsystem-xxx-public:
      - BBC
GEAR:
  Sending:
    Automatic Transimission Commanded Gear:
      subsystem-x-secret:
      - ECM
      subsystem-xxx-public:
      - ECM
GW:
  Receiving:
    Brake Pedal Position:
      subsystem-x-secret:
      - BRKR
SCS:
  Receiving:
    Accelerator Actual  Position:
      subsystem-x-secret:
      - ECM
    Accelerator Actual  Position Validity:
      subsystem-x-secret:
      - ECM
TOP:
  Receiving:
    Brake Bread Beer:
      subsystem-xxx-public:
      - BRKR
WIKI:
  Receiving:
    Accelerator Actual  Position:
      subsystem-xxx-public:
      - ECM
```
Generated Graphviz Source
==========================

```dot
digraph Signals {
	graph [rankdir=LR title="ECU Signals"]
	node [shape=box]
		ECM [label=ECM color="#a500d7" style=filled]
		SCS [label=SCS color="#d500eb" style=filled]
			ECM -> SCS [label="subsystem-x-secret::AcceActPos" color="#7003ca"]
			ECM -> SCS [label="subsystem-x-secret::AcceActPosV" color="#7d0424"]
		GEAR [label=GEAR color="#c30122" style=filled]
			GEAR -> ECM [label="subsystem-x-secret::AutocTrCmdGear" color="#fa057d"]
		BRKR [label=BRKR color="#ea0134" style=filled]
		GW [label=GW color="#e7009f" style=filled]
			BRKR -> GW [label="subsystem-x-secret::BrkPdlPos" color="#9d0382"]
			BRKR -> ECM [label="subsystem-x-secret::BrkPdlPos" color="#9d0382"]
		WIKI [label=WIKI color="#1a0138" style=filled]
			ECM -> WIKI [label="subsystem-xxx-public::AcceActPos" color="#7003ca"]
		BBC [label=BBC color="#9000c9" style=filled]
			ECM -> BBC [label="subsystem-xxx-public::AcceActPosV" color="#7d0424"]
			GEAR -> ECM [label="subsystem-xxx-public::AutocTrCmdGear" color="#fa057d"]
		TOP [label=TOP color="#ed00f5" style=filled]
			BRKR -> TOP [label="subsystem-xxx-public::BBB" color="#8f00c8"]
			BRKR -> ECM [label="subsystem-xxx-public::BBB" color="#8f00c8"]
}
```