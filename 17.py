from asyncio import threads


dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand"
}

def T_convert_nums (n):
    count = 0
    for k in range(1, n + 1):
        if k <= 100:
            if k not in dict:
                num = k // 10 * 10
                dict[k] = dict[num] + dict[k % 10]
        elif k < 1000:
            num = k // 100
            _num = (num * 100) // num

            if k % 100 != 0:
                dict[k] = dict[num] + dict[_num] + "And" + dict[k % 100]
            else:
                dict[k] = dict[num] + dict[_num]
        else:
            num = k // 1000
            _num = (num * 1000) // num

            if k % 1000 != 0:
                dict[k] = dict[num] + dict[_num] + "And" + dict[k % 1000]
            else:
                dict[k] = dict[num] + dict[_num]

        item = dict.get(k)
        print(item)

        count += len(item)
    return count

print(T_convert_nums(1000))
