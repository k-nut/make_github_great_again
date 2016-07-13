SELECT DATE(author.date) as the_date, count(*) as make_great_again_commits
FROM ([bigquery-public-data:github_repos.commits])
where REGEXP_MATCH(subject, r'(?i)^make .* again$')
GROUP BY the_date
ORDER BY the_date;
