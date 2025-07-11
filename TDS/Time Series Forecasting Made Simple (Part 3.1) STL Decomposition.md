# Time Series Forecasting Made Simple (Part 3.1): STL Decomposition

**Author:** Nikhil Dasari  
**Published:** July 9, 2025

---

![Detrended Series Showing Seasonal Patterns and Irregular Spikes/Dips](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/detrended-series-1024x314.png)
*Detrended Series Showing Seasonal Patterns and Irregular Spikes/Dips*

The above plot shows what remains after we remove the long-term trend. You can see the familiar annual rise and fall and that deep drop in January 2020 when COVID hit.

When we average all the January values, including the 2020 crash, that single event blends in and hardly affects the January average.

This helps us ignore rare shocks and focus on the true seasonal pattern. Now we will group the detrended values by month and take their averages to create our first seasonal estimate.

This gives us a stable estimate of seasonality, which STL will then refine and smooth in later iterations to capture any gradual shifts over time.

---

Next, we will repeat our seasonal-decompose approach: we’ll group the detrended values by calendar month to extract the raw monthly seasonal offsets.

Let’s focus on January and gather all the detrended values for that month.

![Table: Detrended January Values (2010–2023)](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/detrended-blog-part-3-1.png)
*Table: Detrended January Values (2010–2023)*

Now, we compute the **average of the detrended values for January** across all years to obtain a rough seasonal estimate for that month.

![Calculating the average of January’s detrended values across 12 years to obtain the seasonal estimate for January.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/CodeCogsEqn-43.png)
*Calculating the average of January’s detrended values across 12 years to obtain the seasonal estimate for January.*

This process is repeated for all 12 months to form the initial seasonal component.

![Monthly average of detrended values, forming the seasonal estimate for each month.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/detrended-by-nonth.png)
*Table: Monthly average of detrended values, forming the seasonal estimate for each month.*

Now we have the average detrended values for each month, we map them across the entire time series to construct the initial seasonal component.

![Detrended values and their monthly averages used for estimating the seasonal pattern.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/detrended-by-nonth-1.png)
*Table: Detrended values and their monthly averages used for estimating the seasonal pattern.*

---

After grouping the detrended values by month and calculating their averages, we obtain a new series of monthly means. Let’s plot this series to observe how the data look after applying this averaging step.

![seasonal estimate by repeating monthly averages.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/seasonal-estimate-monthly-averages-1024x306.png)
*seasonal estimate by repeating monthly averages.*

In the above plot, we grouped the detrended values by month and took the average for each one.

This helped us reduce the effect of that big dip in January 2020, which was likely due to the COVID pandemic.

By averaging all the January values together, that sudden drop gets blended in with the rest, giving us a more stable picture of how January usually behaves each year.

However, if we look closely, we can still see some sudden spikes and dips in the line.

These might be caused by things like special promotions, strikes or unexpected holidays that don’t happen every year.

Since seasonality is meant to capture patterns that repeat regularly each year, we don’t want these irregular events to stay in the seasonal curve.

But how do we know those spikes or dips are just one-off events and not real seasonal patterns? It comes down to how often they happen.

A big spike in December shows up because every December has high sales, so the December average stays high year after year.

We see a small increase in March, but that’s mostly because one or two years were unusually strong.

The average for March doesn’t really shift much. When a pattern shows up almost every year in the same month, that’s seasonality. If it only happens once or twice, it’s probably just an irregular event.

To handle this, we use a low-pass filter. While averaging helps us get a rough idea of seasonality, the low-pass filter goes one step further.

It smooths out those remaining small spikes and dips so that we are left with a clean seasonal pattern that reflects the general rhythm of the year.

This smooth seasonal curve will then be used in the next steps of the STL process.

---

Next, we will smooth out that rough seasonal curve by running a low-pass filter over every point in our monthly-average series.

To apply the low-pass filter, we start by computing a centered 13-month moving average.

For example, consider September 2010. The 13-month average at this point (from March 2010 to March 2011) would be:

![13-Month Average Example for September 2010 using surrounding monthly seasonal values](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/CodeCogsEqn-44-1024x116.png)
*13-Month Average Example for September 2010 using surrounding monthly seasonal values*

We repeat this 13-month averaging for every point in our monthly average series. Because the pattern repeats every year, the value for September 2010 will be the same as for September 2011.

For the first and last six months, we don’t have enough data to take a full 13-month average, so we just use whatever months are available around them.

Let’s take a look at the averaging windows used for the months where a full 13-month average isn’t possible.

![Averaging windows used for the first and last six months, where a full 13-month average was not possible.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/Averaging-Window-Used.png)
*Table: Averaging windows used for the first and last six months, where a full 13-month average was not possible.*

Now we’ll use Python to calculate the 13-month average values:

```python
import pandas as pd

# Load the seasonal estimate series
df = pd.read_csv("C:/stl_with_monthly_avg.csv", parse_dates=['Observation_Date'], dayfirst=True)

# Apply 13-month centered moving average on the Avg_Detrended_by_Month column
# Handle the first and last 6 values with partial windows
seasonal_estimate = df[['Observation_Date', 'Avg_Detrended_by_Month']].copy()
lpf_values = []

for i in range(len(seasonal_estimate)):
    start = max(0, i - 6)
    end = min(len(seasonal_estimate), i + 7)  # non-inclusive
    window_avg = seasonal_estimate['Avg_Detrended_by_Month'].iloc[start:end].mean()
    lpf_values.append(window_avg)

# Add the result to DataFrame
seasonal_estimate['LPF_13_Month'] = lpf_values
```

With this code, we get the 13-month moving average for the full time series.

![Table: Monthly detrended values along with their smoothed 13-month averages.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/Averaging-Window-Used-1.png)
*Table: Monthly detrended values along with their smoothed 13-month averages.*

After completing the first step of applying the low-pass filter by calculating the 13-month averages, the next step is to smooth those results further using a 3-point moving average.

Now, let’s see how the 3-point average is calculated for September 2010.

![Step-by-step calculation of the 3-point moving average for September 2010 as part of the low-pass filtering process.](https://contributor.insightmediagroup.io/wp-content/uploads/2025/07/CodeCogsEqn-45.png)
*Step-by-step calculation of the 3-point moving average for September 2010 as part of the low-pass filtering process.*

For January 2010, we calculate the average using January and February values, and for December 2023, we use December and November.

This approach is used for the endpoints where a full 3-month window isn’t available. In this way, we compute the 3-point moving average for each data point in the series.

Now, we use Python again to calculate the 3-month window averages for our data:

```python
import pandas as pd

# Load CSV file
df = pd.read_csv("C:/seasonal_13month_avg3.csv", parse_dates=['Observation_Date'], dayfirst=True)

# Calculate the 3-point moving average
lpf_values = df['LPF_13_Month'].values
moving_avg_3 = []

for i in range(len(lpf_values)):
    if i == 0:
        avg = (lpf_values[i] + lpf_values[i + 1]) / 2
    elif i == len(lpf_values) - 1:
        avg = (lpf_values[i - 1] + lpf_values[i]) / 2
    else:
        avg = (lpf_values[i - 1] + lpf_values[i] + lpf_values[i + 1]) / 3
    moving_avg_3.append(avg)

# Add the result to a new column
df['LPF_13_3'] = moving_avg_3
``` 