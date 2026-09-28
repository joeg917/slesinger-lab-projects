
def drug_dictionaries():
    drugDict = {
        0: "20K",
        1: "Propanol 100 mM",
        2: "Carbachol 10 uM",
        3: "QX-314 400 uM",
        4: "2K",
        5: "2K + QX314 400 uM",
        6: "n/a",
        7: "BaCl2, 1mM"
    }
    drugDictBrokenValve = {
        0: "20K",
        1: "Propanol 100 mM",
        2: "Carbachol 10 uM",
        3: "N/A broken valve",
        4: "QX-314 400 uM",
        5: "N/A",
        6: "N/A",
        7: "BaCl2, 1mM"
    }
    alcDict = {
        0: "20K",
        1: "EtOH 1 mM",
        2: "EtOH 5 mM",
        3: "EtOH 50 mM",
        4: "PrOH 1 mM",
        5: "PrOH 10 mM",
        6: "PrOH 50 mM",
        7: "BaCl2, 1 mM"
    }
    alcDictBrokenValve = {
        0: "20K",
        1: "EtOH 1 mM",
        2: "EtOH 10 mM",
        3: "N/A broken valve",
        4: "EtOH 50 mM",
        5: "PrOH 1 mM",
        6: "PrOH 10 mM",
        7: "BaCl2, 1mM"
        
        
        
    }
    ncatsDict = {
        0: "20K",
        1: "Propanol 100 mM",
        2: "Compound 1 10 uM",
        3: "Compound 2 10 uM",
        4: "Compound 3 10 uM",
        5: "Compound 4 10 uM",
        6: "Compound 5 10 uM",
        7: "BaCl2, 1 mM"
    }
    ncatsDoseResponse = {
        0: "20K",
        1: "0.01 uM",
        2: "0.1 uM",
        3: "1 uM",
        4: "10 uM",
        5: "N/A",
        6: "N/A",
        7: "BaCl2, 1 mM"
    }
    ncatsDoseResponse2 = {
        0: "20k",
        1: "0.1 uM",
        2: "0.5 uM",
        3: "1 uM",
        4: "5 uM",
        5: "10 uM",
        6: "20 uM",
        7: "BaCl2, 1 mM"
    }
    user_input = input("Choose 1 for KLS, 2 for Kir4.1 Alcohol Experiment, 3 for NCATS (all drugs), 4 for NCATS (dose-response): ")
    if user_input == "1":
        return drugDict
    elif user_input == "2":
        return alcDictBrokenValve
    elif user_input == "3":
        return ncatsDict
    elif user_input == "4":
        return ncatsDoseResponse
    else:
        print("Invalid Response")
