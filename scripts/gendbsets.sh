#!/bin/bash 
DBMAN_ID=kenken9
DBMAN_KEY=8b58S3jGp3Tp
DB_NAME=aichifoods
TAB_NAME=foods

echo MySQL initialization for any DBs...
mysqladm -u root password 'kenken3922' &&
echo done.

echo DB user initialization for db "$DB_NAME"...
mysql -u root -p "kenken3922" -e "CREATE USER ${DBMAN_ID}@localhost IDENTIFIED BY '${DBMAN_KEY}';" &&
mysql -u root -p "kenken3922" -e "GRANT ALL ON ${DB_NAME}.* TO ${DBMAN_ID}@localhost;" &&
echo done.

echo Table "$TAB_NAME" creation...
mysql -u ${DBMAN_ID} -p "${DBMAN_KEY}" -e "CREATE DATABASE ${DB_NAME} CHARSET utf8mb4;" &&
mysql -u ${DBMAN_ID} -p "${DBMAN_KEY}" ${DB_NAME} -e "CREATE TABLE ${TAB_NAME} ( id INT auto_increment, regionname VARCHAR(30), foodname VARCHAR(100), index(id));" &&
echo done.
