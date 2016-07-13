import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')
%matplotlib inline

# taken from http://stackoverflow.com/a/16808448
def _sum(x):
    if len(x) == 0: 
        return 0
    return sum(x)

count_1 = pd.read_csv("/home/aaltje/Downloads/results-20160713-110409.csv",
                      index_col='the_date',
                      parse_dates=True)
count_2 = pd.read_csv("/home/aaltje/Downloads/results-20160713-110423.csv",
                      index_col='the_date',
                      parse_dates=True)

combined = count_1.append(count_2)['1970-01-02':]

make_great_again = pd.read_csv("/home/aaltje/Downloads/results-20160713-104258.csv",
                                 index_col='the_date',
                                 parse_dates=True)
all_data = pd.merge(make_great_again, combined, left_index=True, right_index=True)
all_data['ratio'] = all_data.make_great_again_commits / all_data.all_commits
all_data = all_data.resample('1W').apply(_sum)

all_data['2006-01-01':].plot(figsize=(14,10), subplots=True)
