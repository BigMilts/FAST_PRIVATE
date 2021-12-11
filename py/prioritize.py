'''
This file is part of an ICSE'18 submission that is currently under review.
For more information visit: https://github.com/icse18-FAST/FAST.

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this source.  If not, see <http://www.gnu.org/licenses/>.
'''

import math
import os
import pickle
import glob

import competitors
import fast
import metric

usage = """USAGE: python py/prioritize.py <dataset> <entity> <algorithm> <repetitions>
OPTIONS:
  <dataset>: test suite to prioritize.
    options: flex_v3, grep_v3, gzip_v1, make_v1, sed_v6, closure_v0, lang_v0, math_v0, chart_v0, time_v0
  <entity>: BB or WB (function, branch, line) prioritization.
    options: bbox, function, branch, line
  <algorithm>: algorithm used for prioritization.
    options: FAST-pw, FAST-one, FAST-log, FAST-sqrt, FAST-all, STR, I-TSD, ART-D, ART-F, GT, GA, GA-S
  <repetitions>: number of prioritization to compute.
    options: positive integer value, e.g. 50
NOTE:
  STR, I-TSD are BB prioritization only.
  ART-D, ART-F, GT, GA, GA-S are WB prioritization only."""


def bboxPrioritization(name, prog, v, ctype, k, n, r, b, repeats, selsize, test_cases1):
    javaFlag = True

    # if name == "FAST-" + selsize.__name__[:-1]:
    #     if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
    #         ptimes, stimes, apfds = [], [], []
    #         for run in range(repeats):
    #             print(" Run", run)
    #             if javaFlag:
    #                 stime, ptime, prioritization = fast.fast_(
    #                     fin, selsize, r=r, b=b, bbox=True, k=k, memory=False)
    #             else:
    #                 stime, ptime, prioritization = fast.fast_(
    #                     fin, selsize, r=r, b=b, bbox=True, k=k, memory=True)
    #             writePrioritization(ppath, name, ctype, run, prioritization)
    #             apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
    #             apfds.append(apfd)
    #             stimes.append(stime)
    #             ptimes.append(ptime)
    #             print("  Progress: 100%  ")
    #             print("  Running time:", stime + ptime)
    #             if javaFlag:
    #                 print("  APFD:", sum(apfds[run]) / len(apfds[run]))
    #             else:
    #                 print("  APFD:", apfd)
    #         rep = (name, stimes, ptimes, apfds)
    #         writeOutput(outpath, ctype, rep, javaFlag)
    #         print("")
    #     else:
    #         print(name, "already run.")

    if name == "FAST-pw":
        for run in range(repeats):
            print(" Run", run + 1)
            if javaFlag:
                prioritization = fast.fast_pw(
                    test_cases1, r, b, bbox=True, k=k, memory=False)
            return prioritization

    # elif name == "STR":
    #     if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
    #         ptimes, stimes, apfds = [], [], []
    #         for run in range(repeats):
    #             print(" Run", run)
    #             stime, ptime, prioritization = competitors.str_(fin)
    #             writePrioritization(ppath, name, ctype, run, prioritization)
    #             apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
    #             apfds.append(apfd)
    #             stimes.append(stime)
    #             ptimes.append(ptime)
    #             print("  Progress: 100%  ")
    #             print("  Running time:", stime + ptime)
    #             if javaFlag:
    #                 print("  APFD:", sum(apfds[run]) / len(apfds[run]))
    #             else:
    #                 print("  APFD:", apfd)
    #         rep = (name, stimes, ptimes, apfds)
    #         writeOutput(outpath, ctype, rep, javaFlag)
    #         print("")
    #     else:
    #         print(name, "already run.")
    #
    # elif name == "I-TSD":
    #     if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
    #         ptimes, stimes, apfds = [], [], []
    #         for run in range(repeats):
    #             print(" Run", run)
    #             stime, ptime, prioritization = competitors.i_tsd(fin)
    #             writePrioritization(ppath, name, ctype, run, prioritization)
    #             apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
    #             apfds.append(apfd)
    #             stimes.append(stime)
    #             ptimes.append(ptime)
    #             print("  Progress: 100%  ")
    #             print("  Running time:", stime + ptime)
    #             if javaFlag:
    #                 print("  APFD:", sum(apfds[run]) / len(apfds[run]))
    #             else:
    #                 print("  APFD:", apfd)
    #         rep = (name, stimes, ptimes, apfds)
    #         writeOutput(outpath, ctype, rep, javaFlag)
    #         print("")
    #     else:
    #         print(name, "already run.")
    #
    # else:
    #     print("Wrong input.")
    #     print(usage)
    #     exit()


