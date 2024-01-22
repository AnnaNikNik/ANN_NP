from django import template
#from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter()

def censor(text):
    if type(text) != str:
        raise ValueError("Фильтр цензурирования применяется только к переменным строкового типа")

    spl_text = text.split()
    explicitwords = ['ахуе',
                     'бля,',
                     ]

    for ex_word in explicitwords:
        ex_word = ex_word.title()

        for word in spl_text:
            word1 = word[0].upper() + word[1:]

            if word1 == ex_word:
                text = text.replace(word, word[0] + '*' * (len(word) - 1))


    """Removes all values of arg from the given string"""
    return text


