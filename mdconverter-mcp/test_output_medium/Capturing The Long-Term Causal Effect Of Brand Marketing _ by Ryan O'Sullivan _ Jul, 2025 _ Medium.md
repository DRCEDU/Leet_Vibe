---
title: "Capturing The Long-Term Causal Effect Of Brand Marketing | by Ryan O'Sullivan | Jul, 2025 | Medium"
published: "2025-07-17T01:43:09.495Z"
og_title: "Capturing The Long-Term Causal Effect Of Brand Marketing"
description: "Rome Wasn’t Built In A Day!"
url: "https://medium.com/@raz1470/capturing-the-long-term-causal-effect-of-brand-marketing-bc577621a627"
author: "Ryan O'Sullivan"
---

# Capturing The Long-Term Causal Effect Of Brand Marketing | by Ryan O'Sullivan | Jul, 2025 | Medium

## Article Information

**Author:** Ryan O'Sullivan
**Published:** 2025-07-17T01:43:09.495Z
**Original URL:** https://medium.com/@raz1470/capturing-the-long-term-causal-effect-of-brand-marketing-bc577621a627

**Description:** Rome Wasn’t Built In A Day!

---

# Capturing The Long-Term Causal Effect Of Brand Marketing


## Rome Wasn’t Built In A Day!

