import polib
import pandas as pd


class Localization():

    def __init__(self, filename):
        self.po = polib.pofile(filename)

    # comment 정보
    def get_comment(self, obj):
        return obj.comment.replace('Translators: ', '')

    # msgstr 정보
    def get_msgstr(self, obj):
        return obj.msgstr

    # msgstr_plural(복수형)
    def get_msgstr_plural(self, obj):
        if len(obj.msgstr_plural) != 0:
            return "복수"

        return "단수"

    # msgid
    def get_msgid(self, obj):
        return obj.msgid

    # flags : python-format 인지 아닌지
    def get_flags(self, obj):
        if ''.join(obj.flags) == "python-format":
            return "Y"

        return "N"

    # 번역이 쓰인 위치
    def get_occurrence(self, obj):
        return obj.occurrences

def get_dataframe(path, obj):
    local = obj
    df_msgid = pd.DataFrame(columns=['msgid', 'ko', 'en', 'ja', 'python-format', 'file_path', '서비스명', '단복수'])
    df_file_path = pd.DataFrame(columns=['file_path', 'msgid'])
    list_msgid_tmp = list()
    list_file_path_tmp = list()
    export_file_name = ''
    # print(local.po)
    if path == './ko/django.po':
        export_file_name = 'example_ko.xlsx'

        for idx in range(len(local.po)):
            # print(type(local.get_comment(local.po[po])))
            occurrence_path = local.get_occurrence(local.po[idx])
            plural_value = local.get_msgstr_plural(local.po[idx])
            if len(occurrence_path) == 1:
                # print(occurrence_path)
                if plural_value =="복수":
                    df_msgid.loc[idx] = [local.get_msgid(local.po[idx]), local.po[idx].msgstr_plural[0], '', '', local.get_flags(
                        local.po[idx]), occurrence_path[0][0], '', local.get_msgstr_plural(local.po[idx])]
                else :
                    df_msgid.loc[idx] = [local.get_msgid(local.po[idx]), local.get_msgstr(local.po[idx]), '', '', local.get_flags(
                        local.po[idx]), occurrence_path[0][0], '', local.get_msgstr_plural(local.po[idx])]


                df_file_path.loc[idx] = [occurrence_path[0][0], local.get_msgid(local.po[idx])]
            else:
                for i in range(len(occurrence_path)):
                    # print(i, local.get_msgid(local.po[idx]), local.get_msgstr(local.po[idx]), occurrence_path[i][0])
                    # df_msgid_tmp.loc[idx_count] = [local.get_msgid(local.po[idx]), local.get_msgstr(local.po[idx]), '', '', local.get_flags(
                    #     local.po[idx]), occurrence_path[i][0], '', local.get_msgstr_plural(local.po[idx])]
                    if plural_value =="복수":
                        list_msgid_tmp.append([local.get_msgid(local.po[idx]), local.po[idx].msgstr_plural[0], '','', local.get_flags(
                            local.po[idx]), occurrence_path[i][0], '', local.get_msgstr_plural(local.po[idx])])
                    else :
                        list_msgid_tmp.append([local.get_msgid(local.po[idx]), local.get_msgstr(local.po[idx]), '',  '', local.get_flags(
                            local.po[idx]), occurrence_path[i][0], '', local.get_msgstr_plural(local.po[idx])])

                    # df_file_path_tmp.loc[idx_count] = [occurrence_path[i][0], local.get_msgid(local.po[idx])]
                    list_file_path_tmp.append([occurrence_path[i][0], local.get_msgid(local.po[idx])])

                # print(1, occurrence_path)

    else:
        export_file_name = 'example_en.xlsx'
        for idx in range(len(local.po)):
            # print(type(local.get_comment(local.po[po])))
            # print(type(local.get_comment(local.po[po])))
            plural_value = local.get_msgstr_plural(local.po[idx])
            occurrence_path = local.get_occurrence(local.po[idx])
            if len(occurrence_path) == 1:
                # print(occurrence_path)
                if plural_value =="복수":
                    df_msgid.loc[idx] = [local.get_msgid(local.po[idx]), '', local.po[idx].msgstr_plural[0], '', local.get_flags(
                        local.po[idx]), occurrence_path[0][0], '', local.get_msgstr_plural(local.po[idx])]
                else :
                    df_msgid.loc[idx] = [local.get_msgid(local.po[idx]), '', local.get_msgstr(local.po[idx]), '', local.get_flags(
                        local.po[idx]), occurrence_path[0][0], '', local.get_msgstr_plural(local.po[idx])]

                df_file_path.loc[idx] = [occurrence_path[0][0], local.get_msgid(local.po[idx])]
            else:
                for i in range(len(occurrence_path)):
                    if plural_value =="복수":
                        list_msgid_tmp.append([local.get_msgid(local.po[idx]), '', local.po[idx].msgstr_plural[0], '', local.get_flags(
                            local.po[idx]), occurrence_path[i][0], '', local.get_msgstr_plural(local.po[idx])])
                    else :
                        list_msgid_tmp.append([local.get_msgid(local.po[idx]), '', local.get_msgstr(local.po[idx]), '', local.get_flags(
                            local.po[idx]), occurrence_path[i][0], '', local.get_msgstr_plural(local.po[idx])])

                    # print(i, local.get_msgid(local.po[idx]), local.get_msgstr(local.po[idx]), occurrence_path[i][0])

                    # df_file_path_tmp.loc[idx_count] = [occurrence_path[i][0], local.get_msgid(local.po[idx])]
                    list_file_path_tmp.append([occurrence_path[i][0], local.get_msgid(local.po[idx])])

            # df_msgid.append(df_msgid_tmp)
            # df_file_path.append(df_file_path_tmp)

    for lst in list_msgid_tmp:
        # print(lst)
        df_msgid = df_msgid.append(pd.Series(lst, index=['msgid', 'ko', 'en', 'ja', 'python-format', 'file_path', '서비스명', '단복수']), ignore_index=True)

    # df_file_path = df_file_path.astype(str)
    for file_lst in list_file_path_tmp:
        df_file_path = df_file_path.append(pd.Series(file_lst, index=['file_path', 'msgid']), ignore_index=True)

    # 중복 제거
    df_msgid = df_msgid.astype(str)
    df_msgid = df_msgid.drop_duplicates(subset=['msgid', 'file_path'])

    df_file_path = df_file_path.astype(str)
    df_file_path = df_file_path.drop_duplicates(subset=['file_path', 'msgid'])

    return export_file_name, df_msgid, df_file_path

if __name__ == '__main__':
    po_path_list = ['./ko/django.po', './en/django.po']


    for path in po_path_list:
        local = Localization(path)

        export_file_name , df_msgid, df_file_path = get_dataframe(path, local)
        # print(len(df_msgid))
        # print(len(df_file_path))

        # dataframe excel 저장
        writer = pd.ExcelWriter(export_file_name)
        df_msgid.to_excel(writer, 'msgid', index=False)
        df_file_path.to_excel(writer, 'filepath', index=False)
        writer.save()
