# 🔧 パッケージサイズ削減の修正

## 問題

VercelのServerless Functionが250MBを超えるサイズエラーが発生

## 修正内容

### 1. requirements.txt の削減
**削除した重いライブラリ**:
- matplotlib
- seaborn
- plotly
- reportlab
- pillow
- scipy
- uvicorn[standard] → uvicorn（標準版の一部機能を削除）

**保持したライブラリ**:
- fastapi
- uvicorn
- pydantic
- pandas
- numpy
- openpyxl
- python-multipart
- aiofiles
- python-dotenv
- mangum
- scikit-learn

### 2. simple_export_service.py の簡素化
- matplotlib/pyplotをインポートから削除
- エクスポート機能を無効化（Vercelでは不要）

### 3. 注意事項
- PDF/PNGエクスポート機能は無効化
- Vercelでは直接可視化のみサポート

## 次のステップ

1. **コミット**
```bash
git add clustering-map-backend/requirements.txt clustering-map-backend/app/services/simple_export_service.py api/index.py vercel.json clustering-map-frontend/src/components/UploadStep.tsx clustering-map-frontend/src/components/ProgressIndicator.tsx
git commit -m "Reduce package size for Vercel deployment"
git push origin master
```

2. **Vercelで再デプロイ**
- 自動的に新しいコミットが検出される
- デプロイが成功することを確認

