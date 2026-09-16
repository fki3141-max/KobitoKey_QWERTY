# KobitoKey_QWERTY

小人キーや人キーのケース、TypeSurfer各種の3DデータはReleasesよりダウンロード出来ます。
ダサい使い方はしないこと。

## キーマップの編集方法

`config/KobitoKey.keymap` は ZMK が読み込むファイルですが、devicetree構文で書かれていて直接編集するのは分かりにくいため、
より直感的に書ける `config/keymap.yaml` から自動生成できるようにしています。

1. `config/keymap.yaml` を編集する（1行 = 1段、半角スペース区切りで10列分のキーを並べるだけ）
2. 生成スクリプトを実行してビルド対象の `.keymap` を再生成する

   ```sh
   pip install -r scripts/requirements.txt   # 初回のみ（PyYAMLが必要）
   python3 scripts/generate_keymap.py
   ```

3. 差分を確認し、`config/keymap.yaml` と `config/KobitoKey.keymap` の両方をコミットする

`keymap.yaml` のトークン表記（詳細はファイル冒頭のコメント参照）:

| 書き方 | 意味 |
| --- | --- |
| `_` | 何もしない（`&trans`） |
| `Q` `N1` `SEMI` など | 通常のキーコード（`&kp Q` など） |
| `LT2(SPACE)` | レイヤー2へのタップホールド（`&lt 2 SPACE`） |
| `MT(LALT,SLASH)` | モッドタップ（`&mt LALT SLASH`） |
| `BT0`〜`BT4` | Bluetoothプロファイル選択 |
| `BTCLR` / `BTCLRALL` | Bluetoothプロファイルの解除 |
| `MB1`〜`MB3` | マウスボタン |
| `TO0`〜`TO9` | レイヤー切り替え |
| `&...` で始まるもの | 上記にない場合の生のバインディング（エスケープハッチ） |

レイヤーの追加・削除やコンボ（`combos:`）の変更も同じYAMLファイル内で行えます。


Layer 0 QWERTY
<img width="1280" height="690" alt="Image" src="https://github.com/user-attachments/assets/ef0797b7-a63f-4632-912d-9b5d0115769f" />

Layer 1 NUMBER & ARROW
<img width="1280" height="690" alt="Image" src="https://github.com/user-attachments/assets/d6347b3c-a238-4278-bacd-e58195774d0e" />

Layer 2 Bluetooth & FUNCTION
<img width="1280" height="690" alt="Image" src="https://github.com/user-attachments/assets/f1f7cc93-fbd8-4a98-84ea-c8c36ad3952d" />

Layer 3 AUTO MOUSE
<img width="1280" height="690" alt="Image" src="https://github.com/user-attachments/assets/2efe5275-e460-41bc-ae45-0c0665435268" />
