---
title: "Accuracy Is Dead: Calibration, Discrimination, and Other Metrics You Actually Need | Towards Data Science"
og_title: "Accuracy Is Dead: Calibration, Discrimination, and Other Metrics You Actually Need | Towards Data Science"
description: "A deep dive into advanced evaluation for data scientists"
url: "https://towardsdatascience.com/accuracy-is-dead-calibration-discrimination-and-other-metrics-you-actually-need/"
published: "2025-07-15T00:41:39+00:00"
author: "Pol Marin"
---

# Accuracy Is Dead: Calibration, Discrimination, and Other Metrics You Actually Need | Towards Data Science

## Article Information

**Author:** Pol Marin
**Published:** 2025-07-15T00:41:39+00:00
**Original URL:** https://towardsdatascience.com/accuracy-is-dead-calibration-discrimination-and-other-metrics-you-actually-need/

**Description:** A deep dive into advanced evaluation for data scientists

---

[Data Science](https://towardsdatascience.com/category/data-science/)


# Accuracy Is Dead: Calibration, Discrimination, and Other Metrics You Actually Need

A deep dive into advanced evaluation for data scientists

[Pol Marin](https://towardsdatascience.com/author/polmarin/)

Jul 14, 2025

7 min read

Share

![Image](images/afif-ramdhasuma-RjqCk9MqhNg-unsplash-1.jpg)

Image by [Afif Ramdhasuma](https://unsplash.com/es/@javaistan?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) in [Unsplash](https://unsplash.com/es/fotos/rueda-redonda-roja-blanca-y-negra-RjqCk9MqhNg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

Accuracy is often the metric we, data scientists, cite the most — but also the most misleading.

It was long ago that we found out that models are developed for far more than just making predictions. We create models to make decisions, and that requires trust. And relying on the accuracy is simply not enough.

In this post, we’ll see why and we’ll check other alternatives, more advanced and tailored to our needs. As always, we’ll do it following a practical approach, with the end goal of deep diving into evaluation beyond standard metrics.

Here’s the table of contents for today’s read:


1. Setting Up the Models

2. Classification: Beyond Accuracy

3. Regression: Advanced Evaluation

4. Conclusion


## Setting Up the Models

Accuracy makes more sense for classification algorithms rather than regression tasks… Hence, not all problems are measured equally.

That’s the reason why I’ve decided to tackle both scenarios — the regression and the classification ones — separately by creating two different models.

And they’ll be very simple ones, because their performance and application isn’t what matters today:


- **Classification**: Will a striker score in the next match?

- **Regression**: How many goals will a player score?

If you’re a recurrent reader, I’m sure that the use of football examples didn’t come as a surprise.

**Note**: Even though we won’t be using accuracy on our regression problem and this post is thought to be more focused on that metric, I didn’t want to leave these cases behind. So that’s why we’ll be exploring regression metrics too.

Again, because we don’t care about the data nor the performance, let me skip all the preprocessing part and go straight to the models themselves:

```
```python

# Classification model

model = LogisticRegression()
model.fit(X_train_scaled, y_train)


# Gradient boosting regressor

model = GradientBoostingRegressor()
model.fit(X_train_scaled, y_train)
```
```

As you can see, we stick to simple models: logistic regression for the binary classification, and gradient boosting for regression.

Let’s check the metrics we’d usually check:

```
```python

# Classification

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test accuracy: {accuracy:.2%}")
```
```

The printed accuracy is 92.43%, which is honestly way higher than what I’d have expected. Is the model really that good?

```
```python

# Regression

y_pred = model.predict(X_test_scaled)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Test RMSE: {rmse:.4f}")
```
```

I got an RMSE of 0.3059. Not that good. But is it enough to discard our regression model?

We need to do better.


## Classification: Beyond Accuracy

Too many data science projects stop at accuracy, which is often misleading, especially with imbalanced targets (e.g., scoring a goal is rare).

To evaluate whether our model *really* predicts “Will this player perform?”, here are other metrics we should consider:


- **ROC-AUC**: Measures ability to rank positives above negatives. Insensitive to threshold but doesn’t care about calibration.

- **PR-AUC**: Precision-Recall curve is essential for rare events (e.g., scoring probability). It focuses on the positive class, which matters when positives are scarce.

- **Log Loss**: Punishes overconfident wrong predictions. Ideal for comparing calibrated probabilistic outputs.

- **Brier Score**: Measures mean squared error between predicted probabilities and actual outcomes. Lower is better, and it’s interpretable as overall probability calibration.

- **Calibration Curves**: Visual diagnostic to see if predicted probabilities match observed frequencies.

We won’t test all of them now, but let’s briefly touch upon ROC-AUC and Log Loss, probably the most used after accuracy.


### ROC-AUC

ROC-AUC, or *Receiver Operating Characteristic – Area Under the Curve*, is a popular metric that consists in measuring the area under the ROC curve, which is a curve that plots the True Positive rate (TPR) against the False Positive rate (FPR).

Simply put, the ROC-AUC score (ranging from 0 to 1) sums up how well a model can produce relative scores to discriminate between positive or negative instances across all classification thresholds.

A score of 0.5 indicates random guessing and a 1 is a perfect performance.

Computing it in Python is easy:

```
```python
from sklearn.metrics import roc_auc_score

roc_auc = roc_auc_score(y_test, y_proba)
```
```

Here, y\_true contains the real labels and y\_proba contains our model’s predicted prorbabilities. In my case the score is 0.7585, which is relatively low compared to the accuracy. But how can this be possible, if we got an accuracy above 90%?

Context: We’re trying to predict whether a player will score in a match or not. The “problem” is that this is highly imbalanced data: most players won’t score in a match, so our model learns that predicting a 0 is the most probable, without really learning anything about the data itself.

It can’t capture the minority class correctly and accuracy simply doesn’t show us that.


### Log Loss

The logarithmic loss, cross-entropy or, simply, log loss, is used to evaluate the performance with probability outputs. It measures the difference between the predicted probabilities and the actual (true) values, logarithmically.

Again, we can do this with a one-liner in python:

```
```python
from sklearn.metrics import log_loss

logloss = log_loss(y_test, y_proba)
```
```

As you’ve probably guessed, the lower the value, the better. A 0 would be the perfect model. In my case, I got a 0.2345.

This one is also affected by class imbalance: Log loss penalizes confident wrong predictions very harshly and, since our model predicts a 0 most of the time, those cases in which there was indeed a goal scored affect the final score.


## Regression: Advanced Evaluation

Accuracy makes no sense in regression but we have a handful of interesting metrics to evaluate the problem of how many goals will a player score in a given match.

When predicting **continuous outcomes** (e.g., expected minutes, match ratings, fantasy points), simple RMSE/MAE is a start—but we can go much further.

Other metrics and checks:


- **R²**: Represents the proportion of the variance in the target variable explained by the model.


- **RMSLE**: Penalizes underestimates more and is useful if values vary exponentially (e.g., fantasy points).


- **MAPE / SMAPE**: Percentage errors, but beware divide-by-zero issues.


- **Quantile Loss**: Train models to predict intervals (e.g., 10th, 50th, 90th percentile outcomes).

- **Residual vs. Predicted** **(plot)**: Check for heteroscedasticity.

Again, let’s focus on a subgroup of them.


### R² Score

Also called the coefficient of determination, it compares a model’s error to the baseline error. A score of 1 is the perfect fit, a 0 means that it predicts the mean only, and a value below 0 means that it’s worse than mean prediction.

```
```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
```
```

I got a value of 0.0557, which is pretty close to 0… Not good.


### RMSLE

The *Root Mean Squared Logarithmic Error,* or RMSLE, measures the square root of the average squared difference between the **l**og-transformed predicted and actual values. This metric is useful when:


- We want to penalize under-prediction more gently.

- Our target variables are skewed (it reduces the impact of large outliers).

```
```python
from sklearn.metrics import mean_squared_log_error

rmsle = np.sqrt(mean_squared_log_error(y_test, y_pred))
```
```

I got a 0.19684 which means that my average prediction error is about 0.2 goals. It’s not that big but, given that our target variable is a value between 0 and 4 and highly skewed towards 0…


### Quantile Loss

Also called Pinball Loss, it can be used for quantile regression models to evaluate how well our predicted quantiles perform. If we build a quantile model (GradientBoostingRegressor with quantile loss), we can test it as follows:

```
```python
from sklearn.metrics import mean_pinball_loss

alpha = 0.9
q_loss = mean_pinball_loss(y_test, y_pred_quantile, alpha=alpha)

```
```

Here, with alpha 0.9 we’re trying to predict the 90th percentile. My quantile loss is 0.0644 which is very small in relative terms (~1.6% of my target variable range).

However, distribution matters: Most of our *y\_test* values are 0, and we need to interpret it as “*on average, our model’s error in capturing the upper tail is very low*“.

It’s especially impressive given the 0-heavy target.

But, because most outcomes are 0, other metrics like the ones we saw and mentioned above should be used to assess whether our model is in fact performing well or not.


## Conclusion

Building predictive models goes far beyond simply achieving “good accuracy.”

For **classification** tasks, you need to think about imbalanced data, probability calibration, and real-world use cases like pricing or risk management.

For **regression**, the goal is not just minimizing error but understanding uncertainty—vital if your predictions inform strategy or trading decisions.

Ultimately, true value lies in:


- Carefully curated, temporally valid features.

- Advanced evaluation metrics tailored to the problem.

- Transparent, well-visualized comparisons.

If you get these right, you’re no longer building “just another model.” You’re delivering robust, decision-ready tools. And the metrics we explored here are just the entry point.

---

Written By

Pol Marin

[See all from Pol Marin](https://towardsdatascience.com/author/polmarin/)

[Classification](https://towardsdatascience.com/tag/classification/), [Evaluation Metrics](https://towardsdatascience.com/tag/evaluation-metrics/), [Model Evaluation](https://towardsdatascience.com/tag/model-evaluation/), [Predictive Algorithm](https://towardsdatascience.com/tag/predictive-algorithm/), [Regression](https://towardsdatascience.com/tag/regression/)

Share This Article


- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ftowardsdatascience.com%2Faccuracy-is-dead-calibration-discrimination-and-other-metrics-you-actually-need%2F&title=Accuracy%20Is%20Dead%3A%20Calibration%2C%20Discrimination%2C%20and%20Other%20Metrics%20You%20Actually%20Need)

- [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Ftowardsdatascience.com%2Faccuracy-is-dead-calibration-discrimination-and-other-metrics-you-actually-need%2F&title=Accuracy%20Is%20Dead%3A%20Calibration%2C%20Discrimination%2C%20and%20Other%20Metrics%20You%20Actually%20Need)

- [Share on X](https://x.com/share?url=https%3A%2F%2Ftowardsdatascience.com%2Faccuracy-is-dead-calibration-discrimination-and-other-metrics-you-actually-need%2F&text=Accuracy%20Is%20Dead%3A%20Calibration%2C%20Discrimination%2C%20and%20Other%20Metrics%20You%20Actually%20Need)

Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.

[Write for TDS](https://towardsdatascience.com/questions-96667b06af5/)