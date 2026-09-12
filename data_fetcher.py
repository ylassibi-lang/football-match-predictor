"""
خادم API للتطبيق - يجلب البيانات من المواقع العالمية
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    """فئة جلب البيانات من المواقع العالمية"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.timeout = 10
    
    def fetch_sofascore(self, team_name):
        """جلب البيانات من Sofascore"""
        try:
            url = f"https://www.sofascore.com/football/search?q={team_name}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"✅ تم جلب البيانات من Sofascore: {team_name}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"❌ خطأ في جلب بيانات Sofascore: {e}")
            return False
    
    def fetch_espn(self, team_name):
        """جلب البيانات من ESPN"""
        try:
            url = f"https://www.espn.com/soccer/search?query={team_name}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"✅ تم جلب البيانات من ESPN: {team_name}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"❌ خطأ في جلب بيانات ESPN: {e}")
            return False
    
    def fetch_footystats(self, team_name):
        """جلب البيانات من FootyStats"""
        try:
            url = f"https://footystats.org/search?q={team_name}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"✅ تم جلب البيانات من FootyStats: {team_name}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"❌ خطأ في جلب بيانات FootyStats: {e}")
            return False
    
    def fetch_fbreference(self, team_name):
        """جلب البيانات من FBref"""
        try:
            url = f"https://fbref.com/en/search/search.php?search={team_name}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"✅ تم جلب البيانات من FBref: {team_name}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"❌ خطأ في جلب بيانات FBref: {e}")
            return False
    
    def fetch_aiscore(self, team1, team2):
        """جلب سجل المواجهات من AiScore"""
        try:
            url = f"https://www.aiscore.com/head-to-head/soccer-{team2.lower().replace(' ', '-')}-vs-{team1.lower().replace(' ', '-')}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"✅ تم جلب سجل المواجهات من AiScore: {team1} vs {team2}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"❌ خطأ في جلب سجل المواجهات: {e}")
            return False
    
    def fetch_all_data(self, team1, team2):
        """جلب البيانات من جميع المواقع"""
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "team1": team1,
            "team2": team2,
            "sources": {
                "sofascore": self.fetch_sofascore(team1) and self.fetch_sofascore(team2),
                "espn": self.fetch_espn(team1) and self.fetch_espn(team2),
                "footystats": self.fetch_footystats(team1) and self.fetch_footystats(team2),
                "fbreference": self.fetch_fbreference(team1) and self.fetch_fbreference(team2),
                "aiscore": self.fetch_aiscore(team1, team2)
            }
        }
        
        # عد المصادر الناجحة
        successful_sources = sum(1 for v in results["sources"].values() if v)
        results["successful_sources"] = successful_sources
        results["total_sources"] = len(results["sources"])
        
        return results

# اختبار
if __name__ == "__main__":
    fetcher = DataFetcher()
    data = fetcher.fetch_all_data("Gamba Osaka", "FC Tokyo")
    print(json.dumps(data, indent=2, ensure_ascii=False))
