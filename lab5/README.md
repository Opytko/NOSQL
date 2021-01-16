# LAB 5

 1. Створюємо Resource Group на Azure Portal
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_1.png)
 2. Нажимаємо на New
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_2.png)
 3. Вказуємо назву для групи підписку і регіон і жмемомо Review + Create
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_3.png)
 4. Створюємо Azure Redis for Cache, обираєм resource group, називаєм DNS name, обираємо region, chache type recomended далі Review + Create
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_4.png)
 5. Заходимо у наш redis і в Access keys нам потрібно взнати Primary key і Primary connection string для запису стратегії redis
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_5.png)
 6. Створюємо Evens Space, обираєм resource group, називаємо Namespace name, обираємо region, Pircing tier recomended далі Review + Create
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_6.png)
 7. Заходимо у створений Event Space і створюємо Event Hub нажавши кнопку +Event далі нам потрібно вказати лише його ім'я
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_7.png)
 8. Зайшовши в наш Event Hub потрібно нам створити policy Shared access policies і дати назву і дозвіли
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_8.png)
 9. Запустивши код програми нам потрібно записати дані з dataset'y, що ми зробимо за допомогою Postman
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_9.png)
 10. У програмі Postman ми створюємо новий POST запит для нашої стратегії redis і eventHub щоб ми змогли завантажжити наші данні у Post ми пишимо localhost:9000/url іробимо запити до стратегій
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_10.png)
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_11.png)
 11. Коли ми натискаємо нашу кнопку SEND в Postman то ми бачимо як програм записує данні для наших двох стратегій: evenHub буде показувати данніEvent Hub Ваш Event Hub > Features > Proccess Data > Explore, а redis в Redis Ваш Redis Cache > Console і потрібно буде ввести в консолі команду hgetAll ConsoleLog
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_12.png)
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_13.png)
