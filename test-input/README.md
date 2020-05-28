This folder contains a zip file [test-input.zip](test-input.zip) with the test files without the gold labels. 
There are 20 political debates/speeches that will be used to test the models. 
<br>
Their format is identical to that in the training set, except that the fourth column is missing.  
For instance, 20160303_GOP_michigan.tsv looks like this:

> 1	KELLY	Good evening, and welcome to the fabulous FOX Theatre in downtown Detroit, the site of the 11th Republican presidential debate of the 2016 campaign.<br>
> 2	KELLY	I'm Megyn Kelly, along with my co-moderators, Bret Baier and Chris Wallace.<br>
> 3	BAIER	59 Republican delegates are at stake here in the state of Michigan during next Tuesday's Republican primary, the biggest prize out of four states holding contests that day.<br>
> 4	BAIER	For tonight's debate we're partnering with Facebook.<br>
> [...]

The folder [test-input](./) contains also a submission_instance.zip file that is an example of what we 
expect the participants to submit: <br>

* Twenty prediction files: 		__filename__.tsv <br>

Where __filename__ is in [20160303_GOP_michigan, 20180426_Trump_Fox_Friends, 20181102_Trump_Huntington, 
20160309_democrats_miami, 20180612_Trump_Singapore, 20190304_Trump_CPAC, 
20160907_NBC_commander_in_chief_forum, 20180615_Trump_lawn, 20190619_Trump_Campain_Florida, 
20170207_Sanders_Cruz_healthcare_debate, 20180628_Trump_NorthDakota, 20190730_democratic_debate_Detroit_1, 
20170404_Trump_CEO_TownHall, 20180712_Trump_NATO, 20190731_democratic_debate_Detroit_2, 
20170512_Trump_NBC_holt_interview, 20180731_Trump_Tampa, 20190912_democratic_debate, 
20170713_Trump_Roberston_interiew, 20180821_Trump_Charleston]


As mentioned in the main page in the [Results File Format section](https://github.com/sshaar/clef2020-factchecking-task5#results-file-format) the submission files should have the same format as those used during training: tab-separated id and 
judgment; one instance per line. From the example 20151219_3_dem.tsv:

> [...] <br>
> 1	0.8444218515250481 <br>
> 2	0.7579544029403025 <br>
> 3	0.420571580830845 <br>
> 4	0.25891675029296335 <br>
> [...]

We have implemented some checkers, but it is still the responsibility of the participants to double-check that 
their submissions are correct. <br>

You should submit the zipped file via the [submission link](https://docs.google.com/forms/d/e/1FAIpQLSfsBfruzsYLg9mngQmLkKjBeyazxeAD-uknonXqJhVoozsKDg/viewform). 
<br>
You have to submit **ONE** primary submission and you could submit up to **TWO** contrastive submissions. 
<br>
If there are more than one primary submission made the latest submission will be considered the primary by default. 

As a reminder, participants can submit predictions more than once, but only the last one before the deadline 
**(5 June 2020)** will be evaluated and considered as official. 
