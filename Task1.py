import spacy
import pandas as pd
import nltk
from nltk.corpus import stopwords

# Загрузка ядра модели spaCy
nlp = spacy.load("en_core_web_sm")

# Загрузка стоп-слов
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Текст новости
text = "Apple Inc. reported a surge in revenue for the first quarter, driven by strong sales of its iPhone 13 and Macbook Pro."

# Обработка текста с помощью spaCy
doc = nlp(text)

# Извлечение именованных сущностей
entities = []
for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG']:  # Выбор только персон и организаций
        entities.append(ent.text)

# Извлечение организаций
organizations = []
for ent in doc.ents:
    if ent.label_ == 'ORG':
        organizations.append(ent.text)

# Фильтрация стоп-слов из организаций
organizations = [org for org in organizations if org.lower() not in stop_words]

# Вывод результатов
print("Именованные сущности: ", entities)
print("Организации: ", organizations)

