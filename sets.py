s1={1,2,3,4,5,6,7,8}
s2={3,3,4,4,5,6,7,8}
s3={'perl','python','java'}

print(s1.__sizeof__())
print(len(s1))
print(s1.add(9))
print(f'After adding 9 to set 1 {s1}')
print(f'{s1.pop()} is poped out and the new set is {s1}')
print(f's1 intersection s2 is {s1.intersection(s2)}')
print(f'differnce bw 2 sets {s1-s2}')
print(f'symettric difference is {s1^s2}')
print(f'checking the element {s1.__contains__(4)}')
print(f'clearing a set {s3.clear()} {s3}')
del s2
print(len(s2))
