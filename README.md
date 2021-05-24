# Capstone Project: Use of Force by IMPD Officers

## Introduction

On May 25, 2020, George Floyd, an African-American man, was murdered by Derek Chauvin, a white Minneapolis police officer. George Floyd's death sparked protests against systemic racism and police brutality worldwide, leading to many governments worldwide to take a closer look at police officer training and immunity. On April 20, 2020, Derek Chauvin was found guilty on all charges and is currently waiting conviction. Geroge Floyd's tragedy, and other trajedy's like it, have shown that policing within the United States needs to be reformed in order to best protect communites that are succeptable to over policing and racial profiling. 

My project takes a look at use of force by the Indiananpolis Metropolitan Police Department (IMPD) in order to create a model that can be used by Indianapolis in order to help them create better and stronger reforms for their police deaprtments. I decided to work with this dataset because it is the most transparent and fleshed use of force dataset out there. It is very hard to find a viable use of force dataset since they are relatively new, the data that is documented is either limited do to state laws or very unorganized. This dataset was messy, but it contained many categories with information that could be used to build a strong model that can determine what factors could lead to an incident where an officer uses force. 

## Results

![Civilian Force Type](https://github.com/PNarducci1690/Capstone-Project-Use-ff-Force/blob/main/capstone%20images/Civilian_force_type.PNG)

I built my models around a multi-class classification problem that used various features to determine what kind of use of force a police oficer was using during a policing incident. These classifications, as designated by the IMPD, were physical force, less lethal force, and lethal force. These designations had to be created, and were done so by researching what the IMPD considers physical, lethal, and less lethal, and then recategorizing the tactics used by the officer to against the civilian during this use of force incident. In order to create a good model, I used k-Nearest Neighbors, Naive Bayes, Decision Tree, Random Forest, and XGBoost. I chose these models because they are considered powerful algorithms to use when it comes to run a model on multi-class classification data.

![XGBoost Results](https://github.com/PNarducci1690/Capstone-Project-Use-ff-Force/blob/main/capstone%20images/xgboost_model_results.PNG)

The best model was my XGboost which produced an f1 score of 93.52, I chose f1 as my accuracy score over accuracy score because a multi-class classification model comes with imbalances, and the target with the majority of the values normally sways the accuracy score in its direction, thus producing a more biased model. The f1 score uses the harmonic mean of each target variable in order to try and create a more balanced score in order to fairly weigh the model. 

![Confusion Matrix](https://github.com/PNarducci1690/Capstone-Project-Use-ff-Force/blob/main/capstone%20images/xgboost_conf_matrix.PNG)

Creating a confusion matrix based off of this model lead to some interesting results about the data. The model is very very good at identifying if a situtation was one in which an officer was using force. This isn't a suprise since majority of the data is made up of physical force altercations. However, 506 cases that were less lethal and, 54 that were lethal were mislabeled as physical use of force. This is a problem, because more lethal scenarios may be miscategorized and could lead to mistakes when it comes to training data on the model. In order to begin to figure out why these errors are occuring I looked at the features that the dataset found much more decisive and was surprised by what I found.

Overall, I was expecting race, sex and location (latitude and longitude) to be far more determing of a feature than what the XGBoost ended up using. I was very surprised to find that canine units, park rangers who worked at night, and officers responsible for training young recruits were much more likely to use force during a policing matter. It was very alarming to see that the officers who were training new recruits were the fourth most important feature that the model used. It leads one to believe that the training practices carried out by police officers extend from when there training began as new recruits.

## Looking Ahead

As I continue to develop and further this project, there were a few findings that I wanted to further investigate:
* Why are there many canine attacks from canine unit?
* Why did use of force by park rangers weigh so heavily in my model?
* What significance do felony stops have when it comes to use of force?
* Why does the training and recruiting designation of the IMPD have such a large impact on the model?

I would also like to run through this model again by using a feature selection in order to see if I can create a stronger model that can differentiate between the various targets better. I may also need to dive deeper into the dataset in order to produce better features or to apply better model cleaning practices. 


