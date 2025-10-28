# 50 Matplotlib Interview Questions and Answers

Below are 50 practical Matplotlib questions and answers focusing on plotting, customization, and manipulation of figures and axes using Python's Matplotlib library.

Each question includes:
- A brief scenario
- A code snippet demonstrating one possible solution

**Note:** For all examples, assume you have imported Matplotlib as follows:
```python
import matplotlib.pyplot as plt
```

---

### 1. How do you create a simple line plot with Matplotlib?
**Answer:**  
Use `plt.plot()` and `plt.show()` to display.
```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()
```

---

### 2. How do you set the title of a plot?
**Answer:**  
Use `plt.title("Your Title")`.
```python
plt.plot([1,2,3],[2,4,6])
plt.title("My Line Plot")
plt.show()
```

---

### 3. How do you label the x and y axes?
**Answer:**  
Use `plt.xlabel()` and `plt.ylabel()`.
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.show()
```

---

### 4. How do you add a legend to a plot?
**Answer:**  
Use `plt.legend()` after providing labels in `plt.plot()`.
```python
plt.plot([1,2,3],[2,4,6], label="Line 1")
plt.plot([1,2,3],[3,6,9], label="Line 2")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
```

---

### 5. How do you change the line style in a plot?
**Answer:**  
Use the `linestyle` parameter in `plt.plot()`.
```python
plt.plot([0,1,2],[0,1,4], linestyle='--', label="Dashed")
plt.legend()
plt.show()
```

---

### 6. How do you change the line color in a plot?
**Answer:**  
Use the `color` parameter in `plt.plot()`.
```python
plt.plot([0,1,2],[0,1,4], color='red')
plt.show()
```

---

### 7. How do you plot multiple lines on the same axes?
**Answer:**  
Call `plt.plot()` multiple times before `plt.show()`.
```python
plt.plot([1,2,3],[1,2,3], label="Line A")
plt.plot([1,2,3],[2,4,6], label="Line B")
plt.legend()
plt.show()
```

---

### 8. How do you create a scatter plot?
**Answer:**  
Use `plt.scatter()` with x and y values.
```python
x = [1,2,3,4]
y = [10,8,12,15]
plt.scatter(x, y)
plt.show()
```

---

### 9. How do you change marker style in a scatter plot?
**Answer:**  
Use the `marker` parameter in `plt.scatter()`.
```python
plt.scatter([1,2,3],[2,3,4], marker='o')
plt.show()
```

---

### 10. How do you create a bar plot?
**Answer:**  
Use `plt.bar()` for vertical bars.
```python
categories = ['A','B','C']
values = [10,20,15]
plt.bar(categories, values)
plt.show()
```

---

### 11. How do you create a horizontal bar plot?
**Answer:**  
Use `plt.barh()` for horizontal bars.
```python
categories = ['A','B','C']
values = [10,20,15]
plt.barh(categories, values)
plt.show()
```

---

### 12. How do you add error bars to a plot?
**Answer:**  
Use `plt.errorbar()` with `yerr` parameter.
```python
x = [1,2,3]
y = [2,4,3]
yerr = [0.5, 0.2, 0.3]
plt.errorbar(x, y, yerr=yerr, fmt='o')
plt.show()
```

---

### 13. How do you create a histogram?
**Answer:**  
Use `plt.hist()` with your data.
```python
data = [1,1,2,2,2,3,3,4,5]
plt.hist(data, bins=5)
plt.show()
```

---

### 14. How do you create a pie chart?
**Answer:**  
Use `plt.pie()` with a list of values.
```python
values = [30,40,20,10]
labels = ['A','B','C','D']
plt.pie(values, labels=labels)
plt.show()
```

---

### 15. How do you change figure size?
**Answer:**  
Use `plt.figure(figsize=(width,height))`.
```python
plt.figure(figsize=(8,4))
plt.plot([1,2,3],[2,4,1])
plt.show()
```

---

### 16. How do you save a figure to a file?
**Answer:**  
Use `plt.savefig('filename.png')` before `plt.show()`.
```python
plt.plot([1,2,3],[2,4,6])
plt.savefig('myplot.png')
plt.show()
```

---

### 17. How do you adjust the axis limits?
**Answer:**  
Use `plt.xlim()` and `plt.ylim()`.
```python
plt.plot([1,2,3],[2,4,6])
plt.xlim(0,4)
plt.ylim(0,10)
plt.show()
```

---

### 18. How do you add grid lines?
**Answer:**  
Use `plt.grid(True)`.
```python
plt.plot([1,2,3],[2,4,6])
plt.grid(True)
plt.show()
```

---

### 19. How do you plot a function directly (e.g., y = x^2)?
**Answer:**  
Generate x values and compute y, then plot.
```python
import numpy as np
x = np.linspace(-5,5,100)
y = x**2
plt.plot(x, y)
plt.show()
```

---

### 20. How do you add text at a specific point in the plot?
**Answer:**  
Use `plt.text(x, y, "Text")`.
```python
plt.plot([1,2],[2,4])
plt.text(1.5, 3, "Midpoint")
plt.show()
```

---

### 21. How do you create subplots in a single figure?
**Answer:**  
Use `plt.subplot(rows, cols, index)`.
```python
plt.subplot(1,2,1)
plt.plot([1,2],[2,4])
plt.subplot(1,2,2)
plt.plot([1,2],[3,1])
plt.show()
```

---

### 22. How do you share axes between subplots?
**Answer:**  
Use the `sharex` or `sharey` parameters in `plt.subplots()`.
```python
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
ax1.plot([1,2,3],[2,4,6])
ax2.plot([1,2,3],[3,2,1])
plt.show()
```

---

### 23. How do you adjust spacing between subplots?
**Answer:**  
Use `plt.tight_layout()` after creating subplots.
```python
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot([1,2],[2,4])
ax2.plot([1,2],[3,1])
plt.tight_layout()
plt.show()
```

---

### 24. How do you change tick labels on the x-axis?
**Answer:**  
Use `plt.xticks()` with desired labels.
```python
x = [1,2,3]
y = [2,4,6]
plt.plot(x, y)
plt.xticks([1,2,3], ['One','Two','Three'])
plt.show()
```

---

### 25. How do you rotate tick labels?
**Answer:**  
Use `plt.xticks(rotation=angle)`.
```python
x = [1,2,3]
y = [2,4,6]
plt.plot(x, y)
plt.xticks([1,2,3], ['One','Two','Three'], rotation=45)
plt.show()
```

---

### 26. How do you set a logarithmic scale on an axis?
**Answer:**  
Use `plt.xscale('log')` or `plt.yscale('log')`.
```python
x = [1,10,100,1000]
y = [10,100,1000,10000]
plt.plot(x, y)
plt.xscale('log')
plt.yscale('log')
plt.show()
```

---

### 27. How do you change the figure background color?
**Answer:**  
Use `plt.gca().set_facecolor('color')` or `fig.set_facecolor()`.
```python
fig = plt.figure()
fig.set_facecolor('lightgray')
plt.plot([1,2],[2,4])
plt.show()
```

---

### 28. How do you change the line width of a plot?
**Answer:**  
Use `linewidth` parameter in `plt.plot()`.
```python
plt.plot([1,2],[2,4], linewidth=3)
plt.show()
```

---

### 29. How do you plot a filled area under a curve?
**Answer:**  
Use `plt.fill_between(x, y)` where y is the function.
```python
import numpy as np
x = np.linspace(0,1,50)
y = x**2
plt.plot(x, y)
plt.fill_between(x, y, color='yellow')
plt.show()
```

---

### 30. How do you annotate a point with an arrow?
**Answer:**  
Use `plt.annotate()` with `xy` and `xytext`.
```python
plt.plot([1,2,3],[2,4,3])
plt.annotate('Peak', xy=(2,4), xytext=(2,5), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.show()
```

---

### 31. How do you change the figure DPI?
**Answer:**  
Use `plt.figure(dpi=...)`.
```python
plt.figure(dpi=150)
plt.plot([1,2,3],[2,4,6])
plt.show()
```

---

### 32. How do you clear a figure?
**Answer:**  
Use `plt.clf()` to clear the current figure.
```python
plt.plot([1,2],[2,4])
plt.clf()
# Figure is now cleared
```

---

### 33. How do you close a figure?
**Answer:**  
Use `plt.close()` to close the current figure.
```python
plt.plot([1,2],[2,4])
plt.show()
plt.close()
```

---

### 34. How do you plot a horizontal line?
**Answer:**  
Use `plt.axhline(y=value)`.
```python
plt.axhline(y=0.5, color='red')
plt.show()
```

---

### 35. How do you plot a vertical line?
**Answer:**  
Use `plt.axvline(x=value)`.
```python
plt.axvline(x=2, color='green')
plt.show()
```

---

### 36. How do you add a shaded region (vertical) between two x-values?
**Answer:**  
Use `plt.axvspan(xmin, xmax, color='color')`.
```python
plt.axvspan(1,2, color='grey', alpha=0.3)
plt.show()
```

---

### 37. How do you add a secondary y-axis?
**Answer:**  
Use `ax2 = ax.twinx()` on an existing Axes.
```python
fig, ax = plt.subplots()
ax.plot([1,2,3],[2,4,6], color='blue')
ax2 = ax.twinx()
ax2.plot([1,2,3],[10,20,15], color='red')
plt.show()
```

---

### 38. How do you add a secondary x-axis?
**Answer:**  
Use `ax2 = ax.twiny()` on an existing Axes.
```python
fig, ax = plt.subplots()
ax.plot([1,2,3],[2,4,6])
ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim()) 
plt.show()
```

---

### 39. How do you remove the top and right spines?
**Answer:**  
Use `ax.spines['top'].set_visible(False)` and similarly for 'right'.
```python
fig, ax = plt.subplots()
ax.plot([1,2,3],[2,4,3])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
```

---

### 40. How do you create a polar plot?
**Answer:**  
Use `plt.subplot(projection='polar')`.
```python
ax = plt.subplot(projection='polar')
theta = [0,0.5,1,1.5]
r = [1,2,1,3]
ax.plot(theta, r)
plt.show()
```

---

### 41. How do you display a colorbar for an image plot?
**Answer:**  
Use `plt.colorbar()` after `plt.imshow()` or similar functions.
```python
import numpy as np
data = np.random.rand(10,10)
plt.imshow(data, cmap='viridis')
plt.colorbar()
plt.show()
```

---

### 42. How do you specify colors using hex codes?
**Answer:**  
Use a hex string like `color='#FF5733'`.
```python
plt.plot([1,2],[2,4], color='#FF5733')
plt.show()
```

---

### 43. How do you change the tick frequency?
**Answer:**  
Use `plt.xticks()` or `plt.yticks()` with a custom list of tick positions.
```python
plt.plot([1,2,3],[2,4,6])
plt.xticks([1,1.5,2,2.5,3])
plt.show()
```

---

### 44. How do you fill between two lines?
**Answer:**  
Use `plt.fill_between(x, y1, y2)`.
```python
import numpy as np
x = np.linspace(0,1,50)
y1 = x
y2 = x**2
plt.plot(x, y1, x, y2)
plt.fill_between(x, y1, y2, where=(y1>y2), color='yellow', alpha=0.5)
plt.show()
```

---

### 45. How do you make a scatter plot with varying point sizes?
**Answer:**  
Use the `s` parameter in `plt.scatter()`.
```python
x = [1,2,3,4]
y = [2,3,5,1]
sizes = [50,100,200,300]
plt.scatter(x, y, s=sizes)
plt.show()
```

---

### 46. How do you display a grid of images?
**Answer:**  
Use subplots and `plt.imshow()` in each subplot.
```python
import numpy as np
fig, axes = plt.subplots(1,2)
data1 = np.random.rand(10,10)
data2 = np.random.rand(10,10)
axes[0].imshow(data1, cmap='gray')
axes[1].imshow(data2, cmap='gray')
plt.show()
```

---

### 47. How do you change the direction of tick labels?
**Answer:**  
Use `plt.tick_params()` with `labelrotation`.
```python
plt.plot([1,2,3],[2,4,6])
plt.tick_params(axis='x', labelrotation=90)
plt.show()
```

---

### 48. How do you plot a contour plot?
**Answer:**  
Use `plt.contour()` or `plt.contourf()` for filled contours.
```python
import numpy as np
x = np.linspace(-2,2,50)
y = np.linspace(-2,2,50)
X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2
plt.contour(X, Y, Z, levels=[1,2,3,4])
plt.show()
```

---

### 49. How do you remove all ticks and labels?
**Answer:**  
Set `plt.xticks([])` and `plt.yticks([])`.
```python
plt.plot([1,2],[2,4])
plt.xticks([])
plt.yticks([])
plt.show()
```

---

### 50. How do you plot dates on the x-axis?
**Answer:**  
Convert dates to a suitable format and use `plt.plot_date()` or normal `plt.plot()` if x are datetimes.
```python
import datetime as dt
dates = [dt.datetime(2021,1,1), dt.datetime(2021,1,2), dt.datetime(2021,1,3)]
values = [10,20,15]
plt.plot_date(dates, values, linestyle='-')
plt.show()
```

---

If you found this helpful, consider following or starring the repository!

Stay updated with my latest content and projects!
