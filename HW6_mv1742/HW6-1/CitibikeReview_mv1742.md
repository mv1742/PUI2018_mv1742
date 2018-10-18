### PUI2018 
### HW6 (evening session)
### Assignment 1

Student: Manrique (mv1742).

Questions:

a. verify that their Null and alternative hypotheses are formulated correctly

b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

Write your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown named CitibikeReview_<netID>.md. Suggest variations on the question, if you think it may be made more interesting.



# Citibike Review

# Part A.

Unfortunately, this student did not add a written null and alternative hypothesis (H0 and H1), but I can guess the hypothesis from her code. Her hypothesis would be:

Null Hypothesis
H_0: Male bike tripduration is _the same_ or _higher_  than the female tripduration
Alternative hypothesis
H_1: Female bike tripduration is _the same_ or _higher_  than the male tripduration

She would probably have a significance level  $\alpha=0.05$ or similar.

# Part B
She plots "Mean and Std of Tripduration for different genders". The bar chart shows different mean values for genders 0,1,and 2, and thus we can expect that the differences can be significant. The sample size looks large enough to test that. 

In this csv file gender == 1 is male, gender == 2 is female

I believe gender == 0 doesn't give us any relevant information as it is not defined (not defined as LGBT either). Therefore she should have dropped this gender == 0.


# Part C
## Appropriate test
The studet, YQ729 (SuQian), could use Mann-Whitney U tests.

First of all the dependent variables Genders (male or female) are unpaired. Groups or data sets are regarded as unpaired if there is no possibility of the values in one data set being related to or being influenced by the values in the other data sets.

When comparing two sets of numerical data, a two-group comparison test such as the Mann-Whitney U test (t test non-parametric counterpart) should be used.

- Non-parametric (As you show that there are huge differences in standard deviation among genders, it is safe to use non-parametric test). In order to avoid the multiple testing problem, use non-parametric test here.
- One independent variables which are categorical
- One dependent variable 
- Independence of observations

The  Mann-Whitney U tests whether there is a difference among groups.

### Other suggestions
- It is necessary to have null hypothesis and the alternative hypothesis are.
- It would be helpful if the gender information, i.e. 0=unknown,1=male,2=female.
