# lab4
- **Посилання на Docker:**
    - [yaroslavkoguch/site](https://hub.docker.com/repository/docker/yaroslavkoguch/site)
    - [django](https://hub.docker.com/layers/131376387/yaroslavkoguch/site/django/images/sha256-6a1216ecc3ded1e1cb049db81b7a843ef82c0edac230a61721fa81053215b536?context=explore)
    - [monitoring](https://hub.docker.com/layers/131376599/yaroslavkoguch/site/monitoring/images/sha256-5ac698f71ac662585590fc370707c6b275222356f03209230fca570d3ced399a?context=explore)
---
1. **Ознайомився з Docker.**
---
2. **Виконав команди:**
   - sudo docker -v > my_work.log
   - sudo docker -h >> my_work.log
   - sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log
---
3. **Ознайомився з документацією**
---
4. **Створив файл з іменем Dockerfile та замінив посилання на власний Git репозиторій**
---
5. **Створив власний репозиторій на Docker Hub**
---
6. **Виконав команди:**
   - sudo docker build -t yaroslavkoguch/site:django .
   - sudo docker images
   - sudo docker push yaroslavkoguch/site:django
---
7. **Веб-сайт працює**
---
8. 
   - **створив Dockerfile.site**
   - **Виконав білд імеджа:**
       -  sudo docker build -f Dockerfile.site -t yaroslavkoguch/site:monitoring .
       - sudo docker images
       - sudo docker push yaroslavkoguch/site:monitoring
   - **Щоб отримати логи виконав команди:**
     - sudo docker run -it --rm -p 8000:8000 yaroslavkoguch/site:django
     - sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log yaroslavkoguch/site:monitoring
---
