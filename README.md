# 🗺️ Clustering Map

Excelアンケート結果からクラスタリングマップを生成するWebアプリケーション

## 📋 機能

- **Excelファイルアップロード**: アンケート結果のExcelファイルをアップロード
- **自動タグ生成**: ビジネス文脈に沿ったタグを自動生成
- **可視化**: クラスタリング結果を美しいマップで可視化
- **カスタム図形**: 円形、四角形、三角形、ハート、星形、六角形から選択可能

## 🚀 デプロイ方法

### Vercelでのデプロイ

1. **GitHubリポジトリを作成**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/clustering-map.git
git push -u origin main
```

2. **Vercelでプロジェクトを作成**
- [Vercel](https://vercel.com)にアクセス
- GitHubアカウントでログイン
- 「Add New Project」をクリック
- リポジトリを選択

3. **設定**
   - **Framework Preset**: Vite
   - **Root Directory**: `clustering-map-frontend`
   - **Build Command**: `cd clustering-map-frontend && npm run build`
   - **Output Directory**: `dist`

4. **環境変数の設定（オプション）**
   ```
   PYTHON_VERSION=3.11
   PYTHONPATH=./clustering-map-backend
   ```

5. **デプロイ**
   - 「Deploy」をクリック

### Renderでのデプロイ（従来の方法）

詳細は `clustering-map-backend/render.yaml` および `clustering-map-frontend/render.yaml` を参照

## 📁 プロジェクト構成

```
.
├── api/                           # Vercel Serverless Functions
│   ├── index.py
│   └── vercel_adapter.py
├── clustering-map-backend/        # バックエンド（FastAPI）
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   └── requirements.txt
├── clustering-map-frontend/        # フロントエンド（React + Vite）
│   ├── src/
│   │   ├── components/
│   │   ├── utils/
│   │   └── types/
│   └── package.json
├── vercel.json                    # Vercel設定
└── README.md                      # このファイル
```

## 🛠️ ローカル開発

### バックエンド
```bash
cd clustering-map-backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### フロントエンド
```bash
cd clustering-map-frontend
npm install
npm run dev
```

## 📝 使用技術

### バックエンド
- **FastAPI**: 高速なAPIフレームワーク
- **Python 3.11**: 実行環境
- **Sklearn**: 機械学習ライブラリ
- **Pandas**: データ処理
- **OpenPyXL**: Excel処理

### フロントエンド
- **React 18**: UIライブラリ
- **TypeScript**: 型安全性
- **Vite**: 高速なビルドツール
- **Tailwind CSS**: ユーティリティCSS
- **Echarts**: データ可視化

## 📊 利用方法

1. **テンプレートをダウンロード**: サンプルデータ付きExcelテンプレートを取得
2. **データを入力**: アンケート結果を「自由記述」列に入力
3. **ファイルをアップロード**: Excelファイルをドラッグ&ドロップ
4. **タグを確認**: 自動生成されたタグを確認・編集
5. **マップの形状を選択**: 円形、四角形などから選択
6. **解析を実行**: クラスタリング処理を開始
7. **結果を確認**: 生成されたマップを確認

## 🐛 トラブルシューティング

### ビルドエラー
- Node.jsバージョンを18以上に確認
- `npm install`で依存関係を再インストール

### APIエラー
- 環境変数が正しく設定されているか確認
- `/api/health`エンドポイントでバックエンドの状態を確認

## 📄 ライセンス

MIT License

