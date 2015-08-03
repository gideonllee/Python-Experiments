import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

crashes = sns.load_dataset("car_crashes").sort("total", ascending=False)
sns.set_color_codes("pastel")
sns.barplot(y="abbrev",x="total",data=crashes, label = "Total",color="b")