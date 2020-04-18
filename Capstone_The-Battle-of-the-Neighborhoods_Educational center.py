#!/usr/bin/env python
# coding: utf-8

# # Capstone Project - The Battle of the Neighborhoods (Week 4)
# ### Applied Data Science Capstone by IBM/Coursera

# ## Table of contents
# * [Introduction: Business Problem](#introduction)
# * [Data](#data)
# * [Methodology](#methodology)
# * [Analysis](#analysis)
# * [Results and Discussion](#results)
# * [Conclusion](#conclusion)

# ## Introduction: Business Problem <a name="introduction"></a>

# In this project I will try ti find a optimal location for an educational center. It is a real task for, cause We are with my friends are going to open a school that will educate children on programming, robotics.
# Since there are many educational centers, schools we will try to detect locations that are not crowded with educational centers, but crowded with public schools that are not specialized in robotics.
# 
# We will use our data science powers to generate a few most promising neighborhoods based on this criteria. Advantages of each area will then be clearly expressed so that best possible final location can be chosen by stakeholders.

# ## Data <a name="data"></a>

# Based on definition of our problem, factors that will influence our decision are:
# * number of existing educational centers in the neighborhood
# * number of existing public schools in the neighborhood
# * distance of neighborhood from city center
# 
# We decided to use regularly spaced grid of locations, centered around city center, to define our neighborhoods.
# Following data sources will be needed to extract/generate the required information:
# centers of candidate areas will be generated algorithmically and approximate addresses of centers of those areas will be obtained using Google Maps API reverse geocoding
# number of centers and their type and location in every neighborhood will be obtained using Foursquare API
# coordinate of London center will be obtained using Google Maps API geocoding of well known London location
# 

# ## Methodology <a name="methodology"></a>

# In this project we will direct our efforts on detecting areas of Berlin that have low restaurant density, particularly those with low number of Italian restaurants. We will limit our analysis to area ~6km around city center.
# 
# In first step we have collected the required **data: location and type (category) of every restaurant within 6km from Berlin center** (Alexanderplatz). We have also **identified Italian restaurants** (according to Foursquare categorization).
# 
# Second step in our analysis will be calculation and exploration of '**restaurant density**' across different areas of Berlin - we will use **heatmaps** to identify a few promising areas close to center with low number of restaurants in general (*and* no Italian restaurants in vicinity) and focus our attention on those areas.
# 
# In third and final step we will focus on most promising areas and within those create **clusters of locations that meet some basic requirements** established in discussion with stakeholders: we will take into consideration locations with **no more than two restaurants in radius of 250 meters**, and we want locations **without Italian restaurants in radius of 400 meters**. We will present map of all such locations but also create clusters (using **k-means clustering**) of those locations to identify general zones / neighborhoods / addresses which should be a starting point for final 'street level' exploration and search for optimal venue location by stakeholders.

# In[ ]:




