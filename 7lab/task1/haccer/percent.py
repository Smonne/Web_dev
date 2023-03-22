if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        sum=0
        for i in scores:
            sum+=i
        student_marks[name] = float(sum/len(scores))
    query_name = input()
    print("{:.2f}".format(round(student_marks[query_name], 2)))