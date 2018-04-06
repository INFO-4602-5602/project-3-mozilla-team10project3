# Project 3: Group 10
Bret McSpadden  
Bryan Costanza  
Stephen Smart  
William Temple  
Yoshinari Fujinuma  

## Overview
Over spring break we worked individually to look at the data and other information from Mozilla to get an understanding of what we were working on. Throughtout the week we met as a full group after class to touch base and get on the same page, in vaious combinations of groups to brainstorm, design, and prototype the visualizatinos, and also worked individually to ulitimately create the three visualizations. We also colaborated through email for most communication. 

### [You can view all of our visualizations on this page.]()

## Visualization Descriptions
### Visualization 1 - Regional Breakdown of Known Terms
This visualization displays the percentage of respondants to the Mozilla survey who understand the nine terms about the internet asked in the survey. The respondents are divided into regions and sub-regions, as determined by the United Nations. The user can view a breakdown of each region by clicking that line to display the sub-regions of that region. 

#### Design Process
We first met to brainstorm visualizatios and begin prototyping our ideas. After further discussing the data and thinking about potential visualizations, we decided to look at the known terms in columns AI to AR. Because Mozilla requested breaking down the data by region and country, we decided to begin looking at the data at the regional level. 

Deciding how to determine the regions presented some issues as we thought continental groupings would be too large and diverse for meaningful comparisons and the exact breakdown has many possibilities when deciding to group countries and regions. We found a detailed classification of countries broken down by region and sub-region based on the United Nation's classification of each country. This set classifies the countries in 5 regions and 22 sub-regions. [The Github for the Regional Codes can be found here] (https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes) 

We initially considered bar charts and line charts to visualize the data. In asking, "How do respondents understand the terms across regions?", we thought comparison was the most important feature, and were interested in how seeing if the movement of the data in an interaction would allow for meaningful observation and comparison. A stacked bar chart was one option, but we thought parallel lines may be more helpful in showing the change, so settled on a beginning with a line chart.

Prototyping the vis with all 22 regions resulted in complete spaghetti with no meaninful comparisons. We brainstormed ideas to simplify the sub-regions, and considered grouping them on our own, but in the end decided use interaction to display the sub-regions more clearly by initially displaying the regional breakdown and then being able to click on an individual line to display that regions' sub-regions in the visualization while filtering out the origional regions. 

We built the visualization using D3 and CSV files processed in Python. We used [colorbrewer.com] (http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) to determine the color palet. In building the visualization we ran into typical bugs such as...

Once the visualization was working to display the regional breakdown we encorporated the interaction of clicking the lines display that regions' sub-regions. After the click interaction was working, we encorporated easier interaction by creating a mouseover function that increased the line size to help the user click the line they were intending.

#### How to view
Hover over and click individual lines to display sub-regional data. Click the back button to return to region breakdown. 

### Visualization 2 - Country Breakdown of Known Terms, countries with over 100 entries
This visualization displays a geographical tool that allows the user to explore an individual coutry's breakdown of know computer terms from the Mozilla survey. The user can navigate a world map, clicking individual countries to display that countrys statistics for the known terms. Eighty-six counties data are shown since not all countries have data and countrys with less than 100 results were filterd out.

#### Design Process
The goal of visualization 2 is to explore individual country data using a map in D3. After analyzing the data, the known terms seemed more interesting and less explored than some of the other data from Mozilla. Getting the visualization to work was the priority, so prototyping was done using fake data to explore encoding color in countries and creating the mouse interactions for selection color and displying the ________ showing the individual breakdown in a 9 sided figure. 

Once the general principals of the design and interaction were working in D3, the data was filtered and improted into the visualzation. Countries with less than 100 were responses were determined as insignificant and thrown out leaving 86 countries with data.

One design challenge was quality zoom and how the projection hindered some clarity in seeing individual countries, typically small areas such as Israel or some European countries. We chose the ______ projection as it showed the most countries at the farthest level of zoom.

#### How to view
Click each country to display the idividual statistics for that country.


### Visualization 3 - ?
This visualization displays

#### Design Process

#### How to view


## Team Roles
Bret - Visualization 1 design, documentation

Bryan - Visualization 1 design, documentation, team organization

Stephen - D3 programming, visualization 1 design

William - Visualization 2 designer, D3 and Python programming

Yoshinari - Visualization 1 designer, data filtering in Python, D3 programming

## Above and Beyond
Uncertainty - Shading in Visualization 2

Semantic Zoom - Visualization 1

Missing Data - Filter countries with less than 100 responses in Visualization 2

Style - Text and color scheme





