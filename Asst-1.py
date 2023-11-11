#FINAL COMPLETELY WORKING CODE FOR CONTINUOS CONVERSATION WITH DOCUMENTAION ANALYSIS
#CAUTIONS NEVER START CONVERSASTION ON OPEN AI SITE IT WILL START NEW THREAD WHICH DECLINES THE CURRENT THREAD


api_key = "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"












assist_id = "asst_QNsVazhOzwC34ZkTTTc4JsG7"
thread_id = "thread_96nvgztISY3doL4vgO3LCDNG"
import os
import openai
import speech
import Listen
os.environ["OPENAI_API_KEY"] = api_key

STATUS_COMPLETED = "completed"
client = openai.OpenAI()

instructions = """
    You are a helpful assistant  which keeps track of my work and researches
     through our conversation and documents and help me. remember every thing
      we talk about.Suggest me best things with good knowledge. Humorous and
      sarcastic(sometimes) in speaking behaviour
    """



#thread=  client.beta.threads.create()
#print(thread.id)

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assist_id,
    instructions=instructions
)
print(f"Your run id is - {run.id}\n")

while True:
    #text= str(input("enter you Ayaan: "))
    text = str(Listen.recognize_speech())#input("What's your question?\n")


    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=text,
    )

    new_run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assist_id,
        instructions=instructions,
    )
    print(f"Your new run id is - {new_run.id}")

    status = None
    while status != STATUS_COMPLETED:
        run_list = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=new_run.id
        )
        print(f"{run_list.status}\r", end="")
        status = run_list.status
        print(status)
        if status == 'failed':
            break

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    if(messages.data[0].content[0].text.value=="Quit"):
        print("Bye..")
        break

    print(f"{'Phoenix' if messages.data[0].role == 'assistant' else 'user'} : {
          messages.data[0].content[0].text.value}\n")
    speech.speak(messages.data[0].content[0].text.value)







