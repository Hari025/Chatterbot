from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot(
    'HariBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
def get_bot_response():
    userText=request.args.get('msg')
    botReply=str(bot.get_response(userText))
    if botReply=='I am sorry, but I do not understand.':
        botReply=str(bot.get_response('default_response'))

training_data_quesans = open('training_data/ques_ans.txt',encoding="utf8").read().splitlines()
training_data_personal = open('training_data/personal_ques.txt',encoding="utf8").read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)  

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 
