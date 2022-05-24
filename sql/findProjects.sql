SELECT
  *
FROM (
  SELECT
    p.name,
    p.url,
    p.description,
    COUNT(*) AS NumDeCommits
  FROM
    `ghtorrent-bq.ght.projects` p,
    `ghtorrent-bq.ght.commits` c
  WHERE
    c.project_id = p.id
  GROUP BY
    p.name,
    p.url,
    p.description
  HAVING
    COUNT(*) > 100) AS projects
WHERE
  projects.description LIKE '%selenium webdriver%'
  OR projects.description LIKE '%test%'
  AND projects.description LIKE '%UI%';