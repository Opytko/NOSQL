# 7 Lab
  1. Для 7 лабораторної роботи нам потрібно створити візуалізацію в Kibana заходим в Visualizations > Create visualizations
  ![redis](../screen/L7_1.png)
  ![redis](../screen/L7_2.png)
  2. При створені візуалізації нам потрібно вказати source звідки ми берем наші дані
  ![redis](../screen/L7_5.png)
  3. Добавляємо Buckets і вказуємо параметри для Pie і Line
  - Pie
  ![redis](../screen/L7_6.png)
  - Line  
  ![redis](../screen/L7_7.png)
  4. Для створення фільтра нам потрібно Controls > Option List > Add
  ![redis](../screen/L7_8.png)
  5. Щоб наші данні відобразился в Dashbord нам треба зайти туди і додати наші діаграми і фільтр
  ![redis](../screen/L7_9.png)
  ![redis](../screen/L7_10.png)
  
  Kibana DevTools

  - Топ-3 за полем map.date_of_last_change
```sh
GET _search
{
"size": 0,
"aggs" : {
    "langs" : {
        "terms" : { "field" : "map.activity_number.keyword",  "size" : 3 }
    }
}}
```
![redis](../screen/L7_11.png)
  - Фільтрація записів за датою
```sh
GET _search
{
  "query": {
    "bool": {
      "filter": {
        "bool": {
          "must": [
            {
              "range": {
                "map.intake_date": {
                  "gt": "2019-03-21T15:37:08.595919Z",
                  "lte": "2020-04-21T15:52:08.595919Z"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```
![redis](../screen/L7_12.png)


