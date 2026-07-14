from chains import grammar_chain

response = grammar_chain.invoke({
    "text": "im happy"
})

print(response)