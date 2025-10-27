"""
Vercel Serverless Functions adapter for FastAPI
"""
import sys
from pathlib import Path

# Vercel上でのパス設定
sys.path.insert(0, str(Path(__file__).parent.parent / 'clustering-map-backend'))

from app.main import app
from mangum import Mangum

# Mangumを使用してFastAPIアプリをVercel対応
handler = Mangum(app)

def lambda_handler(event, context):
    """Vercel/Lambda互換ハンドラ"""
    return handler(event, context)

