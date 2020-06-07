
# coding: utf-8

# # POPULATION CAPSTONE PROJECT
# ### Aim = Calculate the average growth in population in every year and make prediction for next year.

# ## Import The Libraries
# I have imported all the necessary library as per requirement of our project.Here I have imported two libraries:<br>
# (A) First pandas as pd : For load the data and other statistics.<br>
# (B) Seccond matplotlib as plt : For plotting line, bar and other graphs.

# In[1]:


# import all the nacessecory library

import pandas as pd
import matplotlib.pyplot as plt

# ## Load The Files
# Here I have loaded three csv files.<br>
# (A) First file is named "total" which contains the whole population around world.<br>
# (B) Seccond file is named "female" which contains the count of the female in whole world.<br>
# (C) Third file is named "male" which contains the count of the male in whole world.

# In[2]:


# Load The Files of total, male and female population.
total = pd.read_csv(r"API_SP.POP.TOTL_DS2_en_csv_v2_1068829.csv",skiprows = 4 )
female = pd.read_csv(r"API_SP.POP.TOTL.FE.IN_DS2_en_csv_v2_1074665.csv",skiprows = 4 )
male = pd.read_csv(r"API_SP.POP.TOTL.MA.IN_DS2_en_csv_v2_1074666.csv",skiprows = 4 )


# ## Load The Dataset
# Next we load the sample data from "total" file into a "New_dataframe" variable. we take the rows(13, 30, 38, 63, 107, 152, 155, 171, 222, 245) and columns(2009 to 2018).<br>
# Next line insert a column "index" at 1st column position(from 0 to 9) for index.<br>
# Next line set the new index column as default index.<br>
# In last display the New_dataframe variable.

# In[3]:


# Load The Dataset of 10 different countries.
New_dataframe = total.loc[[13, 30, 38, 63, 107, 152, 155, 171, 222, 245],"2009":"2018"]

# Insert new column of index and make as default.
New_dataframe.insert(1, 'index', range(0,10))
New_dataframe.set_index("index", inplace=True)
New_dataframe


# ## Load The Countries
# I have loaded the countries name in the "countries" variable of same country which i have loaded before.<br>
# In next insert the index column at 1st position.<br>
# Then set the new index as default index.<br>
# then display the country Name.

# In[4]:


# Load the same countries name which us choosen earlier.
countries = total.loc[[13, 30, 38, 63, 107, 152, 155, 171, 222, 245],["Country Name"]]

# Insert new column of index and make as default.
countries.insert(1, 'index', range(0,10))
countries.set_index("index", inplace=True)
countries['Country Name']


# ## Display The Total Population
# In below cell I am displaying the total population of 10 different countries.<br>
# In first line I am  retrieving the years and save them in x.<br>
# Then create the notebook by using the plt.figure funtion and figsize has been used for size of notebook.<br>
# Then I have used the for loop for retrieving the whole data value in y one by one.ax1.plot has been used for plotting the lines.<br>
# ax1.set has been used for giving the title for subplot and xlabel and ylabel have been used for label of x axis and y axis.<br>
# ax1.legend has been used to identify every line by it's country name respectively.<br>
# plt.setp(ax1.get_xticklabels(), rotation = 45) command has been used to rotate the year by 45deg.<br>
# In last display the figure.

# In[5]:


# load the columns name in x variable.
x = New_dataframe.columns

# Create the notebook.
fig = plt.figure(figsize = (12,5))

# Create the subplot
ax1 = fig.add_subplot(111)

# Plotting the line of every countries one by one in same subplot.
for data in range(0,10):
    y = New_dataframe.loc[data]
    ax1.plot(x,y,marker = 'o')

# Set the title ,x label and y label of subplot.
ax1.set(title = "Total Population Of 10 Different Countries",
        xlabel = "Year",
        ylabel = "Population\n( le9 )")

# Display the all country name with their symbols.
ax1.legend(countries['Country Name'])

# The below has been used for rotate the x axis name by 45deg.
plt.setp(ax1.get_xticklabels(), rotation = 45)

# Display the graph.
plt.show()


# ## Calculate The Difference In Total
# In below cell first i have created the empty dictionary and list and created the zero value variable "ca".<br>
# Then i have used the double "for" loop.In first for loop retrieving the data of 2009 and countries name and save in temp and temp2 respectively.In seccond for loop i have retrieved the rest data and subtract 2009 from 2010 and 2010 from 2011 and so on.<br>
# Add in list by append function and whole row has been finished then list added in dictionary and older list will empty.I have use the same method to all the rows and make new dataframe.

