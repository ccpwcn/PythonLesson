def increment(n):
    return n + 1
def decrement(n):
    return n - 1

def change_num(fn, n):
    return fn(n)

# 在开发中还不能确定到底要执行加法还是减法的时候，就可以预定义一个加法和一个减法，然后动态判断
print(change_num(increment, 2))
print(change_num(decrement, 2))

# 应用案例：让学生输入自己的考试成绩，然后对该学生的考试成绩进行评估
#         如果小于60分，就执行留级函数，如果大于60，就执行毕业函数
def done(student_id):
    print('学生 {} 办理毕业手续'.format(student_id))
def keep(student_id):
    print('学生 {} 不能毕业，先留一级考察再定'.format(student_id))
def check_student(fn, student_id):
    print('对学生 {} 考试成绩开始进行评估'.format(student_id))
    fn(student_id)
    print('对学生 {} 考试成绩的评估已经完成'.format(student_id))
score = input('请输入考试成绩：')
if int(score) < 60:
    check_student(keep, 1)
elif int(score) < 100:
    check_student(done, 1)
else:
    print('神回答')
