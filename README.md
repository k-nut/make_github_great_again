# Make github great again
## An analysis of github commit messages

Having noticed it for myself recently I wanted to see if the big media coverage of Donald Trump's campaign had an influence on how people write commit messages. My assumption was that one would be able to see a spike in commit subjects that follow the pattern `make ... again` or in regex `^make .* again$` after the middle of 2015 when Trump got more and more popular.

I used the data published by github on google bigquery ([blogpost](https://github.com/blog/2201-making-open-source-data-more-available)) to analyze all public commit messages.

The main script that I used to query is [`make_great_again_count.sql`](/make_great_again_count.sql). It filters the commit messages by subject and then gets the daily count. Looking at the data coming out of this one can see that there is indeed an increase in messages following the pattern but I assumed that the same was true for **all** commits as github just became more and more popular.

So I also queried the count of all commit messages ([`new_commit_count.sql`](/new_commit_count.sql) and [`old_commit_count.sql`](/old_commit_count.sql)) and joined those later. I did it in two steps because doing all in one was too much for bigquery to export as a single csv and I did not want to setup google cloud storage.

Finally I wrote a small ipython notebook script ([`analyze_and_plot.py`](/analyze_and_plot.py)) that combines all three csv files (old commits, new commits, trump commits) and plotted the data:

![Plot of the data](/plot.png?raw=true)

As you can see I decided to only plot data after 2006. This is a random choice but I just did not want to go back too far in history. I also resampled to one week to get smoother results.

When looking at the plot now we come to the conclusion: Trump has not brainwashed people as much as I thought. They at least still seem to not think of him any more then before when writing commit messages.


### Update
When explicitly looking for the regex `'(?i)^make .* great again$'` an intersting observation can be made: As one would expect there are much fewer results (only 57 in total) but they do seem to correlate with Trump getting popular. The very first commit message that follows the pattern (being `Make "arc land" great again`) appears on 2015-10-28 with all others coming after that point in time. So maybe Trump did have some influence afterall.

![Plot of the make great again data](/plot_great_again.png?raw=true)

Thanks to [@derhuerst](https://github.com/derhuerst) for the suggestion!