# In[6]:


# Create the empty list and dictionary.
dic = {}
lis = []
ca=0

# Calculate the difference of every year population in every country.
for diff in range(0,10):
    c = New_dataframe['2009']
    temp = c[ca]
    c2 = countries['Country Name']
    temp2 = c2[ca]
    for diff2 in range(2010,2019):
        a =str(diff2)
        b = New_dataframe.loc[diff,a]
        d = b-temp
        temp = b
        
#         Append whole element in list.
        lis.append(d)

#   Add the whole list in dictionary.
    dic[temp2] = lis
    ca = ca+1
    
#   Again set the list as empty.
    lis = []


# ## Making New DataFrame
# Here i have been making the new dataframe with index("2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17").<br>
# Then display the growth of population in every year in table.

# In[7]:


# Making the dataframe from dictionary and index and display.
diff_dataframe = pd.DataFrame(dic,index=["2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17"])
diff_dataframe


# ## Load The Dataset From Male
# Next we load the sample data from "male" file into a "New_dataframe_ma" variable. we take the rows(13, 30, 38, 63, 107, 152, 155, 171, 222, 245) and columns(2009 to 2018).<br>
# Next line insert a column "index" at 1st column position(from 0 to 9) for index.<br>
# Next line set the new index column as default index.<br>
# In last display the New_dataframe_ma variable.

# In[8]:


# Load the data set from male population file and choose the same country which we choosed earlier.
New_dataframe_ma = male.loc[[13, 30, 38, 63, 107, 152, 155, 171, 222, 245],"2009":"2018"]

# Insert the new column of index and make it as default index.
New_dataframe_ma.insert(1, 'index', range(0,10))
New_dataframe_ma.set_index("index", inplace=True)

# Display the dataframe.
New_dataframe_ma


# ## Calculate The Difference In Male
# Here I have used the empty dictionary, list and zero value varible.<br>
# Again I have used 2 for loop.one for retrieving of 2009 and country Name.seccond for retrieving the rest data and subtract 2010-2009 and 2011-2010 and so on.<br>
# Add to list and add to dictionary and do this for every row.

# In[9]:


# Create the empty list and dictionary.
dic_ma = {}
lis = []
ca=0

# Calculate the difference of every year population in every country.
for diff in range(0,10):
    c = New_dataframe_ma['2009']
    temp = c[ca]
    c2 = countries['Country Name']
    temp2 = c2[ca]
    for diff2 in range(2010,2019):
        a =str(diff2)
        b = New_dataframe_ma.loc[diff,a]
        d = b-temp
        temp = b
        
#       Append whole element in list.
        lis.append(d)
        
#   Add the whole list in dictionary.
    dic_ma[temp2] = lis
    ca = ca+1
    
#   Again set the list as empty.
    lis = []


# ## Making New DataFrame For male
# Here I have been making the new dataframe with index("2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17").<br>
# Then display the growth of male population in every year in table.

# In[10]:


# Making the dataframe from dictionary and index and display.
diff_dataframe_ma = pd.DataFrame(dic_ma,index=["2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17"])
diff_dataframe_ma


# ## Load The Dataset From Female
# Next we load the sample data from "female" file into a "New_dataframe_fe" variable. we take the rows(13, 30, 38, 63, 107, 152, 155, 171, 222, 245) and columns(2009 to 2018).<br>
# Next line insert a column "index" at 1st column position(from 0 to 9) for index.<br>
# Next line set the new index column as default index.<br>
# In last display the New_dataframe_fe variable.

# In[11]:


# Load the data set from female population file and choose the same country which we choosed earlier.
New_dataframe_fe = female.loc[[13, 30, 38, 63, 107, 152, 155, 171, 222, 245],"2009":"2018"]

# Insert the new column of index and make it as default index.
New_dataframe_fe.insert(1, 'index', range(0,10))
New_dataframe_fe.set_index("index", inplace=True)

# Display the dataframe.
New_dataframe_fe


# ## Calculate The Difference In Female
# Here I have used the empty dictionary, list and zero value varible.<br>
# Again I have used 2 for loop.one for retrieving of 2009 and country Name.Second for retrieving the rest data and subtract 2010-2009 and 2011-2010 and so on.<br>
# Add to list and add to dictionary and do this for every row.

# In[12]:


