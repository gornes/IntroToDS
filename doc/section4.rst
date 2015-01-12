***************************
Conclusions and Reflections
***************************


Conclusion
==========

**From your analysis and interpretation of the data, do more people ride the**
**NYC subway when it is raining versus when it is not raining?  What analyses**
**lead you to this conclusion?**


We have not found any significant evidence that ridership on the NYC subway is
affected by the rainy conditions, at least for the month of May 2011, given the
dataset used for this work. However, we don't think that we can extend this
conclusion to other periods of the year, as we don't have enough information.

Two analysis were performed that backup this conclusion:

1. A non-parametric statistical test between two samples, being one sample the
   data observed in rainy days and the other the data observed in non-rainy days.
   Even when in the beginning the small difference in the ridership volume reported
   for each sample seemed to be significant by the statistics reported by the test,
   it was not clear that both samples were really independent. After aggregating the
   data from all individual turnstiles to smooth possible selection effects and
   outliers, the test was run again and no significant nor meaningful difference
   was found between both samples.

2. A second analysis was done by means of the use of a machine learning technique.
   We tried to fit the data to multiple regression model, were we aimed to find
   predicting features from with our data. Even when some predicting features
   were found, as the hour of the day, day of the week, holiday or workday,
   the rain indicators didn't have either a significant weight or a high p-value,
   thus confirming by an independent method that precipitations didn't seem to
   play a roll on the ridership behavior of the NYC subway.
   or from the fitting to a multiple regression model, support

After obtaining this result, can we discard some of our previous preconceptions
or intuitions? One prejudgement was to believe that people would prefer to use
the subway on rainy days, instead of using other transportation means as bus or
taxis, since the later would mean to be more exposed to the rain. Another
preconception, in a opposite direction, was to think that people would
prefer instead to remain at home if there is not need to go out, thus only
people that need to commute to work would be riding on those conditions.


Shortcomings, limitations and insights
======================================

**Please discuss potential shortcomings of the methods of your analysis**

Several shortcoming have been raised along the pages of this work. Many of them
are not only related to the analysis methods but also to the dataset. Here we will
summarize the most relevant shortcomings according to our criteria. The order of
the list doesn't necessarily reflect the importance.

1. The statistical test must be used with caution: besides checking that some
   basic assumptions about the shape of the samples distribution should be met,
   the test itself does not indicates any about the actual independence of both
   samples. One should be careful when comparing the two samples on assessing
   if any other feature, or selection problem, can be the responsible of a
   significant difference detected by the test.

2. The use of a linear regression, even with multiple features, was shown to be
   not enough to model the ridership behavior of the NYC subway. The assumption
   of linearity between the predicting features and the entries by hour was not
   met for most of the variables, and the residual analysis confirmed the poor
   fit.

3. We believe that we did not have enough data to answer the question. Even
   studying the system as whole, removing the complications associated to the
   different behavior between different turnstiles and locations, the number
   of rainy points was small: only at 2 times heavy rain was reported, and just
   for short periods of a day; and only at 8 hours the conditions were "rain".
   All the other precipitations reported lasted only for short periods of time,
   affected only specific stations withing the whole NYC area, or where only
   relate to light rain or drizzle.

**Do you have any other insight about the dataset that you would like to share**
**with us?**

As the shortcoming, some other insights have been shown within this work. Many
of the visualizations presented in the different figures wanted to inform the
reader about these findings:

* How the behavior changes for holidays, even when only one holiday was present
  in our data (May 30th, 2011).

* The ridership behavior and features changes between locations, specially when
  comparing the busier downtown stations with the periphery locations.

* The precipitations are different within the NYC area for the month of May, with
  the southern stations reporting a higher precipitation.