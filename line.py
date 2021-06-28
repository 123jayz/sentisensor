
import pandas as pd
import numpy as np
import plotly_express as px  # 现在这种方式也可行：import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
  iris,  # 数据集
  x="sepal_width",  # 横坐标
  y="sepal_length"  # 纵坐标
                )
fig.show()

