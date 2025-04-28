Via Docker (KO) : 
- Commande 1 : docker-compose up
- Commande 2 : curl localhost:4040/api/tunnels
- Mettre l'url récupérée dans slack (Event Subscriptions)

Via cmd (OK) : 
- rasa run --connector slack --port 5005
- rasa run actions
- ngrok http 5005
- Mettre l'url récupérée dans slack (Event Subscriptions)