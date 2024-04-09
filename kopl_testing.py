'''
import kopl
from kopl.test.test_example import *
run_test()
'''
from kopl.kopl import KoPLEngine
from kopl.test.test_example import example_kb

print(type(example_kb))

print(example_kb)

engine = KoPLEngine(example_kb) # 创建可以在example_kb这个知识库上进行操作的engine示例



# Вопрос：Who is taller, LeBron James Jr. or his father?
ans = engine.SelectBetween( # Из двух сущностей выберете ту, которая выше
  engine.Find('LeBron James Jr.'), # найти объект: 'LeBron James Jr'
  engine.Relate( # найти 'LeBron James Jr'который 'father
    engine.Find('LeBron James Jr.'), # найти объект: 'LeBron James Jr'
    'father', # метка связи
    'forward' # ’forward‘ значит 'LeBron James Jr'为头实体
  ),
  'height', # метка атрибута
  'greater' # запрашивайте объекты с большими значениями атрибутов
)

print(ans) # ans список имен сущностей