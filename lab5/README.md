# LAB 5

 1. Ñòâîðþºìî Resource Group íà Azure Portal
 ![redis](https://github.com/Opytko/NOSQL/blob/main/Screen/L5_1.png)
 2. Íàæèìàºìî íà New
 ![redis](../screen/L5_2.png)
 3. Âêàçóºìî íàçâó äëÿ ãðóïè ï³äïèñêó ³ ðåã³îí ³ æìåìîìî Review + Create
 ![redis](../screen/L5_3.png)
 4. Ñòâîðþºìî Azure Redis for Cache, îáèðàºì resource group, íàçèâàºì DNS name, îáèðàºìî region, chache type recomended äàë³ Review + Create
 ![redis](../screen/L5_4.png)
 5. Çàõîäèìî ó íàø redis ³ â Access keys íàì ïîòð³áíî âçíàòè Primary key ³ Primary connection string äëÿ çàïèñó ñòðàòåã³¿ redis
 ![redis](../screen/L5_5.png)
 6. Ñòâîðþºìî Evens Space, îáèðàºì resource group, íàçèâàºìî Namespace name, îáèðàºìî region, Pircing tier recomended äàë³ Review + Create
 ![redis](../screen/L5_6.png)
 7. Çàõîäèìî ó ñòâîðåíèé Event Space ³ ñòâîðþºìî Event Hub íàæàâøè êíîïêó +Event äàë³ íàì ïîòð³áíî âêàçàòè ëèøå éîãî ³ì'ÿ
 ![redis](../screen/L5_7.png)
 8. Çàéøîâøè â íàø Event Hub ïîòð³áíî íàì ñòâîðèòè policy Shared access policies ³ äàòè íàçâó ³ äîçâ³ëè
 ![redis](../screen/L5_8.png)
 9. Çàïóñòèâøè êîä ïðîãðàìè íàì ïîòð³áíî çàïèñàòè äàí³ ç dataset'y, ùî ìè çðîáèìî çà äîïîìîãîþ Postman
 ![redis](../screen/L5_9.png)
 10. Ó ïðîãðàì³ Postman ìè ñòâîðþºìî íîâèé POST çàïèò äëÿ íàøî¿ ñòðàòåã³¿ redis ³ eventHub ùîá ìè çìîãëè çàâàíòàææèòè íàø³ äàíí³ ó Post ìè ïèøèìî localhost:9000/url ³ðîáèìî çàïèòè äî ñòðàòåã³é
 ![redis](../screen/L5_10.png)
 ![redis](../screen/L5_11.png)
 11. Êîëè ìè íàòèñêàºìî íàøó êíîïêó SEND â Postman òî ìè áà÷èìî ÿê ïðîãðàì çàïèñóº äàíí³ äëÿ íàøèõ äâîõ ñòðàòåã³é: evenHub áóäå ïîêàçóâàòè äàíí³Event Hub Âàø Event Hub > Features > Proccess Data > Explore, à redis â Redis Âàø Redis Cache > Console ³ ïîòð³áíî áóäå ââåñòè â êîíñîë³ êîìàíäó hgetAll ConsoleLog
 ![redis](../screen/L5_12.png)
 ![redis](../screen/L5_13.png)
