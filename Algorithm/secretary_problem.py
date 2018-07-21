import itertools

def perm(a):
    '''
    :param a: 지원자 리스트
    :return: 순열 리스트
    지원자 리스트의 모든 경우의 수를 나타낸 순열을 리턴
    '''
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)

        return result


def get_candidate_list(num):
    '''
    :param num: 지원자 수
    :return: 지원자 리스트
    지원자 정보를 반환
    '''
    candidate_list = []
    for c in range(1,num+1):
        candidate_list.append(c)
    return candidate_list


def hire(passLimit, remain):
    '''
    :param passLimit: 합격 커트라인 지원자
    :param remain: 남은 지원자
    :return: 남은지원자
    커트라인 지원자와 남은 지원자를 비교하여 합격자를 리턴
    '''
    for i in range(len(remain)):
        if remain[i] >= passLimit:
            return remain[i]

    return remain[len(remain)-1]


if __name__ == '__main__':
    # 확률 결과 리스트
    probablity_result = []

    for i in range(4,9):
        # best 지원자 변수 저장

        best_dict = {'candidate': i, 'preview': 0, 'probability': 0}
        print('지원자 %d 명' % (i))
        candidate_list = []

        for j in range(1, i-1):
            lst = get_candidate_list(i)
            # 모든 순열 리스트 반환
            candidate_permutation = perm(lst)
            success_list = []
            # 지원자 전체 순열 구하기
            for k in candidate_permutation:
                # 살펴보기 횟수
                preview = k[:j]
                # 합격 커트라인
                passLimit = max(preview)
                # 남은 지원자
                remain = k[j:]

                # 지원결과
                hire_result = hire(passLimit, remain)

                # 결과가 지원자 수와 같은 경우 저장
                if hire_result == i:
                    success_list.append(hire_result)
            # 확률
            probablity = len(success_list) / len(candidate_permutation)

            # 최적의 확률과 비교
            if best_dict['probability'] > probablity:
                break
            if best_dict['probability'] < probablity:
                # 살펴보기 수 저장
                best_dict['preview'] = j
                # 최적의 확률 변경
                best_dict['probability'] = probablity

            print('%d 명 살펴보기 채용 성공 확률 : %d / %d' % (j, len(success_list), len(candidate_permutation)))
        probablity_result.append(best_dict)
    print(str(probablity_result))