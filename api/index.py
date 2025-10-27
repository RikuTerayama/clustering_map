"""
Vercel Serverless Functions entry point
"""
import sys
from pathlib import Path

# Vercel上でのパス設定
backend_path = Path(__file__).parent.parent / 'clustering-map-backend'
sys.path.insert(0, str(backend_path))

from app.main import app
from mangum import Mangum

# Mangumを使用してFastAPIアプリをVercel対応
handler = Mangum(app)

def lambda_handler(event, context):
    """Vercel/Lambda互換ハンドラ"""
    return handler(event, context)

