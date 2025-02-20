import pandas as pd
from os import listdir
from os.path import isfile, join
from settings import ROOT_DIR_CSV, SAVE_DIR_CSV, LIST_COLUMN_CSV, ROOT_DIR_XLSX, SAVE_DIR_XLSX, SHEET_NAME, SAVE_DIR_ALL


def merge_xlsx():
    print('[DEBUG] start merge xlsx')

    files = [f for f in listdir(ROOT_DIR_XLSX) if isfile(join(ROOT_DIR_XLSX, f))]

    flist=[]
    for file in files:
        if '.xlsx' in file:
            print(f"[DEBUG] file name: {join(ROOT_DIR_XLSX, file)}")

            df = pd.read_excel(join(ROOT_DIR_XLSX, file), index_col=False, sheet_name=SHEET_NAME)
            flist.append(df)

    df_out = pd.concat(flist, axis=0, ignore_index=True)

    df_out.to_csv(SAVE_DIR_XLSX, index = False)
    print("[DEBUG] merged all xlsx")


def merge_csv():
    print('[DEBUG] start merge csv')

    files = [f for f in listdir(ROOT_DIR_CSV) if isfile(join(ROOT_DIR_CSV, f))]

    flist=[]
    for file in files:
        if '.csv' in file:
            print(f"[DEBUG] file name: {join(ROOT_DIR_CSV, file)}")

            df = pd.read_csv(join(ROOT_DIR_CSV, file), index_col=False)
            flist.append(df)
    
    df_out = pd.concat(flist, axis=0, ignore_index=True)

    df_out = df_out.drop(LIST_COLUMN_CSV, axis=1)

    df_out.to_csv(SAVE_DIR_CSV, index = False)
    print("[DEBUG] merged all csv")


def merge_all():
    print('[DEBUG] start merge all file')

    df_csv = pd.read_csv(join(SAVE_DIR_CSV), index_col=False)
    df_xlsx = pd.read_csv(join(SAVE_DIR_CSV), index_col=False)

    flist=[df_csv, df_xlsx]

    df_out = pd.concat(flist, axis=0, ignore_index=True)
    df_out.to_csv(SAVE_DIR_ALL, index = False)

    print("[DEBUG] merged all xlsx and csv")


if __name__ == '__main__':

    # to merge only csv
    # merge_csv()

    # to merge only excel file
    # merge_xlsx()

    # to merge all
    if listdir(ROOT_DIR_CSV):
        merge_csv()
    if listdir(ROOT_DIR_XLSX):
        merge_xlsx()
    if isfile(SAVE_DIR_CSV) and isfile(SAVE_DIR_XLSX):
        merge_all()