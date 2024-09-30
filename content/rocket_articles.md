Title: New articles on explainable encodings for time series classification
Summary: Series of articles about an explainable solution to time series classification tasks with X-ROCKET is now online.
Date: 2023-11-08 12:00
Modified: 2024-01-07 12:00
Category: announcements
Tags: announcements, blog, data science, time series
Slug: rocket-blog
Authors: Felix Brunner

## Explainable time series classification with X-ROCKET
A three-part series of articles that I recently released discusses the state of time series classification, and introduces an extension to a state-of-the-art encoding model to add explainability.

The [first part](https://medium.com/dida-machine-learning/explainable-time-series-classification-with-x-rocket-3087b912a08d?source=friends_link&sk=c9e42fa9bfe32cd58f804673ca5aef8c) provides an overview over time series classification problems and one solution to them -- the ROCKET encoder model. 
[Part two](https://medium.com/dida-machine-learning/inside-x-rocket-explaining-the-explainable-rocket-534b104c4a08?source=friends_link&sk=4222cf1591d49181eff368f97d0bdee0) explains more thoroughly how this model uses convolutions to filter input time series for a fixed set of patterns, which can be made explainable if carefully put together.
Finally, [part three](https://medium.com/dida-machine-learning/x-rocket-to-the-moon-c2848e740243?source=friends_link&sk=a8428dac4867839dc22007196c6a4f87) of the article demonstrates the predictive performance and interpretability of the model in a practical usage example.

The code belonging to the described X-ROCKET model can be found in [this repository](https://github.com/dida-do/xrocket).

<p align="center"><img src="../assets/images/rocket_medium-head.png" alt="image" width="700"/></p>