class English:
# properties
 alphabet = "latin"
 total_words = 170_000
 language_code = "en"
# methods
 def sayHi():
  print("Hello")
 def sayBye():
  print("Bye")
 def langCode():
  print("en")
class Russian:
# properties
 alphabet = "cyrillic"
 total_words = 200_000
 language_code = "ru"
# methods
 def sayHi():
  print("Привет")
 def sayBye():
  print("Пока")
 def langCode():
  print("ru")
  print("en")
English.sayHi()
English.sayBye()
Russian.sayHi()
Russian.sayBye()
English.total_words += 1
print("English has", English.total_words, "words.")

# hm1: add another property and method to each class
# hm2: add another class for another language

class Chinese:
# properties
 alphabet = "hieroglyphic"
 total_words = 500_000
 language_code = "zh"
# methods
 def sayHi():
  print("nǐ hǎo")
 def sayBye():
  print("zàijiàn")
 def langCode():
  print("zh")
Chinese.sayHi()
Chinese.sayBye()
Chinese.langCode()
print("In Chinese language they use the", Chinese.alphabet, "writing system.")