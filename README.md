
## Develop
1. Generate ORM from database
    ```bash
   flask-sqlacodegen mysql+pymysql://user:user_pass@localhost/hdbpp > ./src/orm.py
    ```

## Testing
1. Dump last 1000 rows from database
   ```bash
   ssh mipt@vm221-52.jinr.ru
   # mysql -u bmn -h "10.18.11.66" --port 3306 -p # show databases;
   mysqldump -u bmn -h 10.18.11.66 --port 3306 -p --lock-tables=false --where "1=1 LIMIT 1000" hdbpp > hdbpp_schema.sql
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
4. check [admin page](http://localhost:8080)