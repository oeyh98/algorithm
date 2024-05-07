select count(*) as FISH_COUNT
from FISH_INFO as i
join FISH_NAME_INFO as n
on i.FISH_TYPE = n.FISH_TYPE
where (n.FISH_NAME = "BASS") or (n.FISH_NAME = "SNAPPER")
