"""
Vercel Serverless Functions entry point
Simple handler that imports the FastAPI app
"""
import sys
from pathlib import Path

# Add backend to Python path
backend_path = Path(__file__).parent.parent / 'clustering-map-backend'
sys.path.insert(0, str(backend_path))

# Import FastAPI app
from app.main import app
from mangum import Mangum

# Create Mangum handler
handler = Mangum(app)

