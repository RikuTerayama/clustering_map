import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
import logging
from pathlib import Path
import json
import os
from datetime import datetime

from app.models.schemas import DataPoint
from app.models.config import AppConfig

logger = logging.getLogger(__name__)


class SimpleExportService:
    """軽量版エクスポートサービス"""
    
    def __init__(self):
        self.config = AppConfig()
    
    def export_pdf(self, data_points: List[DataPoint], output_path: str, title: str = "Clustering Map") -> bool:
        """PDFエクスポート（軽量版 - 無効化）"""
        try:
            # Vercel Serverless Functionsでは重いライブラリを削除
            logger.warning("PDF export is disabled on Vercel to reduce package size")
            return False
            
            # PDFとして保存
            plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
            plt.close()
            
            logger.info(f"PDF exported successfully: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"PDF export failed: {e}")
            return False
    
    def export_png(self, data_points: List[DataPoint], output_path: str, title: str = "Clustering Map") -> bool:
        """PNGエクスポート（軽量版 - 無効化）"""
        try:
            logger.warning("PNG export is disabled on Vercel to reduce package size")
            return False

    def export_to_pdf(self) -> str:
        """PDFエクスポート（引数なし版）"""
        try:
            # ダミーデータを生成
            data_points = self._generate_dummy_data()
            
            # 出力パスを生成
            output_path = os.path.join(self.config.results_dir, f"clustering_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # PDFエクスポート
            success = self.export_pdf(data_points, output_path, "Clustering Map")
            if success:
                return output_path
            else:
                raise Exception("PDF export failed")
                
        except Exception as e:
            logger.error(f"PDF export failed: {e}")
            raise Exception(f"PDFエクスポートに失敗しました: {str(e)}")

    def export_to_png(self) -> str:
        """PNGエクスポート（引数なし版）"""
        try:
            # ダミーデータを生成
            data_points = self._generate_dummy_data()
            
            # 出力パスを生成
            output_path = os.path.join(self.config.results_dir, f"clustering_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # PNGエクスポート
            success = self.export_png(data_points, output_path, "Clustering Map")
            if success:
                return output_path
            else:
                raise Exception("PNG export failed")
                
        except Exception as e:
            logger.error(f"PNG export failed: {e}")
            raise Exception(f"PNGエクスポートに失敗しました: {str(e)}")

    def _generate_dummy_data(self) -> List[DataPoint]:
        """ダミーデータを生成"""
        dummy_texts = [
            "このサービスはとても使いやすく、機能も充実しています。",
            "料金が少し高いと感じます。もう少し安くなれば利用したいです。",
            "サポートが丁寧で、問題がすぐに解決されました。",
            "機能は良いのですが、もう少しシンプルな操作ができると良いです。",
            "全体的に満足しています。継続して利用したいと思います。"
        ]
        
        data_points = []
        for i, text in enumerate(dummy_texts):
            data_points.append(DataPoint(
                id=i,
                text=text,
                x=np.random.uniform(0, 1),
                y=np.random.uniform(0, 1),
                cluster_id=i % 3,
                tags=[f"tag_{i % 3}"],
                metadata={"word_count": len(text.split())}
            ))
        
        return data_points