# Create the empty list and dictionary.
dic_fe = {}
lis = []
ca=0

# Calculate the difference of every year population in every country.
for diff in range(0,10):
    c = New_dataframe_fe['2009']
    temp = c[ca]
    c2 = countries['Country Name']
    temp2 = c2[ca]
    for diff2 in range(2010,2019):
        a =str(diff2)
        b = New_dataframe_fe.loc[diff,a]
        d = b-temp
        temp = b
        
#       Append whole element in list.
        lis.append(d)
        
#   Add the whole list in dictionary.
    dic_fe[temp2] = lis
    ca = ca+1
    
#   Again set the list as empty.
    lis = []


# ## Making New DataFrame For Female
# Here I have been making the new dataframe with index("2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17").<br>
# Then display the growth of female population in every year in table.

# In[13]:


# Making the dataframe from dictionary and index and display.
diff_dataframe_fe = pd.DataFrame(dic_fe,index=["2010-09","2011-10","2012-11","2013-12","2014-13","2015-14","2016-15","2017-16","2018-17"])
diff_dataframe_fe


# ## Visualization
# In below cell I have created the visualization for better understanding. So I used index as x axis.In seccond line I have used the column name for data retrieving.<br>
# In the third line I have created the notebook and subplots (from ax1 to ax10) and I have created the list for giving the value for plotting.<br>
# Then I have used the for loop for plotting the graphs simultaneously.<br>
# Then I have retrieved the data of total, male, female and save in w,y,z repectively and then I plotted the bar and line graph by using w,y,z.<br>
# In Graph blue,orange and green denotes the total,male and female respectively.

# In[14]:


# Load the index(year) and column(countries) 
x_to = diff_dataframe.index
col_to = diff_dataframe.columns

# Making the notebook and 10 different subplots.
fig = plt.figure(figsize = (40,15))
ax1 = fig.add_subplot(251)
ax2 = fig.add_subplot(252)
ax3 = fig.add_subplot(253)
ax4 = fig.add_subplot(254)
ax5 = fig.add_subplot(255)
ax6 = fig.add_subplot(256)
ax7 = fig.add_subplot(257)
ax8 = fig.add_subplot(258)
ax9 = fig.add_subplot(259)
ax10 = fig.add_subplot(2,5,10)
ax = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]
axn = 0

# Retrieve the data(total, male, female) of all countries and save in W,y and z repectively.
for data in range(0,10):
    w = diff_dataframe[col_to[data]]
    y = diff_dataframe_ma[col_to[data]]
    z = diff_dataframe_fe[col_to[data]]
    axm = ax[axn]
    axn = axn +1
    
#   Plotting line and bar graphs for all countries.
    axm.bar(x_to,w)
    axm.plot(x_to,w,marker="o")
    axm.bar(x_to,y)
    axm.plot(x_to,y,marker="o")
    axm.bar(x_to,z)
    axm.plot(x_to,z,marker="o")
    
#   Assigning color blue for total,orange for male and green for female.
    axm.legend(["Total","Male","Female"])
    plt.setp(axm.get_xticklabels(), rotation = 45)
    axm.set(title = col_to[data],
        xlabel = "Year",
        ylabel = "Population\n( le9 )")
    
# Display the graphs.
plt.show()


# In[15]:


# Display the difference of total in every year for countries.
diff_dataframe


# ## Shape function for total
# Shape function is use for number of rows and number of columns.Difference table for "total" contains 9 rows and 10 columns.

# In[16]:


# Shape gives the number of rows and columns.
diff_dataframe.shape


# ## Describe Function For Total
# Describe function gives the statistic analysis values like count, mean, min, max, 25%, 50%, 75%, etc.

# In[17]:


# Describe function gives the statistic analysis of total population of every country
diff_dataframe.describe()


# ## Info Function For Total
# In Total difference table there has been 9 rows and 10 columns.All the value is in float and non-null value and every country have 9 values. it uses the memory of 792.0+ bytes.

# In[18]:


# Info gives the additional data information of total population.
diff_dataframe.info()


# In[19]:


# Display the difference of male in every year for all countries.
diff_dataframe_ma


# ## Shape function for male
# Shape function is use for number of rows and number of columns.Difference table for male contains 9 rows and 10 columns.

# In[20]:


# Shape gives the number of rows and columns. 
diff_dataframe_ma.shape


# ## Describe Function For male
# Describe function gives the statistic analysis values like count, mean, min, max, 25%, 50%, 75%, etc.

