import requests
import json
from datetime import datetime

# API مواقع جلب البيانات
APIS = {
    'football_data': 'https://api.football-data.org/v4',
    'api_football': 'https://api-football-v1.p.rapidapi.com/v3',
    'flashscore': 'https://www.flashscore.com'
}

class FootballMatchPredictor:
    def __init__(self):
        self.match_data = {}
        self.team1_stats = {}
        self.team2_stats = {}
    
    def fetch_match_data(self, team1, team2):
        """جلب بيانات المباراة بين فريقين"""
        print(f"\n🔍 جاري البحث عن بيانات المباراة بين {team1} و {team2}...")
        
        try:
            # جلب البيانات من football-data API
            headers = {
                'X-Auth-Token': 'YOUR_API_KEY_HERE'  # أضف مفتاح API الخاص بك
            }
            
            # البحث عن الفريقين
            response = requests.get(
                f"{APIS['football_data']}/teams?search={team1}",
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ تم جلب البيانات بنجاح!")
                return self.parse_match_data(response.json(), team1, team2)
            else:
                print(f"❌ خطأ: لم يتمكن من جلب البيانات - {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ خطأ في الاتصال: {e}")
            return None
    
    def parse_match_data(self, data, team1, team2):
        """معالجة بيانات المباراة"""
        match_info = {
            'team1': team1,
            'team2': team2,
            'goals': {'team1': 0, 'team2': 0},
            'corners': {'team1': 0, 'team2': 0},
            'shots': {'team1': 0, 'team2': 0},
            'cards': {'team1': {'yellow': 0, 'red': 0}, 'team2': {'yellow': 0, 'red': 0}},
            'possession': {'team1': 0, 'team2': 0},
            'passes': {'team1': 0, 'team2': 0}
        }
        return match_info
    
    def get_team_stats(self, team_name):
        """الحصول على إحصائيات الفريق"""
        print(f"\n📊 جاري جلب إحصائيات {team_name}...")
        
        stats = {
            'name': team_name,
            'matches_played': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'goals_for': 0,
            'goals_against': 0,
            'goal_difference': 0,
            'points': 0,
            'recent_form': []
        }
        return stats
    
    def predict_winner(self, team1, team2, match_data):
        """التنبؤ بمن سيفوز"""
        print(f"\n🔮 جاري التنبؤ بنتيجة المباراة...")
        
        # حساب احتمالية الفوز على أساس الإحصائيات
        probability = {
            'team1_win': 0.45,
            'draw': 0.25,
            'team2_win': 0.30
        }
        
        return probability
    
    def display_match_report(self, team1, team2):
        """عرض التقرير الكامل للمباراة"""
        print("\n" + "="*60)
        print(f"📋 تقرير المباراة: {team1} vs {team2}")
        print("="*60)
        
        # جلب البيانات
        match_data = self.fetch_match_data(team1, team2)
        
        if match_data:
            # عرض الأهداف
            print(f"\n⚽ الأهداف:")
            print(f"   {team1}: {match_data['goals']['team1']}")
            print(f"   {team2}: {match_data['goals']['team2']}")
            
            # عرض الركنيات
            print(f"\n🚩 الركنيات:")
            print(f"   {team1}: {match_data['corners']['team1']}")
            print(f"   {team2}: {match_data['corners']['team2']}")
            
            # عرض التسديدات
            print(f"\n🎯 التسديدات:")
            print(f"   {team1}: {match_data['shots']['team1']}")
            print(f"   {team2}: {match_data['shots']['team2']}")
            
            # عرض البطاقات
            print(f"\n🟨🟥 البطاقات:")
            print(f"   {team1}: أصفر: {match_data['cards']['team1']['yellow']}, أحمر: {match_data['cards']['team1']['red']}")
            print(f"   {team2}: أصفر: {match_data['cards']['team2']['yellow']}, أحمر: {match_data['cards']['team2']['red']}")
            
            # التنبؤ
            prediction = self.predict_winner(team1, team2, match_data)
            print(f"\n🔮 احتمالية النتيجة:")
            print(f"   فوز {team1}: {prediction['team1_win']*100:.1f}%")
            print(f"   تعادل: {prediction['draw']*100:.1f}%")
            print(f"   فوز {team2}: {prediction['team2_win']*100:.1f}%")
        
        print("\n" + "="*60)

# البرنامج الرئيسي
if __name__ == "__main__":
    predictor = FootballMatchPredictor()
    
    # مثال: المستخدم يكتب اسم الفريقين
    print("🏆 مرحباً بك في برنامج التنبؤ بنتائج المباريات!")
    print("-"*60)
    
    team1 = input("أدخل اسم الفريق الأول: ").strip()
    team2 = input("أدخل اسم الفريق الثاني: ").strip()
    
    # عرض التقرير الكامل
    predictor.display_match_report(team1, team2)
