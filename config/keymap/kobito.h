/*
 * ============================================================
 *  KobitoKey キーマップ用ヘッダ（基本的に編集不要）
 *   - キー位置の名前（コンボ用）
 *   - レイヤー番号の名前
 *   - LAYER / COMBO マクロ
 * ============================================================
 *
 *  ■ キー位置（番号 と 名前）
 *
 *  ┌─────┬─────┬─────┬─────┬─────┐     ┌─────┬─────┬─────┬─────┬─────┐
 *  │  0  │  1  │  2  │  3  │  4  │     │  5  │  6  │  7  │  8  │  9  │
 *  │ LT1 │ LT2 │ LT3 │ LT4 │ LT5 │     │ RT1 │ RT2 │ RT3 │ RT4 │ RT5 │
 *  ├─────┼─────┼─────┼─────┼─────┤     ├─────┼─────┼─────┼─────┼─────┤
 *  │ 10  │ 11  │ 12  │ 13  │ 14  │     │ 15  │ 16  │ 17  │ 18  │ 19  │
 *  │ LM1 │ LM2 │ LM3 │ LM4 │ LM5 │     │ RM1 │ RM2 │ RM3 │ RM4 │ RM5 │
 *  ├─────┼─────┼─────┼─────┼─────┤     ├─────┼─────┼─────┼─────┼─────┤
 *  │ 20  │ 21  │ 22  │ 23  │ 24  │     │ 25  │ 26  │ 27  │ 28  │ 29  │
 *  │ LB1 │ LB2 │ LB3 │ LB4 │ LB5 │     │ RB1 │ RB2 │ RB3 │ RB4 │ RB5 │
 *  ├─────┼─────┼─────┼─────┼─────┤     ├─────┼─────┼─────┼─────┼─────┤
 *  │ 30  │ 31  │ 32  │ 33  │ 34  │     │ 35  │ 36  │ 37  │ 38  │ 39  │
 *  │ LH1 │ LH2 │ LH3 │ LH4 │ LH5 │     │ RH1 │ RH2 │ RH3 │ RH4 │ RH5 │
 *  └─────┴─────┴─────┴─────┴─────┘     └─────┴─────┴─────┴─────┴─────┘
 *   T=上段 M=中段 B=下段 H=最下段(親指)  数字は左から数えた列
 */
#pragma once

/* ---- 左手 ---- */
#define LT1 0
#define LT2 1
#define LT3 2
#define LT4 3
#define LT5 4
#define LM1 10
#define LM2 11
#define LM3 12
#define LM4 13
#define LM5 14
#define LB1 20
#define LB2 21
#define LB3 22
#define LB4 23
#define LB5 24
#define LH1 30
#define LH2 31
#define LH3 32
#define LH4 33
#define LH5 34
/* ---- 右手 ---- */
#define RT1 5
#define RT2 6
#define RT3 7
#define RT4 8
#define RT5 9
#define RM1 15
#define RM2 16
#define RM3 17
#define RM4 18
#define RM5 19
#define RB1 25
#define RB2 26
#define RB3 27
#define RB4 28
#define RB5 29
#define RH1 35
#define RH2 36
#define RH3 37
#define RH4 38
#define RH5 39

/*
 * ■ レイヤー番号
 *   KobitoKey.keymap の #include の順番と必ず一致させること。
 *   MOUSE(3) は KobitoKey_left.overlay のオートマウス設定
 *   (&zip_temp_layer 3 ...) からも参照されている。
 */
#define BASE  0
#define NUM   1
#define FUNC  2
#define MOUSE 3

/*
 * ■ LAYER(ノード名, "表示名", バインディング...)
 *   40個のバインディングを左上から順に並べる。
 *   ノード名は英数字と _ のみ。表示名は ZMK Studio に出る名前。
 */
#define LAYER(_node, _name, ...)       \
    / {                                \
        keymap {                       \
            _node {                    \
                display-name = _name;  \
                bindings = <__VA_ARGS__>; \
            };                         \
        };                             \
    };

/*
 * ■ コンボ
 *   COMBO(名前, キー位置, バインディング)
 *     全レイヤー共通。タイムアウトは COMBO_TIMEOUT。
 *   COMBO_T(名前, キー位置, バインディング, タイムアウトms)
 *     タイムアウトを個別に指定。
 *   COMBO_L(名前, キー位置, バインディング, レイヤー)
 *     指定したレイヤーでのみ有効（例: BASE NUM）。
 */
#ifndef COMBO_TIMEOUT
#define COMBO_TIMEOUT 50
#endif

#define COMBO_T(_name, _pos, _bind, _timeout) \
    / {                                         \
        combos {                                \
            combo_##_name {                     \
                timeout-ms = <_timeout>;        \
                key-positions = <_pos>;         \
                bindings = <_bind>;             \
            };                                  \
        };                                      \
    };

#define COMBO(_name, _pos, _bind) COMBO_T(_name, _pos, _bind, COMBO_TIMEOUT)

#define COMBO_L(_name, _pos, _bind, _layers)    \
    / {                                         \
        combos {                                \
            combo_##_name {                     \
                timeout-ms = <COMBO_TIMEOUT>;   \
                key-positions = <_pos>;         \
                bindings = <_bind>;             \
                layers = <_layers>;             \
            };                                  \
        };                                      \
    };
