# Project 3: Group 10
Bret McSpadden  
Bryan Costanza  
Stephen Smart  
William Temple  
Yoshinari Fujinuma  

## Overview
Over spring break, we worked individually to look at the data and other information from Mozilla to get an understanding of what we were working on. Throughout the week we met as a full group after class to touch base and get on the same page, in various combinations of groups to brainstorm, design, and prototype the visualizations, and also worked individually to ultimately create the three visualizations. We also collaborated through email for most communication. 

### Running Visualizations
Launch a http server from our project directory, navigate to the respective visualization files (vis1.html, vis2.html from the top level of the repository, and index.html from within the vis-interactive-map folder), open the .html file. See individual descriptions for further information on each vis' interactions.

## Visualization Descriptions
### Visualization 1 - Term Recognition Rates Across Regions and Sub-Regions
This visualization displays the percentage of respondents to the Mozilla survey who understand the nine terms about the internet asked in the survey. The respondents are divided into regions and sub-regions, as determined by the United Nations. The user can view a breakdown of each region by clicking that line to display the sub-regions of that region. 

#### Design Process
We first met to brainstorm visualizations and begin prototyping our ideas. After further discussing the data and thinking about potential visualizations, we decided to look at the known terms in columns AI to AR. Because Mozilla requested breaking down the data by region and country, we decided to begin looking at the data at the regional level. 

Deciding how to determine the regions presented some issues as we thought continental groupings would be too large and diverse for meaningful comparisons and the exact breakdown has many possibilities when deciding to group countries and regions. We found a detailed classification of countries broken down by region and sub-region based on the United Nation's classification of each country. This set classifies the countries in 5 regions and 22 sub-regions. [The GitHub for the Regional Codes can be found here](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes) 

We initially considered bar charts and line charts to visualize the data. In asking, "How do respondents understand the terms across regions?", we thought comparison was the most important feature, and were interested in how seeing if the movement of the data in an interaction would allow for meaningful observation and comparison. A stacked bar chart was one option, but we thought parallel lines may be more helpful in showing the change, so settled on a beginning with a line chart.

Prototyping the vis with all 22 regions resulted in complete spaghetti with no meaningful comparisons. We brainstormed ideas to simplify the sub-regions, and considered grouping them on our own, but in the end decided use interaction to display the sub-regions more clearly by initially displaying the regional breakdown and then being able to click on an individual line to display that regions' sub-regions in the visualization while filtering out the original regions. 

We built the visualization using D3 and CSV files processed in Python. We used [colorbrewer.com](http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) to determine the color palette. In building the visualization we ran into typical bugs such as handling asynchronous function calls correctly and managing multidimensional dictionaries.

Once the visualization was working to display the regional breakdown we incorporated the interaction of clicking the lines display that regions' sub-regions. After the click interaction was working, we incorporated easier interaction by creating a mouseover function that increased the line size to help the user click the line they were intending.

#### How to view
Hover over and click individual lines to display sub-regional data. Click the refresh in browser to return to the regional breakdown. 

### Visualization 2 - Explore IoT Term Knowledge
This visualization displays a geographical tool that allows the user to explore an individual country's understanding of know computer terms from the Mozilla survey. The main view color codes countries with data from yellow to red with countries with more responses being more red, and lass being more yellow. Grey signals no data. The user can mouseover individual countries to display that country's total count of responses in a tooltip. Clicking shows a 9-sided figure for that country which displays what terms that country understands by percentage of respondents for each term. Eighty-six countries' data are shown since not all countries have data and countries with less than 100 results were filtered out.

#### Design Process
The goal of visualization 2 is to explore individual country data using a map in D3. After analyzing the data, the known terms seemed more interesting and less explored than some of the other data from Mozilla. Getting the visualization to work was the priority, so prototyping was done using fake data to explore encoding color in countries and creating the mouse interactions for selecting each country by mousing over to highlight and display the tooltip and clicking to display the individual breakdown per country in a 9-sided figure. 

Once the general principals of the design and interaction were working in D3, the data was filtered and imported into the visualization. Countries with less than 100 responses were determined as insignificant and thrown out leaving 86 countries with data.

One design challenge was zoom and how the projection hindered some clarity in seeing individual countries, typically small areas such as Israel or some European countries. The Mercator projection was chosen as it showed the most countries. The zoom was chosen to fill the browser screen.

#### How to view
Mouseover each country to highlight and display the tooltip. Click each country to display the individual statistics for that country.

### Visualization 3 - Feelings Towards a Connected Future Across Countries, Broken Down by Tech-Savvyness
This visualization displays the breakdown of how feel towards a connected future as asked in the Mozilla survey. Each of the 5 potential answers, from scared to excited, can be selected, displaying the percentage of respondents from each country selecting that answer, with the gradient of color displaying the self-reported tech-savviness of those users responding.  Fifty countries with the most total respondents are displayed.

#### Design Process
After finishing visualization 1, we discussed options for visualization 3. With vis 1 and 2 both looking at the terms, we decided to look at the question regarding feelings. 

In looking at the data, we first discussed what we wanted to show. Showing totals in aggregate, by country, and by answer were discussed. We looked back at what Mozilla had done in iot_Survey.pdf as guidance, and decided to show 5 visualizations, one for each potential answer, and animate between the different vis' to see changes. We also decided to encode savviness for each set of answers to attempt to see the different type of users answering for each answer. 

Once we had the visualization in mind we split into 2 groups, one working on the D3 code for displaying the data, and the other preparing the data to insert in the visualization. 

To prepare the data we used Python to filter, calculate, sort, and finally output 5 CSV files, 1 for each response. We first calculated the overall percentage of respondents per each country selecting each of the 5 options. We checked our results against Mozilla's, and although different, we were in the same ballpark, and suspect our dataset has a different number of entries than what they used for their analysis. 

Once we had the percentage of each answer for each country, we calculated a savvy score for the respondents within that answer using a weighted average and assigning each savviness a number from 0-3 and dividing by the total number of respondents for that answer per country. With the 2 measures we needed for the vis, we exported 5 CSVs, one for each potential answer to the feelings question, containing country, percentage of respondents, and savvy score for that set per country. 

On the D3 side....

Once both the data and D3 template were ready, we imported the data. We explored different gradients and other design features but decided to keep the gradient and basic design from the original idea. 

#### How to view
Select the feeling of the respondents from the drop-down menu. Mouseover the individual bars to see the savviness score. Observe the animation and color change to see changes across different feelings in response % and user savvy.

## Team Roles
Bret - Visualization 1 & 3 design, documentation

Bryan - Visualization 1 design, documentation, team organization

Stephen - D3 programming, visualization 1 & 3 design, data filtering support

William - Visualization 2 design, D3 and Python programming

Yoshinari - Visualization 1 & 3 design, data filtering in Python, D3 programming support

## Above and Beyond
Uncertainty - Dots in Visualization 2 showing error margins

Semantic Zoom - Visualization 1

Missing Data - Filter countries with less than 100 responses in Visualization 2, filter null values in visualization 3 and only use top 50 countries with the most responses.