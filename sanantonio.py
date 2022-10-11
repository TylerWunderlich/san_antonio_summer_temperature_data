import matplotlib.pyplot as plt
import matplotlib.patches as mp
import matplotlib.lines as mpl
import pandas as pd
import numpy as np

temperature = pd.read_csv('sanantonio.csv')
temperature.set_index(temperature['Month'], inplace=True)
plt.figure(figsize=[16, 7])
plt.bar(temperature['Month'],temperature['Average High'], color=['red', 'yellow', 'green', 'blue'])

dic = temperature['Average High'].to_dict()
data = list(dic.items())
jun_list = [i for i in data if i[0].startswith('Jun')]
jul_list = [i for i in data if i[0].startswith('Jul')]
aug_list = [i for i in data if i[0].startswith('Aug')]
sep_list = [i for i in data if i[0].startswith('Sep')]

jun_dict = dict(jun_list)
jul_dict = dict(jul_list)
aug_dict = dict(aug_list)
sep_dict = dict(sep_list)

jun = pd.DataFrame.from_dict(jun_dict, orient='index', columns=['Average High'])
jul = pd.DataFrame.from_dict(jul_dict, orient='index', columns=['Average High'])
aug = pd.DataFrame.from_dict(aug_dict, orient='index', columns=['Average High'])
sep = pd.DataFrame.from_dict(sep_dict, orient='index', columns=['Average High'])

plt.plot(jun['Average High'].rolling(10, min_periods=1, center=True).mean(), color='#AF0000')
plt.plot(jul['Average High'].rolling(10, min_periods=1, center=True).mean(), color='#FFAA00')
plt.plot(aug['Average High'].rolling(10, min_periods=1, center=True).mean(), color='#00FFFF')
plt.plot(sep['Average High'].rolling(10, min_periods=1, center=True).mean(), color='#FF00FF')
plt.xticks(np.arange(0, 300, 5), rotation=45, fontsize=6)
plt.ylim(75, 110)
plt.title('Average Summer Month High Temperatures For San Antonio, Texas, 1948-2021', 
fontdict={'size': 18})
plt.ylabel('Average High Temperature (Fahrenheit)', fontdict={'size': 14})
plt.xlabel('Month', fontdict={'size': 14})

red_bar = mp.Patch(color='red', label='June')
yellow_bar = mp.Patch(color='yellow', label='July')
green_bar = mp.Patch(color='green', label='August')
blue_bar = mp.Patch(color='blue', label='September')
dark_red_line = mpl.Line2D([],[], color='#AF0000', label='10 Month June Rolling Average')
orange_line = mpl.Line2D([],[], color='#FFAA00', label='10 Month July Rolling Average')
cyan_line = mpl.Line2D([],[], color='#00FFFF', label='10 Month August Rolling Average')
magenta_line = mpl.Line2D([],[], color='#FF00FF', label='10 Month September Rolling Average')
plt.legend(fontsize=9, loc='upper center', handles=[red_bar, yellow_bar, green_bar, blue_bar, 
dark_red_line, orange_line, cyan_line, magenta_line])
plt.show()
