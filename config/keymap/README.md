# キーマップ設定フォーマット

```
config/
├─ KobitoKey.keymap        … まとめ役（普段は触らない。レイヤー追加時のみ編集）
└─ keymap/
   ├─ kobito.h             … キー位置の図・レイヤー番号・マクロ定義
   ├─ layers/
   │  ├─ 0_base.dtsi       … レイヤー0 QWERTY
   │  ├─ 1_num.dtsi        … レイヤー1 数字・矢印
   │  ├─ 2_func.dtsi       … レイヤー2 Bluetooth・F キー
   │  ├─ 3_mouse.dtsi      … レイヤー3 オートマウス
   │  └─ _template.dtsi.txt… 新レイヤーのひな形
   ├─ combos.dtsi          … コンボ
   └─ behaviors.dtsi       … マクロ・ホールドタップ等（任意）
```

## レイヤーを編集する
`layers/*.dtsi` の 4段×10個（左5＋右5）を書き換えるだけ。

```c
LAYER(layer1, "NUMBER",
    &kp N0  &kp N1  ...  （1段10個 × 4段 = 40個）
)
```

- 何もしない（下のレイヤーを使う）: `&trans`　／　完全に無効: `&none`
- レイヤーは番号の代わりに名前で指定できる: `&lt NUM ENTER`, `&mo FUNC`, `&to BASE`
- 個数が40個でないとビルドエラーになる

## コンボを編集する
`combos.dtsi` に1行ずつ書く。キー位置は `kobito.h` の図の名前（`LM3` など）か番号。

```c
COMBO(   eisu,  LM3 LM4, &kp LANG2 )            // 全レイヤー
COMBO_T( caps,  LB1 LB2, &caps_word, 40 )       // タイムアウト指定
COMBO_L( minus, RT4 RT5, &kp MINUS, BASE NUM )  // レイヤー限定
```

全コンボ共通のタイムアウトは `kobito.h` の `COMBO_TIMEOUT`（初期値50ms）。

## レイヤーを追加する
1. `_template.dtsi.txt` を `layers/4_xxx.dtsi` としてコピーし中身を編集
2. `KobitoKey.keymap` のレイヤー `#include` の最後に `#include "keymap/layers/4_xxx.dtsi"` を追加
3. `kobito.h` に `#define XXX 4` を追加

⚠ `#include` の順番がそのままレイヤー番号。MOUSE(3) はオートマウス設定
（`KobitoKey_left.overlay` の `&zip_temp_layer 3 ...`）でも使っているので番号を変えないこと。

## 注意
- ZMK Studio でキーマップを変更したことがある場合、本体に保存された設定がこのファイルより優先される。
  ファイルの内容を反映させたいときは Studio で「Restore Stock Settings」するか settings_reset を書き込む。
- キーコード一覧: https://zmk.dev/docs/keymaps/list-of-keycodes
# キーマップ設定フォーマット

```
config/
├─ KobitoKey.keymap        … まとめ彷（普段は触らない。レイヤー追加時のみ編集）
└─ keymap/
   ├─ kobito.h             … キー位置の図・レイヤー番号・マクロ定義
   ├─ layers/
   │  ├─ 0_base.dtsi       … レイヤー0 QWERTY
   │  ├─ 1_num.dtsi        … レイヤー1 数字・矢印
   │  ├─ 2_func.dtsi       … レイヤー2 Bluetooth・F キー
   │  ├─ 3_mouse.dtsi      … レイヤー3 オートマウス
   │  └─ _template.dtsi.txt… 新レイヤーのひな形
   ├─ combos.dtsi          … コンボ
   └─ behaviors.dtsi       … マクロ・ホールドタップ等（任意）
```

## レイヤーを編集する
`layers/*.dtsi` の 4段×10個（左5＋右5）を書き換えるだけ。

```c
LAYER(layer1, "NUMBER",
    &kp N0  &kp N1  ...  （1段10個 × 4段 = 40個）
)
```

- 何もしない（下のレイヤーを使う）: `&trans`　／　完全に無効: `&none`
- レイヤーは番号の代わりに名前で指定できる: `&lt NUM ENTER`, `&mo FUNC`, `&to BASE`
- 個数が40個でないとビルドエラーになる

## コンボを編集する
`combos.dtsi` に1行ずつ書く。キー位置は `kobito.h` の図の名前（`LM3` など）か番号。

```c
COMBO(   eisu,  LM3 LM4, &kp LANG2 )            // 全レイヤー
COMBO_T( caps,  LB1 LB2, &caps_word, 40 )       // タイムアウト指定
COMBO_L( minus, RT4 RT5, &kp MINUS, BASE NUM )  // レイヤー限定
```

全コンボ共通のタイムアウトは `kobito.h` の `COMBO_TIMEOUT`（初期値50ms）。

## レイヤーを追加する
1. `_template.dtsi.txt` を `layers/4_xxx.dtsi` としてコピーし中身を編集
2. `KobitoKey.keymap` のレイヤー `#include` の最後に `#include "keymap/layers/4_xxx.dtsi"` を追加
3. `kobito.h` に `#define XXX 4` を追加

⚠ `#include` の順番がそのままレイヤー番号。MOUSE(3) はオートマウス設定
（`KobitoKey_left.overlay` の `&zip_temp_layer 3 ...`）でも使っているので番号を変えないこと。

## 注意
- ZMK Studio でキーマップを変更したことがある場合、本体に保存された設定がこのファイルより優先される。
  ファイルの内容を反映させたいときは Studio で「Restore Stock Settings」するか settings_reset を書き込む。
- キーコード一覧: https://zmk.dev/docs/keymaps/list-of-keycodes
