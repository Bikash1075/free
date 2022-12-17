# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def T_O_H(n,s,d,a):
    if n==1:
        return
    else:
        T_O_H(n-1,s=s,d=a,a=d)
        print(f'move {n-1} disks from tower {s} to {a}')
        print(f'move {n} disk from tower {s} to {d}')
        print(f'move {n-1} disks from tower {a} to {d}')
        T_O_H(n-1,s=a,d=d,a=s)

T_O_H(3,'A','C', 'B')
 
def T_O_H(n,s,d,a):
    if n==1:
        return
    else:
        T_O_H(n-1,s,a,d)
        print(f'move {n-1} disks from tower {s} to {a}')
        print(f'move {n} disk from tower {s} to {d}')
        print(f'move {n-1} disks from tower {a} to {d}')          
        T_O_H(n-1,a,d,s)

T_O_H(3,'A','C', 'B')

def T_O_H(n,s,d,a):
    if n==0:
        return
    else:
        T_O_H(n-1,s,a,d)
        print(f'move {n} disks from {s} to {d}')
        T_O_H(n-1,a,d,s)
T_O_H(3,'A','C', 'B')