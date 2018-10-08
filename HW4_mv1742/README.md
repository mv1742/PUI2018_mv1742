
This is Manrique's HW4.

Assignment 1, Assignment 2 and Assignment 3.

I collaborated with Mark Bauer and Amber YuShi Chen for assigment 2.

Rufei explained how to generate 100 samples of different RANDOM sizes for assignment 1.

### Assignment 1: Write an ipython notebook that demonstrates visually in a data-driven way the Central Limit Theorem. 

- GENERATED  100 samples of different sizes N (N>10 & N<2000) from each of 5 different distributions (500 samples in total), _all with the same population mean_
- Included a _Normal_, a _Poisson_, a _Binomial_, a _Chi-Squared_ distribution, and 1 more of your choice.    
- For each sample PLOTTED the sample mean (dependent var.) against the sample size N (independent var.). 
- DESCRIBED (in a caption to your figure) the behavior you see in the plots in terms of the _law of large numbers_ or _Central Limit Theorem_.
- PLOTTED the distributions of all sample means (together for all distributions).  
  _Mandatory_: as a histogram. 
   
__Extra Credit__: FITTED a gaussian to the distribution of means            

My notebook: 
- generates the distributions, correctly generated for each of the 5 ditributions, all with same mean.
- displays all plots: a scatter plot per distribution and a histogram of all distributions, usual rules for plotting applying: visible and readable axes, title, legend, caption. 
- each plot has a caption which describes the plot in terms of _Central Limit Theorem_


### Assignment 2: Set up the work for data-driven inference based on CitiBike data. You should, even more than usual, work in groups for this!

1. Formulated the Null and Alternative hypothesis in words and as a formula. 
2. Used pandas to read in the CitiBike files, and moved it to $PUIDATA. 
3. Displayed the top few rows of the DF in your notebook. (__rendered__)
5. Displayed the reducted dataframe (___rendered__)
6. Plotted your data distributions.

NULL HYPOTHESIS:
Subscribers bike on weekends is the same or higher than the proportion of customers biking on weekends
_H_0: \S_weekend / S_total <= C_weekend/C_total
_H_1:S_weekend/S_total > C_weekend/C_total

I will use a significance level  $\alpha=0.05$
which means i want the probability of getting a result at least as significant as mine to be less then 5%
I am starting with a single month of data: reading data from citibike csv file from June 2014


## Assignment 3: Finish z-test lab and turn it in as a notebook .

Used Z test to understand if a (fictitious) implementation of an alternative bus route for (fictitious) bus line X8 improves circulation. 

Null hypothesis:
H0: the commute time is the same or longer with the new bus route as it was beforeTold ~ N(μ=36, σ=6)

Alternative
Ha: the commute time is shorter with the new bus route than it was before: Tnew < ToldTold ~ N(μ=36, σ=6)α = 0.05

Z-test
This is 2.5 sigma away from the mean, which means it is sufficient given that we have a 2 sigma threshold.
