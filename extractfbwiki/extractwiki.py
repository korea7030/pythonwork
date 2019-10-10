import os
import wget

downloaded_wiki_dir = 'D:/LASER/docker/WikiMatrix.v1.1620_language_pairs/v1/tsv/'
base_wiki_txt = 'D:/LASER/tasks/WikiMatrix/list_of_bitexts.txt'
wikimatrix_url = 'https://dl.fbaipublicfiles.com/laser/WikiMatrix/v1/'


def get_wiki_list(wiki_txt):
    result = list()
    with open(wiki_txt, 'r') as f:
        while(f.readline()):
            if f.readline() != '\n':
                str_wiki = f.readline().replace('\n', '').split('\t')[0]
                result.append(str_wiki)

    return result


if __name__ == "__main__":
    downloaded_wiki_lst = set(os.listdir(downloaded_wiki_dir))
    wiki_full_lst = set(get_wiki_list(base_wiki_txt))

    complete_lst = list()
    diff_lst = wiki_full_lst.difference(downloaded_wiki_lst)

    for wiki in diff_lst:
        url = wikimatrix_url + wiki + '.gz'
        wget.download(url, wiki)

        try:
            with open(wiki, 'r') as f:
                complete_lst.append(wiki)

            if len(diff_lst) == len(complete_lst):
                print('complete download tsv')

        except FileNotFoundError:
            with open('no_down_list.txt', 'w+') as f2:
                f2.write(wiki+'\n')





