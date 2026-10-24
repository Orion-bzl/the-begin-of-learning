import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#设置中文
plt.rcParams['font.sans-serif']=['SimHei']
figure,axse=plt.subplots(nrows=2,ncols=2,figsize=(15,8),dpi=100)
figure.subplots_adjust(wspace=0.3,hspace=0.5)
line=axse[0,0]
bar0=axse[0,1]
bar1=axse[1,0]
pie=axse[1,1]
figure.suptitle('TOP100电影榜单分析',fontsize=20)
data=pd.read_csv(r"E:\python\1\movies.csv",usecols=["name","language","score","type","duration","date"])
#折线图
data["date"]=data["date"].fillna("2019-01-01")
data["year"]=data["date"].str[:4]
year_count=data.groupby("year")["year"].count()
min_year=year_count.index.astype(int).min()
max_year=year_count.index.astype(int).max()
x=[i for i in range(min_year,max_year+1)]
y=[int(year_count.get(str(i),0)) for i in x]
line.plot(x,y)
line.set_title("TOP100电影年份分布")
line.set_xlabel("年份")
line.set_ylabel("电影数量")
line.set_xticks(x[::10])
line.grid(linestyle="--",alpha=0.5)
line.yaxis.set_major_locator(ticker.MaxNLocator(4))
#柱状图
language_count=data.groupby("language")["language"].count().sort_values(ascending=False)
language_x=language_count.index.tolist()
language_y=language_count.values.tolist()
bar0.bar(language_x,language_y)
bar0.set_title("TOP100电影语言分布")
bar0.set_xlabel("语言")
bar0.set_ylabel("电影数量")
bar0.grid(linestyle="--",alpha=0.3)
bar0.set_xticklabels(language_x,rotation=45)
#柱状图
type_count={}
for i in data["type"].fillna("").str.split(","):
    for j in i:
        if j in type_count:
            type_count[j]+=1
        else:
            type_count[j]=1
types_x=list(type_count.keys())
types_y=list(type_count.values())
bar1.bar(types_x,types_y)
bar1.set_title("TOP100电影类型分布")
bar1.set_xlabel("类型")
bar1.set_ylabel("电影数量")
bar1.grid(linestyle="--",alpha=0.5)
bar1.tick_params(axis="x",rotation=90)
#绘制饼状图
#合并数据
score_count=data.groupby("score")["score"].count()
total=score_count.sum()
large_count=score_count.loc[score_count>=total*0.04]
small_count=score_count.loc[score_count<total*0.04]
if small_count.shape[0]>0:
    large_count["其他"]=small_count.sum()
pie.pie(large_count,labels=large_count.index,autopct="%1.1f%%",radius=1.2)
pie.set_title("TOP100电影评分分布")
pie.legend(loc="lower center",ncol=5,bbox_to_anchor=(0.5,-0.2))

plt.show()