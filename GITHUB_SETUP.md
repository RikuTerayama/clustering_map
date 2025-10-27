# 📤 GitHubセットアップガイド

## ✅ まとめ

1. **1つのリポジトリでOK**: フロントエンドとバックエンドを同じリポジトリに配置
2. **既存のファイル構成を維持**: そのままで問題ありません
3. **新しく追加したファイル**:
   - `vercel.json` (Vercel設定)
   - `api/index.py` と `api/vercel_adapter.py` (Vercel Functions)
   - `.gitignore` (Git無視ファイル)
   - `README.md` (プロジェクト説明)

## 🚀 アップロード手順

### 1. ローカルリポジトリの初期化（まだの場合）

```bash
cd "C:\Users\YCP\Downloads\crystalizing map"
git init
git branch -M main
```

### 2. ファイルをステージング

```bash
git add .
```

### 3. 初回コミット

```bash
git commit -m "Initial commit: Clustering Map application"
```

### 4. GitHubにリポジトリを作成

1. [GitHub](https://github.com)にアクセス
2. 「New repository」をクリック
3. 以下を入力：
   - **Repository name**: `clustering-map`
   - **Description**: Excelアンケート結果からクラスタリングマップを生成するWebアプリケーション
   - **Visibility**: Public または Private
4. 「Create repository」をクリック

### 5. リモートリポジトリを追加

```bash
git remote add origin https://github.com/YOUR_USERNAME/clustering-map.git
```

（`YOUR_USERNAME`を実際のGitHubユーザー名に置き換え）

### 6. プッシュ

```bash
git push -u origin main
```

## 📁 アップロードされるファイル

```
clustering-map/
├── api/                           ✅ 新規追加
│   ├── index.py
│   └── vercel_adapter.py
├── clustering-map-backend/         ✅ 既存
│   ├── app/
│   └── requirements.txt
├── clustering-map-frontend/        ✅ 既存
│   ├── src/
│   └── package.json
├── vercel.json                     ✅ 新規追加
├── .gitignore                      ✅ 新規追加
├── README.md                       ✅ 新規追加
└── VERCEL_DEPLOYMENT.md            ✅ 新規追加
```

## ⚠️ アップロードされないファイル

`.gitignore`により、以下のファイルはアップロードされません：
- `node_modules/`（巨大なため）
- `dist/`（ビルド結果）
- `.env`（環境変数、機密情報）
- `*.log`（ログファイル）

## 🔄 デプロイ手順

### Vercelでのデプロイ

1. [Vercel](https://vercel.com)にアクセス
2. GitHubでログイン
3. 「Add New Project」をクリック
4. `clustering-map`リポジトリを選択
5. 設定：
   - **Framework Preset**: Vite
   - **Root Directory**: `clustering-map-frontend`
   - **Build Command**: `cd clustering-map-frontend && npm run build`
   - **Output Directory**: `dist`
6. 「Deploy」をクリック

### 環境変数（オプション）

Settings → Environment Variables で以下を追加：
```
PYTHON_VERSION=3.11
```

## 🎉 完了！

これで GitHub へのアップロードと Vercel デプロイの準備が完了しました！

