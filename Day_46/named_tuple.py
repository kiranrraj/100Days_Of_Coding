from collections import namedtuple
subjects = namedtuple('subjects', 'English Malayalam Hindi, Mathematics, Science')
my_score = subjects(English=90, Malayalam=88, Hindi=95, Mathematics=70, Science=80)
print(my_score.English)