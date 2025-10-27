# 🚀 Vercelへのデプロイガイド

## 📋 前提条件
1. GitHubアカウント
2. Vercelアカウント（GitHubでサインアップ可能）

## 🔧 デプロイ手順

### 1. GitHubにリポジトリをプッシュ
```bash
git add .
git commit -m "Add Vercel configuration"
git push origin main
```

### 2. Vercelにプロジェクトをインポート

1. [Vercel](https://vercel.com/)にログイン
2. 「Add New Project」をクリック
3. GitHubリポジトリを選択
4. プロジェクト設定：
   - **Framework Preset**: Vite
   - **Root Directory**: `./clustering-map-frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   
5. 「Deploy」をクリック

### 3. バックエンド設定（Serverless Functions）

Vercelのプロジェクト設定で、以下を追加：

**Settings → Environment Variables:**
```
PYTHON_VERSION=3.11
PYTHONPATH=./clustering-map-backend
```

### 4. ビルド設定の追加

`vercel.json`が既に作成されていますが、より詳細な設定が必要な場合：

```json
{
  "builds": [
    {
      "src": "clustering-map-frontend/package.json",
      "use": "@vercel/static-build"
    },
    {
      "src": "clustering-map-backend/app/main.py",
      "use": "@vercel/python"
    }
  ]
}
```

## 📁 ディレクトリ構成

```
project-root/
├── api/
│   └── index.py           # Vercel Functions entry point
├── clustering-map-backend/
│   ├── app/
│   │   └── main.py        # FastAPIアプリ
│   └── requirements.txt
├── clustering-map-frontend/
│   ├── src/
│   ├── dist/              # ビルド出力
│   └── package.json
├── vercel.json            # Vercel設定
├── build.sh              # ビルドスクリプト
└── VERCEL_DEPLOYMENT.md  # このファイル
```

## 🔄 デプロイ後の確認

### フロントエンド
- URL: `https://your-project.vercel.app`

### バックエンドAPI
- URL: `https://your-project.vercel.app/api`
- Health check: `https://your-project.vercel.app/api/health`

## 🐛 トラブルシューティング

### ビルドエラーの場合
1. 「Deployments」タブでログを確認
2. 環境変数が正しく設定されているか確認
3. Pythonバージョンが3.11か確認

### API エラーの場合
1. `/api`エンドポイントが正しく動作しているか確認
2. CORS設定を確認
3. サーバーログを確認

## 📝 注意事項

1. **Serverless Functions の制限**:
   - 実行時間: 最大30秒（プロ版で60秒）
   - メモリ: 最大1GB（プロ版で3GB）
   - タイムアウトに注意

2. **環境変数**:
   - 本番環境と開発環境で異なる値を設定
   - 機密情報は環境変数で管理

3. **ドメイン**:
   - 自動的にサブドメインが割り当て
   - カスタムドメインも設定可能

## 🎉 完了！

これで Vercel へのデプロイが完了です！

