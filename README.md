
## Develop
1. Generate ORM from database
    ```bash
   flask-sqlacodegen --bind-key=hdbpp --flask mysql+pymysql://user:user_pass@localhost/hdbpp > ./server/orm/hdbpp.py
   flask-sqlacodegen --bind-key=bmn --flask postgresql://user:user_pass@localhost/bmn_db > ./server/orm/bmn.py
    ```

## Testing
1. Dump last 1000 rows from database
   ```bash
   ssh mipt@vm221-52.jinr.ru
   # mysql -u bmn -h "10.18.11.66" --port 3306 -p # show databases;

   mysqldump -u bmn -h 10.18.11.66 --port 3306 -p --lock-tables=false --ignore-table=hdbpp.att_conf \\
    --ignore-table=hdbpp.att_conf_data_type --ignore-table=hdbpp.att_history --ignore-table=hdbpp.att_history_event \\
    --ignore-table=hdbpp.att_parameter \\
    --where "data_time > '2018-04-04 19:32:02' AND data_time < '2018-04-04 19:42:36'" hdbpp > mysql/hdbpp_values.sql


   mysqldump -u bmn -h 10.18.11.66 --port 3306 -p --lock-tables=false \\
    hdbpp att_conf att_conf_data_type att_history att_history_event att_parameter > mysql/hdbpp_atts.sql
  
   rm -rd postgres && mkdir postgres && pg_dump -h "vm221-53.jinr.ru" -U db_reader -O -x bmn_db > postgres/bmn_db.sql 
   ```
2. Pull results from virtual machine
   ```bash
   cd testing
   ./pull_db.sh
   ```

1. install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
2. `sudo apt install docker-compose`
3. Initialize database environment
   ```bash
   cd testing
   sudo rm -rf $PWD/db/data/* && sudo docker-compose rm # reinitialise database

   sudo docker-compose up
   ```
4. check admin page
   - mysql: http://localhost:8080
   - postgres: http://localhost:8081
