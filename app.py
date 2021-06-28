
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import csv, re, operator
import plotly.graph_objs as go
import numpy as np
import plotly_express as px

app = Flask(__name__)
gapminder = px.data.gapminder()
iris = px.data.iris()
person = {
    'first_name': 'Zhou',
    'last_name' : 'Qichuan',
    'detail1':'国籍：China',
    'detail2':'住址：湖南省',
    'detail3':'生日：2001 09 01',
    'detail4':'爱好：篮球，跑步',
    'detail5':'性别：男',
    'history1':'java初级工程师',
    'history2':'毕业于湖北师范大学',
    'history3':'有三年的编程经验',
    'education1':'高中',
    'education2':'毕业时间',
    'education3':'2018 06 12',
    'education4':'大学',
    'education5':'毕业时间',
    'education6':'2020 06 20',
    'skill1':'协作',
    'skill2':'创意',
    'skill3':'组织',
    'skill4':'社交',
    'skill5':'管理',
    'technic1':'编程',
    'technic2':'算法',
    'technic3':'精通数学',
    'contact1':'e-mail:2879657430@qq.com',
    'contact2':'tel:19084562785',
    'contact3':'wechat:18765349083',
    'job': 'Collegy student',
    'tel': '1314980',
    'email': '131415zq@gmail.com',
    'description' : 'Zhou is a good student , a nice gu',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' : 'Web Developer',
            'company': 'AZULIK',
            'description' : 'Project manager and lead developer for several AZULIK websites.',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': 'Independant',
            'description' : 'Create Wordpress websites for small and medium companies. ',
            'timeframe' : 'February 2017 - Present'
        },
        {
            'title' : 'Sharepoint Intern',
            'company': 'ALTEN',
            'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
            'timeframe' : 'October 2015 - October 2016'
        }
    ],
    'education' : [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('resume.html', person=person)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))


@app.route('/chart')

def chart():
    return render_template('chartsajax.html',graphJSON=line(),graphJSON1=area()
    ,graphJSON2=scatter(),graphJSON3=choropleth(),graphJSON4=scatter_geo1(),graphJSON5=scatter_geo2()
    ,graphJSON6=line_geo(),graphJSON7=scatter1(),graphJSON8=parallel_coordinates()
    ,graphJSON9=density_contour(),graphJSON10=density_heatmap()
    )
# def gm(country='United Kingdom'):
#     df = pd.DataFrame(px.data.gapminder())

#     fig = px.line(df[df['country']==country], x="year", y="gdpPercap")
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return graphJSON

def line():
    # line 图
    fig = px.line(
    gapminder,  # 数据集
    x="year",  # 横坐标
    y="lifeExp",  # 纵坐标
    color="continent",  # 颜色的数据
    line_group="continent",  # 线性分组
    hover_name="country",   # 悬停hover的数据
    line_shape="spline",  # 线的形状
    render_mode="svg"  # 生成的图片模式
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def area():
        # area 图
    fig = px.area(
    gapminder,  # 数据集
    x="year",  # 横坐标
    y="pop",  # 纵坐标
    color="continent",   # 颜色
    line_group="country"  # 线性组别
    )
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def scatter():
    fig=px.scatter(
    gapminder   # 绘图DataFrame数据集
    ,x="gdpPercap"  # 横坐标
    ,y="lifeExp"  # 纵坐标
    ,color="continent"  # 区分颜色
    ,size="pop"   # 区分圆的大小
    ,size_max=60  # 散点大小
    )
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2

def choropleth():
    fig=px.choropleth(
    gapminder,  # 数据集
    locations="iso_alpha",  # 配合颜色color显示
    color="lifeExp", # 颜色的字段选择
    hover_name="country",  # 悬停字段名字
    animation_frame="year",  # 注释
    color_continuous_scale=px.colors.sequential.Plasma,  # 颜色变化
    projection="natural earth"  # 全球地图
                      )
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3

def scatter_geo1():
    fig = px.scatter_geo(
    gapminder,   # 数据
    locations="iso_alpha",  # 配合颜色color显示
    color="continent", # 颜色
    hover_name="country", # 悬停数据
    size="pop",  # 大小
    animation_frame="year",  # 数据帧的选择
    projection="natural earth"  # 全球地图
                        )
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4

def scatter_geo2():
    fig=px.scatter_geo(
    gapminder, # 数据集
    locations="iso_alpha",  # 配和color显示颜色
    color="continent",  # 颜色的字段显示
    hover_name="country",  # 悬停数据
    size="pop",  # 大小
    animation_frame="year"  # 数据联动变化的选择
    #,projection="natural earth"   # 去掉projection参数
    )
    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5

def line_geo():
    fig = px.line_geo(
    gapminder,  # 数据集
    locations="iso_alpha",  # 配合和color显示数据
    color="continent",  # 颜色
    projection="orthographic")   # 球形的地图
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6

def scatter1():
    fig = px.scatter(
    iris,  # 数据集
    x="sepal_width",  # 横坐标
    y="sepal_length",  # 纵坐标
    color="species"  )
    graphJSON7 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON7

def parallel_coordinates():
    fig=px.parallel_coordinates(
    iris,   # 数据集
    color="species_id",  # 颜色
    labels={"species_id":"Species",  # 各种标签值
          "sepal_width":"Sepal Width",
          "sepal_length":"Sepal Length",
          "petal_length":"Petal Length",
          "petal_width":"Petal Width"},
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2)
    graphJSON8 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON8

def density_contour():
    fig=px.density_contour(
    iris,  # 绘图数据集
    x="sepal_width",  # 横坐标
    y="sepal_length",  # 纵坐标值
    color="species"  # 颜色
    )
    graphJSON9 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON9

def density_heatmap():
    fig=px.density_heatmap(
    iris,  # 数据集
    x="sepal_width",   # 横坐标值
    y="sepal_length",  # 纵坐标值
    marginal_y="rug",  # 纵坐标值为线型图
    marginal_x="histogram"  # 直方图
                  )
    graphJSON10 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON10

@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
