--------------
VacationFinder
--------------

A python program to find the best combination of dates for your vacation so that you get as many days off as possible, including holidays and weekends. It's based on Brazillian vacation rules.

Basic rules, considering 2 date pairs (start1,end1) and (star2,end2):

      - start1 < end1 =< start2 < end2
      - endX-startX >= 10 dias
      - start2 >= end1+1 ou start2 = end1
      - number of days between startX and endX is the biggest possible considering near holidays and weekends.
      - end1 - start1 + end2 - start2 <= 30
