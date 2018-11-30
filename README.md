# CS3001_DataScienceProject

Regarding file structure, we can combine all of the final code into one file, I would think. We may have some functionality that allows us to pre-generate the main data tables and dump them out as local files to speed up execution, but let's not worry too much about how fast our program is until we can actually get some results.

The following is intended to serve as a rough "checklist" as to what we need to be doing. Ideally we can work on these seperately to an extent, but we can split them as needed to ensure that we can work concurrently:

First, we collect all the files, and read into panda frames. We'll need to fill out NULL and empty values to ensure they don't harm our models.

Second, we begin the data pre-processing section. I think the first logical step is to figure out what tables and features are making it in. During this stage, we will be "given" the set of tables constructed from all relevant files. We should decide what files we don't need, which we do, and which features should be pruned from the files that we do use. These generated tables should simply be handed over to the next step.

Third, we begin data synthesis. We need to create user profiles. We need one common table where we can "query" a user from, getting info on them. Odds are if we just combine the tables we have that have a "USERID" key, that table will probably do the job. The point of this component is that we need to be able to, when given some user, quickly grab all their related info. Ideally, getting their profile should be as simple as "UserProfiles[USERID]".

Fourth, we need to construct the actual primary data table. A large table, where every entry has a USERID, a RESTID, the RATINGS, and then a bunch of probably binary features that describe if that user's preferences were provided by the place they rated. We'll probably also have other features too, maybe even some aggregate ones like "how many things did the location have that the user wanted". We could also weight them based on what things the user may care more about.(edited)

Fifth, with the aforementioned data table, we must create and train our model. Be it solely regression or whatever, we need to train something, we so need a table that can be used for training. I think that for the purposes of getting at least something ready, we should just try to get a regression selected and implemented, then worry about improving our model after the rest of the framework is ready.

Sixth, we need to take the testing USERID / RESTID input, and construct them into entries based off the large table we created in the fourth step. We need to make them entries in that form, so that we can predict the user's ratings. Constructing these entries will likely require a profiles for the locations much like the profiles for the users, so we can just take a RESTID and look up it's info. Depending on what tables we generate early on, these tables may already be available to us.

Seventh, a trivial step, we evaluate how we did. This should just be using existing pandas functions.

After these are all done, we write the report, and should probably give a little thought into what we're actually going to present.
