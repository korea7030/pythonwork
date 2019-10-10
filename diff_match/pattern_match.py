from diff_match_patch import diff_match_patch

import sys
import re
import pandas as pd


def nmt_qa_match(text1, text2):
    del_regex = re.compile("<del.*?>(.+?)</del>")

    if (pd.isnull(text1) or pd.isna(text1)) or (pd.isnull(text2) or pd.isna(text2)):
        return None

    dmp = diff_match_patch()
    diffs = list()
    try:
        diffs = dmp.diff_main(str(text1).strip(), str(text2).strip())
    except AttributeError as e:
        print(text1)
        print(e)

    pretty_html = dmp.diff_prettyHtml(diffs)

    extract_del_html = re.sub(del_regex, "", pretty_html).replace("<span>", "").replace("</span>", "")

    return extract_del_html


def split_data(text, red_color_format):
    res_content = list()
    if pd.isnull(text) or pd.isna(text):
        return 'X'

    pattern_find = re.findall(r"<ins.*?>(.+?)</ins>", text)
    full_text = re.split("<ins.*?>(.+?)</ins>", text)

    for txt in full_text:
        if txt in pattern_find:
            res_content.append(red_color_format)
            res_content.append(txt)
        else:
            if txt != '':
                res_content.append(txt)

    return res_content


def convert_list_to_str(text):
    if all(isinstance(s, str) for s in text):
        return ''.join(text)
    else:
        return text


def make_workbook(df):
    print("make result file Start")
    excel_writer = pd.ExcelWriter("qa_match.xlsx", engine='xlsxwriter')
    sheet_name = 'NMT'

    workbook = excel_writer.book
    red_color_format = workbook.add_format({'font_color': 'red'})
    print("split and add format Start")
    df['QA_complete'] = df.new_column.apply(lambda x: split_data(x, red_color_format))
    print("split and add format End")
    print("convert list to string Start")
    df['QA_complete'] = df.QA_complete.apply(lambda x: convert_list_to_str(x))
    print("convert list to string End")

    del df['new_column']
    # del df['QA 완료']
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)
    worksheet = excel_writer.sheets[sheet_name]

    print("diff font color red format adjust Start")
    for idx, x in df['QA_complete'].iteritems():
        worksheet.write_rich_string(idx + 1, df.columns.size - 1, *x)
    print("diff font color red format adjust End")

    wrap_format = workbook.add_format({'text_wrap': True, 'align': 'vcenter'})
    worksheet.set_column('A:C', 20, wrap_format)

    excel_writer.save()
    print("make result file End")


if __name__ == '__main__':
    '''
    확인하고자 하는 엑셀 파일을 같은 경로상에 위치 해야함
    엑셀 컬럼은 변경전, 변경후 두 개의 필드만 존재
    결과는 qa_match.xlsx 결과로 나옴
    '''
    print("Start")
    file_name = sys.argv[1]
    data_df = pd.read_excel(file_name)
    cols = data_df.columns  # column 리스트
    print("NMT QA Matching Start")
    data_df['new_column'] = data_df.apply(lambda x: nmt_qa_match(x[cols[0]], x[cols[1]]), axis=1)
    # data_df['new_column'] = data_df.apply(lambda x: nmt_qa_match(x['NMT'], x['QA 완료']), axis=1)
    print("NMT QA Matching End")
    make_workbook(data_df)