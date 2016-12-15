def longest_common_sub_sequence(seq1, seq2):
    len_seq1, len_seq2 = len(seq1), len(seq2)
    dynamic_list = [[0] * (len_seq1 + 1) for i in range(len_seq2 + 1)]
    for i in range(len_seq1):
        for j in range(len_seq2):
            if seq1[i] == seq2[j]:
                dynamic_list[j][i] = 1 + dynamic_list[j-1][i-1]
            else:
                dynamic_list[j][i] = max(dynamic_list[j-1][i], dynamic_list[j][i-1])
    return dynamic_list[-2][-2]

print(longest_common_sub_sequence('loshadky', 'osedlal'))


def longest_raising_sub_sequence(obj):
    len_obj, dynamic_list = len(obj), []
    for i in range(len_obj):
        counter = 0
        for j in range(i):
            if obj[j] < obj[i] and counter < dynamic_list[j]:
                counter = dynamic_list[j]
        dynamic_list.append(counter + 1)
    return max(dynamic_list)

print(longest_raising_sub_sequence([555, 5333, 6543234, 0, 46, 9999999, 53323, 53324, 9999999]))