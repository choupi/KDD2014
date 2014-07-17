python csv-column.py projects.csv |grep -v '^projectid' | sort -k4 > proj-ts-sort.txt
python gen-teach-new.py proj-ts-sort.txt | sort -k1 > proj-teach.txt
python gen-ts.py |sort -k1 > proj-ts.txt
