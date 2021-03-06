from matplotlib import pyplot as plt
import pandas as pd

# Names of the files and of the legends for the figures
#files = ['easy_tour5_swapco_mut_swap.csv','easy_tour10_swapco_mut_swap.csv','easy_tour5_95swapco_5mut_swap.csv','medium_tour5_swapco_mut_swap.csv','hard_tour5_swapco_mut_swap.csv','easy_rank_swapco_mut_swap.csv','easy_fps_swapco_mut_swap.csv','easy_tour5_co_incommon_mut_swap.csv']
files = ['easy_tour5_swapco_mut_swap.csv','easy_tour10_swapco_mut_swap.csv','easy_tour5_swapco_mut_swapall.csv','easy_tour5_95swapco_5mut_swap.csv','easy_rank_swapco_mut_swap.csv','easy_tour5_co_incommon_mut_swap.csv','medium_tour5_swapco_mut_swap.csv','hard_tour5_swapco_mut_swap.csv','easy_fps_swapco_mut_swap.csv']
legends = ['easy_tour5_swapco_mut_swap','easy_tour10_swapco_mut_swap','easy_tour5_swapco_mut_swapall','easy_tour5_95swapco_5mut_swap','easy_rank_swapco_mut_swap','easy_tour5_co_incommon_mut_swap','medium_tour5_swapco_mut_swap','hard_tour5_swapco_mut_swap','easy_fps_swapco_mut_swap']
#legends = ['easy_tour5_swapco_mut_swap','easy_tour5_swapco_mut_swapall','easy_tour10_swapco_mut_swap','easy_tour5_95swapco_5mut_swap','medium_tour5_swapco_mut_swap','hard_tour5_swapco_mut_swap','easy_rank_swapco_mut_swap','easy_fps_swapco_mut_swap','easy_tour5_co_incommon_mut_swap']

def df(file):
    """
    The aim of this function is to convert a csv file to a dataframe to then be able to plot the results

    :param file: the csv file
    :return: dataframe
    """

    column_names = ['gen', 'bestfitness', 'mean_allfitness', 'time']
    df1 = pd.read_csv(file, names=column_names, usecols=[1, 2, 3, 4])
    df1 = df1.dropna(how='all')
    df1 = df1.groupby(['gen']).mean()
    df1['gen'] = df1.index
    return df1

# Configuration for the figure
plt.figure(figsize=(10, 6))
plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
plt.ylabel("Average Best Fitness", fontsize=15)
plt.xlabel("Generation", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

# For every file in the previously created list we plot the best fitness function values
for file in files:
    dataframe = df(file)
    plt.plot(dataframe["gen"], dataframe["bestfitness"])

# Set legend
plt.legend(legends)
# Set title
plt.title('GAs performance', size=15)
# Save plot
plt.savefig('performance_graph' + ".png", dpi=300)
plt.show()

# get the times comparison for Rank, FPS and Tournament needed for the report
for file in ['performance/easy_rank_swapco_mut_swap.csv', 'performance/easy_fps_swapco_mut_swap.csv', 'performance/easy_tour5_swapco_mut_swap.csv']:
    dataframe = df(file)
    print(dataframe)




