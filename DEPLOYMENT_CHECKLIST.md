# 🚀 Vercelデプロイ チェックリスト

## ⚠️ 発見された問題と対処

### ❌ 重大な問題

1. **ネストされたGitリポジトリ**
   - `clustering-map-backend/.git` を削除済み
   - `clustering-map-frontend/.git` を削除済み
   - これがないと Vercel は正しくファイルを認識できません

2. **ディレクトリ構成の変更**
   - 古い構成（`app/`, `frontend/`）を削除
   - 新しい構成（`clustering-map-backend/`, `clustering-map-frontend/`）を追加

### ✅ 修正済み

1. **Vercel設定**
   - `vercel.json` を修正
   - ビルドコマンドと出力ディレクトリを設定

2. **API設定**
   - `api/index.py` で Mangum を使用
   - パス設定を修正

3. **依存関係**
   - `requirements.txt` に Mangum を追加
   - `api/requirements.txt` を作成

4. **設定ファイル**
   - CORS設定をVercel対応に変更
   - 一時ディレクトリを `/tmp` に変更

### ⚠️ 潜在的な問題

1. **メモリ不足**
   - **問題**: scikit-learn, matplotlib, seaborn などが重い
   - **Vercel制限**: Freeプランは1024MB、Proは3GB
   - **対策**: 最初に動作確認、必要に応じてライブラリを削減

2. **タイムアウト**
   - **問題**: Vercel Serverless Functions は最大30秒（Proで60秒）
   - **現在の実装**: 解析処理は30秒以内で完了可能
   - **対策**: 問題が発生した場合は処理を最適化

3. **ファイルサイズ**
   - **問題**: デプロイパッケージが大きすぎる可能性
   - **Vercel制限**: 50MB（Free）、250MB（Pro）
   - **対策**: `node_modules/` と `dist/` を `.gitignore` に追加済み

## 📋 デプロイ手順

### 1. コミットとプッシュ
```bash
git commit -m "Setup Vercel deployment"
git remote add origin https://github.com/YOUR_USERNAME/clustering-map.git
git push -u origin master
```

### 2. Vercelでプロジェクトを作成

1. [Vercel](https://vercel.com)にアクセス
2. GitHubでログイン
3. 「Add New Project」をクリック
4. リポジトリを選択

### 3. プロジェクト設定

- **Framework Preset**: Other
- **Root Directory**: `./`（ルートを指定）
- **Build Command**: `cd clustering-map-frontend && npm run build`
- **Output Directory**: `clustering-map-frontend/dist`

### 4. 環境変数（Settings → Environment Variables）

```
PYTHON_VERSION=3.11
NODE_VERSION=18
```

### 5. デプロイ実行
- 「Deploy」をクリック

## 🐛 トラブルシューティング

### ビルドエラーの場合

1. **エラー**: "Module not found"
   - 解決策: パス設定を確認、`sys.path.insert(0, ...)` を追加

2. **エラー**: "Memory limit exceeded"
   - 解決策: 重いライブラリを削除または最適化

3. **エラー**: "Timeout"
   - 解決策: 処理時間を短縮、またはProプランにアップグレード

### APIエラーの場合

1. **404エラー**
   - 解決策: `/api/*` のルーティングを確認

2. **CORSエラー**
   - 解決策: CORS設定を確認、Vercel URLを追加

3. **インポートエラー**
   - 解決策: `api/index.py` のパス設定を確認

## ✅ 最終確認事項

- [ ] ネストされたGitリポジトリを削除した
- [ ] 新しいディレクトリ構成に変更した
- [ ] Vercel設定ファイルを作成した
- [ ] 依存関係を更新した
- [ ] CORS設定を更新した
- [ ] 一時ディレクトリを `/tmp` に変更した
- [ ] `.gitignore` を更新した
- [ ] READMEを更新した

## 🎉 準備完了！

これで Vercel にデプロイする準備が整いました！

