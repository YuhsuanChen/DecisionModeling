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
        prob += X[6] == X[7]   # Preference 1 (CN,CP)
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
