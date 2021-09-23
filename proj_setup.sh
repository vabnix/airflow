echo "Setting up Airflow"
echo "----------------------"

echo "Updating System Dependencies"
sudo apt-get install -y --no-install-recommends \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libffi6 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc


echo "Installing Apache Airflow"
pip install apache-airflow


echo "creating working directory"
mkdir airflow_day_1

cd airflow_day_1

echo "Initializing Astro"
astro dev init

ls -ltr

echo "Stopping Airflow if already running!!!"
astro dev stop 


echo "Starting Airflow"
astro dev start