<h2>Project 3:</h2>
Due 4.6.2018 by 11:59pm through GitHub Classroom 
Projects may be submitted up to 3 days late, with a 10% penalty per day.

<h2>Overview: </h2>
Mozilla (the same company that created the Firefox web browser) recently conducted a survey on people's perceptions of privacy in our modern, highly connected world. The survey was aimed at understanding how comfortable people from all over the world are with various technology and how that comfort varies with things like device ownership or tech savvy. You can learn more about their data here: https://blog.mozilla.org/blog/2017/11/01/10-fascinating-things-we-learned-when-we-asked-the-world-how-connected-are-you/?utm_source=newsletter-mofo&utm_medium=email&utm_campaign=IOTsurveyresults&utm_content=callout&utm_term=4434975

The challenge is that, while they have a rich set of data, they don't have strong ways of exploring that data beyond basic spreadsheets and descriptive statistics. Your goal is to create a set of visualizations that allows them to engage with their data. The raw data is available at: https://drive.google.com/file/d/0B5UMbl9u1_wQc2l0ZTU0dTdoYnM/view

<h2>Minimum Requirements:</h2> 
Your project must:
<ul>
<li> Include a README.md file that outlines:
  <ul>
  <li>Information about your visualizations and what they show. Include information about interactions, preprocesses, and design as appropriate.</li>
  <li>Your design process (e.g., how did you go about designing, building, and refining your system? Why did you choose these representations?)</li>
  <li>Your team roles for each individual</li>
  <li>How to run your project</li></ul></li>
<li>Include at least three unique visualizations:
  <ul>
  <li>One visualization must include some element of geography</li>
  <li>One visualization must include categorical data</li>
  <li>Each visualization must be interactive</li>
  <li>Your set of three visualizations should support at least one meaningful comparison between related data attributes</li>
  <li>Your set of three visualizations should visualize at least five data attributes total</li></ul></li>
<li>Be able to work with any dataset of this format (e.g., the numbers are interchangable but the columns and document titles are fixed).</li>
</ul>

<h2>Above and Beyond:</h2> 
The above requirements are the minimum for a passing grade on this project. Some ideas to improve your project include:<ul>
<li>Uncertainty: Include sources of uncertainty in your representation, such as margins of error or variance in your computed data</li>
<li>Semantic Zoom: Allow yourself to zoom into different levels of hierarchically grouped data (e.g., data grouped by continent, device type, etc).</li>
<li>Missing Data: Not all rows have data for all columns. Design ways of handling missing data intelligently.</li>
<li>Perceptually-Informed Design: Integrate perceptual concepts into your visualization design and discuss how you've integrated those concepts in your readme.</li>
<li>Coordinated Views: Have two or more visualizations that interact with one another as you move through the data.</li>
<li>Style: Keep the style consistent across all your views, with an eye towards intelligently applying visual design.</li></ul>

<h2>Platforms:</h2> 
You can use any development platform you'd like so long as it is not proprietary (exception: MatLab as we have a University License). Your project readme should include step-by-step instructions on how to run your projects and it should run without me having to modify the code. You are welcome to use different platforms for each visualization.

Some platforms to look at include:
<ul>
<li>D3</li>
<li>R with ggplot</li>
<li>WebGL or Three.js</li>
<li>Processing or ProcessingJS</li>
<li>Google Maps API</li>
<li>Open Street Map API</li>
<li>Bokeh</li>
<li>Creatively engineered tangible/audio artifacts</li>
</ul>

If you would like to use a platform that will push you in creative ways but may not support all of the requirements of the project, please come talk to me. 

<h2>Submissions:</h2>
All submissions must be made through GitHub with a timestamp by 11:59pm on 4.6. Your submission files should include:
<ul>
<li>Your README</li>
<li>Your code and/or project</li>
</ul>
Note that each group only needs to submit one file. 

Each member of the team should also send Danielle & Jim a project post-mortem through email with the subject line "INFO 4602/5602: Project 3" documenting the following:
* What you worked on in the project
* What your teammates worked on in the project
* How you would rate your performance and why (out of 10 points)
* How you would rate each teammates' performance and why (out of 10 points)

These documents will be kept confidential and will factor into project grades. If you feel all of the team worked hard and performed well, please don't hesitate to tell me that (no curving is necessary on performance reviews :-))! Also, please keep in mind that different team members have different skillsets, roles, and experiences.

<h2>Grading: </h2>
The project will be scored out of 100 points total. Your project will be graded on four different criteria:
<ol>
<li> Creativity</li>
<li> Technical execution (how well does it meet the stakeholder's objectives?)</li>
<li> Design (both aesthetic and your visualization choices)</li>
<li> Project Post-Mortems</li>
</ol>
