# Programme Pédagogique — Diplôme d'Ingénieur IG2I (Centrale Lille)

Cursus de 5 ans organisé en trois grandes phases : socle multidisciplinaire, cycle ingénieur, puis spécialisation de fin d'études.

---

## Années 1 & 2 — Socle Multidisciplinaire

Les deux premières années sont consacrées à l'acquisition des fondamentaux scientifiques et techniques nécessaires à tout ingénieur.

### Informatique et Systèmes

**Algorithmique & Complexité**
Calcul de la complexité temporelle et spatiale — $\mathcal{O}(n)$, $\mathcal{O}(n \log n)$, $\mathcal{O}(n^2)$. Algorithmes de tri (fusion, rapide), parcours de graphes (Dijkstra, A*, BFS/DFS), arbres binaires de recherche.

**Structures de Données**
Implémentation bas niveau de listes chaînées, piles (LIFO), files (FIFO), tables de hachage avec gestion des collisions, graphes et tas (*heaps*).

**Programmation Orientée Objet**
[![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org)
[![Java](https://img.shields.io/badge/Java-007396?logo=openjdk&logoColor=white)](https://openjdk.org)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org)

Encapsulation, héritage, polymorphisme, abstraction, interfaces, surcharge d'opérateurs.

**Architecture des Ordinateurs**
Modèle de Von Neumann, portes logiques (NAND, NOR), algèbre de Boole, bascules, registres, UAL. Programmation en assembleur : gestion de la mémoire, de la pile d'exécution et des interruptions.

---

### Mathématiques Appliquées

**Algèbre linéaire**
Espaces vectoriels, calcul matriciel, déterminants, diagonalisation, valeurs propres et vecteurs propres — fondamental pour la 3D et le Machine Learning.

**Analyse**
Suites et séries (convergence), équations différentielles, transformées de Laplace et de Fourier (essentiel pour le traitement du signal).

**Probabilités & Statistiques**
Variables aléatoires discrètes et continues, espérance, variance, probabilités conditionnelles et théorème de Bayes :

$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

Distributions : normale, binomiale, Poisson, Student, $\chi^2$. Statistiques inférentielles : intervalles de confiance, tests d'hypothèses (conformité, $\chi^2$, ANOVA), p-value.

---

### Physique et Électronique

**Électronique**
Loi d'Ohm, lois de Kirchhoff, théorèmes de Thévenin et Norton. Amplificateurs opérationnels, filtres actifs et passifs (passe-bas, passe-haut), convertisseurs CAN/CNA.

**Automatique**
Modélisation de systèmes dynamiques (systèmes linéaires continus), fonctions de transfert, diagrammes de Bode et Nyquist, stabilité, correcteurs PID.

---

## Années 3, 4 & 5 — Cycle Ingénieur (Tronc Commun)

Le cycle ingénieur approfondit l'expertise technique en combinant infrastructures, génie logiciel et une introduction à l'intelligence artificielle.

### Infrastructures et Réseaux

**Modèles et protocoles**
Maîtrise du modèle OSI et de la pile TCP/IP. Adressage IPv4/IPv6, sous-réseaux, DHCP, DNS. Algorithmes de routage interne (OSPF) et externe (BGP). Switching : VLAN, STP.

**Administration Système**
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](https://kernel.org)
[![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)

Shell scripting (Bash), gestion des droits (`chmod`, `chown`), gestion des processus, système de fichiers, IPC (*Inter-Process Communication*).

**Virtualisation et Conteneurisation**
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![VMware ESXi](https://img.shields.io/badge/VMware_ESXi-607078?logo=vmware&logoColor=white)](https://www.vmware.com/products/esxi-and-esx.html)
[![VirtualBox](https://img.shields.io/badge/VirtualBox-183A61?logo=virtualbox&logoColor=white)](https://www.virtualbox.org)

Hyperviseurs de type 1 (ESXi) et de type 2 (VirtualBox). Conteneurisation avec Docker (Dockerfile, volumes, réseaux), introduction à l'orchestration.

---

### Développement et Génie Logiciel

**Architectures Logicielles**
Modèle MVC, design patterns du GoF (Singleton, Factory, Observer, Strategy). Microservices vs. monolithes, architectures orientées événements, conception d'API RESTful.

**Bases de Données**

*Relationnel (SGBDR) :* algèbre relationnelle, SQL avancé (jointures, sous-requêtes, triggers, procédures stockées), propriétés ACID, formes normales (1NF–3NF).

*NoSQL :*
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com)
[![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)](https://redis.io)
[![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?logo=neo4j&logoColor=white)](https://neo4j.com)

Théorème CAP.

**DevOps & CI/CD**
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
[![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?logo=gitlab&logoColor=white)](https://docs.gitlab.com/ee/ci/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white)](https://www.jenkins.io)

Gestion de version avancée (Git flow). Pipelines d'intégration et de déploiement continus.

**Qualité Logicielle**
[![JUnit](https://img.shields.io/badge/JUnit5-25A162?logo=junit5&logoColor=white)](https://junit.org/junit5/)
[![PyTest](https://img.shields.io/badge/PyTest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org)
[![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?logo=sonarqube&logoColor=white)](https://www.sonarqube.org)

Tests unitaires, tests d'intégration et E2E. Approches TDD et BDD. Analyse statique de code.

---

### Intelligence Artificielle — Socle

**Machine Learning**
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org)

Apprentissage supervisé : régression linéaire/logistique, SVM, arbres de décision, Random Forest. Apprentissage non supervisé : clustering K-Means, ACP.

**Évaluation des modèles**
Matrice de confusion, précision, rappel, score F1, validation croisée K-fold.

---

## Spécialisations — Expertise de fin d'études

En dernière année, les étudiants choisissent l'une des trois voies d'expertise suivantes.

---

### Spécialisation A — Data and Software Engineering

**Big Data**
[![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org)
[![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org)
[![Hadoop](https://img.shields.io/badge/Apache_Hadoop-66CCFF?logo=apachehadoop&logoColor=black)](https://hadoop.apache.org)

Architectures distribuées. Traitement par lots avec Hadoop (HDFS, MapReduce) et Spark (PySpark). Traitement en flux avec Kafka.

**Deep Learning & IA avancée**
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org)

Réseaux de neurones artificiels (ANN), CNN pour la vision par ordinateur, RNN/LSTM et Transformers pour le NLP.

**Software Engineering avancé**
Domain-Driven Design (DDD), architecture hexagonale (*Clean Architecture*).

---

### Spécialisation B — Cloud Computing and Cybersecurity

**Cryptographie**
Chiffrement symétrique (AES) et asymétrique (RSA, courbes elliptiques). Fonctions de hachage (SHA-256), signatures numériques, PKI.

**Sécurité offensive et défensive**
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![OWASP](https://img.shields.io/badge/OWASP_Top_10-000000?logo=owasp&logoColor=white)](https://owasp.org/www-project-top-ten/)

Pentesting, failles web (injections SQL, XSS, CSRF), analyse de malwares, SIEM, SOC.

**Cloud & Infrastructure as Code**
[![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white)](https://aws.amazon.com)
[![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![GCP](https://img.shields.io/badge/GCP-4285F4?logo=googlecloud&logoColor=white)](https://cloud.google.com)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)](https://www.terraform.io)
[![Ansible](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)](https://www.ansible.com)

Modèles IaaS, PaaS, SaaS. Infrastructure as Code, sécurité du Cloud.

---

### Spécialisation C — Smart Systems (IoT & Embarqué)

**Systèmes Embarqués**
[![ARM](https://img.shields.io/badge/ARM_Cortex-0091BD?logo=arm&logoColor=white)](https://www.arm.com/products/silicon-ip-cpu)
[![STM32](https://img.shields.io/badge/STM32-03234B?logo=stmicroelectronics&logoColor=white)](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
[![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org)
[![MicroPython](https://img.shields.io/badge/MicroPython-2B2728?logo=micropython&logoColor=white)](https://micropython.org)

Architecture des microcontrôleurs. Programmation bare-metal et MicroPython. Timers, ADC/DAC, bus I2C, SPI, UART, CAN.

**OS Temps Réel (RTOS)**
[![FreeRTOS](https://img.shields.io/badge/FreeRTOS-8CC84B?logo=freertos&logoColor=white)](https://www.freertos.org)

Ordonnancement temps réel, sémaphores, mutex, files de messages — gestion de la concurrence.

**Internet des Objets (IoT)**
[![MQTT](https://img.shields.io/badge/MQTT-660066?logo=mqtt&logoColor=white)](https://mqtt.org)
[![Zigbee](https://img.shields.io/badge/Zigbee-EB0443?logo=zigbee&logoColor=white)](https://csa-iot.org/all-solutions/zigbee/)
[![BLE](https://img.shields.io/badge/Bluetooth_LE-0082FC?logo=bluetooth&logoColor=white)](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/)
[![LoRaWAN](https://img.shields.io/badge/LoRaWAN-011E57?logo=semtech&logoColor=white)](https://lora-alliance.org)

Protocoles LPWAN (LoRaWAN, Sigfox), protocoles locaux (BLE, Zigbee), MQTT pour la remontée de données, Edge Computing.