# In[21]:


# Describe function gives the statistic analysis of male population of every country.
diff_dataframe_ma.describe()


# ## Info Function For Male
# In male difference table there has been 9 rows and 10 columns.All the value is in float and non-null value and every country have 9 values. it uses the memory of 792.0+ bytes.

# In[22]:


# Info gives the additional data information of male population.
diff_dataframe_ma.info()


# In[27]:


# Display the difference of female in every year for all countries.
diff_dataframe_fe


# ## Shape function for female
# Shape function is use for number of rows and number of columns.Difference table for female contains 9 rows and 10 columns.

# In[23]:


# Shape gives the number of rows and columns.
diff_dataframe_fe.shape


# ## Describe Function For female
# Describe function gives the statistic analysis values like count, mean, min, max, 25%, 50%, 75%, etc.

# In[24]:


# Describe function gives the statistic analysis of female population of every country.
diff_dataframe_fe.describe()


# ## Info Function For Female
# In female difference table there has been 9 rows and 10 columns.All the value is in float and non-null value and every country have 9 values. it uses the memory of 792.0+ bytes.

# In[25]:


# Info gives the additional data information of male population
diff_dataframe_fe.info()


# # Prediction

# ## Comparison Between Prediction And Actual Data
# (A) Here I have created two empty list and one variable.<br>
# (B) Then I have retrieved the mean growth of every country.<br>
# (C) Then store the actual population in list.<br>
# (D) Then add the 2018 population to mean of every country.<br>
# (E) Then I have made the table of column name(Country Name, Y2018_data, diff_mean, Y2019_data_predict, Y2019_data(Google)).<br>
# (F) Then plot the line graph between Y2019_data_predict and Y2019_data(Google).

# In[26]:


# Create the two empty list.
lis2 = []
lis3 = []
li = 1

# Load the Countries data into the temp variable.
temp = countries
prediction_table = temp

# Load the mean value of every country.
diff_mean1 = diff_dataframe.mean()

# Load the 2019 population in list by country index.
Y2019_data = [9980000, 763092, 1433783686, 917358500, 1366417754, 127575529, 2083459, 23310715, 1148130, 44269594]

# Insert the 2018 data into the prediction table.
prediction_table.insert(1, "Y2018_data", New_dataframe['2018'])

# Load the mean growth value for all country.
for diff_mean in temp["Country Name"]:
    diff_mean_str = str(diff_mean)
    item = diff_mean1[diff_mean_str]
    lis2.append(item) 
prediction_table.insert(2, "diff_mean", lis2)

# Add the 2018 data and mean for 2019 prediction.
for li in range(0,9):
    lis3 = lis2[li] + New_dataframe['2018']
prediction_table.insert(3, "Y2019_data_predict", lis3)

# Load the 2019 actual data.
prediction_table.insert(4, "Y2019_data(Google)", Y2019_data)

# Display the table.
prediction_table


# In[27]:


# Create the notebook and make the subplot.
fig = plt.figure(figsize = (20,5))
ax1 = fig.add_subplot(111)

# Plotting the line graph between 2019 prediction and actual data.
ax1.plot(temp["Country Name"],temp["Y2019_data_predict"],marker="o")
ax1.plot(temp["Country Name"],temp["Y2019_data(Google)"],marker="o")
ax1.legend(["Y2019_data_predict","Y2019_data(Google)"])
plt.setp(ax1.get_xticklabels(), rotation = 45)
axm.set(title = "Comparison Between Prediction And Actual Data",
        xlabel = "Year",
        ylabel = "Population\n( le9 )")

# Display the graph.
plt.show()


# ## Data Summary
# ###### This is the last step of our project.Here i tell you what the project does.This is the steps i have used in project :-
# (A) Import the whole library.<br>
# (B) Load all the file and load all the data frame.<br>
# (C) Then Calculate the total Growth of every country in every year.Similarly do this for male and female population.<br>
# (D) Then make all the 10 countries graph in 10 different subplots based on total, male and female population.<br>
# (E) Then I have done some statistical function like describe, info, shape on Total, male and female population respectively.<br>
# (F) Then by describe function I get the mean value of every country growth in list.<br>
# (G) Then I created a table for comparison of 2019 actual data(retrieved from Google) and 2019 prediction value(retrieved by adding 2018 population and mean).<br>
# (H) In the last, plot the line graph between actual data and predicted data. As we see difference between both the line is minor. So that we can say that this prediction works properly.<br>
