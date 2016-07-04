grades = {"AA1" : 100, "AA2" : 90, "AB1" : 85, "AB2" : 80, "AB3" : 75, "AC1" : 70, "AC2" : 65, "AC3" : 60, "AD1" : 55, "AD2" : 50, "AD3" : 45, "AE" : 0, "AF" : 0, "BA1" : 0, "BA2" : 0, "BB1" : 0, "BB2" : 0, "BB3" : 0, "BC1" : 0, "BC2" : 0, "BC3" : 0, "BD1" : 0, "BD2" : 0, "BD3" : 0, "BE" : 0, "BF" : 0, "CFM" : 50, "CGD" : 70, "CPP" : 30, "GA1" : 60, "GA2" : 50, "GB1" : 45, "GB2" : 40, "GB3" : 35, "GC1" : 30, "GC2" : 25, "GC3" : 20, "GD1" : 15, "GD2" : 10, "GD3" : 5, "GE" : 0, "GF" : 0, "U" : 0 }

maths_grades = {"AA1" : 125, "AA2" : 115, "AB1" : 110, "AB2" : 105, "AB3" : 100, "AC1" : 95, "AC2" : 90, "AC3" : 85, "AD1" : 80, "AD2" : 75, "AD3" : 70, "AE" : 0, "AF" : 0, "GA1" : 60, "GA2" : 50, "GB1" : 45, "GB2" : 40, "GB3" : 35, "BC1" : 30, "GC2" : 25, "GC3" : 20, "GD1" : 15, "GD2" : 10, "GD3" : 5, "GE" : 0, "GF" : 0, "BA1" : 0, "BA2" : 0, "BB1" : 0, "BB2" : 0, "BB3" : 0}

columns = ["name", "Id", "Irish", "English", "Maths", "History", "Geography", "Latin", "Ancient_Greek", "Classical_studies", "French", "German", "Spanish", "Italian", "Art", "Applied_Maths", "Physics", "Chemistry", "Physics_and_Chemistry", "Ag_Science", "Biology", "Agricultural_Economics", "Engineering", "Construction_Studies", "Accounting", "Business", "Economics", "Finnish", "Japanese", "Arabic", "Technology", "Music", "Home_Ec", "Russian", "Religious_Education", "Link_Module", "Polish", "Hungarian", "Romanian", "Design_and_Comm_Graphics"]
grade_columns = ["NAME", "ID", "IRISH", "ENGLISH", "MATHS", "HISTORY", "GEOGRAPHY", "LATIN", "ANCIENT_GREEK", "CLASSICAL_STUDIES", "FRENCH", "GERMAN", "SPANISH", "ITALIAN", "ART", "APPLIED_MATHS", "PHYSICS", "CHEMISTRY", "PHYSICS_AND_CHEMISTRY", "AG_SCIENCE", "BIOLOGY", "AGRICULTURAL_ECONOMICS", "ENGINEERING", "CONSTRUCTION_STUDIES", "ACCOUNTING", "BUSINESS", "ECONOMICS", "FINNISH", "JAPANESE", "ARABIC", "TECHNOLOGY", "MUSIC", "HOME_EC", "RUSSIAN", "RELIGIOUS_EDUCATION", "LINK_MODULE", "POLISH", "HUNGARIAN", "ROMANIAN", "DESIGN_AND_COMM_GRAPHICS"]

import re

def dataAlign(df):
    # Strips away leading spaces
    df.columns = [x.lstrip() for x in list(df.columns)]
    # Change all columns to caps
    df.columns = [x.upper() for x in list(df.columns)]
    # Replaces & with 'and'
    df.columns = [x.replace("&", "AND") for x in list(df.columns)]
    # Removes all symbols
    regex = re.compile('[^a-zA-Z ]')
    df.columns = [regex.sub('', x) for x in list(df.columns)]
    # Replaces all spaces with underscores
    df.columns = [x.replace(" ", "_") for x in list(df.columns)]
    # Match with set names and alert if remainders
    clash = set(df.columns) - set(grade_columns)
    if len(clash) > 0:
        print("Column Mismatch" + str(clash))
            # Future fuzzy matching
        # Drop excess
        df = df.drop(clash, axis=1)
    return df


# Convert all letter grades to scores

# Find max points for each student

# Plan

# Views
