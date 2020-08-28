# Datasets

Below are a list of datasets broadly related to culture and the humanities, which might be useful for those interested in cultural analytics and the digital humanities.

## Film 🎬

- **Film dialogue broken down by character gender and age** ({download}`Download <../data/Pudding/Pudding-Film-Dialogue-Clean.csv>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: Hannah Anderson, Matt Daniels
        <br>
        <br>
        The {download}`Film dialogue broken down by character gender and age CSV file (.csv)<../data/Pudding/Pudding-Film-Dialogue-Clean.csv>` is a consolidated and slightly modified version of data shared by Hannah Anderson and Matt Daniels for their Pudding article, ["Film Dialogue from 2,000 screenplays, Broken Down by Gender and Age"](https://pudding.cool/2017/03/film-dialogue/). The original datasets can be found [on GitHub here](https://github.com/matthewfdaniels/scripts/).  
        <br>
        For 2,000 films from 1925 to 2015, the dataset includes information about characters' names, genders, ages, and how many words they spoke in each film (both by number of words and by overall proportion), as well as the release year of each film and how much money the film grossed. 
        <br>
        <br>
        For more information about how Anderson and Daniels compiled the data and determined character gender and age, see [FAQ for the “Film Dialogue, By Gender” Project](https://medium.com/@matthew_daniels/faq-for-the-film-dialogue-by-gender-project-40078209f751)
        ```

## Literature 📚

- ***Harry Potter* series, books 1-7, randomly shuffled** ({download}`Download <harry_potter_series_shuffled.txt>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: David Mimno
        <br>
        <br>
        The {download}`*Harry Potter* series text file (.txt) <../texts/literature/Harry-Potter-Novels-Shuffled.txt>` includes all seven books from J.K. Rowling's *Harry Potter* series, with words randomly shuffled for each page. Each line of the file is tab-separated and contains information about the individual page number (e.g. hp1-15), the book number (e.g. hp1), and the randomly shuffled words for that page. 
        <br>
        <br>
        This text file was originally created and shared by [David Mimno](https://github.com/mimno/info-3350-fall-2019/blob/master/week15/HarryPotterAnalysis.ipynb). The words have been shuffled at the page level to ensure non-infringing fair use of copyrighted material.
        ```

- **txtLAB's multilingual novels** ([Link](https://figshare.com/articles/txtlab_Novel450/2062002/3))
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: Andrew Piper, McGill [txtLAB](https://txtlab.org/data-sets/)
        <br>
        <br>
        The [txtLAB's multilingual novels link](https://figshare.com/articles/txtlab_Novel450/2062002/3) takes you to a repository where you can download a directory of 150 English-language novels, 150 German-language novels, and 150 French-language novels, which span from 1771 to 1932. Authors featured include Goethe, Franz Kafka, Hermann Melville, Mary Shelley, Kate Chopin, Virginia Woolf, Victor Hugo, Alexandre Dumas, and many more. These text files were compiled and shared by Andrew Piper and the txtLab.
        ```
    
- **Modernist journal data (1890s-1920s)** ([Link](https://sourceforge.net/projects/mjplab/files/))
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: [The Modernist Journals Project](https://modjourn.org/)
        <br>
        <br>
        The [Modernist journal data link](https://sourceforge.net/projects/mjplab/files/) takes you to a repository where you can download publication metadata for 14 modernist journals from the 1890s to the 1920s — such as *Poetry Magazine*, *The Little Review*, and *The Crisis*. The Modernist Journals Project, which has digitized these journals, provides CSV and tab-separated text files that contain information for every contributor and every work published in the journals.  
        ```
    
- **Seattle Public Library check-out data (2005-present)** ([Link](https://data.seattle.gov/Community/Checkouts-by-Title/tmmm-ytt6/data))
     - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: [City of Seattle](http://www.seattle.gov/tech/initiatives/open-data/about-the-open-data-program)
        <br>
        <br>
        The [Seattle Public Library check-out data link](https://data.seattle.gov/Community/Checkouts-by-Title/tmmm-ytt6/data) takes you to a database that contains circulation data about the Seattle Public Library system from 2005 until the present. You can filter this database or search for keywords (e.g., "James Baldwin") and export a file of the filtered data by clicking "Export" and your desired file type.
        ```

## Politics 🗳️ & History 📜

- ***The New York Times* obituaries (1852-2000)** ({download}`Download <../texts/history/NYT-Obituaries.zip>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source: [Matthew Lavin](https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#lesson-dataset)
        <br>
        <br>
        The {download}`*New York Times* obituaries zip file (.zip) of text files (.txt) <../texts/history/NYT-Obituaries.zip>` contains 378 *New York Times* obituaries (1852-2000) based on those collected by Matt Lavin for his *Programming Historian* tutorial, [Analyzing Documents with TF-IDF](https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf#lesson-dataset).
        <br>
        <br>
        I re-scraped the 366 obituaries included in Lavin's tutorial so that the obituary subject's name and death year is included in each text file name. And I added 12 more ["Overlooked"](https://www.nytimes.com/interactive/2018/obituaries/overlooked.html) obituaries — belated obituaries of remarkable women and minorities who did not receive a *NYT* obituary at the time of their death. Obituary subjects include academics, military generals, artists, athletes, activists, politicians, and businesspeople — such as Ada Lovelace, Ulysses Grant, Marilyn Monroe, Virginia Woolf, Jackie Robinson, Marsha P. Johnson, Cesar Chavez, John F. Kennedy, Ray Kroc, and many more.
        ```
- **U.S. Inaugural Addresses (1789-2017)** ({download}`Download <../texts/history/US_Inaugural_Addresses.zip>`)
     - ```{admonition} More info about this dataset
        :class: dropdown, info
        The {download}`U.S. Inaugural Addresses zip file (.zip) of text files (.txt) <../texts/history/US_Inaugural_Addresses.zip>` contains U.S. Inaugural Addresses ranging from President George Washington (1789) to President Donald Trump (2017). Each text file is titled with a number, the corresponding last name of the U.S. President, and the corresponding year of the Inaugural Address.
        ```
- **Nobel Prize winners (1901-2017)** ({download}`Download <nobel-prize-winners.csv>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source:  The European Data Portal and [the official Nobel Prize API](https://www.nobelprize.org/about/developer-zone-2/)
        <br>
        <br>
        The {download}`Nobel Prize winners CSV file (.CSV) <../texts/history/US_Inaugural_Addresses.zip>` contains information about 957 Nobel Prize winners from 1901 to 2017. This information includes the Nobel laureate's name, birth and death date (if applicable), birth and death location (plus latitude and longitude coordinates for the locations), the year they won the Nobel Prize, the category of the Nobel Prize, and the "motivation" for the Nobel Prize.
        <br>
        <br>
        Nobel laureates include Marie Curie, Johannes Stark, Woodrow Wilson, Jane Addams, Rabindranath Tagore, John Steinbeck, Gabriel Garcia Marquez, Karl Ziegler, Toni Morrison, and many more.
        ```
- **Refugee arrivals to the U.S. (2005-2015)** ([Link](https://github.com/melaniewalsh/data-viz-lab/tree/master/sample-datasets/us-refugee-arrivals))
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source:  Department of State's Refugee Processing Center and [Jeremy Singer-Vine](https://github.com/BuzzFeedNews/2015-11-refugees-in-the-united-states)
        <br>
        <br>
        The [Refugee arrivals to the U.S. link](https://github.com/melaniewalsh/data-viz-lab/tree/master/sample-datasets/us-refugee-arrivals) takes you to a GitHub repository that contains data about refugee arrivals to the United States between 2005 and 2015. This data was originally compiled from the Department of State's Refugee Processing Center by Jeremy Singer-Vine for his BuzzFeed article ["Where U.S. Refugees Come From — And Go — In Charts."](https://www.buzzfeednews.com/article/jsvine/where-us-refugees-come-from-and-go-in-charts#.vooNwy74jO)
        <br>
        The "refugee-arrivals-by-destination" csv contains information about the number of refugees who arrived in each U.S. city and state, the year that they arrived, and the country from which they arrived. The "refugee-arrivals-by-religion" csv contains information about the number of refugees who arrived in the U.S., the year in which they arrived, and their religious affiliation.
        ```
- **Irish immigrants admitted to NYC's Bellevue Almshouse (1840s)** ([Link](https://docs.google.com/spreadsheets/d/1uf8uaqicknrn0a6STWrVfVMScQQMtzYf5I_QyhB9r7I/edit#gid=2057113261))
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        Original Source:  Anelise Shrout, [Digital Almshouse Project](https://www.nyuirish.net/almshouse/)
        <br>
        <br>
        The [Bellevue Almshouse link](https://docs.google.com/spreadsheets/d/1uf8uaqicknrn0a6STWrVfVMScQQMtzYf5I_QyhB9r7I/edit#gid=2057113261) takes you to a Google spreadsheet that contains data about Irish-born immigrants who were admitted to the Bellevue Almshouse in the 1840s. The Bellevue Almshouse was part of New York City's public health system, a place where poor, sick, homeless, and otherwise marginalized people were sent — sometimes voluntarily and sometimes forcibly. This dataset was transcribed from the almshouse's own admissions records by Anelise Shrout.
        <br>
        For more information about this dataset, see [The Almshouse Records](https://www.nyuirish.net/almshouse/the-almshouse-records/)
        ```
       
## Social Media 🕸️

- **Donald Trump's tweets (2009-2020)** ({download}`Download <../texts/politics/Trump-Tweets.csv>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
       Original Source: [Trump Twitter Archive](http://www.trumptwitterarchive.com/)
        <br>
        <br>
        The {download}`Donald Trump's tweets CSV file (.csv) <../texts/politics/Trump-Tweets.csv>` contains nearly 30,000 tweets from Donald Trump's account from 2009 to March 2020. The information about each tweet includes the source, tweet text, date of tweet, as well as retweet and favorite counts. More updated data can be downloaded at [Trump Twitter Archive](http://www.trumptwitterarchive.com/archive).
        ```
    - 
- **"Am I The Asshole?" Reddit posts** ({download}`Download <top-reddit-aita-posts.csv>`)
    - ```{admonition} More info about this dataset
        :class: dropdown, info
        The {download}`Am I The Asshole?" Reddit posts CSV file (.csv) <top-reddit-aita-posts.csv>` contains 2,932 Reddits posts from the subreddit "Am I the Asshole?" that have at least an upvote score of 2,000. The information in the dataset includes the date of the post, title, body text, url, upvote score, number of comments, and number of crossposts. This data was collected with [PSAW](https://github.com/dmarx/psaw), a wrapper for the [Pushshift API](https://github.com/pushshift/api).
        ```
## Food 🍔

- **The New York Public Library's menu dataset (1840-present)** ([Link](http://menus.nypl.org/data))
     - ```{admonition} More info about this dataset
        :class: dropdown, info
        The [The New York Public Library's menu dataset link](http://menus.nypl.org/data) takes you to a web page where you can download data from the New York Public Library's massive menu collection — tens of thousands of transcribed menus and menu items from the 1840s to the present. Click "Download the latest data export in CSV format" for the most updated menu data.
        ```
<br>

## Other Dataset Compilations

Below are some other great compilations of cultural and humanities-related datasets:
- Jeremy Singer-Vine's [*Data Is Plural* archive](https://docs.google.com/spreadsheets/d/1wZhPLMCHKJvwOkP4juclhjFgqIY8fQFMemwKL2c64vk/edit#gid=0)
    - You can [subscribe to his excellent dataset newsletter here](https://tinyletter.com/data-is-plural)
- *The Pudding*'s [GitHub repository](https://github.com/the-pudding/data)
- Alan Liu's [DH Toychest](http://dhresourcesforprojectbuilding.pbworks.com/w/page/69244469/Data%20Collections%20and%20Datasets)
- Reddit's [r/datasets subreddit](https://www.reddit.com/r/datasets/)