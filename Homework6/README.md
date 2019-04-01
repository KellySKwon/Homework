# Unit 6 | Assignment - What's the Weather Like?

## Background

Whether financial, political, or social -- data's true power lies in its ability to answer questions definitively. So let's take what you've learned about Python requests, APIs, and JSON traversals to answer a fundamental question: "What's the weather like as we approach the equator?"

Now, we know what you may be thinking: _"Duh. It gets hotter..."_

But, if pressed, how would you **prove** it?

![Equator](Images/equatorsign.png)

-----------------------------------------------------------------------------------------------------------------------

## Analysis

In Summary, there is a correlation between latitude with temperature and humidity. As the sample shows (Figure 1 & 2), higher temperature and increase of humidity are concentrated with cities are around the equator (0 degrees latitude). There is almost no relationship between cloudiness and latitude, and just a slight trend of wind speed increasing as you go further away from the equator. 

Our sample consisted of 504 cities with varying latitudes from -54.81 degrees in Ushuala (53.6 F), Argentina to +78.22 degrees in Longyearbyen (10.4 F), Norway. Temperature in the sample varied from scorching 97.54 F in Cludad Bolivar, Venezuela (latitude 8.12) to below freezing -9.93 F in Deputatskly, Russia (latitude 69.3).

## temperature

* The equator is on 0 degrees latitude. Figure 1 displays max temperature (F) with city's latitude. We can see from the curve of the scatter plot, the temperature around the equator at this time of 01 Apr 2019 is higher then the north and the sourthern hemisphere.

* Interestingly at this time of the year, the temperature is colder in the northern hemisphere then the southern hemisphere. This may be due to the tilt of the earth from the sun. 


## humidity

* A city close to the equator, Paita, Peru (latitude -5, max temperature 62.6 F) is an outlier when visualizing figure 2 humidity. Although its neighboring cities has strong humidity bands near 100%, it outshines or outhumes other cities with humidity at 290%.

* Humidity follows a similar correlation to temperature where closer to the equator higher the humidity and away from the equator the humidity % decreases. 

## cloudiness

* We cannot discern any correlation of cloudiness with latitude. Cloudiness is dispersed throughout the hemispheres. Further analysis should be done to test other factors then latitude to forecast cloudiness in cities.

## wind speed

* In figure 4, we can see cities closer to the equator has a lower wind speed then the cities away from the equator. However, wind speed doesn't have as of a strong correlation as temperature and humidity. For example, minimum wind speed in our sample is from Kichera, Russia at 0.51 mph and maximum wind speed in our sample is from Torbay, England at 28.86 mph. However, these two cities are not vastly different in terms of latitude with Kichera on 55.9 degrees and Torbay on 47.66 degrees.

-----------------------------------------------------------------------------------------------------------------------
## WeatherPy

In this example, you'll be creating a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. To accomplish this, you'll be utilizing a [simple Python library](https://pypi.python.org/pypi/citipy), the [OpenWeatherMap API](https://openweathermap.org/api), and a little common sense to create a representative model of weather across world cities.

Your objective is to build a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

Your final notebook must:

* Randomly select **at least** 500 unique (non-repeat) cities based on latitude and longitude.
* Perform a weather check on each of the cities using a series of successive API calls.
* Include a print log of each city as it's being processed with the city number and city name.
* Save both a CSV of all data retrieved and png images for each scatter plot.

As final considerations:

* You must complete your analysis using a Jupyter notebook.
* You must use the Matplotlib or Pandas plotting libraries.
* You must include a written description of three observable trends based on the data.
* You must use proper labeling of your plots, including aspects like: Plot Titles (with date of analysis) and Axes Labels.
* See [Example Solution](WeatherPy_Example.pdf) for a reference on expected format.

## Hints and Considerations

* The city data is generated based on random coordinates; as such, your outputs will not be an exact match to the provided starter notebook.

* You may want to start this assignment by refreshing yourself on the [geographic coordinate system](http://desktop.arcgis.com/en/arcmap/10.3/guide-books/map-projections/about-geographic-coordinate-systems.htm).

* Next, spend the requisite time necessary to study the OpenWeatherMap API. Based on your initial study, you should be able to answer  basic questions about the API: Where do you request the API key? Which Weather API in particular will you need? What URL endpoints does it expect? What JSON structure does it respond with? Before you write a line of code, you should be aiming to have a crystal clear understanding of your intended outcome.

* A starter code for Citipy has been provided. However, if you're craving an extra challenge, push yourself to learn how it works: [citipy Python library](https://pypi.python.org/pypi/citipy). Before you try to incorporate the library into your analysis, start by creating simple test cases outside your main script to confirm that you are using it correctly. Too often, when introduced to a new library, students get bogged down by the most minor of errors -- spending hours investigating their entire code -- when, in fact, a simple and focused test would have shown their basic utilization of the library was wrong from the start. Don't let this be you!

* Part of our expectation in this challenge is that you will use critical thinking skills to understand how and why we're recommending the tools we are. What is Citipy for? Why would you use it in conjunction with the OpenWeatherMap API? How would you do so?

* In building your script, pay attention to the cities you are using in your query pool. Are you getting coverage of the full gamut of latitudes and longitudes? Or are you simply choosing 500 cities concentrated in one region of the world? Even if you were a geographic genius, simply rattling 500 cities based on your human selection would create a biased dataset. Be thinking of how you should counter this. (Hint: Consider the full range of latitudes).

* Lastly, remember -- this is a challenging activity. Push yourself! If you complete this task, then you can safely say that you've gained a strong mastery of the core foundations of data analytics and it will only go better from here. Good luck!

## Copyright

Data Boot Camp © 2018. All Rights Reserved.
