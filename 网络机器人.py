import requests
import csv
from lxml import html
import re
#常量
TMDB_URL = 'https://www.themoviedb.org'
TMDB_TOP_URL = 'https://www.themoviedb.org/movie/top-rated'
TMDB_TOP_URL2='https://www.themoviedb.org/discover/movie/items'

#获取电影上映时间
def get_date(movie_date):
    date=re.findall(r"\d{4}-\d{2}-\d{2}", movie_date[0].strip() if movie_date else "")
    return date[0]

#获取时长
def get_duration(movie_duration):
    h_d=re.findall(r"(\d+)h",movie_duration[0].strip() if movie_duration else "")
    m_d=re.findall(r"(\d+)m",movie_duration[0].strip() if movie_duration else "")
    h=int(h_d.group(1)) if h_d else 0
    m=int(m_d.group(1)) if m_d else 0
    return h*60+m
#获取详情
def get_detail(movie_info_url):
    #发送请求,获取详情
    movie_response = requests.get(movie_info_url,timeout=60)
    #解析数据
    movie_doc = html.fromstring(movie_response.text)
    movie_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_score = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_date = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_type = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_actor = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_duration = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_intro = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    movie_language = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    #组装并返回数据
    movie_info={
        "name": movie_name[0].strip() if movie_name else "",
        "intro": movie_intro[0].strip() if movie_intro else "",
        "language": movie_language[0].strip() if movie_language else "",
        "date":get_date(movie_date),
        "score": movie_score[0].strip() if movie_score else "",
        "type":",".join(movie_type) if movie_type else "",
        "duration":get_duration(movie_duration),
        "actor": movie_actor[0].strip() if movie_actor else ""
    }
    return movie_info

#保存数据--csv
def save_data(all_movies):
    with open("movies.csv", "w", encoding="utf-8", newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["name", "intro", "language", "date", "score", "type", "duration", "actor"])
        writer.writeheader()
        writer.writerows(all_movies)
#主函数
def main():
    all_movies=[]
    for page in range(1,6):
        #发送请求,获取电影榜单
        if page==1:
            response = requests.get(TMDB_TOP_URL,timeout=60)
            print(f"发送请求,获取第{page}页电影榜单")
        else:
            response = requests.post(TMDB_TOP_URL2,
                      data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-04-07&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated",               
            timeout=60)
            print(f"发送请求,获取第{page}页电影榜单")
        #解析数据获得榜单列表
        doc = html.fromstring(response.text)
        movie_list = doc.xpath("//div[@class='media-list-results contents']/div[@class='w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300']")
        #遍历榜单列表，获取详情
        for movie in movie_list:
            movie_url=movie.xpath(".//div/div/a/@href")
            if movie_url:
                movie_info_url=TMDB_URL+movie_url[0]
                movie_info=get_detail(movie_info_url)
                print(f"向{movie_info_url}发送请求,获取电影详情")
                all_movies.append(movie_info)    
    #保存数据
    save_data(all_movies)
    print("数据保存完毕")



if __name__ == '__main__':
    main()

   

    