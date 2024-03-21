Title: Projects
Date: 2020-01-01 12:00
Modified: 2023-07-13 18:00
Category: General
Tags:
Slug: projects
Authors: Felix Brunner
Summary:

This page presents descriptions of some of the **data projects** I have been involved in.

## Quality prediction based on sensor time series data in a manufacturing context
<!-- with [Bond3D](https://www.bond3d.com/), [Fraunhofer IPT](https://www.ipt.fraunhofer.de/), and [dida machine learning](https://dida.do/), 2021-2023 -->

### Overview:
This project focuses on analyzing large volumes of time series data collected from production machines to determine their predictive power in assessing the quality of final products. Extracting meaningful patterns from sensory recordings presents a challenge due to the vast data quantities associated with a single outcome label.

### Objectives:
1. **Pattern identification:** Identify patterns in time series data correlated with the quality of final products to guide process optimization.
2. **Data integration:** Filter, connect, and integrate various data sources to construct consistent datasets suitable for predictive modeling.
3. **Model development:** Conceptualize and implement data pipelines and modeling approaches to develop a machine learning system for quality prediction.
4. **Algorithm testing:** Test multiple predictive algorithms, including simple statistical models and deep neural networks, to evaluate their efficacy in quality prediction.
5. **AI explainability:** Emphasize the interpretability of AI findings to facilitate understanding and interpretation by production engineers.

### Activities:
1. **Data analysis:** Analyzed and visualized large amounts of time series data to discern patterns and trends.
2. **Data preparation:** Explored, filtered, and connected various data sources to construct consistent datasets suitable for predictive modeling.
3. **Pipeline development:** Conceptualized and implemented data pipelines to preprocess and prepare data for ingestion by machine learning models in PyTorch.
4. **Model implementation:** Implemented an interpretable machine learning system to predict product quality in a manufacturing context.
5. **Algorithm evaluation:** Tested and evaluated various predictive algorithms to identify the most effective approach for quality prediction and AI explainability.

### Outcome:
The project yielded qualitative insights that serve as valuable guidance for process engineers in optimizing production processes, ultimately enhancing product quality and operational efficiency.

### Stack:
PyTorch, CNNs, ROCKET model, data wrangling, git, time series classification, explainable AI, python

### Additional details and links:
In this machine learning use case, various predictive model architectures were tested, including simple statistical models and deep convolutional neural networks. Special emphasis was placed on AI explainability to facilitate understanding by production engineers.

For further details on the model architecture and implementation, refer to my three-part article series on the X-ROCKET architecture ([Part One](https://medium.com/dida-machine-learning/explainable-time-series-classification-with-x-rocket-3087b912a08d?source=friends_link&sk=c9e42fa9bfe32cd58f804673ca5aef8c), [Part Two](https://medium.com/dida-machine-learning/inside-x-rocket-explaining-the-explainable-rocket-534b104c4a08?source=friends_link&sk=4222cf1591d49181eff368f97d0bdee0), and [Part Three](https://medium.com/dida-machine-learning/x-rocket-to-the-moon-c2848e740243?source=friends_link&sk=a8428dac4867839dc22007196c6a4f87)), and the corresponding [code repository](https://github.com/dida-do/xrocket).


<!-- <p align="center"><img src="https://miro.medium.com/v2/resize:fit:1268/format:webp/1*9Xopehn3Z_V8aCr-ZVGCzQ.png" alt="drawing" width="700"/></p> -->
<p align="center"><img src="assets/drawings/xrocket-full.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


## Machine status detection in 3D printing based on infrared image data
<!-- with [Bond3D](https://www.bond3d.com/), [Fraunhofer IPT](https://www.ipt.fraunhofer.de/), and [dida machine learning](https://dida.do/), 2021-2023 -->

### Overview:
The objective of this project is to automate the process monitoring in industrial additive manufacturing, specifically targeting the identification of irregularities during the printing process through computer vision techniques. By leveraging visual deep learning algorithms, the system aims to detect pollution of production machines in real-time, thereby preventing damage and optimizing machine utilization.

### Objectives:
1. **Use case definition:** Conduct workshops with domain experts to analyze potential of machine learning approaches to the production environment.
2. **Automated detection:** Develop a visual deep learning algorithm to identify pollution in production machines during the printing process.
3. **Data augmentation:** Implement data augmentation techniques to address data heterogeneity among various production machines and limited data availability.
4. **Model deployment:** Supply a containerized model with API endpoints for seamless deployment to production machines.

### Activities:
1. **Data collection and pre-processing:** Guided systematic data collection and pre-processing procedures to prepare datasets for machine learning algorithms.
2. **Labeling process:** Defined the labeling process and implemented an interface for annotating the image datasets to facilitate model training.
3. **Algorithm development:** Contributed to the development of a visual deep learning algorithm to detect machine pollution in the live production environment.
4. **Data augmentation:** Applied data augmentation techniques to handle data heterogeneity and improve model robustness.
5. **Model deployment:** Supplied a containerized model with API endpoints for deployment to production machines.
6. **Project coordination:** Coordinated with project partners and represented a five-person project team in meetings, presentations, and reporting activities for stakeholders.

### Outcome:
The project delivered a production-ready system capable of informing operators of potential faults in real-time during an automated cleaning step in industrial additive manufacturing, thereby optimizing machine utilization and preventing damage.

### Stack:
PyTorch, Convolutional neural networks (CNNs), docker, git, OpenCV, FastAPI, Computer vision, pytorch-lightning, ipywidgets, python

### Additional details and links:
For more information on the machine learning use case and the overall project, refer to the project pages of [dida](https://dida.do/projects/contamination-detection-in-industrial-3d-printing), [Fraunhofer IPT](https://www.ipt.fraunhofer.de/de/projekte/ai-gent3d.html), and [BMBF](https://www.zukunft-der-wertschoepfung.de/projekte/eranet-ki-gesttztes-generatives-3d-drucken-manunet-aigent3d/).

Additionally, details about the labeling tool created for the annotation of the image dataset can be found in [this article](https://medium.com/dida-machine-learning/how-to-implement-an-image-labeling-tool-in-a-jupyter-notebook-4aa4099addba?source=friends_link&sk=3ee7eabd27f2bf29226fbd8e970cc1f6) I wrote, and the corresponding code is available in [this code repository](https://github.com/dida-do/public/tree/master/labelingtool).

<p align="center"><img src="https://cdn.dida.do/labelled-1687853311-(1).jpg" alt="drawing" width="700"/></p>
<!-- <p align="center"><img src="/content/assets/images/" alt="drawing" width="700"/></p> -->

<br/><br/><br/>


## Automated question answering via retrieval of internal natural language documents
<!-- with [dida machine learning](https://dida.do/), 2022 -->

### Overview:
The project aimed to integrate a chatbot for question answering (QA) based on on internal documents into the communication platform used by the employees. This initiative sought to test out state-of-the-art NLP techniques internally, and to enhance employee productivity by providing instant access to relevant information stored in internal documents.

### Objectives:
1. **Proof of concept:** Demonstrate the feasibility of question answering based on internal documents using state-of-the-art NLP techniques.
2. **Demo development:** Create a demo showcasing extractive QA based on semantic search for initial validation and feedback.
3. **Proof-of-concept expansion:** Develop a proof-of-concept for automatic question answering with generative QA, leveraging large language models (LLMs) and retrieval augmented generation (RAG).
4. **Knowledge sharing:** Keep developers informed about recent advancements in natural language processing (NLP) to drive innovation and stay abreast of industry trends.

### Activities:
1. **Demo creation:** Tested extractive QA in a demo based on a single provided document.
2. **Proof-of-concept development:** Extended the QA capabilities by including automatic document retrieval with semantic search and experimented with generative QA using an LLM.
3. **Knowledge sharing:** Provided updates to developers on the latest trends and advancements in NLP research and industry practices.

### Outcome:
The project successfully delivered a responsive chatbot for document-based extractive QA, empowering employees with instant access to pertinent information. The chatbot is responsive to all employees, promising to contribute to increased productivity and streamlined communication within the company.

### Stack:
huggingface transformers, haystack, LLMs, document retrieval, semantic search, question answering, BERT, git, beautifulsoup, python

### Additional details and links:
The project journey began with an early demo showcasing extractive question answering based on semantic search, still accessible online [here](https://dida.do/demos/question-answering). Subsequent stages explored full-fledged generative question answering using large language models (LLMs) and retrieval augmented generation (RAG) techniques.

<p align="center"><img src="https://files.readme.io/0343fcb-RAG_2.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


## Estimation and analysis of financial variance spillover networks for academic research
<!-- with [Ruben Hipp](https://sites.google.com/view/rubenhipp/home) at [Nova SBE](https://www.novasbe.unl.pt/en/) 2022 -->

<!-- **Description:** -->
<!-- As a basis for some of my [research papers](research), substantial coding effort was necessary in the context of financial time series data.
First, this project required extensive data acquisition from large databases via **SQL**.
Then, the project samples representative data points and uses a **data pre-processing pipeline** to prepare estimation data over a rolling time interval.
[This repository](https://github.com/felixbrunner/euraculus) implements various **object-oriented programs (OOP)** for the estimation of **regularized statistical learning** algorithms with **cross-validation**.
Finally, there are various flavors of **statistical analysis** to obtain the empirical results of the research papers.
The code in the repository is written by myself, with conceptual help of my co-author [Ruben Hipp](https://sites.google.com/view/rubenhipp/home). -->

### Overview:
The project aimed to enhance network estimation methodologies for economic and financial data analysis by leveraging machine learning methods. The primary objective was to develop robust models for the analysis of large-dimensional datasets to provide new insights in economic questions related to industrial production and stock market volatility.

### Objectives:
1. **Methodology exploration:** Explore and compare statistical learning algorithms for multivariate forecasting to identify the most suitable approach.
2. **Data acquisition:** Acquire datasets from SQL databases to ensure access to comprehensive and relevant financial time series data.
3. **Automated pre-processing:** Set up an automated pre-processing pipeline to handle large datasets and ensure data quality and consistency.
4. **Model implementation:** Develop object-oriented code to run cross-validated regularized machine learning algorithms for network estimation.
5. **Statistical analysis:** Conduct extensive statistical and econometric analyses to empirically evaluate the performance of the developed models.
6. **Research publication:** Author research papers presenting the results at academic standards and contribute to the advancement of knowledge in the field of applied econometrics.

### Activities:
1. **Data acquisition:** Acquireed financial time series data from large databases using SQL queries.
2. **Data pre-processing:** Implemented a data pre-processing pipeline to prepare estimation data over rolling time intervals.
3. **Model development:** Developed object-oriented programs for the estimation of regularized statistical learning algorithms with cross-validation.
4. **Statistical analysis:** Performed various flavors of statistical analysis to obtain empirical results for research papers.
5. **Collaborative effort:** Collaborated internationally to conceptualize and refine the research approach.

### Outcome:
The project culminated in the publication of an acclaimed paper in _Quantitative Economics_, with follow-up papers currently under review. The developed methodologies and findings contribute to advancing the field of financial time series analysis and forecasting.

### Stack:
pandas, numpy, time series forecasting, scikit-learn, python, SQL, glmnet, econometrics, vector auto-regression, networkx

### Additional Details:
For more information on the research papers and the underlying code repository, visit the [research page](research) and the [GitHub repository](https://github.com/felixbrunner/euraculus). The repository contains object-oriented programs for implementing regularized statistical learning algorithms with cross-validation, reflecting the culmination of substantial coding efforts in financial time series data analysis. The first related research publication with [Ruben Hipp](https://sites.google.com/view/rubenhip/home) is available in [_Quantitative Economics_](https://www.econometricsociety.org/publications/quantitative-economics/2023/07/01/Estimating-Large-Dimensional-Connectedness-Tables-The-Great-Moderation-through-the-Lens-of-Sectoral-Spillovers).

published 

<p align="center"><img src="/assets/graphs/contour_var.png" alt="drawing" width="550"/></p>

<br/><br/><br/>


## System to predict success of police searches and AI fairness analysis
<!-- LDSSA batch 4, 2020 -->

### Overview:
This project, conducted as a capstone project for the [Lisbon Data Science Academy](https://www.lisbondatascience.org/), focuses on developing a machine learning model to optimize police search approval decisions while minimizing discrimination. Using a tabular dataset of UK police data, the goal is to create a predictive system that maximizes search success rates while mitigating biases in stop and search practices.

### Objectives:
1. **Exploratory data analysis (EDA):** Conduct detailed EDA to understand existing stop and search practices and identify potential biases.
2. **Model development:** Develop a machine learning model to predict the authorization of police searches, ensuring fairness and effectiveness.
3. **Deployment:** Deploy the developed system as an accessible application via a responsive API endpoint for practical use.

### Activities:
1. **Data exploration:** Performed thorough EDA on the UK police dataset to uncover insights into stop and search practices and identify patterns related to search authorization.
2. **Model building:** Developed a predictive model using machine learning techniques to approve police searches while minimizing discrimination and maximizing success rates.
3. **Deployment:** Implemented the predictive system as an accessible application with a responsive API endpoint for easy access and utilization.
   
### Outcome:
The project culminated in the development of a predictive model for police search approval, contributing to the optimization of stop and search practices while ensuring fairness and effectiveness.

### Stack:
pandas, numpy, gradient boosting, scikit-learn, python, Flask, heroku
   
### Additional details and links:
The implementation and analysis of this project were carried out independently, contributing to the development of strong fundamentals in data science and machine learning pipelines. Detailed reportsassociated with the project can be found [here](https://docs.google.com/document/d/17R__XRJQlo-NuDK9H9dAb_7soOW80RDrAHdl_L5oI_o/edit?usp=sharing) and [here](https://docs.google.com/document/d/1R-ibDWOvTEMWNsaBjlbt3BOdZ4dMhwDJlwd4FwDt0KQ/edit?usp=sharing), related code repositories are available [here](https://github.com/felixbrunner/capstone) and [here](https://github.com/felixbrunner/capstone-deploy).

<p align="center"><img src="/assets/drawings/capstone-pipeline.png" alt="drawing" width="700"/></p>

<br/><br/><br/>


<!-- ## yetagain
library to estimate and study layered probabilistic time series models 

**Description:**

-->