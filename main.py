from paris import VisitList
from paris import Comparison

VisitList(0, 0, 0, 0, 0)  # VisitList-1
"""
The 5 parameter represents preference Mr.Doe considered.
For example: VisitList(1, 0, 0, 0, 0)  # Preference 1: Near Attraction
             VisitList(0, 1, 0, 0, 0)  # Preference 2: Absolutely visit (TE) and (CA)
             VisitList(0, 0, 1, 0, 0)  # Preference 3 : If visits CN then he will not visit SC
             VisitList(0, 0, 0, 1, 0)  # Preference 4: Absolutely visit (TM)
             VisitList(0, 0, 0, 0, 1)  # Preference 5: If visits ML then must visit the CP
For question (b) to (l), the answer will be in the csv file that generate after running VisitList
"""
#
VisitList(1, 0, 0, 0, 0)  # Preference 1: Near Attraction
VisitList(0, 1, 0, 0, 0)  # Preference 2: Absolutely visit (TE) and (CA)
VisitList(0, 0, 1, 0, 0)  # Preference 3 : If visits CN then he will not visit SC
VisitList(0, 0, 0, 1, 0)  # Preference 4: Absolutely visit (TM)
VisitList(0, 0, 0, 0, 1)  # Preference 5: If visits ML then must visit the CP
VisitList(1, 1, 0, 0, 0)  # (b) Preference1 & 2
VisitList(1, 0, 1, 0, 0)  # (c) Preference1 & 3
VisitList(1, 0, 0, 1, 0)  # (d) Preference1 & 4
VisitList(0, 1, 0, 0, 1)  # (e) Preference 2 & 5
VisitList(0, 0, 1, 1, 0)  # (f) Preference 3 & 4
VisitList(0, 0, 0, 1, 1)  # (g) Preference 4 & 5
VisitList(1, 1, 0, 1, 0)  # (h) Preference 1 & 2 & 4
VisitList(0, 1, 1, 0, 1)  # (i) Preference 2 & 3 & 5
VisitList(0, 1, 1, 1, 1)  # (j) Preference 2 & 3 & 4 & 5
VisitList(1, 1, 0, 1, 1)  # (k) Preference 1 & 2 & 4 & 5,
VisitList(1, 1, 1, 1, 1)  # (l) Preference 1 & 2 & 3 & 4 & 5
# (m) Is the solution ListVisit1 different to these solutions founded above (with the combination of preferences) ?


Comparison()