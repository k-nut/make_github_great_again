SELECT DATE(author.date) as the_date, count(*) as all_commits
FROM ([bigquery-public-data:github_repos.commits])
WHERE DATE(author.date) < DATE('2010-01-01')
GROUP BY the_date
ORDER BY the_date;
