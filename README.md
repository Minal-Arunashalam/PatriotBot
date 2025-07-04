# PatriotBot
PatriotBot for PatriotHacks Fall 2023

PatriotBot is a chatbot website that helps incoming freshman navigate their college experience at GMU much more seamlessly, saving them the hassle of sifting through the entire GMU website themselves. 

GMU's website contains important guides, resources, and directions. However, the user experience is convoluted, making it hard to for incmoing freshman to find the information they need. PatriotBot solves this by scraping the relevant information from GMU's site, and training a GPT 3.5 model on the data, giving it the context it needs to accurately answer any queries incoming freshman ask. 

Improvements that could be made to this include:
- Limiting/controlling user queries/model responses (guardrails).
- RAG system that retrives the relevant scraped info at query time. Scraped info can be split into chunks, embedded, and stored into vector database. The RAG system can then retrieve the top-k similar chunks based on the user's query.
- Feedback loop (user can thumbs up/down based on model response quality).
