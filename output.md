subsystem-1.yaml
==========================
subsystem-2.yaml
==========================
subsystem-3.yaml
==========================

Generated Data
==========================

```yaml
ECU1:
  Receiving:
    H:
      subsystem-1:
      - ECU2
    I:
      subsystem-1:
      - ECU2
      subsystem-2:
      - ECU2
    J:
      subsystem-2:
      - ECU2
    K:
      subsystem-2:
      - ECU2
    U:
      subsystem-1:
      - ECU4
    V:
      subsystem-1:
      - ECU4
  Sending:
    A:
      subsystem-1:
      - ECU4
      - ECU2
      subsystem-2:
      - ECU4
    B:
      subsystem-1:
      - ECU2
      subsystem-2:
      - ECU4
      - ECU2
    C:
      subsystem-1:
      - ECU2
    D:
      subsystem-1:
      - ECU4
    E:
      subsystem-2:
      - ECU4
      - ECU2
    F:
      subsystem-2:
      - ECU4
ECU2:
  Receiving:
    A:
      subsystem-1:
      - ECU1
    B:
      subsystem-1:
      - ECU1
      subsystem-2:
      - ECU1
    C:
      subsystem-1:
      - ECU1
    E:
      subsystem-2:
      - ECU1
  Sending:
    H:
      subsystem-1:
      - ECU1
    I:
      subsystem-1:
      - ECU1
      subsystem-2:
      - ECU4
      - ECU1
    J:
      subsystem-2:
      - ECU4
      - ECU1
    K:
      subsystem-2:
      - ECU4
      - ECU1
ECU3:
  Sending:
    O:
      subsystem-3:
      - ECU4
    P:
      subsystem-3:
      - ECU4
    Q:
      subsystem-3:
      - ECU4
    R:
      subsystem-3:
      - ECU4
    V:
      subsystem-3:
      - ECU4
    W:
      subsystem-3:
      - ECU4
ECU4:
  Receiving:
    A:
      subsystem-1:
      - ECU1
      subsystem-2:
      - ECU1
    B:
      subsystem-2:
      - ECU1
    D:
      subsystem-1:
      - ECU1
    E:
      subsystem-2:
      - ECU1
    F:
      subsystem-2:
      - ECU1
    I:
      subsystem-2:
      - ECU2
    J:
      subsystem-2:
      - ECU2
    K:
      subsystem-2:
      - ECU2
    O:
      subsystem-3:
      - ECU3
    P:
      subsystem-3:
      - ECU3
    Q:
      subsystem-3:
      - ECU3
    R:
      subsystem-3:
      - ECU3
      - ECU3
    V:
      subsystem-3:
      - ECU3
    W:
      subsystem-3:
      - ECU3
  Sending:
    U:
      subsystem-1:
      - ECU1
    V:
      subsystem-1:
      - ECU1
```
Generated Graphviz Source
==========================

```dot
digraph Signals {
	graph [rankdir=LR title="ECU Signals"]
	node [shape=box style=filled]
	edge [fontsize=10]
		ECU1 [label=ECU1 color="#dd034"]
		ECU2 [label=ECU2 color="#c8a47"]
			ECU1 -> ECU2 [label="subsystem-1::A" color="#7fc56" fontcolor="#7fc56" tooltip=A]
		ECU4 [label=ECU4 color="#a9b5f"]
			ECU1 -> ECU4 [label="subsystem-1::A" color="#7fc56" fontcolor="#7fc56" tooltip=A]
			ECU1 -> ECU2 [label="subsystem-1::C" color="#0d61f" fontcolor="#0d61f" tooltip=C]
			ECU1 -> ECU2 [label="subsystem-1::B" color="#9d5ed" fontcolor="#9d5ed" tooltip=B]
			ECU1 -> ECU4 [label="subsystem-1::D" color="#f623e" fontcolor="#f623e" tooltip=D]
			ECU2 -> ECU1 [label="subsystem-1::I" color="#dd753" fontcolor="#dd753" tooltip=I]
			ECU2 -> ECU1 [label="subsystem-1::H" color="#c1d9f" fontcolor="#c1d9f" tooltip=H]
			ECU4 -> ECU1 [label="subsystem-1::U" color="#4c614" fontcolor="#4c614" tooltip=U]
			ECU4 -> ECU1 [label="subsystem-1::V" color="#52065" fontcolor="#52065" tooltip=V]
			ECU1 -> ECU4 [label="subsystem-2::A" color="#7fc56" fontcolor="#7fc56" tooltip=A]
			ECU1 -> ECU2 [label="subsystem-2::B" color="#9d5ed" fontcolor="#9d5ed" tooltip=B]
			ECU1 -> ECU4 [label="subsystem-2::B" color="#9d5ed" fontcolor="#9d5ed" tooltip=B]
			ECU1 -> ECU2 [label="subsystem-2::E" color="#3a3ea" fontcolor="#3a3ea" tooltip=E]
			ECU1 -> ECU4 [label="subsystem-2::E" color="#3a3ea" fontcolor="#3a3ea" tooltip=E]
			ECU1 -> ECU4 [label="subsystem-2::F" color="#80061" fontcolor="#80061" tooltip=F]
			ECU2 -> ECU1 [label="subsystem-2::I" color="#dd753" fontcolor="#dd753" tooltip=I]
			ECU2 -> ECU4 [label="subsystem-2::I" color="#dd753" fontcolor="#dd753" tooltip=I]
			ECU2 -> ECU1 [label="subsystem-2::K" color="#a5f3c" fontcolor="#a5f3c" tooltip=K]
			ECU2 -> ECU4 [label="subsystem-2::K" color="#a5f3c" fontcolor="#a5f3c" tooltip=K]
			ECU2 -> ECU1 [label="subsystem-2::J" color="#ff445" fontcolor="#ff445" tooltip=J]
			ECU2 -> ECU4 [label="subsystem-2::J" color="#ff445" fontcolor="#ff445" tooltip=J]
		ECU3 [label=ECU3 color="#d1a53"]
			ECU3 -> ECU4 [label="subsystem-3::Q" color="#f0956" fontcolor="#f0956" tooltip=Q]
			ECU3 -> ECU4 [label="subsystem-3::P" color="#44c29" fontcolor="#44c29" tooltip=P]
			ECU3 -> ECU4 [label="subsystem-3::R" color="#e1e1d" fontcolor="#e1e1d" tooltip=R]
			ECU3 -> ECU4 [label="subsystem-3::R" color="#e1e1d" fontcolor="#e1e1d" tooltip=R]
			ECU3 -> ECU4 [label="subsystem-3::W" color="#61e9c" fontcolor="#61e9c" tooltip=W]
			ECU3 -> ECU4 [label="subsystem-3::V" color="#52065" fontcolor="#52065" tooltip=V]
			ECU3 -> ECU4 [label="subsystem-3::O" color="#f1862" fontcolor="#f1862" tooltip=O]
}
```

![graphviz](https://williamjoy.github.io/signal-matrix/graph.dot.svg)