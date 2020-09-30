# -*- coding: utf-8 -*-
from _csv import reader

from pulp import *
import pandas as pd
import os


def VisitList(p1, p2, p3, p4, p5):
    """
    p1,p2,p3,p4,p5 represents preference 1 to 5 respectively
    """
    preference = [p1, p2, p3, p4, p5]
    prob = LpProblem("Paris", LpMaximize)
    sites = ["TE", "ML", "AT", "MO", "JT", "CA", "CP", "CN", "BS", "SC", "PC", "TM", "AC"]
    X = []
    for site in sites:
        X.append(LpVariable(site, 0, 1, LpInteger))

    """Data info"""
    duration = [4.5, 3, 1, 2, 1.5, 2, 2.5, 2, 2, 1.5, 0.75, 2, 1.5]
    price = [15.5, 12, 9.5, 11, 1, 10, 10, 5, 8, 8.5, 1, 15, 1]
    appreciations = [5, 4, 3, 2, 3, 4, 1, 5, 4, 1, 3, 2, 5]

    # VisitList-1 Objective function
    numSites = 0
    for site in X:
        numSites += site

    prob += numSites, "Objective Function"

    # Constraint
    i = 0
    site_duration = 0
    site_price = 0

    for x in X:
        site_duration += x * duration[i]
        site_price += x * price[i]
        i += 1

    """Basic constraint"""
    prob += site_duration <= 12  # C1:for duration
    prob += site_price <= 65  # C2:for price

    """Preference constraint"""
    if p1 == 1:
        prob += X[3] == X[4]  # Preference 1 (MO,JT)
        prob += X[6] == X[7]  # Preference 1 (CN,CP)
        prob += X[1] == X[6] == X[7] == X[9]  # Preference 1 (SC,ML,CP,CN)
    if p2 == 1:
        prob += X[0] + X[5] == 2  # C-Preference2
    if p3 == 1:
        prob += X[7] + X[9] <= 1  # C-Preference3
    if p4 == 1:
        prob += X[11] == 1  # C-Preference4
    if p5 == 1:
        prob += X[1] == X[6]  # C-Preference5

    prob.writeLP("Paris.lp")
    prob.solve()

    # Review
    print(LpStatus[prob.status])
    UsedPreference = []
    if p1 == 1:
        UsedPreference.append("P1")
    if p2 == 1:
        UsedPreference.append("P2")
    if p3 == 1:
        UsedPreference.append("P3")
    if p4 == 1:
        UsedPreference.append("P4")
    if p5 == 1:
        UsedPreference.append("P5")
    visitList = []

    for v in prob.variables():
        if v.varValue == 1: visitList.append(v.name)

    df = pd.DataFrame([{'Preference': str(UsedPreference).replace("[", "").replace("]", "").replace("'", ""),
                        'VisitList': str(visitList).replace("[", "").replace("]", "").replace("'", ""),
                        'Maximum places:': int(value(prob.objective))
                        }])

    if not os.path.isfile('answer.csv'):
        df.to_csv('answer.csv', index=False)
    else:
        df.to_csv('answer.csv', mode='a', header=False, index=False)


def Comparison():
    df = pd.read_csv("answer.csv")
    VisitList1 = df.loc[0, "VisitList"]
    compare = []
    for l in df["VisitList"]:
        if l != VisitList1:
            compare.append("False")
        elif l == VisitList1:
            compare.append("True")
    df2 = df.assign(Same=compare)
    df2.to_csv("answer.csv", index=False)


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
