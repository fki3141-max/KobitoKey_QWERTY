#!/usr/bin/env python3
"""config/keymap.yaml から ZMK 用の config/KobitoKey.keymap を生成する。

使い方:
    python3 scripts/generate_keymap.py

keymap.yaml のシンプルな記法（トークン）:
    _              -> &trans
    Q, N1, SEMI... -> &kp Q / &kp N1 / &kp SEMI ...  (そのまま &kp の引数になる)
    LT2(SPACE)     -> &lt 2 SPACE          (レイヤー番号はどの数字でも可)
    MT(LALT,SLASH) -> &mt LALT SLASH
    BT0 ... BT4    -> &bt BT_SEL 0 ... &bt BT_SEL 4
    BTCLR          -> &bt BT_CLR
    BTCLRALL       -> &bt BT_CLR_ALL
    MB1, MB2, MB3  -> &mkp MB1 / &mkp MB2 / &mkp MB3
    TO0 ... TO9    -> &to 0 ... &to 9
    &... で始まるトークンはそのまま生のバインディングとして出力される（エスケープハッチ）
"""
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_PATH = REPO_ROOT / "config" / "keymap.yaml"
OUTPUT_PATH = REPO_ROOT / "config" / "KobitoKey.keymap"

HEADER = """#include <input/processors.dtsi>
#include <behaviors.dtsi>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/pointing.h>
"""

TOKEN_PATTERNS = [
    (re.compile(r"^_$"), lambda m: "&trans"),
    (re.compile(r"^LT(\d+)\((\w+)\)$"), lambda m: f"&lt {m.group(1)} {m.group(2)}"),
    (re.compile(r"^MT\((\w+),(\w+)\)$"), lambda m: f"&mt {m.group(1)} {m.group(2)}"),
    (re.compile(r"^BT(\d+)$"), lambda m: f"&bt BT_SEL {m.group(1)}"),
    (re.compile(r"^BTCLRALL$"), lambda m: "&bt BT_CLR_ALL"),
    (re.compile(r"^BTCLR$"), lambda m: "&bt BT_CLR"),
    (re.compile(r"^MB(\d+)$"), lambda m: f"&mkp MB{m.group(1)}"),
    (re.compile(r"^TO(\d+)$"), lambda m: f"&to {m.group(1)}"),
]


def token_to_binding(token: str) -> str:
    if token.startswith("&"):
        return token
    for pattern, fn in TOKEN_PATTERNS:
        m = pattern.match(token)
        if m:
            return fn(m)
    return f"&kp {token}"


def parse_grid(keys_text: str, rows: int, columns: int, layer_name: str):
    lines = [line.strip() for line in keys_text.strip("\n").splitlines() if line.strip()]
    if len(lines) != rows:
        raise ValueError(
            f"layer '{layer_name}': expected {rows} rows, got {len(lines)}"
        )
    grid = []
    for row_idx, line in enumerate(lines):
        tokens = line.split()
        if len(tokens) != columns:
            raise ValueError(
                f"layer '{layer_name}' row {row_idx}: expected {columns} keys, "
                f"got {len(tokens)} ({line!r})"
            )
        grid.append([token_to_binding(tok) for tok in tokens])
    return grid


def render_layer_bindings(grid) -> str:
    columns = len(grid[0])
    widths = [
        max(len(grid[r][c]) for r in range(len(grid))) for c in range(columns)
    ]
    lines = []
    for row in grid:
        cells = [cell.ljust(widths[i]) for i, cell in enumerate(row)]
        lines.append("  ".join(cells).rstrip())
    return "\n".join(lines)


def render_combos(combos) -> str:
    if not combos:
        return ""
    blocks = []
    for combo in combos:
        name = combo["name"]
        timeout_ms = combo.get("timeout_ms", 50)
        positions = " ".join(str(p) for p in combo["positions"])
        binding = token_to_binding(combo["binding"])
        blocks.append(
            f"""        {name} {{
            timeout-ms = <{timeout_ms}>;
            key-positions = <{positions}>;
            bindings = <{binding}>;
        }};"""
        )
    body = "\n\n".join(blocks)
    return f"""    combos {{
        compatible = "zmk,combos";

{body}
    }};

"""


def render_layers(layers, rows: int, columns: int) -> str:
    blocks = []
    for layer in layers:
        name = layer["name"]
        label = layer.get("label")
        grid = parse_grid(layer["keys"], rows, columns, name)
        bindings_text = render_layer_bindings(grid)
        label_line = f'            label = "{label}";\n' if label else ""
        blocks.append(
            f"""        {name} {{
{label_line}            bindings = <
{bindings_text}
            >;
        }};"""
        )
    return "\n\n".join(blocks)


def main() -> int:
    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))

    layout = data.get("layout", {})
    rows = layout.get("rows", 4)
    columns = layout.get("columns", 10)

    combos_text = render_combos(data.get("combos", []))
    layers_text = render_layers(data["layers"], rows, columns)

    output = f"""{HEADER}
/ {{
{combos_text}    keymap {{
        compatible = "zmk,keymap";

{layers_text}
    }};
}};
"""

    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"generated {OUTPUT_PATH.relative_to(REPO_ROOT)} from {YAML_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
