# LAB 5

 1. ��������� Resource Group �� Azure Portal
 ![redis](../screen/L5_1.png)
 2. �������� �� New
 ![redis](../screen/L5_2.png)
 3. ������� ����� ��� ����� ������� � ����� � ������� Review + Create
 ![redis](../screen/L5_3.png)
 4. ��������� Azure Redis for Cache, ������ resource group, ������� DNS name, ������� region, chache type recomended ��� Review + Create
 ![redis](../screen/L5_4.png)
 5. �������� � ��� redis � � Access keys ��� ������� ������ Primary key � Primary connection string ��� ������ ������㳿 redis
 ![redis](../screen/L5_5.png)
 6. ��������� Evens Space, ������ resource group, �������� Namespace name, ������� region, Pircing tier recomended ��� Review + Create
 ![redis](../screen/L5_6.png)
 7. �������� � ��������� Event Space � ��������� Event Hub ������� ������ +Event ��� ��� ������� ������� ���� ���� ��'�
 ![redis](../screen/L5_7.png)
 8. �������� � ��� Event Hub ������� ��� �������� policy Shared access policies � ���� ����� � ������
 ![redis](../screen/L5_8.png)
 9. ���������� ��� �������� ��� ������� �������� ��� � dataset'y, �� �� ������� �� ��������� Postman
 ![redis](../screen/L5_9.png)
 10. � ������� Postman �� ��������� ����� POST ����� ��� ���� ������㳿 redis � eventHub ��� �� ������ ������������ ���� ���� � Post �� ������ localhost:9000/url ������� ������ �� ��������
 ![redis](../screen/L5_10.png)
 ![redis](../screen/L5_11.png)
 11. ���� �� ��������� ���� ������ SEND � Postman �� �� ������ �� ������� ������ ���� ��� ����� ���� ��������: evenHub ���� ���������� ����Event Hub ��� Event Hub > Features > Proccess Data > Explore, � redis � Redis ��� Redis Cache > Console � ������� ���� ������ � ������ ������� hgetAll ConsoleLog
 ![redis](../screen/L5_12.png)
 ![redis](../screen/L5_13.png)