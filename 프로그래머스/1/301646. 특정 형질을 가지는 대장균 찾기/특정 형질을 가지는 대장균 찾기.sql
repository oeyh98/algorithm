select count(*) as count
from ECOLI_DATA
where (genotype & 5) and !(genotype & 2)