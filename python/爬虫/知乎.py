import requests
import json
import time

def fetch_zhihu_hotlist():
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.zhihu.com/hot',
        'Coookie': '_xsrf=78UXt1k3vP9in9stGu0ACVSRifLSaPVh; _zap=8f16ae96-9752-4f9a-8891-4f07d16dcc83; d_c0=lYLT3lDtJBqPTphA0SBZpKdSas6tOIByrFM=|1741934728; __snaker__id=Hi1JrWI0WWodhofz; q_c1=0caf13a86f8242ad95b6b1c77331c43c|1742175060000|1742175060000; edu_user_uuid=edu-v1|6b116e80-14aa-4a01-900f-32e0f2ae2aff; _tea_utm_cache_20001731={%22utm_content%22:%22search_suggestion%22}; z_c0=2|1:0|10:1747701575|4:z_c0|80:MS4xQktVa0JBQUFBQUFtQUFBQVlBSlZUVWNkR1duRGJWTEEwSjRLMmVNVW1Lbm5aZEk1ZlEwR0RRPT0=|d2c77c39c2f6de40a5d1ec7c185346b1d0963cb080cb9faeb1b8f9e687c9c0ab; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1746584285,1747096740,1747700185,1747902125; HMACCOUNT=2ECD045862AA3D7E; SESSIONID=s8lRlMV9dAyyuJns7j73amPosSYafvJWYtpg73cllkX; JOID=VVgWA03uisIVhPXyE-pOVQzQH9ANmrGtQem_pymLzLhv976bY0RU6XqC8fIWt79nn-bW3syq9_juHYo4Ows5rOc=; osd=W14cAUjgjMgXgfv0GehLWwraHdUDnLuvROe5rSuOwr5l9buVZU5W7HSE-_ATubltnePY2Mao8vboF4g9NQ0zruI=; __zse_ck=004_P=fNo1MlqHlT6DIYgi9jTdj2bF50WfvaDkmC4fZ=Fp96/ekPMM72qYZOPnpci0789=FQKDfsKmR4cSokTlWw64y9mica9DuHrCAnC0bPeQ3ODl46DXjeI7FPCwsAtP=y-4Mgk5uADksFwda+8x8SvUn4U1ot54J7EogVG9Swbys5X/3aTAi8nbqLdVpf9ZvdFhzyLHTqxFnBUkXwyQ1t2aN107Vfh59kniptZc0HgtHd5piPxu1hSTv97DiW6VQmOqr7hc0NxYZztLc7VGFArGoyOjBR1Pt0AnLvJFtsQ0jM=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1747903743; BEC=32377ec81629ec05d48c98f32428ae46; tst=h'
        # 设置请求头中的Referer字段，指定请求来源页面为知乎热门页面
    }

    # API地址（需自行维护最新地址）
    api_url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=100"

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    
    except Exception as e:
        print(f"请求失败：{str(e)}")
        return []

def display_hotlist(hotlist):
    print("📈 知乎热榜实时追踪")
    print(f"更新时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for index, item in enumerate(hotlist, 1):
        target = item.get('target', {})
        title = target.get('title', '无标题')
        url = target.get('url', '').replace("api.zhihu.com/questions", "www.zhihu.com/question")
        metrics = target.get('metrics_area', {})
        
        print(f"{index}. {title}")
        print(f"   🔥 热度：{metrics.get('text', '未知')}")
        print(f"   🔗 链接：{url}\n")

if __name__ == "__main__":
    hotlist = fetch_zhihu_hotlist()
    if hotlist:
        display_hotlist(hotlist)
    else:
        print("未能获取热榜数据")