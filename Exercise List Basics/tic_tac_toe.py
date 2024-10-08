# f_r = first roll, s_r = second roll and t_r = third roll.
f_r = input().split()
s_r = input().split()
t_r = input().split()

f_r = [int(x) for x in f_r]
s_r = [int(x) for x in s_r]
t_r = [int(x) for x in t_r]

if (f_r[0] == 1 and f_r[1] == 1 and f_r[2] == 1) or \
   (s_r[0] == 1 and s_r[1] == 1 and s_r[2] == 1) or \
   (t_r[0] == 1 and t_r[1] == 1 and t_r[2] == 1) or \
   (f_r[0] == 1 and s_r[0] == 1 and t_r[0] == 1) or \
   (f_r[1] == 1 and s_r[1] == 1 and t_r[1] == 1) or \
   (f_r[2] == 1 and s_r[2] == 1 and t_r[2] == 1) or \
   (f_r[0] == 1 and s_r[1] == 1 and t_r[2] == 1) or \
   (f_r[2] == 1 and s_r[1] == 1 and t_r[0] == 1):
    print("First player won")
elif (f_r[0] == 2 and f_r[1] == 2 and f_r[2] == 2) or \
     (s_r[0] == 2 and s_r[1] == 2 and s_r[2] == 2) or \
     (t_r[0] == 2 and t_r[1] == 2 and t_r[2] == 2) or \
     (f_r[0] == 2 and s_r[0] == 2 and t_r[0] == 2) or \
     (f_r[1] == 2 and s_r[1] == 2 and t_r[1] == 2) or \
     (f_r[2] == 2 and s_r[2] == 2 and t_r[2] == 2) or \
     (f_r[0] == 2 and s_r[1] == 2 and t_r[2] == 2) or \
     (f_r[2] == 2 and s_r[1] == 2 and t_r[0] == 2):
    print("Second player won")
else:
    print("Draw!")