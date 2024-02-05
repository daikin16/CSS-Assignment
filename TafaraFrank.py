# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:21:39 2024

@author: g21b7647
"""

# CSS 2024 Assingnment 1 

import pandas as pd
df = pd.read_csv ("movie_dataset.csv")

import pandas as pd
df2 = pd.read_csv ("country_data.csv")


#Question 1
## Replace Nans inplace for column Revenue Millions generated.
x = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(x, inplace = True)

## Replace Nans in column Metascore
x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace = True)

## 
print(df.describe())

print(df["Rating"].max())
filtred_data = df[(df["Year"]>=2015) & (df["Year"]<= 2017)]

Average_Revenue = filtred_data["Revenue (Millions)"].mean()
print(Average_Revenue)

## Question 4 
Movies_2016 = df[(df["Year"] ==2016)]
Movies_total = len(Movies_2016)
print(Movies_total)

##Question 5
Movies_directed = df[(df["Director"] =="Christopher Nolan")]
By_Christopher_Nolan = len(Movies_directed)
print(By_Christopher_Nolan)

##Question 6
Movies_at_least_rating_greater_than_zero = df[(df["Rating"] >=8.0)]
Number_of_movies = len(Movies_at_least_rating_greater_than_zero)
print(Number_of_movies)

##Question 7 
Movies_directed = df[(df["Director"] =="Christopher Nolan")]
Median_Chris = Movies_directed["Rating"].median()
print(Median_Chris)

## Question 8
Average_yearly_rating = df.groupby("Year")["Rating"].mean()
Highest_rating = Average_yearly_rating.idxmax
print(Highest_rating)
highest = Average_yearly_rating.max()
print(highest)

## Question 9
##Filter movies between 2006 and 2016
Movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]
## Calculate the %
nun_movies_2006 = len(df[df["Year"] == 2006])
nun_movies_2016 = len(df[df["Year"] == 2016]) 


# Calculate the number of movies made in 2006 and 2016
num_movies_2006 = len(df[df['Year'] == 2006])
num_movies_2016 = len(df[df['Year'] == 2016])

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print(percentage_increase)

##Question 10
# Combining actors in a single list
all_actors = [actor.strip() for actors_list in df['Actors'].str.split(',') for actor in actors_list]

# Finding the most common actor in the dataset
import pandas as pd 
from collections import Counter
most_common_actor = Counter(all_actors).most_common(1)[0]

print(most_common_actor)

## Question 11
# Combine all genres into a single list
all_genres = [genre.strip() for genres_list in df['Genre'].str.split(',') for genre in genres_list]

# Find the number of unique genres
unique_genres_count = len(set(all_genres))

print(unique_genres_count)


### Question 12
# Perform correlation analysis on numerical features
correlation_matrix = df[['Runtime (Minutes)', 'Votes', 'Revenue (Millions)', 'Metascore']].corr()

# Print correlation matrix
print(correlation_matrix)
____







