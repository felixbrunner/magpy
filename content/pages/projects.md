Title: Projects
Date: 2020-01-01 12:00
Modified: 2023-07-13 18:00
Category: General
Tags:
Slug: projects
Authors: Felix Brunner
Summary:

<!-- ## Data Science Projects -->

This page presents descriptions of some of the **data projects** I have been involved in.

## Quality prediction based on time series data in a manufacturing context
<!-- with [Bond3D](https://www.bond3d.com/), [Fraunhofer IPT](https://www.ipt.fraunhofer.de/), and [dida machine learning](https://dida.do/), 2021-2023 -->

<!-- **Description:** -->
In this machine learning use case in the manufacturing domain the task is to analyze large amounts of **time series data** recorded from production machines with regards to their predictive power when it comes to the quality of the final products.
Finding useful patterns in the **sensory recordings** is challenging due to the large data quantities connected to a single outcome label.
A main task here is filtering and connecting various data sources and combining the data in way that can be ingested by a PyTorch neural network model.
Multiple predictive model architectures have been tested, spanning from simple statistical models to deep convolutional neural networks.
An additional emphasis is on **AI explainability** since the production engineers are especially interested in making sense of the findings.
My role in this project was mainly in conceptualizing and implementing **data pipelines** and predictive algorithms.
Details about the employed **model architecture** can be found in a three-part article (parts [one](https://medium.com/dida-machine-learning/explainable-time-series-classification-with-x-rocket-3087b912a08d?source=friends_link&sk=c9e42fa9bfe32cd58f804673ca5aef8c), [two](https://medium.com/dida-machine-learning/inside-x-rocket-explaining-the-explainable-rocket-534b104c4a08?source=friends_link&sk=4222cf1591d49181eff368f97d0bdee0) and [three](https://medium.com/dida-machine-learning/x-rocket-to-the-moon-c2848e740243?source=friends_link&sk=a8428dac4867839dc22007196c6a4f87)), and in the belonging [code repository](https://github.com/dida-do/xrocket).

<!-- <p align="center"><img src="https://miro.medium.com/v2/resize:fit:1268/format:webp/1*9Xopehn3Z_V8aCr-ZVGCzQ.png" alt="drawing" width="700"/></p> -->
<p align="center"><img src="assets/drawings/xrocket-full.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


## Machine status detection in 3D printing based on infrared image data
<!-- with [Bond3D](https://www.bond3d.com/), [Fraunhofer IPT](https://www.ipt.fraunhofer.de/), and [dida machine learning](https://dida.do/), 2021-2023 -->

<!-- **Description:** -->
The goal of this project is to identify irregularities during an automated cleaning step in industrial additive manufacturing through **computer vision** techniques.
A visual **deep learning algorithm** detects pollution of the production machine during the printing process, such that damage can be prevented and machine time is saved.
A core challenge here is to deal with data heterogeneity among various production machines and limited data availability, which was tackled via approaches to **data augmentation**.
More information about the machine learning use case and the overall project can be found [here](https://dida.do/projects/contamination-detection-in-industrial-3d-printing), [here](https://www.ipt.fraunhofer.de/de/projekte/ai-gent3d.html) and [here](https://www.zukunft-der-wertschoepfung.de/projekte/eranet-ki-gesttztes-generatives-3d-drucken-manunet-aigent3d/).
As an auxiliary result, the labeling tool we created for the **annotation of the image dataset** is described in [this article](https://medium.com/dida-machine-learning/how-to-implement-an-image-labeling-tool-in-a-jupyter-notebook-4aa4099addba?source=friends_link&sk=3ee7eabd27f2bf29226fbd8e970cc1f6), and the belonging code is in [this code repository](https://github.com/dida-do/public/tree/master/labelingtool).
I contributed to this project in the development of the implemented solution and in the coordination with the project partners.

<p align="center"><img src="https://cdn.dida.do/labelled-1687853311-(1).jpg" alt="drawing" width="700"/></p>
<!-- <p align="center"><img src="/content/assets/images/" alt="drawing" width="700"/></p> -->

<br/><br/><br/>


## Automated question answering via retrieval of internal natural language documents
<!-- with [dida machine learning](https://dida.do/), 2022 -->

<!-- **Description:** -->
This line of work aimed to proof the concept of question answering based on internal documents and to gain experience with state-of-the-art **NLP** developments.
An early demo using **extractive** question answering based on **semantic search** is still online [here](https://dida.do/demos/question-answering).
Later stages explored full-fletched **generative** question answering with the help of **large language models (LLMs)** and **retrieval augmented generation (RAG)**.
My role in this project was to make contributions to the codebase and to update the involved developers about the latest trends in research and industry.

<p align="center"><img src="https://files.readme.io/0343fcb-RAG_2.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


## Estimation and analysis of financial variance spillover networks for academic research
<!-- with [Ruben Hipp](https://sites.google.com/view/rubenhipp/home) at [Nova SBE](https://www.novasbe.unl.pt/en/) 2022 -->

<!-- **Description:** -->
As a basis for some of my [research papers](research), substantial coding effort was necessary in the context of financial time series data.
First, this project required extensive data acquisition from large databases via **SQL**.
Then, the project samples representative data points and uses a **data pre-processing pipeline** to prepare estimation data over a rolling time interval.
[This repository](https://github.com/felixbrunner/euraculus) implements various **object-oriented programs (OOP)** for the estimation of **regularized statistical learning** algorithms with **cross-validation**.
Finally, there are various flavors of **statistical analysis** to obtain the empirical results of the research papers.
The code in the repository is written by myself, with conceptual help of my co-author [Ruben Hipp](https://sites.google.com/view/rubenhipp/home).

<p align="center"><img src="/assets/graphs/contour_var.png" alt="drawing" width="550"/></p>

<br/><br/><br/>


## System to predict success of police searches and AI fairness analysis
<!-- LDSSA batch 4, 2020 -->

<!-- **Description:** -->
This is a sample of work that I produced as a capstone project for the [Lisbon data science academy](https://www.lisbondatascience.org/) (additional info in the wiki [here](https://ldssa.github.io/wiki/)).
Given a **tabular dataset** of UK police data, the goal of this mock project is to come up with a **machine learning model** to approve police searches to maximize success rates while minimizing discrimination.
The main tasks are to perform detailed **exploratory data analysis (EDA)** with regards to existing stop and search practices, to develop a prediction system to "authorize" searches such that biases are mitigated, and to **deploy** this system as an accessible application via a responsive **API endpoint**.
More detailed reports about this project can be found [here](https://docs.google.com/document/d/17R__XRJQlo-NuDK9H9dAb_7soOW80RDrAHdl_L5oI_o/edit?usp=sharing) and [here](https://docs.google.com/document/d/1R-ibDWOvTEMWNsaBjlbt3BOdZ4dMhwDJlwd4FwDt0KQ/edit?usp=sharing), with the respective code being hosted [here](https://github.com/felixbrunner/capstone) and [here](https://github.com/felixbrunner/capstone-deploy).
I prepared the implementation and analysis in this project by myself, which helped to develop good fundamentals in data science and machine learning pipelines. 

<p align="center"><img src="/assets/drawings/capstone-pipeline.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


<!-- ## yetagain
library to estimate and study layered probabilistic time series models 

**Description:**

-->