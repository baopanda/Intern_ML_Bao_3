import matplotlib.pyplot as plt

bears = [10, 58, 85, 115, 139, 182]
dolphins = [150, 75, 32, 14, 8, 5]
whales = [80, 50, 100, 75, 90, 70]
x = [0, 1, 2, 3, 4, 5]
years = ["2009", "2010", "2011", "2012", "2013", "2014"]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(years, bears, '#16a085', marker='o', linewidth=3.0, label='Bears')
plt.plot(years, dolphins, '#c0392b', marker='s', linewidth=3.0, label='Dolphins')
plt.plot(years, whales, '#3498db', marker='^', linewidth=3.0, label='Whales')

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.title("Number of animals each year")
plt.xlabel("Years")
plt.xticks(x, years)
plt.show()