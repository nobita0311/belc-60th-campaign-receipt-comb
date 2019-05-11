
# レシートのデータを取得
receipts = open("receipts.txt", "r")

_lines = receipts.readlines()
lines = list(map(int, _lines))

results = []
result = []

while len(lines):
    # 最大値を取得して結果に挿入
    max_value = max(lines)
    result.append(max_value)
    max_key = lines.index(max_value)
    lines.pop(max_key)

    num = max_value

    # 最大値が3000以上の場合は離脱
    if num >= 3000:
        result = map(str, result)
        results.append(' & '.join(result))
        result = []
        continue

    # 3000以上になるまで最小値を足す
    while len(lines):
        min_value = min(lines)
        result.append(min_value)
        min_key = lines.index(min_value)
        lines.pop(min_key)
        num += min_value
        # 3000 以上になったら結果に入れて初期化して離脱
        if num >= 3000:
            result = map(str, result)
            results.append(' & '.join(result))
            result = []
            num = 0
            break
# 出力
for i, comb in enumerate(results, 1):
    print('組み合わせ{0}:{1}'.format(i, comb))
receipts.close()
