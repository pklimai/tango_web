# BM@N Slow Control Viewer

Slow control system viewer for BM@N Tango database.

## Configuration

The configuration must be provided in `server/config.py` and/or `server/config_local.py`

Example of [config_local.py](server/config_local.py):
```python
DEBUG=True

BMN_UNICONDA_CONNECTION = "postgresql://db_reader:reader_pass@bmn-unidb.jinr.ru/uni_db"
TANGO_BASE_API_URL = "http://10.220.16.81:8000"

ALIASES = [
   {
        'name': "temperature pir230e_1",
        'param': dict(domain="bmn", family="env", member="pir230e_1", name="temperature")
   }
]
```
Note how parameter aliases are specified using `ALIASES` dictionary.


## Run in Docker
```bash
# build container
docker build -t bmn-visualization .
# run container
docker run --rm -it -d -v $PWD/config_local.py:/root/bmn-visualisation/server/config_local.py:Z -p 8050:8050 \
  --name bmn-visualization bmn-visualization
```
(note the Z modifier)


## Develop
1. Generate ORM from database
    ```bash
   flask-sqlacodegen --bind-key=bmn --flask postgresql://user:user_pass@localhost/bmn_db > ./server/orm/bmn.py
    ```


## Steps for local compilation (see also Dockerfile)

Run from your activated virtual environment, e.g. PyCharm terminal:
```
cd .\nica_dash_components\ 
npm install
npm run build

pip.exe install wheel
python.exe setup.py sdist bdist_wheel

cd .\nica_dash_components\dist\                          
pip install .\nica_dash_components-0.0.1-py3-none-any.whl
```
(now `import nica_dash_components` works and GUI becomes available)

Also
```
pip install psycopg2
```
is required on Windows but breaks things in Linux (Docker)...

