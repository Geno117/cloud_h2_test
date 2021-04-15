cd ~/anntools
touch results.txt
for k in  data/free_1.vcf data/premium_2.vcf data/premium_2.vcf; do
for i in {1..3}; do
time python run.py $k > results.txt
done;
done;