import matplotlib.pyplot as plt
import pandas as pd

# Referred to https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html for reading the csv, since it's been some time
rawPenglingsDf = pd.read_csv("C:/Users/klaud/WebstormProjects/klaudio-fusha-a2-datavis-5ways/a2-DataVis-5ways/penglings.csv")
print(rawPenglingsDf)

rawPenglingsDf = rawPenglingsDf.dropna()
print(rawPenglingsDf)

# Referred to https://www.w3schools.com/python/matplotlib_scatter.asp for making sure I was properly using plt.scatter
flipperLength = rawPenglingsDf["flipper_length_mm"]
bodyMass = rawPenglingsDf["body_mass_g"]
plt.scatter(flipperLength, bodyMass)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

# Note to self: Will color-code data point by species later, and will change point size based on bill length