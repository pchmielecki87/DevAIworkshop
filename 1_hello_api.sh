
# auth
curl -d '{"apikey":""}' https://tasks.aidevs.pl/token/helloapi

# get_task
curl https://tasks.aidevs.pl/task/e1fea75aa2e567f35c1717d1cc2c0df3e707f51d

# send_answer
curl -d '{ "answer": "tutaj wpisujesz odpowiedz" }' https://tasks.aidevs.pl/answer/e1fea75aa2e567f35c1717d1cc2c0df3e707f51d