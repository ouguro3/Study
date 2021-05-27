
filename = 'yesterday.txt'
with open(filename, 'r') as f:
    song_lines = {}
    for lines in f:
        lines = lines.lower() # 소문자로 변환
        words = lines.split() # 공백 기준으로 자르기
        for i in words:
            if i not in song_lines:
                    song_lines[i] = 1
            else:
                song_lines[i] += 1
    word = []
    for i,j in song_lines.items():
        word.append((i,j))
        word.sort()
    for i,j in word:
        print(i,':',j)



