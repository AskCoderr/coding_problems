import re
from collections import OrderedDict


def top_3_words(text):
    text += " "
    dictionary = OrderedDict()
    pattern = re.compile(r"[a-z]")
    init = None
    final = None
    li = []
    for i in enumerate(text):
        if (bool(pattern.match(i[1].lower())) or (i[1] == "'" and (bool(pattern.match(text[i[0]-1].lower())) or bool(pattern.match(text[i[0]+1].lower()))))):
            final = i[0]
            if init == None:
                init = i[0]
        else:
            if init != None:
                if text[init:final+1].lower() not in dictionary.keys():
                    dictionary[text[init:final+1].lower()] = 1
                else:
                    dictionary[text[init:final+1].lower()] += 1
            init = None
            final = None

    num = 0
    dict_keys = list(dictionary.keys())
    dict_values = list(dictionary.values())

    while len(dict_values) != 0:
        max_value_index = dict_values.index(max(dict_values))
        li.append(dict_keys[max_value_index])
        dict_keys.pop(max_value_index)
        dict_values.pop(max_value_index)
        num += 1
        if num == 3:
            break
    print(dictionary)
    return li


print(top_3_words("""Every night in my dreams
I see you, I feel you
That is how I know you go on
Far across the distance
And spaces between us
You have come to show you go on
Near, far, wherever you are
I believe that the heart does go on
Once more, you open the door
And you're here in my heart
And my heart will go on and on
Love can touch us one time
And last for a lifetime
And never let go 'til we're gone
Love was when I loved you
One true time I'd hold to
In my life, we'll always go on
Near, far, wherever you are
I believe that the heart does go on
(Why does the heart go on?)
Once more, you open the door
And you're here in my heart
And my heart will go on and on
You're here, there's nothing I fear
And I know that my heart will go on
We'll stay forever this way
You are safe in my heart
And my heart will go on and on
Mm, mm-mm"""))

# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
