# mlops-study-ml-pipeline

Airflow 설치 및 프로젝트 셋팅
========================
<br>

# Airflow 설치 URL
```
https://airflow.apache.org/docs/apache-airflow/stable/start.html
```
Starting with Airflow 2.3.0, Airflow is tested with Python 3.7, 3.8, 3.9, 3.10.
Note that Python 3.11 is not yet supported.
<br><br>

# 프로젝트 생성
1. Pycharm > New Project >
<br><br>

2. Pure Python
   * Location : /Users/kakaobank/Dev/mlops-study-ml-pipeline
   * 프로젝트명 : mlops-study-ml-pipeline
   * Base interpreter : 3.9 ??? --> 가상환경으로
<br><br>

# Airflow 환경 구성
1. 프로젝트 venv 환경에서 ./mlops-study-ml-pipeline/shell 디렉토리에 있는 aiflow_install.sh 파일을 실행시킨다.
    ```shell
    (venv) ➜  pwd
    /Users/kakaobank/Dev/mlops-study-ml-pipeline/shell
    (venv) ➜  ./airflow_install.sh
    ```
   * airflow home : ~/airflow
   * dags_folder : ~/airflow/dags
   * plugins_folder : ~/airflow/plugins
   * base_log_folder : ~/airflow/logs
<br><br>

2. requirements.txt 실행

2. login : airflow / airflow 

3. user 추가 : toby.k / toby.k


2. symbolic 링크 생성
    ```shell
    ln -snf ~/Dev/mlops-study-ml-pipeline/features ~/airflow/dags/features
    ln -snf ~/Dev/mlops-study-ml-pipeline/models ~/airflow/dags/models
    ln -snf ~/Dev/mlops-study-ml-pipeline/support ~/airflow/dags/support
    ```
    ```shell
    ln -snf ~/Dev/mlops-study-ml-pipeline/dags ~/airflow/dags
    ln -snf ~/Dev/mlops-study-ml-pipeline/plugins ~/airflow/plugins
    ```
   * -s, --symbolic make symbolic links instead of hard links
   * -n, --no-dereference treat destination that is a symlink to a
   * -f, --force remove existing destination files
<br><br>

# Airflow task 테스트
* run your first task instance
airflow tasks test example_bash_operator runme_0 2015-01-01
* run a backfill over 2 days
airflow dags backfill example_bash_operator \
    --start-date 2015-01-01 \
    --end-date 2015-01-02
<br><br>

# Airflow 관리
   * Airflow Run
    ```shell
    ./airflow_run.sh
    ```
   * Airflow Stop
    ```shell
    ./kill_process.sh
    ```
<br><br>

# 인증문제는 해결!!
<br><br>


# 테스트코드 실행환경 셋팅
Tools > Python Integrated Tools

Testing : Unittests
 ㄴ auto dectation??


** __init_ 파일에서 테스트코드 실행 시 아래와 같은 메시지가 출력됨.
Error running 'Python tests for UnitTestCase.test_code':
Can't find file where UnitTestCase.test_code declared. Make sure it is in the project root.



# 아래와 같이, airflow WebUI 접속시 나타나는 메시지 무시하기!
- The scheduler does not appear to be running. Last heartbeat was received 50 seconds ago.
  The DAGs list may not update, and new tasks will not be scheduled.
- Do not use SQLite as metadata DB in production
- it should only be used for dev/testing. We recommend using Postgres or MySQL. Click here for more information.
- Do not use SequentialExecutor in production. Click here for more information.



# *.pid 파일 삭제
airflow-webserver.pid


# airflow run, stop ...
* venv 환경내에서만 실행해야 한다.
```shell
$ ./airflow_run.sh
./airflow_run.sh: line 18: airflow: command not found  # airflow command가 존재하지 않아 오류 발생
```



# install mysqlclient
Install MySQL and mysqlclient:

## Assume you are activating Python 3 venv
```shell
$ brew install mysql
$ pip install mysqlclient
```
If you don't want to install MySQL server, you can use mysql-client instead:

## Assume you are activating Python 3 venv
```shell
$ brew install mysql-client
$ echo 'export PATH="/opt/homebrew/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
$ export PATH="/opt/homebrew/opt/mysql-client/bin:$PATH"
$ pip install mysqlclient --no-cache-dir
```

```text
(venv) ➜ bin git:(stable) which mysql_config
/opt/homebrew/opt/mysql-client/bin/mysql_config



install mysql-client 실행 시 ... 설치 로그에서 mysql-client 위치 확인 가능.

... 생략

If you need to have mysql-client first in your PATH, run:
echo 'export PATH="/opt/homebrew/opt/mysql-client/bin:$PATH"' >> ~/.zshrc

For compilers to find mysql-client you may need to set:
export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"
export CPPFLAGS="-I/opt/homebrew/opt/mysql-client/include"
... 생략
```
* zsh 사용 시 아래와 같이, .zshrc 파일에 추가해 준다.
```shell
if [ -f ~/.bash_profile ]; then
. ~/.bash_profile
fi
```
brew install mysql-connector-c

## requirements
mysqlclient
apache-airflow-providers-mysql
sqlparse==0.4.4
pymysql
