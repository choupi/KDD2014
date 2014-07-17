mkdir tmp
join ../teach/proj-teach.txt ../proj/proj-proj.txt > tmp/aa
join tmp/aa ../dummy/proj-dummy.txt > tmp/a1
join tmp/a1 ../essay/proj-essay.txt | sed '/^projectid/d' > all.txt

cat ../projects.csv | head -512394 |awk -F',' '{print $1}' |sort > tmp/pp
cat ../outcomes.csv | awk -F',' '$2=="t"{print $1,"1"} $2=="f"{print $1,"0"}' |sort -k1 > tmp/o
join tmp/pp tmp/o > tmp/oo
cat ../sampleSubmission.csv | awk  -F',' '{print $1}' |sort -k1 > tmp/s
join tmp/oo all.txt > train.txt
join tmp/s all.txt > test.txt
