#1/bin/bash

DBMAN=nkadm
DBPASS=758573
DB=aichifoods

for ((i=1;i<335;i++)); do
       REG=$(sed -n "${i}p" $1 | awk '{print $1}') &&
       FOOD=$( sed -n "${i}p" $1 | awk '{print $2}') &&
       mysql -u $DBMAN --password="$DBPASS" $DB -e "INSERT INTO test2(regionname,foodname) VALUES ('$REG','$FOOD');";
done