def wboxPrioritization(name, prog, v, ctype, n, r, b, repeats, selsize):
    javaFlag = True if v == "v0" else False

    fin = "input/{}_{}/{}-{}.txt".format(prog, v, prog, ctype)
    if javaFlag:
        fault_matrix = "input/{}_{}/fault_matrix.pickle".format(prog, v)
    else:
        fault_matrix = "input/{}_{}/fault_matrix_key_tc.pickle".format(prog, v)

    outpath = "output/{}_{}/".format(prog, v)
    ppath = outpath + "prioritized/"

    if name == "GT":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                stime, ptime, prioritization = competitors.gt(fin)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "FAST-" + selsize.__name__[:-1]:
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                if javaFlag:
                    stime, ptime, prioritization = fast.fast_(
                        fin, selsize, r=r, b=b, memory=False)
                else:
                    stime, ptime, prioritization = fast.fast_(
                        fin, selsize, r=r, b=b, memory=True)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "FAST-pw":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                if javaFlag:
                    stime, ptime, prioritization = fast.fast_pw(fin, r, b)
                else:
                    stime, ptime, prioritization = fast.fast_pw(
                        fin, r, b, memory=True)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "GA":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                stime, ptime, prioritization = competitors.ga(fin)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "GA-S":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                stime, ptime, prioritization = competitors.ga_s(fin)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "ART-D":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                stime, ptime, prioritization = competitors.artd(fin)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    elif name == "ART-F":
        if ("{}-{}.tsv".format(name, ctype)) not in set(os.listdir(outpath)):
            ptimes, stimes, apfds = [], [], []
            for run in range(repeats):
                print(" Run", run)
                stime, ptime, prioritization = competitors.artf(fin)
                writePrioritization(ppath, name, ctype, run, prioritization)
                apfd = metric.apfd(prioritization, fault_matrix, javaFlag)
                apfds.append(apfd)
                stimes.append(stime)
                ptimes.append(ptime)
                print("  Progress: 100%  ")
                print("  Running time:", stime + ptime)
                if javaFlag:
                    print("  APFD:", sum(apfds[run]) / len(apfds[run]))
                else:
                    print("  APFD:", apfd)
            rep = (name, stimes, ptimes, apfds)
            writeOutput(outpath, ctype, rep, javaFlag)
            print("")
        else:
            print(name, "already run.")

    else:
        print("Wrong input.")
        print(usage)
        exit()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def writePrioritization(path, name, ctype, run, prioritization):
    fout = "{}/{}-{}-{}.pickle".format(path, name, ctype, run + 1)
    pickle.dump(prioritization, open(fout, "wb"))


def writeOutput(outpath, ctype, res, javaFlag):
    if javaFlag:
        name, stimes, ptimes, apfds = res
        fileout = "{}/{}-{}.tsv".format(outpath, name, ctype)
        with open(fileout, "w") as fout:
            fout.write("SignatureTime\tPrioritizationTime\tAPFD\n")
            for st, pt, apfdlist in zip(stimes, ptimes, apfds):
                for apfd in apfdlist:
                    tsvLine = "{}\t{}\t{}\n".format(st, pt, apfd)
                    fout.write(tsvLine)
    else:
        name, stimes, ptimes, apfds = res
        fileout = "{}/{}-{}.tsv".format(outpath, name, ctype)
        with open(fileout, "w") as fout:
            fout.write("SignatureTime\tPrioritizationTime\tAPFD\n")
            for st, pt, apfd in zip(stimes, ptimes, apfds):
                tsvLine = "{}\t{}\t{}\n".format(st, pt, apfd)
                fout.write(tsvLine)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Getting Test cases from java files


def get_all_java_test_files():
    """
     Gets all java test path in the repository
    """
    files = []
    files += glob.glob('../**/*Test*.java', recursive=True)
    files += glob.glob('../**/*__*Test*.java', recursive=True)
    return files


def compact_files(tests_directories):
    """
     Compacts a
    """
    test_suites = []
    for testSuite in tests_directories:
        test_suites.append(minify_test_class(testSuite))
    return test_suites


def minify_test_class(path: str):
    file = open(path, "r")
    lines = file.readlines()
    compressed_file = ""
    for line in lines:
        compressed_file += line.replace("\n", "").strip()
    return compressed_file


def get_test_class_number(tests_directories):
    classes = {}
    for number in range(len(tests_directories)):
        classes[number + 1] = tests_directories[number]
    return classes


if __name__ == "__main__":

    files_paths = get_all_java_test_files()
    test_classes_order = get_test_class_number(files_paths)
    processed_test_cases = compact_files(files_paths)

    entity = "bbox"
    algname = "FAST-pw"
    repeats = 1

    algnames = {"FAST-pw", "FAST-one", "FAST-log", "FAST-sqrt", "FAST-all",
                "STR", "I-TSD",
                "ART-D", "ART-F", "GT", "GA", "GA-S"}

    entities = {"bbox", "function", "branch", "line"}

    # FAST parameters
    k, n, r, b = 5, 10, 1, 10

    # FAST-f sample size
    if algname == "FAST-all":
        def all_(x):
            return x


        selsize = all_
    elif algname == "FAST-sqrt":
        def sqrt_(x):
            return int(math.sqrt(x)) + 1


        selsize = sqrt_
    elif algname == "FAST-log":
        def log_(x):
            return int(math.log(x, 2)) + 1


        selsize = log_
    elif algname == "FAST-one":
        def one_(x):
            return 1


        selsize = one_
    else:
        def pw(x):
            pass


        selsize = pw

    priorizated_tests = bboxPrioritization(
        algname, '', '', entity, k, n, r, b, repeats, selsize
        , processed_test_cases)

    print(priorizated_tests)
    print(test_classes_order)
    tests_post_priorization = []
    for priorizated_test in priorizated_tests:
        tests_post_priorization.append(test_classes_order[priorizated_test])
    print(tests_post_priorization)
