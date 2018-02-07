#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

class Ran:
    lucky = 100
    run = True

    def ing(self):
        if self.run == True:
            self.lucky = self.lucky + random.randint(-10, 10)
            if self.lucky <= 0:
                self.run = False

test = Ran()
point = 0
end = 1000
while point < end:
    if test.run == False:
        print('end :'+(str)(point))
        break
    test.ing()
    print(test.lucky)
    point=point+1