[![Ryan O'Sullivan](images/1_tAw1S072P0f0sUswKPN6VQ.jpg)](https://medium.com/@raz1470?source=post_page---byline--bc577621a627---------------------------------------)

[Ryan O'Sullivan](https://medium.com/@raz1470?source=post_page---byline--bc577621a627---------------------------------------)

26 min read

·

12 hours ago

--

Listen

Share

More

![]()

Photo by [David Köhler](https://unsplash.com/@davidkhlr?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)


# Motivation

I’ve worked across measurement (marketing, promotions, CRM) for coming up to 10 years now. In this time, I’ve leant heavily on the causal AI toolbox. But causal AI is just a buzzword – All of the tools within it are built on the foundations of economic theory and causal inference. So every now and then it’s worth delving deep into this area to see if it can help solve our toughest problems.

So today we are going to delve deep – But into which problem I hear you ask? That leads me onto my first motivation…Capturing long-term causal effects!

In this article expect to gain insight into the following areas:


- Why is capturing long-term causal effects important in brand marketing?

- How does brand building work?

- What do we need from a measurement solution?

- What is co-integration and why is it so important?

We will finish things off with a Python case study to help put all the theory to practice!

Before we kick-off, it’s worth calling out that this article is inspired by the brilliant paper from 2021 by Peter Cain:

<https://www.sciencedirect.com/science/article/abs/pii/S0167811621000495>

Reference: P.M. Cain, 
Modelling short-and long-term marketing effects in the consumer purchase journey, 
International Journal of Research in Marketing


# Why Is Capturing Long-term Causal Effects Important In Brand Marketing?

If you bumped into me in the street and asked me what problem I think organisations need to be solving in 2025 it would be this — Capturing long-term causal effects. Let me illustrate with an example from marketing…

We can split marketing into two distinct areas: Performance marketing and brand marketing.

Performance marketing is usually delivered across digital channels like social, display, paid search and affiliates. Social and display help generate demand whilst paid search and affiliates help capture it. The ads usually have a direct-call-to-action served at your target audience who are already in the lower sales funnel. It’s a great lever for driving short-term sales uplifts.

Brand marketing, on the other hand, is typically delivered through more traditional or high-reach channels such as TV, radio, billboards, or video content on social platforms. Its primary goal is to build awareness and consideration among a broad audience. Unlike performance marketing, which targets in-market consumers for immediate action, brand marketing plays the long game — it’s foundational to building brand equity over time. Since a significant portion of the population is often out-of-market at any given time, the impact of brand marketing tends to manifest gradually rather than instantly.

![]()

User generated image

To measure the causal effect of both of these marketing initiatives it’s common to use marketing mix modelling (MMM). MMM is a statistical model used to estimate the short-term effect of marketing on sales whilst controlling for confounding factors like seasonality and market demand.

Hang on, isn’t using a short-term method to measure a long-term effect (brand marketing) problematic? Absolutely! And this is where my second motivation for this article comes from: Organisations are weighting marketing budgets towards performance marketing based on an unfair measurement system. The scenario worsens when execs demand higher sales numbers next quarter, as this just leads to spending more on performance marketing and less on building their long term brand equity.

Some attempt to account for longer-term effects using ad stock, a mechanism that models the lingering impact of media over time. While ad stock works well for performance media — where effects decay in a predictable, short-term pattern — it falls short for brand marketing, which often influences consumer behaviour in more complex, delayed, and less directly measurable ways. Simply setting a high decay rate like 0.9 doesn’t magically make brand impact measurable.

Peter Cain covers the adstock illusion in his prequel to the paper I mention earlier in my article:

[## Long-term advertising effects: The Adstock illusion


### Notice The full text article is not available for purchase. The publisher only permits individual articles to be…

www.ingentaconnect.com](https://www.ingentaconnect.com/contentone/hsp/ama/2025/00000011/00000001/art00004;jsessionid=chws785fprd0.x-ic-live-02?source=post_page-----bc577621a627---------------------------------------)

So if MMM is suited to measuring the short-term effects of performance marketing, what method can we use to capture the long-term effects of brand marketing?


# How Does Brand Building Work?

Before we talk solutions, let’s think about the concept behind brand building. It all starts with consumers becoming aware of your brand, which leads to a consideration phase before they purchase from you. Imagine this as a network where each step influences the next, and word-of-mouth plays a pivotal role. Let’s break this down with a few examples:


- **Example 1:** You’re scrolling through your social media feed and come across an ad for a new trainer brand. You haven’t really thought about it before, but now you know about it (**awareness**). Weeks later, when your old trainers finally wear out, you recall that brand you saw online. You start considering their products (**consideration**), and eventually, you make a purchase (**sales**).

![]()

User generated image


- **Example 2:** While you’re pondering which brand of running shoes to buy (**consideration**), you ask your friend if they’ve heard of the brand you’ve been eyeing. Your friend wasn’t familiar with it, but a quick google search makes them aware (**awareness**). Now, not only are you considering the brand more seriously, but you’ve also unintentionally making friends aware of it.

![]()

User generated image


- **Example 3:** You’ve just bought a brand-new smartwatch (**sales**) and the next day, your colleague asks about your weekend. You excitedly share that you’ve bought the latest model from a brand they haven’t heard of. In that moment, you’ve made them aware of the brand (**awareness**)and starting to influence your colleague.

![]()

User generated image


- **Example 4:** After using that smartwatch for a few months (**sales**), you’ve become such a fan that you can’t stop talking about it. You tell your friends and family about how it’s changed your daily routine, and now they’re seriously considering buying one for themselves (**consideration**). In this case, your own positive experience has triggered consideration among people you’ve shared it with.

![]()

User generated image

So what role does brand marketing play? It plays a vital role in persistently chipping away at awareness and consideration. Brand marketing isn’t about immediate conversions; instead, it’s a long-term investment in building the foundation for future sales. Let’s break this down with a couple of examples:


- **Example 5:** You’ve seen a series of TV ads for a brand you didn’t know about before. The ads highlight their values and mission, and over time, they stick in your mind. You’re now aware of the brand, even though you haven’t yet needed to buy anything from them. This sustained exposure is how brand marketing works its magic: consistently increasing awareness, even without an immediate call to action.

![]()

User generated image


- **Example 6:** Now, let’s say you’ve been seeing these ads regularly for a few months. The more you see the brand’s messaging, the more intrigued you become. You start to consider their products, even though you didn’t initially have a need. Through consistent brand marketing, the brand has managed to shift your mindset from simple awareness to serious consideration, getting closer to that all-important purchase decision.

![]()

User generated image

As it slowly chips away, these small short-term impacts on awareness and consideration get mediated through the brand building network. In the long-term this can have a significant effect on sales.


# What Do We Need From A Measurement Solution?

So what do we need from a measurement solution? First of all, it would help if we could isolate the long term trend of sales in order to represent brand equity growth (base sales). Secondly, it needs to be able represent our brand building network, with word-of-mouth linking together awareness, consideration and base sales. And finally, it needs to be able to be able to capture the long-term causal effect of brand marketing being mediated through the system.


## 1) Brand Equity Growth

Let’s start by thinking about how we could isolate the long-term trend of sales to represent brand equity growth. Earlier, we touched on MMM and how it is best suited for measuring short-term effects. However, we can also use it to break down sales into distinct components:


- **Marketing & Promotions** — The short-term uplift from advertising and promotional activities.

- **External Factors** — Seasonality, competitor activity etc.

- **Base Sales** — The underlying sales trend driven by brand equity and shifts in market demand.

The key challenge becomes modelling base sales in a way that robustly captures long-term trends while separating out short-term noise.

**1. Dynamic Linear Models (DLMs)**

DLMs are a natural choice when dealing with time series data that may exhibit evolving trends and seasonal patterns. They allow for components such as the intercept (representing base sales) to vary over time in a structured, probabilistic way.

You can explore using this in statsmodel:

[## statsmodels.tsa.statespace.structural.UnobservedComponents - statsmodels 0.14.4


### Univariate unobserved components time series model These are also known as structural time series models, and decompose…

www.statsmodels.org](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.structural.UnobservedComponents.html?source=post_page-----bc577621a627---------------------------------------)

**2. Hilbert Space Gaussian Process (HSGP)**

HSGP is a scalable approximation to Gaussian Process (GP) regression that retains the flexibility of GPs while being computationally tractable. In this context, the time-varying intercept can be modelled as a smooth function using an HSGP prior. This allows us to capture non-linear, long-horizon shifts in sales (i.e. brand equity growth), while still integrating into a broader regression model.

The team at pymc have implemented it into their MMM package:

[## MMM with time-varying parameters (TVP) - Open Source Marketing Analytics Solution


### In classical marketing mix models, the effect of advertising (or other factors) on sales is assumed to be constant over…

www.pymc-marketing.io](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_tvp_example.html?source=post_page-----bc577621a627---------------------------------------)

But isolating base sales is only the first step. The real challenge is understanding how brand equity actually grows — how awareness, consideration, and word-of-mouth interact over time to influence long-term sales. In the next section, we’ll explore how to represent this brand-building process in a measurable way.


## 2) Brand Building Network

Now, let’s explore how we can represent our brand-building network. Within this network, word-of-mouth must link awareness, consideration, and base sales over time.But before we dive into the solution, we first need to understand how we collect awareness and consideration data.

Awareness and consideration are key brand health metrics that most organisations track. These are typically measured through brand tracker surveys, which collect consumer sentiment toward a brand on a monthly basis.

Now that we have awareness, consideration, and base sales as time-series data, the next step is to model the dynamic relationship between them. A simple regression wouldn’t capture the feedback loops between these variables — but a vector autoregression (VAR) model can!

VAR is a powerful statistical model designed to analyse how multiple time-series influence each other over time. Unlike simple regression models, VAR allows each variable to be explained by its own past values as well as the past values of all other variables in the system.

In our case, the endogenous variables (variables that influence and are influenced by each other) are:


- **Awareness** — Captures consumer familiarity with the brand.

- **Consideration** — Measures the likelihood of consumers choosing the brand.

- **Base Sales** — Represents long-term brand equity growth.

Our system can then be represented mathematically as:

![]()

User generated image

Before fitting a VAR model, we must ensure that our time series are stationary — meaning their statistical properties like mean and variance stay constant over time. If a series is non-stationary (for example, if it trends upward over time), it can lead to spurious results. Typically, we check for stationarity using tests like the Augmented Dickey-Fuller (ADF) test, and apply differencing if needed.

Once we have stationary data, we can explore the causal relationships between variables using Granger causality tests. In simple terms, if past values of awareness help predict future values of consideration (beyond what consideration’s own past can predict), we say that awareness “Granger-causes” consideration. This is key to uncovering the directional influence paths within our brand-building network.

With this setup, we can now explore how brand marketing impacts awareness and consideration, and how those effects cascade into long-term sales through our brand-building network.


## 3) Brand Marketing Mediation

So how can we adapt our VAR model to allow brand marketing to be mediated through the network? VARX, that’s how!

VARX (Vector Autoregression with Exogenous Variables) extends the VAR model by incorporating external factors — variables that influence the system but are not influenced by it. In our case, the key exogenous variable is brand marketing spend.

While our VAR model captures the interdependencies between awareness, consideration, and base sales, it doesn’t explicitly account for the role of brand marketing. Since brand marketing primarily influences awareness and consideration, we need a model that allows marketing to drive changes in these variables while still preserving the feedback loops within our brand-building network.

In a standard VAR model, each variable is expressed as a function of its own past values and the past values of all other endogenous variables. VARX extends this by adding brand marketing spend as an additional input. The model now looks like this:

![]()

User generated image

Where:


- **Marketing** — Brand Marketing spend at time *t* (exogenous variable).

- **Demand** — A proxy for market demand at time *t* (exogenous variable). Including this is important as when demand is also a key driver of awareness and consideration e.g. When demand is high more prospects need the product you are offering.

This structure allows us to measure the long-term causal effect of brand marketing, as its impact propagates through awareness and consideration before ultimately affecting base sales. Unlike traditional MMM, which attributes short-term effects directly to sales, VARX captures the delayed and indirect effects of brand marketing, making it a more suitable tool for understanding brand-building dynamics.

It’s worth pointing out that by design marketing won’t drive base sales directly and the long-term effect is indirect through the brand metrics

Next, let’s explore how we can use our model to quantify the long-term effects of brand marketing.


## 4) Estimating Long-term Causal Effects

Now that we’ve built our VARX model, we can estimate the long-term effects of brand marketing — not by using formal impulse response functions (IRFs), but through forecast simulations.

In a traditional VAR model, IRFs show how a one-time shock to an endogenous variable affects the rest of the system over time. However, in our case, marketing spend is exogenous, and most implementations do not support formal IRFs for exogenous variables.

Instead, we can simulate the impact of marketing spend using a scenario-based approach:


- First, we forecast outcomes under a baseline scenario, where marketing spend is held constant or set to zero.

- Next, we introduce a shock to marketing spend — for example, increasing it by 1 unit in a single month — and generate a new forecast.

- By comparing the two forecast paths, we can observe the dynamic response of our endogenous variables (awareness, consideration, and base sales) to this one-time increase.

This approach allows us to capture the timing, magnitude, and persistence of marketing’s effect. For instance, we might see that a marketing spike initially lifts awareness, which then drives consideration, and eventually translates into higher base sales over several months. These dynamics help quantify the role of marketing in brand building over time.

While not a theoretical IRF in the econometric sense, this simulation method is often more practical for marketers and decision-makers. It frames brand marketing as a long-term strategic investment, helping to align marketing spend with future value creation — not just short-term sales lifts.


# What Is Co-integration And Why Is It So Important?

As we’ve discussed, the VARX model is useful for capturing the immediate and delayed effects of brand marketing on variables like awareness, consideration, and base sales. However, when we deal with multiple time-series variables that are non-stationary (i.e. their statistical properties like mean and variance change over time), we need to dig deeper into the long-term relationships between these variables. This is where co-integration and the Vector Error Correction Model (VECM) come into play.

As Davidson and Hall (1991) demonstrate, cointegration allows us to uncover meaningful long-term equilibrium relationships in recursive systems, providing a solid foundation for causal interpretation:

[## Cointegration in Recursive Systems


### Downloadable (with restrictions)! This paper studies the cointegration properties of vector autoregressive models…

ideas.repec.org](https://ideas.repec.org/a/ecj/econjl/v101y1991i405p239-51.html?source=post_page-----bc577621a627---------------------------------------)

Co-integration is a statistical concept that refers to a long-term equilibrium relationship between two or more non-stationary time-series variables. In simpler terms, even though individual time-series might show trends (like increasing sales or awareness), their relationship might remain stable over time. If two or more variables are co-integrated, it means they share a long-term equilibrium, and their movements are connected, despite short-term fluctuations.

For example, awareness and base sales may individually trend upwards, but they may move together in the long run. If we can prove that they are co-integrated, it suggests that shifts in awareness over time will have a corresponding long-term impact on sales.

There are two main approaches to test for co-integration between time-series variables. The Engle-Granger two-step method is a simpler approach typically used when testing the relationship between two variables. It involves running a regression between the variables and then checking if the residuals are stationary. For systems involving more than two variables, the Johansen test is more appropriate. It treats all variables symmetrically and can identify multiple co-integrating relationships within a network.

Once we’ve established that our time-series variables are co-integrated, we can use the Vector Error Correction Model (VECM) to model these long-term relationships more accurately. The VECM allows us to incorporate the error correction term, which accounts for deviations from the long-term equilibrium. It helps in correcting short-term shocks and bringing the variables back in line with their long-term equilibrium relationship.

The VECM is an extension of the VAR model, specifically designed for co-integrated variables. While VAR models the short-term dynamics of the system, VECM accounts for both the short-term deviations and the long-term co-integrating relationships, making it a more suitable model for systems where the variables share a stable long-term relationship.

![]()

User generated image

The equation looks a little scary at first, so we will break it down below to make it easier to understand:


- **Γ1** — Short-term coefficients of the endogenous variables

- **Γ2** — Short-term coefficients of the exogenous variables

- **Π** — This is the long-term coefficient matrix, which represents the error correction term in the VECM

In the context of our brand-building network, if we find that awareness, consideration, and base sales are co-integrated, the VECM will help us understand how changes in one variable, such as brand marketing spend, impact the others in the long run. The error correction term in VECM would also help us identify how quickly the system corrects itself if there are deviations from the long-term equilibrium.


# Python Case Study

Now we have understood the concept and theory, it’s time for the case study! We are going to simulate some data and use it to show how we can build a VARX model. After we have mastered this, we will cover how to build and understand the output of a VECM.

You can find the full notebook here:

[## GitHub - raz1470/brand\_long\_term\_effects: An overview of how to capture the long term effects of…


### An overview of how to capture the long term effects of brand marketing - raz1470/brand\_long\_term\_effects

github.com](https://github.com/raz1470/brand_long_term_effects/tree/main?source=post_page-----bc577621a627---------------------------------------)


## 1a) Preparing The Data For VARX

We start by simulating some data to create time series data suitable for building a VARX model. This time series span 62 monthly periods starting from **November 2019**. The five key series — **Brand Marketing**, **Market Demand**, **Awareness**, **Consideration**, and **Base Sales** — illustrate a simulated brand performance landscape influenced by marketing pulses and evolving consumer behavior. Here’s what each series reveals:


- Brand marketing — Campaigns are run in a series of pulses.

- Awareness — Gradual, cumulative growth with bumps after marketing pulses.

- Consideration — Responsive but bounded growth, following awareness and demand.

- Market demand — Three-phase trend — rise, dip, and rise again.

- Base sales — Upward trend with volatility, driven by cumulative effects.

```

# Settings 

start_date = '2019-11-30' 
np.random.seed(42) 
n_periods = 62 
 

# Varying Brand Marketing Pulses (in £000s) 

brand_marketing = np.zeros(n_periods) 
pulse_profiles = [ 
 [120, 80, 50], # Pulse 1 

 [100, 70, 40], # Pulse 2 

 [90, 60, 30], # Pulse 3 

 [110, 75, 45] # Pulse 4 

] 
pulse_starts = [5, 20, 35, 50] 
 
for i, start in enumerate(pulse_starts): 
 for j, value in enumerate(pulse_profiles[i]): 
 if start + j < n_periods: 
 brand_marketing[start + j] = value 
brand_marketing_scaled = brand_marketing * 10000 # Convert to £ 

 

# Market Demand (unchanged) 

trend = np.concatenate([ 
 np.linspace(0.5, 1.2, 20), 
 np.linspace(1.2, 0.8, 20), 
 np.linspace(0.8, 1.5, 22) # Adjusted to match 62 periods 

]) 
market_demand = trend + np.random.normal(0, 0.05, n_periods) 
market_demand_scaled = market_demand * 50 + 30 
 

# Awareness, Consideration, Base Sales 

awareness = np.zeros(n_periods) 
consideration = np.zeros(n_periods) 
base_sales = np.zeros(n_periods) 
 
for t in range(1, n_periods): 
 awareness[t] = max(0, ( 
 0.8 * awareness[t - 1] 
 + 0.03 * brand_marketing[t] 
 + 0.01 * t 
 + np.random.normal(0, 0.5) 
 )) 
awareness_scaled = awareness * 5 + 20 
 
for t in range(2, n_periods): 
 raw_consideration = ( 
 0.5 * market_demand[t] 
 + 0.1 * awareness[t - 1] 
 + 0.05 * brand_marketing[t - 1] 
 + 0.1 * base_sales[t - 1] 
 + np.random.normal(0, 0.3) 
 ) 
 consideration[t] = max(0, min(raw_consideration, awareness[t - 1])) 
consideration_scaled = consideration * 5 + 10 
 
for t in range(2, n_periods): 
 base_sales[t] = ( 
 0.3 * base_sales[t - 1] 
 + 0.4 * market_demand[t] 
 + 0.25 * consideration[t] 
 + np.random.normal(0, 0.5) 
 ) 
base_sales_scaled = base_sales * 100 + 500 
 

# Time index for plotting 

date_range = pd.date_range(start=start_date, periods=n_periods, freq='M') 
 

# Plotting 

series_names = [ 
 "Brand Marketing", "Market Demand", 
 "Awareness", "Consideration", "Base Sales" 
] 
series_data = [ 
 brand_marketing_scaled, market_demand_scaled, 
 awareness_scaled, consideration_scaled, base_sales_scaled 
] 
 
df = pd.DataFrame({ 
 'Month': date_range, 
 'Brand_Marketing': brand_marketing_scaled, 
 'Market_Demand': market_demand_scaled, 
 'Awareness': awareness_scaled, 
 'Consideration': consideration_scaled, 
 'Base_Sales': base_sales_scaled 
}) 
 
for name, data in zip(series_names, series_data): 
 plt.figure(figsize=(10, 4)) 
 plt.plot(date_range, data, label=name) 
 plt.title(f"{name} Over Time") 
 plt.xlabel("Date") 
 plt.ylabel(name) 
 plt.legend(loc="upper right") 
 plt.grid(True) 
 plt.tight_layout() 
 plt.show()
```

![]()

User generated image

![]()

User generated image

![]()

User generated image

![]()

User generated image

![]()

User generated image

Next, we define functions to test and enforce stationarity through differencing.

```
def check_stationarity(series, name): 
 result = adfuller(series.dropna()) 
 return result[1] < 0.05 # True if stationary 

 
def make_stationary(series, name, max_diff=3): 
 temp_series = series.copy() 
 diff_count = 0 
 
 while diff_count < max_diff: 
 is_stationary = check_stationarity(temp_series, f"{name} (diff={diff_count})") 
 if is_stationary: 
 return temp_series.dropna(), diff_count 
 temp_series = temp_series.diff() 
 diff_count += 1 
 
 print(f"Warning: {name} could not be made stationary after {max_diff} differences.\n") 
 return temp_series.dropna(), diff_count
```

We run all our series through — Below you can see the results where only market demand needs differencing twice.

```
df['Awareness_stationary'], awareness_diff = make_stationary(df['Awareness'], 'Awareness') 
df['Consideration_stationary'], consideration_diff = make_stationary(df['Consideration'], 'Consideration') 
df['Base_stationary'], base_diff = make_stationary(df['Base_Sales'], 'Base_Sales') 
df['Brand_stationary'], brand_diff = make_stationary(df['Brand_Marketing'], 'Brand_Marketing') 
df['Market_stationary'], market_diff = make_stationary(df['Market_Demand'], 'Market_Demand') 
 
stationary_df = df[[ 
 'Month', 
 'Awareness_stationary', 
 'Consideration_stationary', 
 'Base_stationary', 
 'Brand_stationary', 
 'Market_stationary' 
]].dropna() 
 
print("\n✅ Differencing Summary:") 
print(f"Awareness: {awareness_diff} diff(s)") 
print(f"Consideration: {consideration_diff} diff(s)") 
print(f"Base Sales: {base_diff} diff(s)") 
print(f"Brand Spend: {brand_diff} diff(s)") 
print(f"Market Demand: {market_diff} diff(s)")
```

![]()


## 1b) Fitting The VARX Model

Next we can fit the VARX model by feeding it the endogenous and exogenous series. We can use the statsmodel package in Python:

[## VARMAX models - statsmodels


### The class in statsmodels allows estimation of VAR, VMA, and VARMA models (through the argument), optionally with a…

www.statsmodels.org](https://www.statsmodels.org/v0.13.5/examples/notebooks/generated/statespace_varmax.html?source=post_page-----bc577621a627---------------------------------------)

When `order=(1, 0)`, the `VARMAX` class essentially behaves like a VARX model as we set the number of moving average (MA) lags to 0. We also scale the data to ensure all variables contribute equally to the model, regardless of their original units or magnitudes. This improves model stability, speeds up convergence, and makes relationships easier to interpret.

```
scaler_endog = StandardScaler() 
scaled_endog = pd.DataFrame( 
 scaler_endog.fit_transform(endog), 
 columns=endog.columns, 
 index=endog.index 
) 
 
scaler_exog = StandardScaler() 
scaled_exog = pd.DataFrame( 
 scaler_exog.fit_transform(exog), 
 columns=exog.columns, 
 index=exog.index 
) 
 
model = VARMAX(scaled_endog, exog=scaled_exog, order=(1, 0), trend='c') 
fitted = model.fit(maxiter=1000, disp=False) 
print(fitted.summary())
```

![]()

User generated image

Before calculating the IRF, let’s evaluate how well our model fits the data.

```
fitted_values_scaled = fitted.fittedvalues 
 
fitted_values = pd.DataFrame( 
 scaler_endog.inverse_transform(fitted_values_scaled), 
 columns=endog.columns, 
 index=endog.index 
) 
 
for col in endog.columns: 
 plt.figure(figsize=(10, 4)) 
 plt.plot(stationary_df["Month"], endog[col], label="Actual", color="black") 
 plt.plot(stationary_df["Month"], fitted_values[col], label="Fitted", color="blue", linestyle="--") 
 plt.title(f"{col}: In-Sample Fit") 
 plt.xlabel("Time") 
 plt.ylabel(col) 
 plt.legend() 
 plt.grid(True) 
 plt.tight_layout() 
 plt.show()
```

![]()

User generated image

![]()

User generated image

![]()

User generated image

We can see we get a good fit for awareness. Consideration and base sales is harder to model but we still get a reasonable fit.

Now we can calculate the IRF looking at how marketing spend impacts our endogenous variables over 24 months.

```
n_forecast = 24 
 
future_index = range(n_forecast) 
 
exog_base = pd.DataFrame({ 
 "Brand_stationary": [0] * n_forecast, 
 "Market_stationary": [0] * n_forecast 
}, index=future_index) 
 
exog_shock = exog_base.copy() 
exog_shock.loc[0, "Brand_stationary"] = 1 
 
forecast_base = fitted.forecast(steps=n_forecast, exog=exog_base) 
forecast_shock = fitted.forecast(steps=n_forecast, exog=exog_shock) 
 
impact = forecast_shock["Base_stationary"] - forecast_base["Base_stationary"] 
 
plt.figure(figsize=(10, 4)) 
plt.plot(future_index, impact, marker='o') 
plt.title("Impact of 1-unit Increase in Brand Marketing on Base Sales") 
plt.xlabel("Months") 
plt.ylabel("Impact on Base Sales") 
plt.ylim(bottom=0) 
plt.grid(True) 
plt.tight_layout() 
plt.show()
```

![]()

User generated image

We can see that 1 unit increase in brand marketing spend has a long last effect out to 2 years!

We can also look at the cumulative effect which we can use to quantify a long term ROI.

```
cumulative_impact = impact.cumsum() 
plt.figure(figsize=(10, 4)) 
plt.plot(future_index, cumulative_impact, marker='o', color='orange', label='Cumulative Impact') 
plt.title("Cumulative Impact of 1-unit Increase in Brand Marketing on Base Sales") 
plt.xlabel("Months") 
plt.ylabel("Cumulative Impact on Base Sales") 
plt.grid(True) 
plt.legend() 
plt.tight_layout() 
plt.show()
```

![]()

User generated image


## 2a) Preparing The Data For VECM

To better understand how a Vector Error Correction Model (VECM) works, let’s simulate some simple synthetic data. This allows us to build intuition about cointegration, long-run relationships, and how short-term shocks interact across time series.

It’s worth noting that we have oversimplified the example to help readers understand a very difficult approach.

We’ll simulate three time series variables:


1. **Brand Marketing Pulses**

We start by defining marketing activity as a series of pulses over time. These are short bursts of spend — each pulse lasts 3 months and declines in intensity.


2. **Awareness**

Awareness behaves like a random walk with drift. It has:


- A memory (builds on its past value)

- An immediate response to marketing spend

- A small positive drift

- Some random noise.

```
awareness[t] = awareness[t-1] + 0.03 * brand_marketing[t] + 0.01 + ε
```

This creates a series that trends upward over time but in a stochastic, unpredictable way — a classic example of a non-stationary series.


3. **Base Sales — Co-integrated with Awareness**

Sales are also non-stationary, but they don’t drift freely. Instead, they adjust slowly toward awareness over time.

The key mechanism is an error correction term:

```
base_sales[t] = base_sales[t-1] + 0.02 * (awareness[t-1] - base_sales[t-1]) + ε
```

If sales diverge from awareness, this term gradually pulls them back into alignment — mimicking long-term equilibrium. This dynamic creates co-integration between sales and awareness.

```

# Settings 

start_date = '2019-11-30' 
np.random.seed(42) 
n_periods = 62 
 

# Brand Marketing Pulses (£000s) 

brand_marketing = np.zeros(n_periods) 
pulse_profiles = [ 
 [120, 80, 50], # Pulse 1 

 [100, 70, 40], # Pulse 2 

 [90, 60, 30], # Pulse 3 

 [110, 75, 45] # Pulse 4 

] 
pulse_starts = [5, 20, 35, 50] 
 
for i, start in enumerate(pulse_starts): 
 for j, value in enumerate(pulse_profiles[i]): 
 if start + j < n_periods: 
 brand_marketing[start + j] = value 
brand_marketing_scaled = brand_marketing * 10000 # Convert to £ 

 

# Awareness (non-stationary: random walk with drift) 

awareness = np.zeros(n_periods) 
for t in range(1, n_periods): 
 awareness[t] = ( 
 awareness[t - 1] 
 + 0.03 * brand_marketing[t] # Immediate marketing effect 

 + 0.01 # Drift 

 + np.random.normal(0, 0.5) 
 ) 
awareness_scaled = awareness * 5 + 20 # Scaled for realism 

 

# Base Sales (cointegrated with awareness via error correction) 

base_sales = np.zeros(n_periods) 
for t in range(2, n_periods): 
 base_sales[t] = ( 
 base_sales[t - 1] 
 + 0.02 * (awareness[t - 1] - base_sales[t - 1]) # Cointegration: Error correction term 

 + np.random.normal(0, 0.5) 
 ) 
base_sales_scaled = base_sales * 100 + 500 # Scale to real-world units 

 

# Time index 

date_range = pd.date_range(start=start_date, periods=n_periods, freq='M') 
 
df = pd.DataFrame({ 
 'Month': date_range, 
 'Brand_Marketing': brand_marketing_scaled, 
 'Awareness': awareness_scaled, 
 'Base_Sales': base_sales_scaled 
}) 
 
for name in ['Brand_Marketing', 'Awareness', 'Base_Sales']: 
 plt.figure(figsize=(10, 4)) 
 plt.plot(df['Month'], df[name], label=name) 
 plt.title(f"{name} Over Time") 
 plt.xlabel("Date") 
 plt.ylabel(name) 
 plt.legend() 
 plt.grid(True) 
 plt.tight_layout() 
 plt.show()
```

![]()

User generated image

![]()

User generated image

![]()

User generated image


## 2b) Fitting The VECM Model

Next we can fit the VECM model by feeding it the endogenous and exogenous series. We can use the statsmodel package in Python:

[## statsmodels.tsa.vector\_ar.vecm.VECM - statsmodels 0.14.4


### Combinations of these are possible (e.g. or for linear trend with intercept). When using a constant term you have to…

www.statsmodels.org](https://www.statsmodels.org/stable/generated/statsmodels.tsa.vector_ar.vecm.VECM.html?source=post_page-----bc577621a627---------------------------------------)

Like before, we scale the data to get variables on the same scale.

```
endog = df[["Awareness", "Base_Sales"]] 
exog = df[["Brand_Marketing"]] 
 
scaler_endog = StandardScaler() 
scaled_endog = pd.DataFrame( 
 scaler_endog.fit_transform(endog), 
 columns=endog.columns, 
 index=endog.index 
) 
 
scaler_exog = StandardScaler() 
scaled_exog = pd.DataFrame( 
 scaler_exog.fit_transform(exog), 
 columns=exog.columns, 
 index=exog.index 
)
```

Before fitting the VECM, we first check if the endogenous variables are co-integrated — that is, whether there’s a stable, long-run relationship between them despite being individually non-stationary.

We use the Johansen Cointegration Test for this purpose. It provides trace statistics and compares them against critical values to estimate the co-integration rank, i.e. the number of long-run equilibrium relationships among the variables.

```

# Run Johansen Cointegration Test 

jres = coint_johansen(scaled_endog, det_order=1, k_ar_diff=2) 
print("Johansen Trace Stats:", jres.lr1) 
print("Critical Values (95%):", jres.cvt[:, 1]) 
 

# Determine cointegration rank 

rank = np.sum(jres.lr1 > jres.cvt[:, 1]) 
print(f"\nEstimated Cointegration Rank: {rank}")
```

![]()

User generated image

Here, the first trace statistic (22.57) exceeds its critical value (18.40), but the second does not. This suggests there is 1 co-integrating relationship — i.e. one stable long-term equilibrium linking the variables.

Next, we determine how many lags to include in the model. This is important because it controls how much past information the VECM uses to explain current changes.

We use an automatic lag selection procedure (`select_order`) which evaluates multiple lag structures and selects the one that minimizes the Akaike Information Criterion (AIC). A lower AIC indicates a better trade-off between model fit and complexity.

```

# Lag Order Selection 

lag_order = select_order(scaled_endog, maxlags=5, deterministic="ci", exog=exog) 
print("\nLag Order Selection:\n", lag_order.summary()) 
optimal_lag = lag_order.aic 
print(f"\nOptimal Lag (AIC): {optimal_lag}")
```

![]()

User generated image

Although the output suggests an optimal lag of 0, this refers to the number of lagged differences included in the VECM. It corresponds to a VAR(1) in levels, meaning one lag of the original variables is used — which aligns with our data-generating process.

Now we estimate the Vector Error Correction Model (VECM) using the scaled data.

This model captures both:


- Short-run dynamics (how variables react to recent changes), and

- Long-run relationships (through the co-integration vectors).

We also include the exogenous variable `Brand_Marketing`, which allows us to isolate its effect—particularly how marketing influences awareness in the short run and, indirectly, base sales over time.

```

# Estimate VECM 

vecm_model = VECM( 
 endog=scaled_endog, 
 exog=scaled_exog, 
 k_ar_diff=optimal_lag, 
 coint_rank=rank, 
 deterministic="ci" # Constant in cointegrating equation 

) 
vecm_res = vecm_model.fit() 
print("\nVECM Summary:\n", vecm_res.summary())
```

![]()

User generated image

The estimated **cointegration vector** tells us how the endogenous variables relate to each other in the long run. We normalize the coefficients so that `Base_Sales` is expressed as a function of `Awareness`, making the relationship easier to interpret.

The exogenous coefficients reveal the short-run impact of marketing. Specifically, we examine how marketing affects awareness directly.

Finally, we combine the short-run and long-run components to calculate the implied long-run effect of marketing on base sales — tracing the influence of marketing through its impact on awareness and, in turn, base sales.

```

# Extract Cointegration Coefficients 

beta = vecm_res.beta.flatten() 
beta_awareness = beta[0] 
beta_base_sales = beta[1] 
const_val = vecm_res.det_coef_coint.flatten()[0] 
 

# Normalize to express Base_Sales as a function of Awareness 

beta_awareness_norm = -beta_awareness / beta_base_sales 
const_norm = -const_val / beta_base_sales 
 
print("\n--- Long-run Cointegration Equation ---") 
print(f"Base_Sales = {beta_awareness_norm:.3f} * Awareness + {const_norm:.3f}") 
 

# Extract Exogenous Coefficient on Awareness 

exog_coefs = vecm_res.exog_coefs 
marketing_coef_on_awareness = exog_coefs[0, 0] 
print(f"\nShort-run Effect of Marketing on Awareness: {marketing_coef_on_awareness:.6f}") 
 

# Compute Implied Long-run Effect of Marketing on Base Sales 

long_run_effect = marketing_coef_on_awareness * beta_awareness_norm 
print(f"\nImplied Long-run Effect of Marketing on Base Sales (via Awareness): {long_run_effect:.4f}")
```

![]()

User generated image

Let’s break this down further to add intuition:


## 🔹 Long-run Cointegration Equation


> `Base_Sales = 1.047 * Awareness + 3.229`

This tells us that Base Sales and Awareness move together over the long term. Specifically, for every 1 standard deviation increase in Awareness, Base Sales are expected to increase by about 1.05 standard deviations in the long run (since the data is scaled).


## 🔹 Short-run Effect of Marketing on Awareness


> `0.1605`

This means that a 1 standard deviation increase in Brand Marketing causes a 0.16 standard deviation rise in Awareness in the next period.


## 🔹 Implied Long-run Effect of Marketing on Base Sales


> `0.1605 × 1.047 ≈ 0.1682`

This is the indirect, long-term payoff of marketing: via its effect on awareness, marketing ultimately lifts base sales by ~0.17 standard deviations per unit of effort.

📌 **Strategic takeaway**: 
You’re quantifying the **long-term ROI** of brand marketing — not just how it boosts awareness, but how that awareness translates into lasting sales growth.

**Note on Estimating Long-Term Effects:**

Just a quick clarification: when estimating the indirect long-term effect of marketing on the base, we shouldn’t use the cointegration parameter between the base and the brand metric. Instead, we should use the impulse response.

In a simple VAR(1) without feedback (like our example) they give the same result. But in higher-order VARs or VECMs with feedback, the long-term effects can differ significantly. The impulse response properly captures the full dynamic impact over time, while the cointegration parameter does not.


# What Problems Might We Face In Practice?

Unfortunately, things are rarely as clean-cut in the real world as in our simplified example. Here are a few practical challenges to keep in mind:


- **Identifying the impulse response function (IRF)** 
 Even if you’ve established co-integration, using impulse response functions meaningfully requires identifying the underlying shocks. This means defining the structure of the system well enough to determine which variable is causing what — and how. Without proper identification (typically done using structural assumptions or restrictions), IRFs can be misleading and reflect mere correlation rather than true causation.

- **Market demand as a driver of consideration** 
 If market demand heavily influences brand consideration, you may need to model it as an endogenous variable, which complicates estimation and identification.

- **Brand metrics collected too infrequently** 
 If your brand metrics are only collected monthly, the limited number of data points can make it difficult to estimate coefficients with confidence. Bayesian methods can help somewhat by incorporating prior beliefs or smoothing, but they won’t solve everything.

- **No historical brand data available** 
 If you haven’t been collecting brand metrics — or only just started — you’ll need to find a suitable proxy or be prepared to wait until enough data accumulates. One potential workaround: consider using **share of search** as a proxy for brand interest.


# Closing Thoughts

Today, we focused on understanding how we can estimate the long-term effects of brand marketing. But brand marketing isn’t the only lever businesses can pull on to increase brand equity. We also need to focus on other internal drivers, such as new products, product changes, and PR. After all, marketing can’t do it all on its own!

Equally important are the external drivers that influence brand equity. From a causal inference perspective, we must account for all potential confounders — external factors like market trends, competitor actions, and economic shifts. But understanding these external forces is also crucial because they can help us refine our marketing strategy, improve product offerings, and tailor messaging that resonates with our audience.

Let’s not forget about nurturing existing customers! It’s not all about acquisition growth. So, what are the long-term drivers of retention? It’s likely not the intrusive product offers you’re throwing at customers just to grab short-term attention.

What role does CRM play in product adoption? Are CRM campaigns effectively driving long-term product adoption, or is it just about pushing promotions?

And what about Operations? How do their actions impact retention rates? Are their efforts mediating through customer satisfaction scores and translating into better long-term retention?

![]()

User generated image

By considering both internal and external drivers of brand equity — along with the long-term effects of brand marketing — we can better understand the full scope of levers that influence growth and retention, ultimately leading to more sustainable business success.

I hope you enjoyed my article. Follow me if you would like to learn more about complex topics from Data Science.