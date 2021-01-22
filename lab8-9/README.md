# Lab 8-9

# Для того що наша лаба працювала нам потрібно встановити потрібні елементи на Azure
1. Databricks service
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_1.png)
2. Клацаємо на +New і сворюємо наш Databricks вибираємо параметри і жмемо review and create
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_2.png)
3. Далі нам потрібно створити Storage Account і перейти в advanced та включити Data Lake storage Gen2
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_3.png)
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_4.png)
4. Потім нам потрібно створити аплікацію Azure Active Directory 
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_5.png)
5. В Azure Active Directory ми обираємо App registration і створюємо + New registration і вказуємо лише імя і жмемо register
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_6.png)
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_7.png)
6. Також нам потрібен буде EventHub можна взяти з попередньої лаби
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_8.png)
7. Після цього переходимо у уже створений databricks і запускаєм його
   ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_9.png)
8. Потім переходмимо в Cluster і стартуємо його start
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_10.png)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_11.png)
9. Після запуску Cluster ідемо в бібліотки і інсталимо maven `com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.18`
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_12.png)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_13.png)
10. Тепер у Workspace маємо створити python і scala file> пкм> create > notebook
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_14.png)
11. Тепер переходимо у наші створені файли вставляємо код з eventHub у notebook scala, mounty.py у notebook py
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_15.png)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_16.png)
12. Далі створюємо container і вказуєм його імя
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_17.png)
13. У розділі Access Control створюємо contributor до нашої аплікації і зберігаємо його
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_18.png)
14. Заходимо у App Registraation і взнаємо потрібні нам id
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_19.png)
15. Перейдемо у Сertіficates and secret тф створимо secret (копіюємо його бо він з часо закриється)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_20.png)
16. Тепер нам потрібно встановити Azure Storage Explorer (переходимо по лінку)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_21.png)
17. В Azure Storage Explorer нам треба надати доступ до контейнера
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_22.png)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_23.png)
    
    так само пророблюємо для папки
    
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_24.png)
18. Повертаємося в Databricks і в ostaplab9.py вказуємо імя контейнера та акаунта`source="abfss://ostaplab9@ostaplab9.dfs.core.windows.net/"`
    `mount_point = "/mnt/ostaplab9",`
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_25.png)
    і жмемо mount
19. Переходим в scala і вставляємо id і conection string в код і в `config.json` треба вставити conection string і імя eventhub
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_27.png)
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_28.png)
20. У функції filtered нам потрібно змінити поля які відповідають за парсення файлу csv, а у фалйлі `EventHubWriter.py` також можна додати ще поля чи забрати    
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_29.png)
21. Змінюємо директорію у яку ми маунтели теку
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_30.png)
22. Далі раним директорію і запускаєм програму на пайтоні, у програмі postman нам протрібно створити REST запит POST на лінку `http://127.0.0.1:5000/eventhub`
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_31.png)
23. Заходимо у Microsoft Azure Storage Exporter у наш контейнер і дерикторію і обновляємо там появляються наші дані у csv файлах
    ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L89_32.png)
