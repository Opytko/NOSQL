# 6 Lab
  1. Для 6 лабораторної роботи нам потрібно створити проект та акаунт на GCP (Google Cloud Platform)
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_1.png)
  2. Наступним кроком нам потрібно встановити VM instances 
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_2.png)
  
    Деталі нашого Instances
    
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_4.png)
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_4_1.png)
  3. Тепер прописуємо Firewall для kibana tcp:5601 і elasic на порті tcp:9200
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_3.png)
  4. Підключившись до машини через SSH
  ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_5.png)
  в консолі яка появилася прописуємо настуні команди:
     
   - встановленння джави
```sh
sudo apt-get install default-jre
```
   - встановлення та запуск elastic 
```sh
sudo apt update
sudo apt install apt-transport-https
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
sudo apt update
sudo apt install elasticsearch
sudo service elasticsearch status
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
```
   - відкриваємо `elasticsearch.yml` та змінюємо нетворк хост на 0.0.0.0
```sh
sudo nano /etc/elasticsearch/elasticsearch.yml
sudo service elasticsearch restart
sudo service elasticsearch status
```
   - встановлюєм Logstash та Kibana
```sh
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
sudo apt-get update
sudo apt-get install logstash
sudo service logstash start
echo "deb http://packages.elastic.co/kibana/7.0/debian stable main" | sudo tee -a /etc/apt/sources.list.d/kibana-7.0.x.list
sudo wget --directory-prefix=/opt/ https://artifacts.elastic.co/downloads/kibana/kibana-7.6.1-amd64.deb
sudo dpkg -i /opt/kibana*.deb
sudo apt-get update
sudo apt-get install kibana
```
   - редагуємо файл `kibana.yml`,пропусуємо server.host "0.0.0.0" nа розкоментовуємо порт 5601 для Kibana
```sh
sudo nano /etc/kibana/kibana.yml
```
   - Стартуємо Kibana
```sh
sudo service kibana start
```
  - Перевіряємо статус Kibana
```sh
sudo service kibana status
```
5. Після цього переходимо в наш інстанс та копіюємо External IP і в прописуємо порти: `:5601` та `:9200`
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_6.png)
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_6_1.png)
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_6_2.png)
6. Тепер потрібно створити Logic app у Azure та створити connect у Logic app designer та заранити
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_7_1.png)
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_7_2.png)
7. Після цього у Kibana відкриваємо Managment > Stack Management > Index Patterns > lab6* можна буде побачити дані 
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_6_1.png)
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_8_1.png)
![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L6_8_2.png)






