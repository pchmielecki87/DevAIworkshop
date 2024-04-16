
# auth
curl -d '{"apikey":""}' https://tasks.aidevs.pl/token/inprompt

# get_task
curl https://tasks.aidevs.pl/task/4aa10b770b4f7d9f21fa0d9adeab6ae5eccc39a7

# send_answer
curl -d '{"answer": "YES"}' https://tasks.aidevs.pl/answer/f4f10f42ea30c2e2c446bbd15ce6dc5b657481a4


Lista jest zbyt duża, aby móc ją wykorzystać w jednym zapytaniu, więc dowolną techniką odfiltruj te zdania, które zawierają wzmiankę na temat osoby wspomnianej w pytaniu. Ostatnim krokiem jest wykorzystanie odfiltrowanych danych jako kontekst na podstawie którego model ma udzielić odpowiedzi na pytanie. Zatem: 
+ pobierz listę zdań oraz pytanie, 
- skorzystaj z LLM, aby odnaleźć w pytaniu imię, 
- programistycznie lub z pomocą no-code odfiltruj zdania zawierające to imię. 
- Ostatecznie spraw by model odpowiedział na pytanie, a jego odpowiedź prześlij do naszego API w obiekcie JSON zawierającym jedną właściwość “answer”.