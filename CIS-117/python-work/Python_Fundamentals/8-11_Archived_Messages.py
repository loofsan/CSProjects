messages = ["hello", "Noway", "Deway", "wtf", "nonono", "TT"]
sent_messages = []

def send_messages(messages, sent_messsages):
	for i in messages:
		print(f"{i} is sending...")
	while messages:
		for i in messages:
			sent = messages.pop()
			sent_messages.append(sent)

	for i in sent_messages:
		print(f"{i} has been sent.")

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)






