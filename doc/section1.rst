****************
Statistical Test
****************

In lecture 3 and its problem set, the following question was given *Do rainy*
*days affect the ridership of the NYC subway?* To answer this problem we began by
 creating two samples from our data:

* Sample A (`No rain`) is a subgroup containing the entries where no rain was reported, using the
  information of the `rain` variable (:math:`rain = 0`)
* Sample B (`Rain`) is a subgroup with the entries where some precipitation was reported
  by means of the `rain` variable (:math:`rain = 1`)

By studying the distributions, using histograms, we were able to characterize
both data samples. We found out that both samples have a similar shape, clearly
not normal, and positively skewed (:ref:`figure 2.1 <figure21>`).

.. _figure21:
.. figure:: samples_compared.png
   :scale: 60%
   :align: center

   Ridership distribution comparison between rainy and dry days.

   Please note the logarithmic scale on axis Y. It was used to allows us to study
   the visualization with more detail.

Because of the non-normal distribution we decided to use the median as measure
of average for the samples:

* Sample A, days without precipitation, show a **median ridership of**
  **901 passengers per hour.**
* Sample B, rainy days, report a **median of 945 passengers per hour.**

To assess the significance of this result, that rain seems to increase ridership
in the NYC system by a small amount, we will use a non-parametric test.


Statistical Test Used
=====================

The Mann Whitney U test is chosen to assess the statistical significance of this
result. The null hypothesis in our case is that both populations are equal, or
that there is no significant deviation on both populations medians (two-tailed
hypothesis).

Justify the Statistical Test
============================

The Mann Whitney U test, or Wilcoxon rank-sum test, is chosen because of
characteristics of our samples: we can't use a parametric test because the
distributions do not seem to follow any particular and well known probability
distribution which we could use to make inferences that could directly report the
significance of any difference between both populations.

The U test is particularly powerful to assess the significance of the difference
between the median of two samples that have similar distributions. The assumptions
that our data samples must comply with are basically:

* All observations of both groups are independent
* The responses are ordinal (so we can use the ranking algorithm of the U test).

Results
=======

We used the scipy implementation of the Mann Whitney U test
(scipy.stats.mannwhitneyu). The results from the test are:

* :math:`U = 150678745.0`
* :math:`p = 1.91 \cdot 10^{-6}`

But the user should be aware that scipy reports p-value for a one-tailed
hypothesis, so we multiply by 2 to get the significance for our hypothesis:

* :math:`p = 3.82 \cdot 10^{-6}`


Interpretation and discussion
=============================

The interpretation, given the result from the U test, is that the the ridership
is not the same for rainy days than non-rainy days, with a significance higher
than 95% (p < 0.05). Furthermore, from the descriptive statistics of our samples
we can conclude that the ridership tends to be higher in rainy days.

However we have limited ourselves here to follow the procedure suggested by the
lectures, assuming that observations of both groups are independent and there
no other factors that might wrongly induce this result. Even when the data sample
we use for the project has been through a more complete wrangling, there are
still some issues that might affect the results:

* There is missing data for several turnstiles. From the original sample of 240
  turnstiles, only 52 have complete data for May; also, as discussed on the forums,
  some precipitation data is missing from some weather stations.

* We are using the variable `rain` to create our samples: this variable
  indicates if the conditions at anytime of the day at a
  particular turnstile were rainy. Is it the appropriate variable to use to
  build the subgroups?

* There is one day which was a holiday (Monday 30th), should the data from this
  day be discarded?

Let's look with more detail at these problems.

Missing data and precipitation distribution
-------------------------------------------

.. _figure22:
.. figure:: dataentries.png
   :scale: 60%
   :align: center

   Number of data points (measurements) by turnstile on project's improved
   dataset.


:ref:`Figure 2.2 <_figure22>` shows some turnstiles have missing data for the
month of May; with 31 days and 6 daily reports it is expected that a complete
monitored turnstile should have 186 measurements. This is the case for 52 turnstiles,
but 185 turnstiles have a number of measurements between 160 and 185. 3 turnstiles
had less than 160 entries, and after inspections they have been removed because
of the huge amount of missing data or time stamps reporting 0 entries. Of the 185
turnstiles with incomplete data, there was one case where at all time stamps the
number of entries was 0, which was also removed as it does not add any information
to our analysis (even when in other cases it could give further information).

The problem with the missing data is that, for some not clear explanation we
could provide, affects more the suburb stations turnstiles than the ones in downtown
areas. And suburb stations tend also to show lower number of hourly entries, i.e, a
lower ridership, than downtown turnstiles. This effect can be seen in
:ref:`Figure 2.3 <figure23>`.

.. _figure23:
.. figure:: medrider_loc.png
   :scale: 60%
   :align: center

   Turnstiles monthly median ridership, location and number of data points

   The figure shows the distribution of the turnstiles within NYC which are in
   our dataset. The size is proportional to the monthly median ridership (entries
   by hour) while the color indicates the data completeness of each turnstile: whiter
   colors indicate locations with more missing data.

We, as the reader may, wonder if this missing data could affect in anyway
our previous study. We are not completely sure, but we think that given the way
we performed our analysis it could happen that the results are affected: the downtown
station data, which also correspond to the group of stations with higher ridership,
is contributing to increase the median "entries by hour" that we calculate, as they are
located in the higher values side of the ridership distribution. What happens if
the stations in this locations are also the ones that tend to have more rainy days?
We didn't believe this was the case, but just to be sure we created the
plot shown in :ref:`Figure 2.4 <figure24>`.


.. _figure24:
.. figure:: medprecip_loc.png
   :scale: 60%
   :align: center

   Turnstiles monthly median ridership, location and mean precipitation.

   The figure shows the geographical distribution of the NYC turnstiles in the
   project's improved dataset. Size is proportional to the monthly median ridership
   and color represent the month's mean precipitation per turnstile. The figure
   shows that precipitations are higher in southern (and downtown) NYC.

The figure shows that the precipitation is higher in the northern NYC, which is
also the location of the most busy turnstiles: the median ridership of stations with
higher precipitation (> 0.004 inches) is 1116 entries by hour, while the stations
with lower precipitation (<= 0.004 inches) is 832 entries by hour. Also the stations
with higher precipitation report on average 7 rainy days while the lower precipitation
turnstiles only report 6.

